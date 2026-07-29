from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from PIL import Image, ImageFont

from scripts import generate_agentops_gif
from scripts.generate_agentops_gif import generate_gif, load_font


ROOT = Path(__file__).resolve().parents[1]


def assert_v2_gif_contract(test_case: unittest.TestCase, path: Path) -> None:
    with Image.open(path) as image:
        loop = image.info.get("loop")
        durations = []
        for frame_index in range(image.n_frames):
            image.seek(frame_index)
            durations.append(image.info.get("duration", 0))

        test_case.assertEqual(image.format, "GIF")
        test_case.assertEqual(image.size, (960, 540))
        test_case.assertGreaterEqual(image.n_frames, 70)
        test_case.assertEqual(loop, 0)
        test_case.assertGreaterEqual(sum(durations), 12_000)


class AgentOpsGifTests(unittest.TestCase):
    def test_font_loading_falls_back_when_truetype_fonts_are_unavailable(self) -> None:
        fallback_font = ImageFont.load_default()
        with (
            patch(
                "scripts.generate_agentops_gif.ImageFont.truetype",
                side_effect=OSError("font unavailable"),
            ),
            patch(
                "scripts.generate_agentops_gif.ImageFont.load_default",
                return_value=fallback_font,
            ),
        ):
            try:
                loaded_font = load_font(13)
            except OSError:
                self.fail("load_font did not use Pillow's safe default")
            self.assertIs(loaded_font, fallback_font)

    def test_generator_creates_professional_trace_gif(self) -> None:
        with TemporaryDirectory() as directory:
            output = Path(directory) / "agentops-v2.gif"
            generate_gif(output)
            assert_v2_gif_contract(self, output)

    def test_workspace_asset_matches_v2_contract(self) -> None:
        asset = ROOT / "assets" / "llm-agentops-flow.gif"
        self.assertTrue(asset.exists())
        self.assertLess(asset.stat().st_size, 6_000_000)
        assert_v2_gif_contract(self, asset)

    def test_v2_timeline_and_semantics_are_stable(self) -> None:
        self.assertEqual(
            (generate_agentops_gif.WIDTH, generate_agentops_gif.HEIGHT),
            (960, 540),
        )
        self.assertEqual(generate_agentops_gif.FRAME_COUNT, 96)
        self.assertEqual(generate_agentops_gif.FRAME_DURATION_MS, 140)
        self.assertEqual(
            generate_agentops_gif.STAGES,
            (
                "REQUEST",
                "GUARDRAIL",
                "CONTEXT",
                "PLAN",
                "TOOL / SQL",
                "EVALUATE",
                "REPLAN",
                "REPORT",
            ),
        )
        self.assertEqual(
            getattr(generate_agentops_gif, "DECISION_TEXT", None),
            "Prioritize 3 at-risk orders before capacity lock.",
        )

    def test_generator_is_deterministic_in_one_environment(self) -> None:
        with TemporaryDirectory() as directory:
            first = Path(directory) / "first.gif"
            second = Path(directory) / "second.gif"
            generate_gif(first)
            generate_gif(second)
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_final_decision_checkmark_is_drawn_without_font_glyphs(self) -> None:
        frame = generate_agentops_gif.draw_frame(
            generate_agentops_gif.FRAME_COUNT - 1
        )
        for point in ((896, 501), (900, 505), (907, 496)):
            with self.subTest(point=point):
                self.assertEqual(
                    frame.getpixel(point),
                    generate_agentops_gif.BACKGROUND,
                )


class ProfileReadmeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        korean_path = ROOT / "README.ko.md"
        cls.korean_readme = (
            korean_path.read_text(encoding="utf-8") if korean_path.exists() else ""
        )

    def test_leads_with_llm_agentops_and_verified_projects(self) -> None:
        self.assertIn("LLM AgentOps Engineer", self.readme)
        self.assertIn("Symphony — LLM AgentOps for APS Analytics", self.readme)
        self.assertIn("Taelim — Manufacturing APS & Scheduling Engine", self.readme)
        self.assertLess(self.readme.index("Symphony"), self.readme.index("Taelim"))

    def test_includes_financial_and_digital_twin_platform_experience(self) -> None:
        self.assertIn("Additional Platform Experience", self.readme)
        self.assertIn(
            "Financial Services Platform — Real-Time Fund Processing",
            self.readme,
        )
        self.assertIn("BeaconFire Inc.", self.readme)
        self.assertIn("100,000+ orders", self.readme)
        self.assertIn("Kafka", self.readme)
        self.assertIn("OpenShift", self.readme)
        self.assertIn("Warehouse Digital Twin Service Platform", self.readme)
        self.assertIn("VisionSpace", self.readme)
        self.assertIn("MQTT", self.readme)
        self.assertIn("AWS IoT", self.readme)
        self.assertLess(
            self.readme.index("Taelim — Manufacturing APS & Scheduling Engine"),
            self.readme.index("Additional Platform Experience"),
        )
        self.assertLess(
            self.readme.index("Additional Platform Experience"),
            self.readme.index("Technology focus"),
        )

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

    def test_linkedin_badge_uses_tonys_public_profile(self) -> None:
        self.assertIn(
            'href="https://www.linkedin.com/in/sung-jun-tony-baek-9b505b11a"',
            self.readme,
        )

    def test_omits_unconfirmed_metrics_and_old_positioning(self) -> None:
        self.assertNotIn("90%", self.readme)
        self.assertNotIn("15%", self.readme)
        self.assertNotIn("currently looking for a project", self.readme)
        self.assertNotIn("beak_heamin_saipan", self.readme)

    def test_professional_gif_is_responsive_and_descriptive(self) -> None:
        self.assertIn('src="./assets/llm-agentops-flow.gif"', self.readme)
        self.assertIn('width="100%"', self.readme)
        self.assertIn(
            "guardrails, planning, tool execution, evaluation, replanning, "
            "demo telemetry, and a verified decision",
            self.readme,
        )

    def test_links_english_and_korean_profiles_bidirectionally(self) -> None:
        self.assertIn('href="./README.ko.md"', self.readme)
        self.assertIn('href="./README.md"', self.korean_readme)
        self.assertIn('href="./README.ko.md"', self.korean_readme)

    def test_korean_profile_preserves_featured_project_order(self) -> None:
        self.assertIn("LLM AgentOps 엔지니어", self.korean_readme)
        self.assertLess(
            self.korean_readme.index("Symphony"),
            self.korean_readme.index("Taelim"),
        )
        self.assertLess(
            self.korean_readme.index("Taelim"),
            self.korean_readme.index(
                "### 금융 서비스 플랫폼 — 실시간 펀드 처리"
            ),
        )
        self.assertLess(
            self.korean_readme.index(
                "### 금융 서비스 플랫폼 — 실시간 펀드 처리"
            ),
            self.korean_readme.index(
                "### 물류창고 디지털 트윈 서비스 플랫폼"
            ),
        )

    def test_korean_profile_includes_curated_resume_evidence(self) -> None:
        normalized_korean_readme = " ".join(self.korean_readme.split())
        for expected in (
            "초당 5,000개 이상의 메시지",
            "3시간에서 15분",
            "100만 건",
            "60초에서 2초",
            "시간당 40건에서 0건",
            "대한민국 해군",
            "Robolink",
            "Florida Institute of Technology",
            "SQL 개발자",
            "데이터아키텍처 준전문가",
            "네트워크관리사 2급",
            "MS 365 Fundamentals",
            "OPIc AL",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, normalized_korean_readme)

    def test_korean_profile_reuses_visual_identity(self) -> None:
        self.assertGreaterEqual(
            self.korean_readme.count("capsule-render.vercel.app/api"),
            2,
        )
        self.assertIn("readme-typing-svg.demolab.com", self.korean_readme)
        self.assertIn("./assets/llm-agentops-flow.gif", self.korean_readme)
        self.assertIn("github-readme-stats.vercel.app/api", self.korean_readme)
        self.assertIn("streak-stats.demolab.com", self.korean_readme)

    def test_korean_profile_excludes_resume_only_personal_data(self) -> None:
        self.assertNotIn("주소:", self.korean_readme)
        self.assertNotIn("생년월일", self.korean_readme)
        self.assertNotIn("1995년 11월 29일", self.korean_readme)
        for private_client in (
            "DriveWealth",
            "Navy Federal",
            "OMRON",
            "현대 무벡스",
        ):
            with self.subTest(private_client=private_client):
                self.assertNotIn(private_client, self.korean_readme)
        self.assertNotRegex(
            self.korean_readme,
            r"(?:\+?1[-.\s]?)?\d{3}[-.\s]\d{3}[-.\s]\d{4}",
        )


if __name__ == "__main__":
    unittest.main()
