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


if __name__ == "__main__":
    unittest.main()
