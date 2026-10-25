# Acquisition Decision Tasks
## Evidence Changes. The Decision Should Follow.

**Nicholas Lauga**  
**Technical showcase · October 2026 · Version 0.1.13**

*Research direction and underlying acquisition judgments are human-led. The fictional demonstrations, supporting calculations, explanatory writing and task construction were developed with artificial intelligence assistance. This technical showcase has not undergone independent scholarly peer review.*

## Abstract

Buying a small business requires decisions that evolve as new facts arrive. Reported earnings may be corrected, financing conditions may change, and permissions to review information may be withdrawn or restored. An artificial intelligence system that continues repeating its earlier recommendation may therefore become inaccurate or inappropriate.

**Acquisition Decision Tasks** presents a practical approach for evaluating whether models detect these changes, use the information available at a specified decision time, follow constraints and select defensible next actions. Two fictional demonstrations show the idea: a business whose lower asking price conceals weaker earnings, and a diligence process that must pause and later resume when document access changes.

The broader research draws on **Nicholas Lauga's original written acquisition records, professional reasoning and personally selected decisions**, with artificial intelligence assisting in organizing these materials into structured research and task workflows. In a matched fine-tuning experiment, Qwen2.5 models with 7 billion and 14 billion parameters each learned from **the same 20 structured acquisition decision scenarios**. One training version used Nicholas Lauga's personally selected next actions; the other used actions selected by Qwen. **The scenarios and training settings were identical; the source of the decision labels was the controlled difference.** Across three fixed training seeds, the versions trained with his judgments scored an average **3.3 percentage points higher at 7B** and **5.0 points higher at 14B** on the same 40 development questions. A separate smaller-model study also found an average gain in the same direction. The results offer **positive preliminary evidence for the value of human-selected acquisition judgments**. They come from fictional structured examples and a limited, previously used development set, so they do not yet establish a statistically reliable gain across all acquisition tasks.

## 1. The problem: A correct decision can become incorrect

A broker reports that a business is profitable. The prospective buyer begins evaluating it. A few days later, additional costs emerge. The business is still for sale, perhaps at a lower price, but the investment may now be less attractive.

In a different acquisition, the seller initially allows the buyer to view financial and customer information. The seller then suspends access and later restores permission to review only a redacted financial summary. Even an otherwise sensible diligence step may be inappropriate if the information required is no longer authorized for that use.

These situations share a central challenge: **the recommendation should reflect the latest reliable information that the decision-maker is permitted to use**.

A useful system must answer not only “What is the number?” but also:

- What information was known at the decision time?
- What changed, and which earlier assumptions are now obsolete?
- Which facts are established, and which remain requested or uncertain?
- What actions are permitted under the current constraints?
- What next step is supported, without assuming an offer has been accepted or a transaction completed?

We propose making those behaviors observable through source-grounded, time-specific acquisition decision tasks.

## 2. How the approach relates to existing research

Financial and legal artificial intelligence evaluation is already a developed research area. **FinQA** evaluates numerical reasoning over financial reports; **ConvFinQA** examines chains of financial reasoning across a conversation; **MAUD** contains expert-annotated merger-agreement interpretation questions; and **FinanceBench** studies evidence-supported financial question answering. [1–4]

Our proposed narrower focus is on **changing acquisition decisions**: identifying the information available at each point, recognizing permission and evidence changes, and distinguishing the next action a human took from the action a professional reviewer would consider acceptable.

This is a candidate area for useful evaluation work, **not a claim that temporal reasoning, financial arithmetic, document citations or acquisition evaluation were invented here**. Whether authentic decision trajectories deliver a measurable advantage beyond well-designed generic examples remains an open research question.

## 3. Example 1: When a cheaper business turns out to be a worse deal

### The situation

Imagine you are considering buying a small business.

The broker initially reports **$310,000 in adjusted annual earnings** and an asking price of **$1,080,000 Canadian**. At first glance, the price is approximately 3.5 times reported annual earnings.

A week later, the seller reduces the asking price by $150,000 to **$930,000**.

That sounds encouraging. But the buyer discovers that the business will cost substantially more to operate than the broker's presentation suggested.

**The question:** Does the lower asking price actually make the business a better acquisition, and what is the highest price permitted by the buyer's own financial rules?

### How the situation changes

| Date | New information |
| --- | --- |
| April 1 | The broker reports adjusted annual earnings of $310,000 and an asking price of $1,080,000. |
| April 7 | The seller indicates a lower, nonbinding price of $930,000. |
| April 7 | The buyer learns that replacing the current owner with a manager would cost $70,000 per year. |
| April 7 | The buyer confirms that $18,000 of legal expenses excluded from reported adjusted earnings are recurring. |
| April 8 | Financing amounts, annual loan payments, closing expenses and required operating cash are available for the screening decision. |

*All facts, dates and financial amounts in this example are fictional.*

### Correct the earnings first

The company cannot be evaluated using the broker's original earnings figure without adjusting for continuing expenses.

| Annual earnings calculation | Amount |
| --- | ---: |
| Broker's adjusted annual earnings | $310,000 |
| Less replacement manager | −$70,000 |
| Less recurring legal expenses | −$18,000 |
| **Corrected maintainable annual earnings** | **$222,000** |

The manager expense is deducted once. The buyer must not mistakenly deduct the former owner's compensation a second time.

### Apply the buyer's financial constraints

Assume the buyer has access to the following fixed hypothetical financing:

| Financing or closing item | Amount |
| --- | ---: |
| Bank loan | $700,000 |
| Seller-provided loan | $90,000 |
| Buyer's cash available before closing | $230,000 |
| Total annual loan repayments | $138,000 |
| Closing expenses | $24,000 |
| Initial working capital | $42,000 |

The buyer has established three screening requirements:

1. **Price:** Pay no more than four times corrected maintainable annual earnings.
2. **Repayment:** Corrected maintainable annual earnings must be at least 1.5 times annual loan repayments.
3. **Liquidity:** Retain at least $50,000 in buyer cash after the purchase and stated closing requirements.

For this simplified exercise, the loan principal and annual repayment amounts remain fixed as the proposed purchase price changes.

**Price check:** $930,000 ÷ $222,000 = **4.19 times** annual earnings. This fails the maximum multiple of four.

**Repayment check:** $222,000 ÷ $138,000 = **1.61 times** annual repayments. This passes the required 1.5 ratio. It is a simplified screening ratio, not a lender-approved cash-flow or debt-service assessment.

**Cash check at $930,000:**

| Cash remaining calculation | Amount |
| --- | ---: |
| Initial buyer cash | $230,000 |
| Buyer's contribution to purchase price after the $790,000 combined loans | −$140,000 |
| Closing expenses | −$24,000 |
| Working capital | −$42,000 |
| **Cash remaining** | **$24,000** |

This fails the $50,000 cash-reserve rule.

### The appropriate next decision

**Do not agree to $930,000. Consider revised, nonbinding terms at or below an indicative $888,000, subject to further verification.**

The earnings-based price ceiling is **4 × $222,000 = $888,000**.

The liquidity-based price ceiling is **$904,000**, calculated from fixed debt of $790,000, available cash of $230,000, closing costs of $24,000, working capital of $42,000 and a required reserve of $50,000.

The lower ceiling, **$888,000**, governs. At this price, the buyer would retain **$66,000** and pass all three fictional screening constraints.

This is **not** an independent appraisal, approved bank financing, accepted offer or completed purchase. Real due diligence would still require verification of earnings quality, owner replacement costs, available financing and working capital needs.

**What the task tests:** Can the model replace outdated financial assumptions, avoid counting an expense twice, apply multiple constraints and revise the recommended acquisition terms even when the asking price has fallen?

## 4. Example 2: When permission to review a business disappears and then returns

### The situation

Imagine considering another small business acquisition. The seller provides an online document room containing a financial summary and a client list.

You want to involve an accountant. However, the seller controls **which people may view which documents and for what purpose**.

At first, the buyer may read both documents. Later, the seller temporarily suspends access. Finally, the seller restores a narrower permission to view updated financial information, while keeping the client list restricted.

**The question:** Should the buyer continue, pause or resume a limited investigation as the seller's instructions change?

### How the situation changes

| Date and time | What happens | Consequence |
| --- | --- | --- |
| April 2 | The seller permits the buyer to view a financial summary showing $248,000 in annual earnings and a client list. The accountant requires separate authorization. | Buyer may conduct the initial permitted review. |
| April 3 | The accountant signs a non-disclosure agreement, promising to keep information confidential. Document access has not been separately activated. | The signature alone does not permit accountant access. |
| April 4, 10 a.m. | The seller suspends access to the financial summary and client list and directs the team not to continue using the earlier materials until permission is restored. | **Pause the document-based investigation.** |
| April 4, 11 a.m. | The seller prepares a replacement summary reducing annual earnings to $216,000 after identifying $32,000 in omitted recurring wages. The buyer has not yet been granted access to it. | Do not pretend the buyer has already reviewed that new document. |
| April 4, noon | The seller permits the buyer and named accountant to view the corrected, partially redacted summary. Separate accountant access is activated. The client list remains restricted. | **Resume only a limited financial review.** |
| April 5 | The lender indicates that financing remains conditional. No binding acquisition offer has been accepted or authorized. | Continue limited diligence without assuming a completed deal. |

*All people, documents, permissions and numbers are fictional. Times are Coordinated Universal Time.*

### Why the difference matters

Viewing a document does not automatically permit downloading it. A confidentiality agreement is not automatically permission to access restricted files. The right to ask an accountant to review a specified summary does not authorize sharing a client list. Nor does viewing permission necessarily allow submission to an external artificial intelligence service.

In this exercise, neither downloading nor external artificial intelligence processing is ever authorized.

The model needs to apply the **permissions valid at the time of the requested action**, rather than relying on old permissions or later events.

### The three correct decisions

| Decision time | What is currently permitted? | Correct next action |
| --- | --- | --- |
| **April 2:** Initial review | Buyer may view initial summary and client list; accountant is not authorized yet. | **Continue preliminary review.** |
| **April 4, 10:30 a.m.:** Suspension | Neither party has a current route for reviewing those documents, and the seller has prohibited continued use of the earlier materials. | **Pause document-based review and request authorization.** |
| **April 5, noon:** Limited restoration | Buyer and named accountant may view the corrected, redacted summary; client list remains restricted. | **Resume limited financial review.** |

The progression is the point: **continue, pause, and later resume under narrower conditions**.

The buyer is not required to abandon the acquisition permanently. The buyer also cannot assume that the return of one financial document restores every earlier permission.

### The appropriate final decision

At the final decision point, the buyer may continue limited review using the authorized redacted summary showing **$216,000** rather than the earlier **$248,000**.

The buyer may involve the named, authorized accountant within the viewing restrictions. However, the buyer must request separate permission for client-level records, downloads or external artificial intelligence processing. Conditional financing must be verified before proposing an appropriately authorized offer.

No purchase is agreed or completed.

**What the task tests:** Can the model distinguish a request from an approval, track authorization over time, refuse to act on revoked permissions, use the newest available financial figure and recommend an appropriately limited next step?

## 5. Turning examples into evaluable tasks

The two cases above are **explanatory demonstrations**. To become reliably scored model evaluations, their stories must be represented as dated source packets with explicit expected outputs.

A task package should contain:

| Element | Purpose |
| --- | --- |
| **Decision-time cutoff** | Defines what evidence the model can know at the moment being tested. |
| **Permitted source documents** | Provides dated, versioned facts and restrictions, with stable source identifiers. |
| **Question and response format** | States which calculations, decisions, explanations and unknown values must be returned. |
| **Separate reference answers** | Holds expected facts, derivations, source support and acceptable action alternatives, with review status. |
| **Scoring program** | Checks numerical accuracy, date and permission logic, source support and required response structure. |
| **Provenance and rights record** | Distinguishes origins, author contributions, privacy restrictions and permitted evaluation or training uses. |

At an April 4 decision checkpoint, for example, an artificial intelligence model must not be shown the April 5 outcome. Nor should a later correction be treated as if it were already accessible to the buyer when the initial recommendation was made.

A complete evaluation should score **correct facts, sufficiently supported citations, compliance with the response format, appropriate uncertainty and the next action** separately. It should distinguish failures of reasoning from failures caused purely by an answer-format requirement.

The public technical showcase now includes **two fictional acquisition scenarios represented by four time-specific decision questions, with 30 reference fields**. The accompanying fictional source packets record what information is available at each decision cutoff, and the deterministic scorer has passed **15 offline regression and negative-control tests**. Four example responses constructed directly from the provisional references pass all four questions. This demonstrates **software self-consistency, not Qwen model accuracy, independent professional judgment or performance on unseen acquisition decisions**. These public examples are separate from the Qwen experiments reported in Section 7.

Software correctness is not equivalent to professional agreement on the best acquisition decision.

## 6. Why actual human decision histories may be more valuable

The long-term research opportunity is not simply to generate thousands of fictional acquisition questions. It is to preserve authentic decision trajectories, subject to permissions, that show:

**Evidence available at the time → human judgment and alternatives → action selected → new evidence or constraints → revised judgment → later observed response or outcome.**

A bounded internal inventory audit identified **50 normalized financial and commercial decision records across 45 opportunity identifiers**. Twenty records reflected repetitive screening patterns, while 30 reflected more varied decision types. A separate acquisition inventory recorded ten source groups with outbound action evidence and five later-process signals.

These are overlapping inventory views, **not 60 independent, commercially licensable tasks**. They are also not proof that any transaction created a positive financial return. Historical owner decisions are real human selections where their sources support that attribution; subsequent task wording, mathematical support and scenario construction can still involve artificial intelligence assistance.

This distinction is central to the proposed product:

- **Observed human action:** What the decision-maker actually chose. Useful for studying or predicting real workflow behavior.
- **Objectively checkable answer:** A financial calculation or factual interpretation verifiable against permitted source evidence.
- **Professionally preferred action:** A recommendation requiring appropriate independent judgment and a defensible set of acceptable answers.
- **Observed business outcome:** What subsequently happened, when actual evidence supports it, rather than an outcome invented to complete a story.

The project's own past work has also included independent practitioner input on operational acquisition risks. Such input can help identify missing decision variables, but it must not be misrepresented as independent review of fictional task answers.

These time-stamped, human-led decision histories offer a potential source of richer training and evaluation tasks. The next research phase will measure which task types and model capacities can make productive use of that context.

## 7. What our Qwen experiments actually demonstrate

We have conducted several archived exploratory tests using downloadable **Qwen open-weight models**.

Open-weight models provide downloadable numerical model parameters under applicable licenses. In **fine-tuning**, additional parameters are optimized from example inputs and expected outputs. In **inference-only testing**, the existing model is prompted or evaluated without changing its weights. These are distinct interventions.

The experiments below took place **before and separately from the two revised fictional examples in Sections 3 and 4**.

### 7.1 Actual model fine-tuning with owner-selected judgments

In an initial experiment, we assembled **20 structured fictional acquisition scenarios** and paired each with two alternative next-action labels: a judgment personally selected by Nicholas Lauga and an action selected by a model. **The owner's decisions supplied the human-origin judgment signal; artificial intelligence assisted in constructing and formatting the illustrative scenarios.**

Using **Qwen3 with 1.7 billion parameters**, the study trained small additional parameter sets with **Low-Rank Adaptation**, a method that modifies model behavior without retraining all original weights. Twelve adapters were trained across four configurations and three random initializations.

Evaluation used 40 artificial-intelligence-written development cases, including dependent pairs across five public-guidance families.

| Training condition | Average agreement with provisional reference answers |
| --- | ---: |
| Original model without task-specific training | **57.5%** |
| Fine-tuned using model-selected labels | **62.5%** |
| Fine-tuned using Nicholas Lauga's selected labels | **65.0%** |

The owner-label condition averaged **2.5 percentage points** above the model-label condition. However, the exploratory uncertainty interval ranged from **minus 5.0 to plus 7.5 percentage points**. It includes zero, meaning no reliable owner-label advantage was established.

The broader research is grounded in **Nicholas Lauga's original human-written acquisition records, professional reasoning and decisions**. Artificial intelligence has been used to organize and structure project materials into evaluation formats designed to limit the exposure of private and confidential information.

For this particular training experiment, the model-facing scenarios were constructed as fictional cases rather than reproductions of confidential acquisition records. Nicholas Lauga personally selected the decision labels used in the human-judgment training condition.

The distinction is important: **the underlying professional judgment is human-origin, while artificial intelligence assists with structuring, calculations and preparation of the evaluation materials.**

### 7.2 A second real fine-tuning experiment using public legal examples

In a separate experiment, we trained two Low-Rank Adaptation adapters for **Qwen2.5 with 0.5 billion parameters** on publicly sourced merger-agreement classification examples. Both versions used the same 96 training examples from 53 source agreements. One used source expert labels; the other used the model's own selected labels.

Testing used 122 cases drawn from 35 other agreement identifiers.

| Training condition | Correct answers |
| --- | ---: |
| Original model | **62 of 122 (50.8%)** |
| Fine-tuned using model-selected labels | **65 of 122 (53.3%)** |
| Fine-tuned using public expert labels | **68 of 122 (55.7%)** |

The expert-label advantage over model-selected labels was approximately **2.1 percentage points** after balancing by agreement. Its uncertainty interval included zero. A simple majority-label control also scored **69 of 122**.

This was a real, archived model-training exercise, but **it used public legal classification material, not private acquisition decision records**. It did not prove that the owner's proprietary data creates a performance advantage.

### 7.3 Changing instructions can improve permission decisions without training

Another experiment used **32 fictional decisions about whether a document could currently be shared or used**. We compared each model's ordinary instructions against **extra written instructions to check who gave permission, whether it had since been withdrawn, and whether any restrictions or conditions still applied**. These are additional *permission-checking steps* in the prompt, not extra training examples.

| Unchanged model | Ordinary instructions | Added permission-checking steps |
| --- | ---: | ---: |
| Qwen2.5 with 0.5 billion parameters | 20 of 32 | 20 of 32 |
| Qwen2.5 with 1.5 billion parameters | 21 of 32 | **27 of 32** |

For the 1.5-billion-parameter model, the extra permission-checking steps led to six additional correct answers in this narrow evaluation. For the 0.5-billion-parameter model, those same steps did not improve performance.

**Neither model was fine-tuned for this test.** The constructed items share eight template families; they are not 32 independent real acquisition decisions.

### 7.4 Testing contextual examples on actual historical acquisition sequences

A later experiment completed on **October 20, 2026** tested whether examples constructed from the owner's historical acquisition processes performed better than matched generic demonstrations.

It used eight verified first-party source messages forming **two historical acquisition process episodes**. These produced six dependent decision-time views and 20 reference fields. Qwen3 with eight billion parameters and Qwen2.5 with seven billion parameters returned **48 saved predictions** across four instruction conditions, with identical response-format requirements.

The primary comparison was between generic examples and contextual examples.

| Model | Generic examples: fully correct views | Contextual examples: fully correct views |
| --- | ---: | ---: |
| Qwen3, 8 billion parameters | **4 of 6** | **4 of 6** |
| Qwen2.5, 7 billion parameters | **1 of 6** | **1 of 6** |

Here, a fully correct view required the right typed factual answers, sufficient source support and the specified response format.

The contextual examples **did not outperform generic examples** on that primary measure in either model. Secondary factual and citation results were mixed. The historical episodes were already visible to the study designer, and no independent professional adjudication was obtained.

This is useful negative evidence. It does **not** establish that authentic decision records have no value; it shows that a premium for these specific contextual examples has not been demonstrated on this small cohort.

### 7.5 Privacy and task usefulness must be tested together

A separate October 21 experiment investigated eight fictional acquisition task families where sensitive information had to be removed **without destroying the facts needed for the decision**.

All 14 returned outputs from the originally tested model-based sanitizers retained the source packets unchanged, including the declared sensitive strings. A later exploratory rule-based transformation removed all the specifically listed target strings in eight of eight tasks, but met the complete combined privacy-and-task-quality standard in only **one of eight** under the frozen grader.

A disclosed grading sensitivity concerning short supporting quotations raised that result to **three of eight**. This is not evidence of effective general anonymization: the rule-based transformation addressed specified strings, and altered amounts may still be inferable.

The experiment used fictional data, experienced interrupted execution and did not train any model. It illustrates an important engineering challenge: **a task can lose its evidentiary value when information is removed, while seemingly sanitized information may remain sensitive**.

### 7.6 Follow-up: Do extra permission-checking steps help larger Qwen models?

On October 23, 2026, we completed a separately frozen **instructions-only test** using Qwen2.5 models with **7 billion and 14 billion parameters**. We did not retrain either model. Instead, each answered the same questions once with ordinary instructions and again with **a checklist to examine the latest permission, any revocation and the conditions attached to sharing information**. The experiment reused the earlier 32 fictional decisions for a developmental comparison and added **96 new fictional time-specific questions**, arranged into 24 four-question sequences.

The new examples are not 96 independent real acquisitions. They follow **six recurring structural patterns**, with programmatically determined Yes/No answers. No confidential acquisition correspondence or original professional judgment labels were part of these model inputs.

| Model | Ordinary instructions, new 96 cases | Added permission-checking steps | Difference |
| --- | ---: | ---: | ---: |
| Qwen2.5, 7 billion parameters | **76/96 (79.2%)** | 71/96 (74.0%) | −5.2 percentage points |
| Qwen2.5, 14 billion parameters | **84/96 (87.5%)** | 77/96 (80.2%) | −7.3 percentage points |

The 14-billion-parameter model performed better than the seven-billion-parameter model with ordinary instructions on this set of questions. But **the extra permission-checking steps did not improve either larger model**. On the previously used 32 development questions, the 7-billion-parameter model fell from 23 to 21 correct answers when the steps were added, while the 14-billion-parameter model remained at 25 of 32.

Across the 96 new questions, neither model incorrectly approved a prohibited document submission. All incorrect answers instead **denied permission when permission was actually valid**. The extra checking steps increased these overly cautious denials. This finding concerns the specific fictional tasks, not a general safety guarantee.

The extra permission-checking steps that helped the 1.5-billion-parameter model therefore did not produce the same gain in either larger model. Because the new questions repeat only six fictional structural patterns, the experiment cannot establish a population-wide effect. It does show **that model size and how instructions are framed can matter—and that more detailed instructions are not automatically better**.

All 512 model responses, the exact frozen questions, model versions and scoring results have been preserved in the private research record. This was **a comparison of instructions given to unchanged models**, not a fine-tuning experiment or a direct test of how the owner's historical acquisition data improves a model.

### 7.7 The intended experiment: Fine-tuning larger Qwen models with personally selected acquisition judgments

The experiment most directly relevant to **licensing human acquisition judgments** was completed on October 23, 2026. We fine-tuned Qwen2.5 models with **7 billion and 14 billion parameters** using a controlled, matched comparison. Each model saw **the same 20 structured acquisition decision scenarios**, but learned either **the next action personally selected by Nicholas Lauga** or the action previously selected by Qwen. The two sets differed on **10 of the 20 decisions**. The author's judgments are the human-origin information being tested.

Each model was fine-tuned using the same Low-Rank Adaptation method, training schedule and **three fixed random seeds**. Both training conditions were then graded against the same **40 developmental acquisition questions**, grouped into 20 related pairs across five public-guidance source families. Their reference answers were **provisional rather than independently adjudicated professional answers**, a distinction relevant to interpreting the results, not a requirement that all human-judgment training tasks undergo external certification.

| Qwen2.5 model | Unadapted baseline | After model-selected action labels | After Nicholas Lauga's selected action labels | Human-label advantage |
| --- | ---: | ---: | ---: | ---: |
| 7 billion parameters | 77.5% | 77.5% | **80.8%** | **+3.3 percentage points** |
| 14 billion parameters | 60.0% | 68.3% | **73.3%** | **+5.0 percentage points** |

*The two fine-tuned columns average three predeclared seeds; each seed was evaluated on the same 40 development questions. They represent provisional-reference agreement, not business acquisition outcomes.*

The direction of the average improvement was positive in **both larger models**, an encouraging indication that substituting personally selected human action judgments for model-selected action labels can change task performance. The results were not uniform: for the 14-billion-parameter model, one seed performed **three questions worse** with human-selected labels while the other two performed better by three and six questions respectively. The five-source-family descriptive uncertainty ranges were **0 to +6.7 points** for 7B and **−1.7 to +11.7 points** for 14B. These are exploratory ranges, not confirmatory statistical confidence intervals.

The preserved technical record contains **all 560 scored predictions, all 12 trained model adapters, fixed model versions, input checksums and seed-by-seed results**. It allows the measured differences, including unfavorable results, to be inspected and reproduced.

This study differs from the **instructions-only** comparison in Section 7.6: it actually **trained the models on different answers**, isolating the contribution of the owner's human-selected decisions. The scenario descriptions were **fictional training examples structured with artificial intelligence assistance**, not verbatim copies of confidential historical deal records. The author supplied the original judgment on what action to take; confidential source documents and rights-unclear third-party material were not used as model-training inputs.

### 7.8 What the combined testing supports

We can reproduce matched model fine-tuning, preserve the original owner-selected judgment layer, compare it with model-selected labels, grade fixed task sets and retain unfavorable seed-level outcomes. In the most relevant larger-model study, personally selected action labels produced **measured average developmental improvements of 3.3 and 5.0 percentage points** over matched model-selected labels.

The results remain **exploratory**, based on 20 structured fictional training scenarios with 10 different human-versus-model decisions, five related evaluation source families, and previously used provisional reference answers. No actual transaction return was being predicted. The author's broader historical acquisition records were not transferred in this particular test, and their commercial training or resale rights must be established separately.

The **acquisition-task production workflow is operational**: it can prepare structured decision scenarios, attach documented human-selected judgments and deliver traceable task collections. **The commercial offering is direct licensing of acquisition-decision task batches and commissioned production at agreed volumes.** Each agreement specifies the task content, provenance, permitted uses, quantity, delivery terms and price.

## 8. How the tasks could become a commercial product

A customer developing a financial or acquisition assistant could use the approach in several different ways:

| Potential offering | What the customer receives |
| --- | --- |
| **Human-judgment training task batches** | Structured acquisition questions and documented next-action judgments selected by a human practitioner, with scenario and label authorship identified separately. |
| **Evaluation task collection** | Dated permitted source packets, questions, reference answers and scoring tools for assessing model decisions. |
| **Commissioned task production at volume** | A buyer-specified number of acquisition tasks, output formats, review standards and permitted uses, delivered under an agreed commercial contract. |
| **Rights-cleared decision-history dataset** | Authentic human decisions and subsequent process evidence, where source-specific rights permit the contracted training or evaluation use. |

These offerings are not interchangeable. The provenance of every task should state whether the scenario text was human-written or AI-assisted and whether its decision label was personally selected by a human. **The proposed sales model is straightforward: license curated task collections or contract for specified volumes of new tasks.**

A licensing or production agreement should define source rights, authorship and decision-label provenance, task quantities, permitted model training and evaluation uses, confidentiality, any sublicensing permissions, delivery formats, schedule and price.

**Public demonstrations should be small and clearly labeled.** Proprietary evaluation answers or unseen test cases should not be openly released if they need to remain protected from model training exposure. Training and evaluation partitions should be separated by **entire underlying acquisition episode**, not merely by neighboring questions from the same deal.

Historical documents do not become legally reusable simply because they are summarized or anonymized. Seller materials, confidential correspondence, third-party professional opinions and recordings require source-specific rights and privacy review before external use.

The current project treats historical material with unresolved training or sublicensing rights as having **no established monetizable licensing value** until those rights are clarified. New, specifically commissioned tasks may have different ownership terms, but only after those terms are established.

**The technical production and evaluation workflow is demonstrated; a third-party dataset licensing agreement, confirmed task order or realized licensing revenue has not yet been recorded.**

## 9. What remains before scientific peer review

This manuscript is a **technical showcase and documented research progress report**, not an accepted or peer-reviewed scientific article.

The longer-term scientific question is whether authentic, rights-cleared and accurately attributed acquisition decision sequences contribute useful information beyond established generic task designs.

A defensible future study would need:

1. A clearly specified decision endpoint—factual extraction, observed human action or independently judged action quality.
2. Sufficient original acquisition episodes with documented rights and reliable decision-time evidence.
3. Reference standards appropriate to the task: a traceable human-selected action for human-behavior training, or additional expert adjudication when claiming a single professionally preferred action.
4. Separate training, development and test cases drawn from different underlying acquisition roots, with prior model exposure documented.
5. Appropriate baseline methods, including simple calculations or rule systems where they can solve the task.
6. Prespecified scoring, error analysis, uncertainty reporting and preservation of negative outcomes.
7. Reproducibility materials that can be legally and safely shared with researchers or reviewers.

Academic peer review would examine the research claims and methodology. It would **not** automatically establish customer demand or transfer rights to license historical data.

The contemplated public showcase channels include GitHub, Hugging Face and a professional announcement, subject to final content, rights and release approvals. Public posting on those platforms is distinct from scholarly peer review.

## 10. Acknowledgments

**Ryan Chandra of PeopleWise Solutions** contributed a human-authored second opinion on people and practitioner risks in a separate acquisition review within the broader research project.

His assessment highlighted ownership transition, minimum viable practitioner staffing, service capacity, recruitment and the role of operations management in succession planning.

This acknowledgment recognizes his practitioner perspective. It **does not** imply that he coauthored these fictional scenarios, reviewed their reference answers, validated the Qwen experiments or endorsed this paper.

## 11. Conclusion

Small-business acquisition decisions change as financial information, financing constraints and document permissions change. An artificial intelligence assistant should be able to recognize these changes, explain which evidence is current, acknowledge uncertainty and revise its suggested next step appropriately.

The two fictional demonstrations show how those behaviors can be expressed as understandable, structured decision tasks. The broader project offers a potential path to augmenting such demonstrations with authentic human-led decision trajectories and later evidence, while keeping human judgment, computational assistance, source rights and professional review distinguishable.

The model experiments provide two complementary findings. An inference-only permission study showed that extra instructions do not automatically improve larger models. More relevant to the proposed human-judgment licensing product, **matched fine-tuning with personally selected human acquisition action labels outperformed the same training using model-selected labels on average in both Qwen2.5 7B and 14B**, by 3.3 and 5.0 percentage points respectively on the fixed development tasks. These are exploratory results, but they demonstrate a measurable difference between training on human-selected and model-selected acquisition judgments.

The commercial opportunity is **direct licensing of curated acquisition-decision task batches and commissioned task production for AI developers**. Customers can purchase defined quantities of structured tasks containing traceable human-selected judgments, or contract for new tasks built to their specifications. **Rights, permitted uses, volume, delivery and pricing are agreed in the license or production contract.**

**Correspondence:** Nicholas Lauga · nicklauga@gmail.com

## References

The following are academic research papers relevant to the evaluation approach, not sources of the fictional transaction facts.

1. Chen, Zhiyu, and colleagues (2021). [*FinQA: A Dataset of Numerical Reasoning over Financial Data.*](https://aclanthology.org/2021.emnlp-main.300/) Proceedings of the Conference on Empirical Methods in Natural Language Processing.
2. Chen, Zhiyu, and colleagues (2022). [*ConvFinQA: Exploring the Chain of Numerical Reasoning in Conversational Finance Question Answering.*](https://aclanthology.org/2022.emnlp-main.421/) Proceedings of the Conference on Empirical Methods in Natural Language Processing.
3. Wang, Steven H., and colleagues (2023). [*MAUD: An Expert-Annotated Legal Natural Language Processing Dataset for Merger Agreement Understanding.*](https://aclanthology.org/2023.emnlp-main.1019/) Proceedings of the Conference on Empirical Methods in Natural Language Processing.
4. Islam, Pranab, and colleagues (2023). [*FinanceBench: A New Benchmark for Financial Question Answering.*](https://arxiv.org/abs/2311.11944) Research preprint.

---

*End of technical showcase, version 0.1.13.*
