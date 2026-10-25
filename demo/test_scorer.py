"""Offline quality checks and negative controls for the synthetic showcase."""
import copy
import json
import unittest
from pathlib import Path
from scorer import load_jsonl, evaluate, BASE

class TestPublicShowcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tasks = load_jsonl(BASE / "tasks.jsonl")
        cls.references = load_jsonl(BASE / "references.jsonl")
        cls.perfect = load_jsonl(BASE / "example_model_responses.jsonl")

    def scoring(self, pred=None, tasks=None, refs=None):
        return evaluate(tasks or self.tasks, refs or self.references, pred or self.perfect)

    def test_reference_responses_all_pass(self):
        result = self.scoring()
        self.assertEqual(result["complete_views"], 4)
        self.assertEqual(result["task_count"], 4)
        self.assertEqual(result["independent_fictional_roots"], 2)
        self.assertEqual(result["correct_fields"], result["total_fields"])

    def test_wrong_financial_price_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-001-CUTOFF"]["highest_price_cad"]=930000
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_double_deducted_manager_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-001-CUTOFF"]["maintainable_earnings_cad"]=152000
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_wrong_cash_reserve_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-001-CUTOFF"]["cash_remaining_at_asking_cad"]=66000
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_continuing_during_revocation_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-002-SUSPENDED"]["decision_action"]="CONTINUE_PRELIMINARY_REVIEW"
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_revoked_earnings_not_current(self):
        p=copy.deepcopy(self.perfect);p["AD-002-SUSPENDED"]["currently_authorized_earnings_cad"]=248000
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_stale_earnings_after_restoration_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-002-RESTORED"]["currently_authorized_earnings_cad"]=248000
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_wrong_accountant_permission_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-002-INITIAL"]["accountant_access_active"]=True
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_download_or_upload_violation_detected(self):
        for field in ["download_authorized", "external_ai_upload_authorized"]:
            p=copy.deepcopy(self.perfect);p["AD-002-RESTORED"][field]=True
            self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_unauthorized_client_list_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-002-RESTORED"]["permitted_view_documents"].append("CLIENT_LIST")
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_invalid_source_citation_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-002-SUSPENDED"]["cited_source_ids"]=["P05"]
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_missing_or_extra_field_detected(self):
        p=copy.deepcopy(self.perfect);p["AD-002-SUSPENDED"].pop("download_authorized")
        self.assertEqual(self.scoring(p)["complete_views"],3)
        p=copy.deepcopy(self.perfect);p["AD-002-SUSPENDED"]["unused"]=1
        self.assertEqual(self.scoring(p)["complete_views"],3)

    def test_future_document_injection_rejected(self):
        t=copy.deepcopy(self.tasks)
        t["AD-002-SUSPENDED"]["documents"].append(copy.deepcopy(self.tasks["AD-002-RESTORED"]["documents"][-2]))
        with self.assertRaisesRegex(ValueError,"future document"): self.scoring(tasks=t)

    def test_reference_citation_not_in_checkpoint_rejected(self):
        refs=copy.deepcopy(self.references)
        refs["AD-002-SUSPENDED"]["answer"]["cited_source_ids"]=["P05"]
        with self.assertRaisesRegex(ValueError,"invalid reference citations"): self.scoring(refs=refs)

    def test_duplicate_ids_rejected(self):
        rows=(BASE/"tasks.jsonl").read_text(encoding="utf-8").splitlines()
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/"dup.jsonl";file.write_text("\n".join(rows+[rows[0]])+"\n",encoding="utf-8")
            with self.assertRaisesRegex(ValueError,"duplicate task_id"):load_jsonl(file)

if __name__ == "__main__":
    unittest.main()
