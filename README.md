# Acquisition Decision Tasks
### Evidence changes. The decision should follow.

**Nicholas Lauga · October 2026 · Technical showcase 0.1.13**

**Read the paper:** [Markdown](paper/Acquisition_Decision_Tasks.md) | [PDF](paper/Acquisition_Decision_Tasks.pdf)

**Fictional demonstration dataset:** [Hugging Face](https://huggingface.co/datasets/Nicklauga/acquisition-decision-tasks-showcase)

This repository demonstrates how source-grounded acquisition questions can
test whether an artificial intelligence system updates its answer when
financial evidence and document-use permission change.

## Public fictional examples

The demonstration includes **two fictional acquisition source roots**, split
into **four time-specific checkpoint questions**:

| Task | Expected action |
| --- | --- |
| AD-001-CUTOFF | Revise nonbinding terms; maximum CAD 888,000 under the fictional rules |
| AD-002-INITIAL | Continue preliminary review |
| AD-002-SUSPENDED | Pause document-based investigation |
| AD-002-RESTORED | Resume limited investigation of authorized information |

All four public cases are **AI-assisted fictional demonstrations**.
The numeric and action references are **provisional examples**, not blinded
professional determinations. The underlying research direction was informed
by Nicholas Lauga's own historical acquisition decisions, but none of the
published fictional source packets is a reproduction of a confidential deal.

## Run the example evaluator

Python 3.11 or later; standard library only; no downloads or model API needed:

    cd demo
    python -m unittest -q test_scorer.py
    python scorer.py example_model_responses.jsonl

The fixture responses were written to match the public reference answers.
Therefore a 4/4 fixture score **does not measure Qwen model performance**.
The human-selected label effects reported for Qwen2.5 7B and 14B come
from separate matched fine-tuning studies, not these four demo questions.
The measured average +3.3 and +5.0 percentage-point differences were
exploratory, not statistically established. The 4/4 fixtures below
are not model performance.

## How buyers can use this approach

Directly license task batches with documented human-selected judgments, or
commission new acquisition tasks at agreed quantities and delivery terms.
The fictional examples here are for inspection only; publication does not
confer rights to original seller correspondence or confidential human
acquisition records.

## Content rights

Copyright (c) 2026 Nicholas Lauga. **All rights reserved.**
The paper, sample data, and code are published for inspection and technical
demonstration, without an open-source or open-data reuse license. This is
not a license to reproduce, train on, redistribute, sublicense or commercially
use the material. GitHub platform viewing/forking terms still apply.
Contact the author to discuss specific permissions or commercial terms.

**Contact:** nicklauga@gmail.com

## Further information

See the paper for experimental methods, results, source/provenance boundaries,
limitations, and acknowledgment of Ryan Chandra at PeopleWise Solutions.
This technical showcase has not undergone scholarly peer review.
