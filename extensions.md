# Extensions and prior-coverage checks

**PAPER / access boundary.** Page references refer to the supplied, fully read arXiv v12. I did not obtain the Online Appendix or verify the proofs in earlier versions v6/v10. The following inventory records what the main text *says* is covered; it does not pretend to have inspected the unavailable material. The reference list identifies “Ide and Talamàs (2024)” as v6 and the earlier “(2025)” as v10 (p.37). Neither should replace the published citation in the README.

| Candidate already flagged by the authors | Where v12 says it is covered |
|---|---|
| Arbitrarily many layers | Footnote 9, p.10; Section 6, pp.29-30, footnote 22 |
| Perfect AI a=1 and its discontinuity | Footnote 11, p.11; footnote 19, pp.26-27 |
| Limited compute and differing compute levels across autonomy regimes | p.14; p.27; footnote 21, p.30 |
| Multiple AI technologies, including less capable models using less compute | p.16, Online Appendix |
| Finite production opportunities and technological unemployment | pp.16-17, Online Appendix |
| High communication costs h≥h₀ | p.19 cites v6; p.26 cites v10 for possible top losses |
| Firm size, productivity and decentralization | p.22; footnote 20, p.28, Online Appendix |
| AI versus heterogeneous immigration/offshoring | p.31, Online Appendix |
| Different human knowledge distributions and communication technologies across economies | p.32, Online Appendix |
| Lower asking-party costs and additional escalation opportunities | pp.29-30, discussed explicitly |

**INTERPRETATION — Choice.** I selected two quantitative explorations because they target two specific gaps between the wage propositions and the examples: obtaining useful AI advice costs a junior worker time, and labor income excludes ownership of scalable compute. I did not choose “more layers,” “limited compute,” or “multiple models” as original extensions because the paper explicitly flags them as done. A third, dynamic candidate addresses the investment-banking evidence but would require new data and a dynamic solution, so it remains a proposal. These are my explorations, not results attributed to the paper and not claims of literature-wide novelty.

## 1. AI query time that depends on human knowledge — implemented

**PAPER.** The baseline helping cost h is borne by the solver. On pp.29-30 the authors explicitly discuss asking-party time as an alternative to a two-layer limit for explaining selective adoption. Section 7, p.32, also distinguishes automation from lower communication or learning costs. Merely adding asking time is therefore **not a new idea** relative to the paper.

**DERIVATION — Our specification.** Keep two layers and h=0.5, but make a human using AI spend d(z)=1+τ(1−z)² units of time per production opportunity: one for production and τ(1−z) per failed problem to formulate/check a query. Knowledge remains fixed. The human's AI-assisted wage offer becomes

$$w_A(z)=\frac{a-rh(1-z)}{1+\tau(1-z)^2},\qquad z\le a.$$

AI compute use per unit human time is h(1−z)/d(z). Human-human firms and AI-worker firms are unchanged. Independent autonomous AI still pins r=a when compute is abundant; non-autonomous idle compute still pins r=0. The code recomputes all occupational allocations and checks remaining compute. This is an asymmetric friction specifically in human use of AI advice, not an across-the-board change in h and not partial autonomy.

**DERIVATION — Result in our grid.** At a=0.85, increasing τ from 0 to 4 lowers the autonomous bottom wage from 0.425 to about 0.350, below pre-AI ≈0.358; non-autonomous bottom wages fall from 0.85 to the pre-AI value as adoption disappears. At a=0.425, autonomous wages do not change because no human uses an AI solver in the initial equilibrium. These outcomes are reported in [the query-time plot](figures/exploration_query_time.png) and [diagnostics](figures/diagnostics.json), on 201 types. Proposition 5's threshold does not apply unchanged to this altered model.

**OPEN QUESTION.** The inspected main text does not solve this particular knowledge-dependent specification. Its absence from the full Online Appendix is unverified. A useful next check is whether an intermediate τ changes adoption from a bottom interval to an interior interval; the solver allows this rather than imposing the baseline stratification theorem on the extension.

## 2. Ownership of compute: labor-income results versus household income — implemented

**PAPER.** Section 3.1, pp.12-14, introduces compute owners and decomposes total output into labor income and μr. Section 7, pp.32-33, discusses the output/inequality tradeoff and calls for quantification. The propositions compare labor income, not a fully specified joint distribution of earnings and capital ownership.

**DERIVATION — Our accounting experiment.** Assign compute to the same human population with ownership density θ(z), normalized by ∫θ dG=1. Then household income is y(z)=w(z)+μrθ(z). Compare equal ownership θ=1 to top-heavy ownership proportional to z⁴. Hold equilibrium production and μ=5 fixed; rents are distributed, not taxed, and there are no behavioral or general-equilibrium feedbacks from ownership under risk-neutral income maximization. Non-autonomous compute earns zero, so these ownership profiles do not change its income distribution in this model.

**DERIVATION — Result in our grid.** For basic autonomous AI, equal ownership gives a total-income Gini ≈0.096 versus ≈0.587 for top-heavy ownership. Both allocate exactly the same aggregate income, ≈2.885. For advanced autonomous AI the corresponding Ginis are ≈0.027 and ≈0.598. See [ownership plot](figures/exploration_ownership.png). Under equal ownership, even the individual with knowledge a can gain in total income while losing in labor income. This does not contradict Proposition 5.

**INTERPRETATION / OPEN QUESTION.** This experiment demonstrates why a labor-income theorem alone cannot establish a household-income inequality ranking. It is intentionally an accounting exercise, not a calibrated policy evaluation: μ=5 creates large rents, and pre-AI alternative returns to compute are outside the model. No joint ownership/knowledge exercise is stated in the inspected text or its extension pointers; full-appendix coverage remains unverified. Endogenous savings, taxation and compute supply would require a different model.

## 3. Learning from escalations and the junior-senior pipeline — proposed only

**PAPER.** Human knowledge is exogenous (p.10). The Litera survey and Beane–Anthony evidence are connected to occupational shifts and separation from senior solvers on p.24. The bibliography includes Caicedo, Lucas and Rossi-Hansberg (2019) on learning and careers. Section 7, p.32, acknowledges knowledge-acquisition costs as a distinct mechanism already studied elsewhere.

**OPEN QUESTION — Our proposed dynamic object.** Let a junior's next-period knowledge depend on the unresolved problems actually discussed with a human solver: z′=min{1,z+η(s−z)·q_H}, with q_H the frequency of human escalation. Fix the AI technology initially, but let today's matching alter tomorrow's human knowledge distribution. Basic AI may raise junior occupational titles today while shrinking access to expert feedback and future solver supply. A comparison with AI-generated feedback would need a separately identified learning parameter, not the assumption that equal immediate productivity implies equal learning.

**INTERPRETATION.** This candidate is motivated by this paper's concrete evidence, but it is not presented as a discovered theorem or a new learning literature. The available text and footnote inventory do not establish whether this exact dynamic channel is analyzed in the unavailable appendix. I left it uncoded because η and the human-versus-AI learning difference require evidence; an arbitrary dynamic simulation would conceal rather than resolve that uncertainty.
