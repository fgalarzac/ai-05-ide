> **Version read:** the supplied v12 PDF, **39 pages, May 20, 2025**; byte-identical to current [arXiv v12](https://arxiv.org/abs/2312.05481v12), submitted May 17. The course's stated PDF URL returned 404, so a course-copy identity check was unavailable. I also checked Propositions 1-6 against v11 (35 pages, February 25, 2025); their statements match. This does not establish equivalence of other text or proofs.

# Artificial Intelligence in the Knowledge Economy

**Ide, E., & Talamàs, E. (2025).** *Journal of Political Economy*, **133**(12), 3762-3800. [DOI: 10.1086/737233](https://doi.org/10.1086/737233).

**PAPER — Question and problem.** How does scalable AI knowledge reorganize workers, solvers, their matches, and labor income? Humans maximize income; competitive firms choose their configuration and worker/solver knowledge to maximize expected output less wages and compute rent. Humans have unit time and knowledge distributed with continuous, strictly positive density on [0,1]; problems have difficulty U[0,1]. A worker of knowledge z requires h(1-z) solver time, so n(z)=1/[h(1-z)]. Firms have at most two layers, complete information, free entry, and zero profits. Their possible profits, with a=z_AI and z≤s, are

$$z-w(z),\quad a-r,\quad n(z)[s-w(z)]-w(s),\quad n(z)[a-w(z)]-r\ (z\le a),\quad n(a)[s-r]-w(s)\ (a\le s).$$

Human and compute markets clear. Production opportunities exceed resources; compute is abundant relative to human time. For the results below, **0<h<h₀(G), 0≤a<1**, with the same compute supply in both AI regimes. No-AI occupations obey W⪯S and w(z)>z; human matching is strictly positive assortative. Autonomous AI can occupy all roles; residual independent AI production pins r*=a and w*(a)=a<w(a). Non-autonomous AI can only solve; idle compute pins r⋆=0. These are separate restrictions from capability.

**PAPER — Proposition 5, fully stated.** Define B={z∈[0,a]:w*(z)>w(z)} and T={z∈[a,1]:w*(z)>w(z)}. There exists **ā∈int W** such that **B≠∅ iff a>ā**; **T≠∅ for every a∈[0,1)**. Winners, when present, occupy bottom and top intervals; the matching type a loses. Strict equality a=ā gives no bottom winners. The all-capabilities top result requires h<h₀ and excludes a=1.

**PAPER — Proposition 6, fully stated.** Non-autonomous equilibrium is unique, efficient, maximizes labor income, and has r⋆=0. If a≤w(0), AI is unused and human wages and occupations remain pre-AI. If a>w(0), W⋆ₐ⪯(W⋆ₚ∪I⋆∪S⋆ₚ), with all these sets nonempty except possibly I⋆: only the least knowledgeable use AI solvers. In every case:

1. Output is strictly higher with autonomous AI.
2. Some z∈(0,1] satisfies w⋆(z)≤w(z), strictly when a>w(0).
3. Some ε>0 satisfies w⋆(z)≥max{w(z),w*(z)} for every z∈[0,ε), strictly when a>w(0).
4. Some ε>0 satisfies w⋆(z)≤w*(z) for every z∈(1−ε,1], strictly for z≠1. The statement allows equality at 1.

**INTERPRETATION — The trap.** The ā threshold concerns **capability conditional on autonomy**; autonomy separately changes feasible roles and rent. Thus both dimensions matter. Even some *basic* autonomous AI (ā<a<sup W) benefits the bottom. “Autonomy, not capability” is incorrect; “only advanced AI benefits the bottom” is also incorrect. Section 7's broad language does not override these qualifications.

**DERIVATION — Numerical illustrations, not proofs.** [sim.py](sim.py) reproduces wage comparisons underlying Figures [3](figures/fig03.png), [4](figures/fig04.png), [5](figures/fig05.png), [7](figures/fig07.png), and [9](figures/fig09.png), using G(z)=z, h=0.5, a=0.425/0.85 and abundant μ=5; Figure 3 also uses h=0.8125. The [capability scan](figures/capability_threshold.png) gives ā≈0.715, below the pre-AI split ≈0.764; non-autonomous adoption instead starts above w(0)≈0.358. These are grid approximations.

Run `python -m pip install -r requirements.txt`, then `python sim.py --n 401`. [Analysis](analysis.md) explains mechanisms, discrete structure and checks; [extensions](extensions.md) distinguishes our query-time and ownership experiments from author-flagged extensions. [Raw prompt/output](prompts.md) preserves the calculation error and correction. The handwritten photo is [pending](hand/PENDING.md).
