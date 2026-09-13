# Reading notes and numerical analysis

Labels distinguish **PAPER** (what v12 states), **DERIVATION** (our algebra or computation), **INTERPRETATION** (our reading of the mechanism), and **OPEN QUESTION** (not established here). Page numbers are printed v12 pages. The README is the short course summary; these notes supply the detail without turning it into a long survey. Source and access qualifications are in [paper/README.md](paper/README.md).

## 1. What is scarce, and why AI is a different shock

**PAPER — Sections 2-3, pp.7-16.** Tacit knowledge is embodied in people who cannot write a complete contingent plan before production. A worker discovers a problem only while pursuing an opportunity; consulting an expert consumes that expert's time whether or not the expert can solve it. People differ in the fraction of problems they can solve. The uniform difficulty distribution is a normalization of this fraction, not a claim that human knowledge must be uniformly distributed. The theory permits any continuous, strictly positive human density g; the figures happen to use G(z)=z.

The three developments motivate three distinct assumptions:

| Development documented by the paper | Modeling consequence | Example and its role in the argument |
|---|---|---|
| AI applies tacit-like knowledge at scale | A trained capability a can be copied across μ units of inference compute, instead of being limited to one person's time | Klarna's reported automation of customer-service roles illustrates AI pursuing production opportunities |
| Shared foundation models handle diverse tasks | Firms access a common, exogenously given knowledge technology | Harvey uses a foundation model in legal work; the example motivates shared capability, not identical real-world adoption constraints |
| Agents can execute work autonomously | AI may initiate production as well as answer escalations | Agentforce's contacting prospects and scheduling meetings illustrates the production role; GitHub Copilot's code suggestions illustrate assistance |

**INTERPRETATION.** Harvey is also a useful warning against equating useful legal advice with full autonomy: the paper notes that document analysis does not imply representing clients or arguing cases. These are the authors' historical examples, not independently verified claims about what those products can do in 2026. They anchor model roles, not a calibration. Workers pursue opportunities; they do not create them (footnote 15). This distinction matters even for a=0: an autonomous agent can bring a problem to a human solver without solving any problem itself.

**PAPER — Section 5.1, p.24.** The Litera (2022) survey reports junior M&A lawyers moving from routine document work toward complex responsibilities, consistent with basic AI moving marginal workers into solving. Beane and Anthony (2024) describe junior investment bankers losing direct contact with senior partners as AI takes over tasks; this is consistent with the best solvers switching toward AI production and worse support for remaining human workers. **INTERPRETATION:** these observations illustrate the two distinct margins in Propositions 3 and 4; they are not causal tests of a general-equilibrium model.

## 2. Pre-AI: occupations, matching and the wage premium

**PAPER — Proposition 1, pp.17-19.** Single-layer firms hire an independent producer and obtain expected output z. Two-layer firms hire one solver of knowledge s and n(z)=1/[h(1−z)] workers of knowledge z≤s. Output is n(z)s; solver time is fully used. Competitive equilibrium is unique and output-efficient, with W⪯I⪯S, nonempty W and S, and a strictly increasing human match m. I is nonempty iff h>h₀. The wage schedule is continuous, strictly increasing and convex, strictly convex within worker and solver regions:

$$w(z)=m(z)-h(1-z)w(m(z))\quad(z\in W),\qquad w(z)=z\quad(z\in I),$$
$$w(s)=C+\int_{\inf S}^{s}n(e(u))\,du\quad(s\in S),\qquad e=m^{-1}.$$

C>inf S for h<h₀, and C=inf S otherwise. Thus w(z)>z outside cl I; with h<h₀, the inequality holds for everyone. At h=h₀, I has no positive interval but the occupational boundary is a corner where equality can occur. The clean all-human strict premium used by later comparisons therefore requires h<h₀.

**INTERPRETATION.** More knowledgeable humans have a comparative advantage in solving because their knowledge can affect several problems. Lower-knowledge humans benefit more from being assisted than from working independently. Worker knowledge also increases the team size one solver can handle. The return to higher solver knowledge is consequently larger with better workers, generating positive assortative matching. These are organizational gains; w(z)>z compares a person's equilibrium marginal value with solo output, not with total firm output per worker.

**DERIVATION.** Market clearing is ∫Y h(1−u)dG(u)=∫m(Y)dG(u), giving g(m(z))m′(z)=h(1−z)g(z). The solver hiring condition gives w′(m(z))=n(z). The solver's marginal return to knowledge exceeds one, whereas a worker's marginal knowledge saves only part of the solver's time. Wage continuity, no positive profits and occupation choice pin the boundary, rather than an arbitrary division of a firm's surplus.

**PAPER / INTERPRETATION.** The restriction h<h₀ removes pre-AI independent producers and makes team-size amplification strong enough for the unconditional top-winner result. It is substantive for Proposition 5, not just a harmless simplification. The paper explicitly says top earners can lose for h≥h₀ in an earlier version (p.26), and at a=1 in the Online Appendix (footnote 19). For the figures G(z)=z and h₀=3/4; this is not a distribution-free value.

## 3. Autonomous AI: all five configurations

**PAPER — Proposition 2, pp.19-21.** There are human independent firms, human-worker/human-solver firms, AI independent firms, AI-worker/human-solver firms, and human-worker/AI-solver firms. An AI/AI hierarchy is wasteful because both layers know exactly the same problems. Positive assortative matching and stratification extend to the post-AI equilibrium, which remains unique and efficient. Specifically W*⪯I*⪯S*, W*⪯{a}⪯S*, W*ₐ⪯W*ₚ and S*ₚ⪯S*ₐ. Subscript p means a human partner, and subscript a an AI partner.

Compute abundance means some compute cannot be matched to scarce human time and must produce independently. Zero profit there pins r*=a. An AI agent can substitute for a human with exactly that knowledge, pinning w*(a)=a. A sufficient abundance condition from footnote 14 is

$$\mu>\int_0^a h(1-z)\,dG(z)+n(a)[1-G(a)].$$

For G(z)=z, h=.5 this right side is .5(a−a²/2)+2<2.25; μ=5 is sufficient for all the capabilities we simulate. AI is always an independent producer. If a∈W, it must additionally be a worker; if a∈S, it must additionally be a solver. Both additional roles may coexist. The main text defers the complete simultaneous-role classification to the Online Appendix, so these two implications should not be rewritten as exclusive roles.

Zero profit gives w*(z)=a[1−h(1−z)] on W*ₐ and w*(s)=(s−a)/[h(1−a)] on S*ₐ. Human-human firms obey the same matching and wage equations as before, with new boundaries; human independent producers earn z. Continuity determines human-solver wage integration constants. AI-assisted wages are linear in human knowledge, while human-human wage segments are strictly convex.

**DERIVATION.** The code admits an AI role only when its zero-profit wage offer beats the competing feasible uses of that human type. It then recovers the allocation and checks compute clearing. In the figure parameterizations, a=.425 uses AI as workers and independent producers, while a=.85 uses all three AI roles. This is a computed classification of these parameterizations, not a claim to have recovered the unavailable appendix's general classification.

## 4. Section 5: displacement and the people who stay in their occupations

**PAPER — Proposition 3, p.23.** If a∈int W, then W*⊂W and S*⊃S: basic autonomous AI displaces humans from routine production into specialized solving. If a∈int S, then W*⊃W and S*⊂S: advanced autonomous AI displaces humans in the opposite direction. These are occupational changes, not unemployment; abundant production opportunities keep every human employed in some capacity. Boundary cases are excluded from this strict comparison.

**PAPER — Proposition 4, p.23.** Worker productivity means expected output per worker's time, equal to the knowledge of the matched solver. Solver span of control is the number of supervised workers, increasing in their knowledge. For people **not displaced from the relevant occupation**:

| Capability | Worker productivity | Human solver's span of control |
|---|---|---|
| a∈int W | Strictly lower for every z∈W*⊂W | For s∈S⊂S*, strictly higher if e(s)<a, strictly lower if e(s)>a |
| a∈int S | For z∈W⊂W*, strictly higher if z<e(a), strictly lower if z>e(a) | Strictly higher for every s∈S*⊂S |

The strict clauses do not assert a sign at equality. With basic AI, top human solvers turn toward AI workers and marginal humans enter solving, worsening the support available to remaining human workers. Yet top solvers may supervise **fewer** workers than before when their pre-AI human employees were more knowledgeable than AI. Their wages can still rise, because a wage change is not a productivity or team-size change alone.

## 5. Proposition 5: separating a match from its price

**PAPER — pp.25-27.** Total labor income increases after autonomous AI: otherwise the pre-AI organization of production could earn positive aggregate profits at post-AI wages. Output also increases. This aggregate gain coexists with w*(a)=a<w(a) and losses around the directly substituted knowledge level. Winners are located in intervals at the two extremes. Proposition 5's full conditions are in the README.

**DERIVATION — Explicit accounting convention for Figure 7.** For the bottom worker let s be the solver's knowledge and p=w(0)/s the worker's share of output. For the top solver, let N be the team size and q=w(1)/N the solver's share of firm output (the top solver solves all problems, so firm output is N). Changing the match first while holding the old share fixed yields exact identities:

$$\Delta w(0)=\underbrace{p_0(s_1-s_0)}_{\text{match}}+\underbrace{s_1(p_1-p_0)}_{\text{share}},$$
$$\Delta w(1)=\underbrace{q_0(N_1-N_0)}_{\text{match}}+\underbrace{N_1(q_1-q_0)}_{\text{share}}.$$

These are our transparent accounting conventions for the authors' mechanism, not unique causal decompositions or equilibrium counterfactuals. Reversing the order reallocates an interaction term. The [Figure 7 illustration](figures/fig07.png) computes them from equilibrium matches and wages, using actual worker mass per solver for N when grid atoms split matches.

**PAPER / INTERPRETATION.** For basic AI, the bottom's solver is worse, so its match effect is negative. But the newly marginal solver earns solo output rather than the old solver's organizational premium; the worker's share rises. The share effect wins only when a>ā. For advanced AI the bottom's match and share both improve. At the top, basic AI can worsen worker quality and shrink the team, but workers' cheaper price increases the solver's share sufficiently to dominate under h<h₀. The top always gains somewhere near 1 for every a<1; do not extrapolate the *negative* top match effect from the basic case to all advanced cases.

**DERIVATION.** At a=.425 our 401-type calculation gives bottom match −0.1080, share +0.0166 and net −0.0914; at the top the corresponding components are approximately −0.9150, +1.3385 and +0.4235. Thus a positive share effect does not establish that the bottom benefits. The basic/advanced occupational cutoff is ≈.764; the bottom-winner threshold is ≈.715. For example a=.75 is still basic but can benefit the bottom, despite worsening its match.

**INTERPRETATION — Autonomy versus capability.** In Proposition 5, ā is a capability threshold *inside the autonomous regime*, determined by the pre-AI economy's G and h. Autonomy is not a continuously varying argument of that particular proposition. Proposition 6 separately changes the technology's feasible occupations and equilibrium rent. Thus the full distributional comparison involves **both** dimensions. Section 7's “Co-pilots vs. Co-workers” discussion is a broad interpretation; it does not say all autonomous AI harms the bottom, or all basic AI does so. Nor does the bottom necessarily have to use AI directly to experience a wage effect.

## 6. Non-autonomous AI: useful advice can create losers

**PAPER — Section 6, pp.27-30.** Removing production roles eliminates AI independent production and AI-worker firms. The remaining configurations are human independent production, human-human hierarchies and human-worker/AI-solver firms. Some compute is idle, so r⋆=0; a human of knowledge a is no longer interchangeable with an AI agent because the human can produce. AI-assisted workers receive w⋆(z)=a where that arrangement is active. The adoption condition is a>w(0), not a>sup W and not a>ā. At or below w(0) there is no positive-measure adoption and the pre-AI allocation is unchanged.

**INTERPRETATION.** Only the least knowledgeable adopt because each worker has just one escalation opportunity: using a free but mediocre AI solver can forfeit a much better human match. Free compute does not make that lost option free. The restriction to two layers therefore matters even when h is paid entirely by the solver. The authors discuss additional layers and asking costs explicitly on pp.29-30.

**PAPER.** The four numbered comparisons are stated in full in the README, including weak inequalities when AI is unused and the possible equality at z=1 in the top comparison. Non-autonomy maximizes labor income within its own feasible technology, because capital earns zero; it does **not** maximize total output across autonomy regimes. At a>w(0), some humans strictly lose relative to pre-AI even though the bottom strictly gains. Advisory substitution and re-matching can harm human solvers. Autonomous AI gives higher output because it can use compute for additional production instead of leaving it idle.

**INTERPRETATION.** “Non-autonomous AI benefits the least knowledgeable” needs the distinction between strict gains when adopted and unchanged wages when not adopted. “Autonomous AI mainly benefits the top” describes a comparison, not a theorem that every inequality statistic rises. Neither sentence erases capability.

## 7. A finite-type economy the student can check

**DERIVATION — Sketch, not a completed handwritten proof.** Replace G by masses p_L,p_H>0 at z_L<z_H (or add a middle type), with total mass one. Keep divisible populations: a type may split between occupations. A human hierarchy employing t low-type workers uses h(1−z_L)t high-type solver time and yields z_H t. Independent output, time feasibility, and no-positive-profit inequalities remain essential; the single equation n(z_L)w_L+w_H=n(z_L)z_H does not generally pin both wages.

If high types remain independent, their outside option can pin w_H; if all high types solve, another active use or complementary-slackness condition is needed. At exact mass balance p_L=n(z_L)p_H, an interval of wage divisions may support the same allocation. This finite-type nonuniqueness is compatible with the continuum uniqueness theorem, which assumes a positive continuous density. Do not claim the two-type model automatically has Proposition 5's interval geometry or a unique threshold.

Autonomous AI adds a scalable type a and the two human-AI activities; include μ and residual independent AI before substituting r=a. Non-autonomous AI removes production activities and leaves unused compute. Comparing feasible allocations before and after either technology then illustrates the mechanisms in Sections 3-5. A third human type makes it easier to see a marginal occupation switch, but does not eliminate the need to check all alternative configurations. The specific suggested handwritten exercise is supplied separately to the student, rather than placed in the repository as a finished derivation.

## 8. Numerical method, evidence and limits

**DERIVATION.** The code approximates G(z)=z by trapezoidal masses on n grid points, including 0 and 1. It solves the linear-program wage dual

$$\min_w\sum_i p_iw_i\quad\text{s.t.}\quad w_i\ge z_i,\qquad w_i+h(1-z_i)w_j\ge z_j\quad(i<j),$$

plus wage lower bounds from each feasible human-AI configuration. Minimizing the wage bill here is a **dual computation**: its value equals maximum feasible human contribution to output after pricing AI opportunity costs. It is not an assumption that firms collude to suppress wages. The inequality is the human-human firm's no-positive-profit condition per worker; active configurations satisfy zero profit. Dual multipliers recover production, occupations and matches, including splitting grid atoms. Independent AI's μa is added back to obtain total autonomous output; idle compute contributes zero in the non-autonomous case.

Checks include human resource clearing, unused-compute positivity, nonnegative profits' absence, zero-profit complementary slackness, weak assortative matching of active discrete pairs, and output=aggregate wages+μr. Additional checks cover unused non-autonomous AI below its adoption cutoff, occupational directions for the two figure cases, and the bottom/top and output comparisons. These validate the implemented finite economy and illustrations, not all continuum propositions.

| Case, μ=5 where applicable | Labor income | Total output |
|---|---:|---:|
| No AI, h=.5 | .69234 | .69234 |
| Autonomous, a=.425 | .76017 | 2.88517 |
| Non-autonomous, a=.425 | .69578 | .69578 |
| Autonomous, a=.85 | .71334 | 4.96334 |
| Non-autonomous, a=.85 | .87075 | .87075 |

The high autonomous totals include independent AI production, and should not be described as gains in human wages. μ=5 is an illustrative abundance choice, not a fitted compute quantity.

At 201, 401 and 801 types, selected endpoint wages move by less than .008, with non-monotone discretization error. Therefore the reported threshold is approximate (about .715), not an exact estimate to six decimals. The finite LP can have multiple supporting wage vectors and split occupations at grid boundaries. Accounting residuals below 2×10⁻⁷ do not measure approximation error relative to the continuum. The default reproduction grid is 401; the broad capability scan and query-time exploration use 201 for speed. Figure 3's h=.8125 case illustrates Proposition 1 only; later strict results retain h=.5<h₀.

All numerical figures are **illustrations of existing results**, except the two plots explicitly headed **OUR EXPLORATION**. [figures/diagnostics.json](figures/diagnostics.json) records allocations, residuals, convergence, the decomposition and extension results; [figures/wages.csv](figures/wages.csv) contains wage curves. The program is deterministic and uses no fitted data or randomized draws. Tested with Python 3.11.11, NumPy 1.26.4, SciPy 1.17.1 and Matplotlib 3.10.0.

**OPEN QUESTION.** Nothing here supplies the unavailable appendix's proofs, a causal test of the examples, or a rigorous continuum derivation from the numerical grid. Those boundaries are deliberate and visible.
