"""Numerical illustrations of Ide & Talamàs (2025), arXiv v12.

Figures 3-5, 7, 9 illustrate existing results; they are not new proofs.
Query-time and ownership experiments are this repository's explorations.
Run: python sim.py --n 401  (NumPy, SciPy, Matplotlib).
"""
from pathlib import Path
import argparse
import csv
import json
import numpy as np
from scipy.optimize import linprog, brentq
from scipy.sparse import coo_matrix
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
COLORS = {"pre": "#737b87", "auto": "#126a81", "non": "#d36b35"}


def equilibrium(n=401, h=.5, a=None, mode="pre", mu=5., tau=0.):
    """Solve the discrete competitive-equilibrium wage dual.

    Uniform trapezoid masses on [0,1]. Each HH activity uses one worker
    and h(1-z) solver time; its output is s. Thus w(z)+h(1-z)w(s)>=s.
    AI activities supply additional lower bounds. Dual multipliers recover
    all human allocations. Abundant compute is checked ex post, not assumed
    from a zero-profit wage formula alone. Atoms can split occupations.
    """
    if n < 5 or not 0 < h < 1 or mode not in COLORS or tau < 0:
        raise ValueError("Invalid grid, helping cost, mode or query cost")
    if mode != "pre" and (a is None or not 0 <= a < 1):
        raise ValueError("AI capability must lie in [0,1)")
    z = np.linspace(0, 1, n)
    mass = np.ones(n) / (n - 1)
    mass[[0, -1]] /= 2
    i, j = np.triu_indices(n, 1)
    count = len(i)
    help_time = h * (1-z[i])
    rows = np.repeat(np.arange(count), 2)
    cols = np.column_stack((i,j)).ravel()
    vals = np.column_stack((-np.ones(count), -help_time)).ravel()
    A = coo_matrix((vals,(rows,cols)),shape=(count,n)).tocsr()
    # Bounds: independent human; worker assisted by AI; human solving for AI.
    options = np.full((3,n), -np.inf)
    options[0] = z
    r = a if mode == "auto" else 0.
    duration = 1 + tau * (1-z)**2
    if mode != "pre":
        options[1,z<=a] = (a-r*h*(1-z[z<=a])) / duration[z<=a]
    if mode == "auto":
        options[2,z>=a] = (z[z>=a]-a)/(h*(1-a))
    which = np.argmax(options,axis=0)
    lower = options[which,np.arange(n)]
    sol = linprog(mass,A_ub=A,b_ub=-z[j],bounds=list(zip(lower,[None]*n)),
                  method="highs", options={"dual_feasibility_tolerance":1e-9,
                                           "primal_feasibility_tolerance":1e-9})
    if not sol.success:
        raise RuntimeError(sol.message)
    wage = sol.x
    pairs = -sol.ineqlin.marginals
    residual = sol.lower.marginals
    wp = np.bincount(i,weights=pairs,minlength=n)
    sp = np.bincount(j,weights=pairs*help_time,minlength=n)
    independent = np.where(which==0,residual,0.)
    wa = np.where(which==1,residual,0.)
    sa = np.where(which==2,residual,0.)
    mus = float(np.sum(wa*h*(1-z)/duration))
    muw = float(sa.sum()/(h*(1-a))) if mode == "auto" else 0.
    mui = mu-mus-muw if mode != "pre" else 0.
    if mode != "pre" and mui <= 1e-8:
        raise ValueError("Compute is not abundant; the reduced price model is invalid")
    # Independent primal reconstruction, including capital opportunity cost.
    output = float(np.dot(independent,z)+np.dot(pairs,z[j]))
    if mode != "pre":
        output += float(np.sum(wa*a/duration))
    if mode == "auto":
        output += float(np.dot(sa,z)/(h*(1-a))+mui*a)
    income = float(np.dot(mass,wage))
    gap = abs(output-income-(mu*r if mode != "pre" else 0))
    clearing = float(np.max(np.abs(independent+wa+sa+wp+sp-mass)))
    violation = float(max(0.,np.max(A@wage+z[j]),np.max(lower-wage)))
    complement = float(np.max(np.abs(pairs*(A@wage+z[j]))))
    assert max(gap,clearing,violation,complement) < 2e-7
    used = pairs > 1e-9
    ordered = sorted(zip(i[used],j[used]))
    # Strict continuum PAM becomes weak PAM between discrete atoms.
    last_i,last_j = -1,-1
    for ii,jj in ordered:
        if ii != last_i:
            assert jj >= last_j
        last_i,last_j = ii,jj
    match = np.divide(np.bincount(i,weights=pairs*z[j],minlength=n),wp,
                      out=np.full(n,np.nan),where=wp>1e-10)
    employee = np.divide(np.bincount(j,weights=pairs*help_time*z[i],minlength=n),sp,
                         out=np.full(n,np.nan),where=sp>1e-10)
    span = np.divide(np.bincount(j,weights=pairs,minlength=n),sp,
                     out=np.full(n,np.nan),where=sp>1e-10)
    return dict(z=z,w=wage,mass=mass,wp=wp,sp=sp,wa=wa,sa=sa,I=independent,
                match=match,employee=employee,span=span,output=output,income=income,
                mu_i=mui,mu_s=mus,mu_w=muw,r=r,h=h,a=a,tau=tau,
                gap=gap,clearing=clearing,violation=violation,complement=complement)


def setup_axis(ax,title):
    ax.set(title=title,xlabel="Human knowledge z",ylabel="Labor income w(z)",xlim=(0,1))
    ax.grid(alpha=.18)
    ax.spines[["top","right"]].set_visible(False)


def line(ax,e,mode,label=None):
    ax.plot(e["z"],e["w"],color=COLORS[mode],lw=2,
            ls="--" if mode=="non" else "-",label=label or mode)


def finish(fig,name,subtitle):
    fig.suptitle(subtitle,fontsize=12)
    fig.tight_layout(rect=(0,0,1,.95))
    fig.savefig(ROOT/"figures"/name,dpi=170)
    plt.close(fig)


def gini(x,p):
    order=np.argsort(x)
    p,x=p[order],x[order]
    y=p*x
    return float(1-np.sum(p*(2*np.cumsum(y)-y))/y.sum())


def main(n):
    (ROOT/"figures").mkdir(exist_ok=True)
    pre=equilibrium(n)
    high=equilibrium(n,h=.8125)
    autos={a:equilibrium(n,a=a,mode="auto") for a in [.425,.85]}
    nons={a:equilibrium(n,a=a,mode="non") for a in autos}
    pre_cut=3-np.sqrt(5)  # c + .5*(c-c*c/2) = 1; G(z)=z, no independents
    assert .425 < pre_cut < .85
    assert np.all(pre["w"]>pre["z"])
    unused=equilibrium(n,a=.2,mode="non")
    assert np.max(np.abs(unused["w"]-pre["w"])) < 1e-7
    for a,e in autos.items():
        f=nons[a]
        assert e["output"]>f["output"] and e["income"]>pre["income"]
        assert f["w"][0]>max(pre["w"][0],e["w"][0])
        assert e["w"][-1]>=f["w"][-1]-1e-7
        assert np.min(f["w"]-pre["w"]) < 0
        assert abs(np.interp(a,e["z"],e["w"])-a)<.01
        if a==.425:
            assert (e["wp"]+e["wa"]).sum()<pre["wp"].sum()
            assert (e["sp"]+e["sa"]).sum()>pre["sp"].sum()
        else:
            assert (e["wp"]+e["wa"]).sum()>pre["wp"].sum()
            assert (e["sp"]+e["sa"]).sum()<pre["sp"].sum()
    fig,axes=plt.subplots(1,2,figsize=(10,4))
    for ax,e in zip(axes,[pre,high]):
        line(ax,e,"pre","Pre-AI wage")
        ax.plot(e["z"],e["z"],":",color="black",label="Independent output z")
        setup_axis(ax,f"h = {e['h']}; h0 = 0.75")
        ax.legend(fontsize=8)
    finish(fig,"fig03.png","Figure 3 illustration | Uniform human knowledge")
    for name,include_pre in [("fig04.png",False),("fig05.png",True)]:
        fig,axes=plt.subplots(1,2,figsize=(10,4))
        for ax,(a,e) in zip(axes,autos.items()):
            if include_pre: line(ax,pre,"pre","Pre-AI")
            line(ax,e,"auto","Autonomous AI")
            ax.plot(e["z"],e["z"],":",color="black",alpha=.5)
            ax.axvline(a,color="#bbbbbb",ls="--")
            setup_axis(ax,f"{'Basic' if a<pre_cut else 'Advanced'} AI: a = {a}")
            ax.legend(fontsize=8)
        finish(fig,name,f"Figure {5 if include_pre else 4} illustration | h = 0.5")
    fig,axes=plt.subplots(1,2,figsize=(10,4))
    for ax,(a,e) in zip(axes,autos.items()):
        for state,mode,label in [(pre,"pre","Pre-AI"),(e,"auto","Autonomous"),
                                 (nons[a],"non","Non-autonomous")]:
            line(ax,state,mode,label)
        setup_axis(ax,f"{'Basic' if a<pre_cut else 'Advanced'} AI: a = {a}")
        ax.legend(fontsize=8)
    finish(fig,"fig09.png","Figure 9 illustration | Same capability, different autonomy")
    # Exact accounting decomposition, changing match first at old output share.
    # It is our accounting convention, not an additional equilibrium.
    e=autos[.425]
    s0=pre["match"][0]; s1=e["match"][0]
    p0=pre["w"][0]/s0; p1=e["w"][0]/s1
    bottom_match=p0*(s1-s0); bottom_share=s1*(p1-p0)
    n0=pre["span"][-1]; n1=1/(.5*(1-.425))
    q0=pre["w"][-1]/n0; q1=e["w"][-1]/n1
    top_match=q0*(n1-n0); top_share=n1*(q1-q0)
    decomposition={"bottom_match":float(bottom_match),"bottom_share":float(bottom_share),
                   "top_match":float(top_match),"top_share":float(top_share)}
    assert abs(bottom_match+bottom_share-(e["w"][0]-pre["w"][0]))<1e-7
    assert abs(top_match+top_share-(e["w"][-1]-pre["w"][-1]))<1e-7
    fig,axes=plt.subplots(2,2,figsize=(10,7))
    for ax,old_match,new_match,label in [(axes[0,0],s0,s1,"Bottom worker's solver"),
                                        (axes[0,1],pre["employee"][-1],.425,"Top solver's workers")]:
        line(ax,pre,"pre","Pre-AI")
        line(ax,e,"auto","Autonomous AI")
        for state,point,color in [(pre,old_match,COLORS["pre"]),(e,new_match,COLORS["auto"])]:
            value=np.interp(point,state["z"],state["w"])
            ax.vlines(point,0,value,color=color,ls=":")
            ax.scatter([point],[value],color=color,s=30,zorder=4)
        setup_axis(ax,label)
        ax.legend(fontsize=8)
    for ax,label,values in [(axes[1,0],"Least knowledgeable",[bottom_match,bottom_share,bottom_match+bottom_share]),
                            (axes[1,1],"Most knowledgeable",[top_match,top_share,top_match+top_share])]:
        ax.bar(["Match","Share","Net"],values,color=["#c85a54","#379282","#126a81"])
        ax.axhline(0,color="black",lw=.7)
        ax.set(title=label,ylabel="Change in labor income")
    finish(fig,"fig07.png","Figure 7 illustration | a = 0.425; match prices and our share accounting")
    # Capability threshold at fixed autonomy; not the non-autonomous adoption cutoff.
    threshold=brentq(lambda a:equilibrium(n,a=a,mode="auto")["w"][0]-pre["w"][0],.425,pre_cut,xtol=2e-6)
    caps=np.linspace(.1,.95,25)
    bottoms=[equilibrium(min(n,201),a=float(a),mode="auto")["w"][0] for a in caps]
    fig,ax=plt.subplots(figsize=(7,4))
    ax.plot(caps,bottoms,label="Autonomous w*(0)",color=COLORS["auto"])
    ax.axhline(pre["w"][0],color=COLORS["pre"],label="Pre-AI w(0)")
    ax.axvline(threshold,ls="--",color="#d36b35",label=f"Bottom-winner threshold ~ {threshold:.4f}")
    ax.axvline(pre_cut,ls=":",color="black",label="Pre-AI worker/solver split")
    ax.set(xlabel="AI capability a",ylabel="Least knowledgeable person's wage")
    ax.legend(fontsize=8)
    finish(fig,"capability_threshold.png","Illustration of Proposition 5 | Autonomy held fixed")
    # Own exploration 1: knowledge-dependent time to formulate/verify AI queries.
    # A human spends 1 + tau(1-z)^2 time per production opportunity with AI.
    taus=np.linspace(0,4,13)
    query=[]
    for a in autos:
        for tau in taus:
            for mode in ["auto","non"]:
                x=equilibrium(min(n,201),a=a,mode=mode,tau=float(tau))
                query.append(dict(a=a,tau=float(tau),mode=mode,bottom=float(x["w"][0]),
                                  adoption=float(x["wa"].sum()),output=x["output"]))
    fig,axes=plt.subplots(1,2,figsize=(10,4))
    for ax,a in zip(axes,autos):
        for mode in ["auto","non"]:
            subset=[x for x in query if x["a"]==a and x["mode"]==mode]
            ax.plot(taus,[x["bottom"] for x in subset],label=mode,color=COLORS[mode])
        ax.axhline(pre["w"][0],color=COLORS["pre"],ls=":",label="Pre-AI")
        ax.set(title=f"a = {a}",xlabel="Query-time parameter tau",ylabel="Bottom wage")
        ax.legend(fontsize=8)
    finish(fig,"exploration_query_time.png","OUR EXPLORATION | AI query time borne by the worker")
    # Own exploration 2: capital ownership changes total-income distribution.
    # Normalize ownership under the SAME quadrature, so distributed rents = mu*r.
    ownership=[]
    fig,axes=plt.subplots(1,2,figsize=(10,4))
    for ax,(a,e) in zip(axes,autos.items()):
        line(ax,e,"auto","Labor income only")
        for label,raw in [("Equal ownership",np.ones(n)),("Top-heavy ownership",e["z"]**4)]:
            density=raw/np.dot(e["mass"],raw)
            total=e["w"]+5*a*density
            assert abs(np.dot(e["mass"],total)-e["output"])<1e-7
            ownership.append(dict(a=a,ownership=label,gini=gini(total,e["mass"]),
                                  bottom=float(total[0]),total=float(np.dot(total,e["mass"]))))
            ax.plot(e["z"],total,label=label,lw=1.8)
        ax.set(title=f"a = {a}",xlabel="Human knowledge z",ylabel="Labor + capital income")
        ax.legend(fontsize=8)
    finish(fig,"exploration_ownership.png","OUR EXPLORATION | Same production, different ownership of compute")
    convergence=[]
    for size in sorted(set([max(51,(n+1)//2),n,2*n-1])):
        base=equilibrium(size)
        aa=equilibrium(size,a=.425,mode="auto")
        bb=equilibrium(size,a=.85,mode="non")
        convergence.append(dict(n=size,pre_bottom=float(base["w"][0]),pre_top=float(base["w"][-1]),
                                basic_bottom=float(aa["w"][0]),advanced_non_top=float(bb["w"][-1])))
    fields=["output","income","mu_i","mu_s","mu_w","r","gap","clearing","violation","complement"]
    cases={"pre":pre,"pre_high_h":high,**{f"auto_{a}":e for a,e in autos.items()},
           **{f"non_{a}":e for a,e in nons.items()}}
    summary={k:{f:float(e[f]) for f in fields} for k,e in cases.items()}
    for k,e in cases.items():
        summary[k]["occupational_masses"]={role:float(e[role].sum()) for role in ["wp","wa","I","sp","sa"]}
    summary.update(grid=n,worker_solver_split=float(pre_cut),bottom_winner_threshold=float(threshold),
                   decomposition=decomposition,convergence=convergence,query_time=query,ownership=ownership)
    (ROOT/"figures"/"diagnostics.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    with (ROOT/"figures"/"wages.csv").open("w",newline="",encoding="utf-8") as handle:
        writer=csv.writer(handle); writer.writerow(["z",*cases])
        writer.writerows(zip(pre["z"],*[e["w"] for e in cases.values()]))
    print(json.dumps({"n":n,"worker_solver_split":pre_cut,"bottom_winner_threshold":threshold,
                      "decomposition":decomposition,"convergence":convergence,
                      "max_accounting_gap":max(e["gap"] for e in cases.values())},indent=2))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n",type=int,default=401)
    main(parser.parse_args().n)
