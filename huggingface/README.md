---
language:
- en
language_creators:
- machine-generated
annotations_creators:
- machine-generated
pretty_name: Acquisition Decision Tasks - Fictional Showcase
tags:
- business-acquisitions
- small-business
- temporal-reasoning
- permission-reasoning
- financial-reasoning
- model-evaluation
---

# Acquisition Decision Tasks - Fictional Showcase

**Nicholas Lauga, October 2026 - four public demonstration questions from two
fictional acquisition situations.** See the accompanying technical paper.

## What this contains

- One fictional financial acquisition screen: revise nonbinding terms.
- Three checkpoints in a single fictional document-permission sequence:
  continue, pause, then resume limited review.
- Each task specifies a source timestamp, decision cutoff, question,
  schema fields and fictional documents.
- The reference file contains published **provisional AI-assisted answers**,
  not blind human gold labels.

## Source and authorship

The source documents and question wordings are constructed fictional examples,
not original seller records or clinical, employment or customer information.
The larger research was directed by Nicholas Lauga and informed by his
human-origin acquisition judgments, which are **not included** in these data
files. No third-party confidential source text is offered or licensed.

## Data format

Both data files use UTF-8 JSON Lines:

- tasks.jsonl: case inputs with \`task_id\`, \`root_id\`, \`cutoff_utc\`,
  \`documents\`, \`question\`, \`required_fields\`.
- references.jsonl: provisional example answers, matching task IDs.

**Counts:** 4 dependent views; **2 fictional roots**; **0 published real
historical transaction roots**. Do not report four independent cases.

## Intended use

Understand data schemas, test a local parser and demonstrate an illustrative
scoring method. The supplied answers are public: do not treat them as
untouched hidden evaluation data. No licensed model training permissions are
provided by this public sample.

The earlier Qwen experiments described in the full paper **did not use these
four demonstration views**. The 4/4 public example responses are not Qwen
model predictions.

## Limits and access conditions

The acquisition pricing rule is fictional and not a professional valuation or
lending decision. Permission snapshots illustrate a controlled scenario, not
legal advice. No independent qualified professional has reviewed these public
reference answers. Privacy transformations for actual business files require
their own source rights and privacy checks.

**Copyright (c) 2026 Nicholas Lauga. All rights reserved.**
The sample is posted for inspection, without an open data or training license.
Contact **nicklauga@gmail.com** for permissions or commissioned task programs.

There is no license grant for any underlying historical acquisition archive.
