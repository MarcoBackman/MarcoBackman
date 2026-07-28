from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from PIL import Image

from scripts.generate_agentops_gif import generate_gif


ROOT = Path(__file__).resolve().parents[1]


class AgentOpsGifTests(unittest.TestCase):
    def test_generator_creates_readable_looping_gif(self) -> None:
        with TemporaryDirectory() as directory:
            output = Path(directory) / "agentops.gif"
            generate_gif(output)

            with Image.open(output) as image:
                self.assertEqual(image.format, "GIF")
                self.assertEqual(image.size, (960, 360))
                self.assertGreaterEqual(image.n_frames, 30)
                self.assertEqual(image.info.get("loop"), 0)
                self.assertGreater(image.info.get("duration", 0), 0)

    def test_workspace_asset_matches_generator_contract(self) -> None:
        asset = ROOT / "assets" / "llm-agentops-flow.gif"
        self.assertTrue(asset.exists())
        self.assertLess(asset.stat().st_size, 4_000_000)

        with Image.open(asset) as image:
            self.assertEqual(image.size, (960, 360))
            self.assertGreaterEqual(image.n_frames, 30)


class ProfileReadmeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_leads_with_llm_agentops_and_verified_projects(self) -> None:
        self.assertIn("LLM AgentOps Engineer", self.readme)
        self.assertIn("Symphony — LLM AgentOps for APS Analytics", self.readme)
        self.assertIn("Taelim — Manufacturing APS & Scheduling Engine", self.readme)
        self.assertLess(self.readme.index("Symphony"), self.readme.index("Taelim"))

    def test_integrates_requested_visual_services_and_local_gif(self) -> None:
        self.assertGreaterEqual(self.readme.count("capsule-render.vercel.app/api"), 2)
        self.assertIn("readme-typing-svg.demolab.com", self.readme)
        self.assertIn("./assets/llm-agentops-flow.gif", self.readme)
        self.assertIn("github-readme-stats.vercel.app/api", self.readme)
        self.assertIn("streak-stats.demolab.com", self.readme)

    def test_public_stats_use_profile_username(self) -> None:
        self.assertGreaterEqual(self.readme.count("username=MarcoBackman"), 2)
        self.assertIn("user=MarcoBackman", self.readme)
        self.assertIn("Public GitHub Snapshot", self.readme)

    def test_omits_unconfirmed_metrics_and_old_positioning(self) -> None:
        self.assertNotIn("90%", self.readme)
        self.assertNotIn("15%", self.readme)
        self.assertNotIn("currently looking for a project", self.readme)
        self.assertNotIn("beak_heamin_saipan", self.readme)


if __name__ == "__main__":
    unittest.main()
