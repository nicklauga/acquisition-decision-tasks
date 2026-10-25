#!/usr/bin/env python3
"""Deterministic scorer for four fictional acquisition showcase checkpoints.

No network/API calls, third-party packages, or access to confidential data.
The reference file is intentionally PUBLIC for illustrative grading only.
"""
import argparse
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def load_jsonl(path):
    rows = [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [row["task_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate task_id")
    return {row["task_id"]: row for row in rows}


def evaluate(tasks, references, predictions):
    if set(tasks) != set(references):
        raise ValueError("task/reference set mismatch")
    if set(predictions) != set(tasks):
        raise ValueError("prediction task coverage mismatch")
    all_results = []
    for task_id, task in tasks.items():
        reference = references[task_id]["answer"]
        prediction = {key: value for key, value in predictions[task_id].items() if key != "task_id"}
        expected_fields = set(task["required_fields"])
        documented_ids = {doc["source_id"] for doc in task["documents"]}
        if set(reference) != expected_fields:
            raise ValueError(f"invalid reference schema: {task_id}")
        if any(doc["issued_utc"] > task["cutoff_utc"] for doc in task["documents"]):
            raise ValueError(f"future document leaked: {task_id}")
        if not set(reference["cited_source_ids"]).issubset(documented_ids):
            raise ValueError(f"invalid reference citations: {task_id}")
        field_scores = {}
        for field in task["required_fields"]:
            target = reference[field]
            actual = prediction.get(field)
            if field == "cited_source_ids":
                valid = isinstance(actual, list) and all(
                    isinstance(x, str) and x in documented_ids for x in actual
                )
                passed = valid and set(reference[field]).issubset(set(actual))
            elif field in ("failed_rules", "permitted_view_documents"):
                passed = isinstance(actual, list) and sorted(actual) == sorted(target)
            else:
                passed = actual == target and type(actual) is type(target)
            field_scores[field] = bool(passed)
        structure_ok = set(prediction) == expected_fields
        all_results.append({
            "task_id": task_id,
            "root_id": task["root_id"],
            "correct_fields": sum(field_scores.values()),
            "total_fields": len(field_scores),
            "structure_ok": structure_ok,
            "complete_view": structure_ok and all(field_scores.values()),
            "field_results": field_scores,
        })
    total = sum(x["total_fields"] for x in all_results)
    correct = sum(x["correct_fields"] for x in all_results)
    return {
        "task_count": len(all_results),
        "independent_fictional_roots": len(set(x["root_id"] for x in all_results)),
        "correct_fields": correct,
        "total_fields": total,
        "complete_views": sum(x["complete_view"] for x in all_results),
        "views": all_results,
    }


def score_file(path):
    return evaluate(
        load_jsonl(BASE / "tasks.jsonl"),
        load_jsonl(BASE / "references.jsonl"),
        load_jsonl(path),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions", nargs="?", default=str(BASE / "example_model_responses.jsonl"))
    args = parser.parse_args()
    print(json.dumps(score_file(args.predictions), indent=2))
