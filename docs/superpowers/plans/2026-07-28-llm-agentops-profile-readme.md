# LLM AgentOps Profile README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an animated GitHub profile README that positions Sung Jun "Tony" Baek as an LLM AgentOps engineer and proves that positioning through Symphony and Taelim contributions.

**Architecture:** Keep the professional story in accessible Markdown and use remote SVG services only as progressive visual enhancement. Generate the workflow GIF locally from deterministic Pillow drawing code, store both its source generator and final asset, and validate the README and GIF contracts with Python `unittest`.

**Tech Stack:** GitHub Flavored Markdown, remote SVG generators, Python 3.13, Pillow 12.1, `unittest`

## Global Constraints

- Published README copy is English.
- Recent-career positioning is `LLM AgentOps Engineer`.
- Symphony appears before Taelim.
- Symphony is described through reliability, observability, validation, inference tracing, and cost awareness.
- Taelim is described through manufacturing APS correctness, testing, and operational support.
- Do not include private repository links, commit hashes, ticket identifiers, internal paths, factory codes, or customer data.
- Do not include the unconfirmed `90%` or `15%` metrics.
- Dynamic cards are labeled as a public GitHub snapshot.
- The profile remains informative if every remote SVG/card fails to load.
- Use `MarcoBackman` for public GitHub statistics.
- Use the navy/cyan/violet palette `#0F172A`, `#22D3EE`, `#8B5CF6`, `#E2E8F0`, and `#38BDF8`.

## File map

- Verify: `docs/superpowers/specs/2026-07-28-profile-readme-refresh-design.md`
  - Records the user-approved LLM AgentOps positioning.
- Create: `scripts/generate_agentops_gif.py`
  - Deterministically generates the animated workflow asset.
- Create: `assets/llm-agentops-flow.gif`
  - GitHub-ready animation embedded by the profile README.
- Create: `tests/__init__.py`
  - Makes the profile contract tests importable through `python -m unittest`.
- Create: `tests/test_profile_readme.py`
  - Verifies the GIF contract and README content/integration contract.
- Modify: `README.md`
  - Publishes the final profile story, visual integrations, badges, and public stats.

---

### Task 1: Verify the LLM AgentOps specification baseline

**Files:**
- Verify: `docs/superpowers/specs/2026-07-28-profile-readme-refresh-design.md`

**Interfaces:**
- Consumes: User instruction that the recent career should be positioned as LLM AgentOps.
- Produces: Approved copy and visual requirements used by all later tasks.

- [ ] **Step 1: Confirm the specification uses LLM AgentOps consistently**

Run:

```powershell
rg -n "LLM AgentOps|AI Agent & Manufacturing APS Engineer|Building production AI agents" docs/superpowers/specs/2026-07-28-profile-readme-refresh-design.md
```

Expected:

- `LLM AgentOps Engineer` appears as the displayed identity.
- The outdated broad title and typing line do not appear.

- [ ] **Step 2: Check the specification diff**

Run:

```powershell
git diff --check
git diff -- docs/superpowers/specs/2026-07-28-profile-readme-refresh-design.md
```

Expected: no whitespace errors and only the requested career-positioning changes.

- [ ] **Step 3: Confirm the approved specification is already committed**

```powershell
git status --short
git log -2 --oneline
```

Expected: the specification has no uncommitted changes and the documentation
commit containing the approved plan is visible.

### Task 2: Build the reproducible AgentOps GIF

**Files:**
- Create: `scripts/generate_agentops_gif.py`
- Create: `assets/llm-agentops-flow.gif`
- Create: `tests/__init__.py`
- Create: `tests/test_profile_readme.py`

**Interfaces:**
- Produces: `generate_gif(output_path: pathlib.Path) -> None`
- Produces: a `960 × 360` looping GIF with at least 30 frames at `assets/llm-agentops-flow.gif`.
- Consumed by: `README.md` through the relative path `./assets/llm-agentops-flow.gif`.

- [ ] **Step 1: Write the failing GIF contract test**

Create an empty `tests/__init__.py`, then create
`tests/test_profile_readme.py`:

```python
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
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```powershell
python -m unittest tests.test_profile_readme.AgentOpsGifTests -v
```

Expected: FAIL because `scripts.generate_agentops_gif` does not exist.

- [ ] **Step 3: Implement the GIF generator**

Create `scripts/generate_agentops_gif.py` with these exact public constants and
interface:

```python
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 960
HEIGHT = 360
FRAME_COUNT = 48
FRAME_DURATION_MS = 90
BACKGROUND = (15, 23, 42)
PANEL = (22, 32, 56)
TEXT = (226, 232, 240)
MUTED = (148, 163, 184)
CYAN = (34, 211, 238)
BLUE = (56, 189, 248)
VIOLET = (139, 92, 246)
STAGES = ("QUESTION", "PLAN", "QUERY", "VALIDATE", "INSIGHT")


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    filename = "consolab.ttf" if bold else "consola.ttf"
    return ImageFont.truetype(str(Path("C:/Windows/Fonts") / filename), size)


def mix(left: tuple[int, int, int], right: tuple[int, int, int], amount: float) -> tuple[int, int, int]:
    amount = max(0.0, min(1.0, amount))
    return tuple(round(a + (b - a) * amount) for a, b in zip(left, right))


def draw_background(draw: ImageDraw.ImageDraw) -> None:
    for y in range(HEIGHT):
        amount = y / (HEIGHT - 1)
        draw.line((0, y, WIDTH, y), fill=mix(BACKGROUND, (31, 20, 58), amount))
    for x in range(0, WIDTH, 32):
        draw.line((x, 0, x, HEIGHT), fill=(22, 33, 57), width=1)
    for y in range(0, HEIGHT, 32):
        draw.line((0, y, WIDTH, y), fill=(22, 33, 57), width=1)


def draw_frame(frame_index: int) -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw_background(draw)

    title_font = load_font(24, bold=True)
    label_font = load_font(15, bold=True)
    small_font = load_font(13)
    draw.text((46, 30), "LLM AGENTOPS // FROM QUESTION TO DECISION", font=title_font, fill=TEXT)
    draw.text((46, 66), "observable · validated · cost-aware · reliable", font=small_font, fill=MUTED)

    left = 46
    top = 112
    node_width = 150
    node_height = 58
    gap = 28
    active_position = (frame_index / (FRAME_COUNT - 1)) * (len(STAGES) + 0.75)

    centers: list[tuple[int, int]] = []
    for index, stage in enumerate(STAGES):
        x = left + index * (node_width + gap)
        center = (x + node_width // 2, top + node_height // 2)
        centers.append(center)
        if index:
            previous = centers[index - 1]
            connector_progress = max(0.0, min(1.0, active_position - index + 0.35))
            draw.line((previous[0] + node_width // 2, previous[1], center[0] - node_width // 2, center[1]), fill=(51, 65, 85), width=4)
            if connector_progress > 0:
                start_x = previous[0] + node_width // 2
                end_x = round(start_x + (center[0] - node_width // 2 - start_x) * connector_progress)
                draw.line((start_x, previous[1], end_x, center[1]), fill=CYAN, width=4)

        intensity = max(0.0, min(1.0, active_position - index))
        border = mix((51, 65, 85), VIOLET if stage == "INSIGHT" else CYAN, intensity)
        fill = mix(PANEL, (28, 62, 82), intensity * 0.7)
        draw.rounded_rectangle((x, top, x + node_width, top + node_height), radius=14, fill=fill, outline=border, width=3)
        text_box = draw.textbbox((0, 0), stage, font=label_font)
        text_width = text_box[2] - text_box[0]
        draw.text((x + (node_width - text_width) / 2, top + 19), stage, font=label_font, fill=mix(MUTED, TEXT, intensity))

    draw.rounded_rectangle((46, 213, 558, 320), radius=16, fill=PANEL, outline=(51, 65, 85), width=2)
    draw.text((66, 230), "TRACE", font=label_font, fill=BLUE)
    messages = (
        ("context ready", 0.4),
        ("query validated", 2.0),
        ("report generated", 4.1),
    )
    for row, (message, threshold) in enumerate(messages):
        visible = active_position >= threshold
        marker = "●" if visible else "○"
        color = CYAN if visible else (71, 85, 105)
        draw.text((66, 262 + row * 20), f"{marker} {message}", font=small_font, fill=color)

    draw.rounded_rectangle((580, 213, 914, 320), radius=16, fill=PANEL, outline=(51, 65, 85), width=2)
    draw.text((600, 230), "DECISION SIGNAL", font=label_font, fill=VIOLET)
    chart_ready = max(0.0, min(1.0, active_position - 4.0))
    bars = (42, 68, 54, 88, 74)
    for index, height in enumerate(bars):
        x = 608 + index * 48
        rendered_height = round(height * chart_ready)
        draw.rounded_rectangle((x, 302 - rendered_height, x + 24, 302), radius=5, fill=mix(BLUE, VIOLET, index / 4))
    draw.text((600, 292), "validated insight", font=small_font, fill=mix((71, 85, 105), TEXT, chart_ready))
    return image


def generate_gif(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frames = [draw_frame(index) for index in range(FRAME_COUNT)]
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=FRAME_DURATION_MS,
        loop=0,
        optimize=True,
        disposal=2,
    )


if __name__ == "__main__":
    generate_gif(Path("assets/llm-agentops-flow.gif"))
```

- [ ] **Step 4: Generate the workspace asset**

Run:

```powershell
python scripts/generate_agentops_gif.py
```

Expected: `assets/llm-agentops-flow.gif` exists.

- [ ] **Step 5: Run the GIF contract tests**

Run:

```powershell
python -m unittest tests.test_profile_readme.AgentOpsGifTests -v
```

Expected: two tests PASS.

- [ ] **Step 6: Inspect the generated GIF**

Open the first, middle, and last frames and confirm:

- the five stage labels are legible;
- the active path progresses left to right;
- generic trace messages appear progressively;
- no internal product or customer information is present;
- the final chart is visible before the loop resets.

- [ ] **Step 7: Commit the GIF generator and asset**

```powershell
git add scripts/generate_agentops_gif.py tests/__init__.py tests/test_profile_readme.py assets/llm-agentops-flow.gif
git commit -m "feat: add animated LLM AgentOps workflow"
```

### Task 3: Replace the profile README

**Files:**
- Modify: `tests/test_profile_readme.py`
- Modify: `README.md`

**Interfaces:**
- Consumes: `./assets/llm-agentops-flow.gif`.
- Consumes: remote capsule-render, readme-typing-svg, shields.io, GitHub stats, and streak-card URLs.
- Produces: a self-contained English GitHub profile README.

- [ ] **Step 1: Add the failing README contract tests**

Append this class above the `if __name__ == "__main__"` block in
`tests/test_profile_readme.py`:

```python
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
```

- [ ] **Step 2: Run the README tests to verify they fail**

Run:

```powershell
python -m unittest tests.test_profile_readme.ProfileReadmeTests -v
```

Expected: FAIL because the existing README does not contain the LLM AgentOps
identity, new project sections, or local GIF.

- [ ] **Step 3: Replace `README.md` with the approved structure**

The replacement must contain these exact narrative blocks:

```markdown
I specialize in **LLM AgentOps**—turning agentic prototypes into observable,
testable, cost-aware, and reliable production systems. I also build
manufacturing planning platforms where complex operational workflows must
become validated and explainable decisions.

## Symphony — LLM AgentOps for APS Analytics

> A production AI-agent platform where LLM AgentOps practices make
> natural-language analytical workflows observable, validated, cost-aware, and
> reliable for advanced planning and scheduling.

- Built and refined multi-step agent behavior across planning, SQL-assisted
  analysis, validation, replanning, and report generation.
- Centralized LLM execution paths so runtime context, token usage, inference
  traces, and cost signals remain consistent across agent workflows.
- Added regression coverage for prompt injection, execution context, and SQL
  tooling to protect behavior during refactoring.
- Expanded production observability with Prometheus metrics and Grafana
  dashboards across agent, API, database, model, session, and tool layers.
- Contributed operational controls for usage reporting and protected API
  documentation access.

## Taelim — Manufacturing APS & Scheduling Engine

> A manufacturing planning engine for order allocation, machine scheduling, and
> lot composition in corrugated-packaging operations.

- Prevented stale demand from being processed twice during lot composition.
- Fixed confirmed-order recomposition flows so eligible orders remain in
  factory-specific planning.
- Refactored coating domain rules and strengthened work-in-progress and
  order-length data integrity.
- Added repeatable QA coverage with unit tests, integration datasets, and GitHub
  Actions workflows.
- Improved operational support with Oracle schema/index versioning,
  configurable logging, and engine-result exports.
```

The first screen must include:

- a full-width `capsule-render` waving header;
- the title `Sung Jun "Tony" Baek`;
- the subtitle `LLM AgentOps Engineer`;
- the three approved typing lines;
- LinkedIn, blog, and email badges;
- the local AgentOps GIF and meaningful alt text.

Use these exact visual-service URLs, encoding ampersands as `&amp;` when they
appear inside an HTML `src` attribute:

```text
https://capsule-render.vercel.app/api?type=waving&height=250&color=0:0F172A,50:0EA5E9,100:8B5CF6&text=Sung%20Jun%20%22Tony%22%20Baek&fontSize=44&fontColor=E2E8F0&animation=fadeIn&fontAlignY=38&desc=LLM%20AgentOps%20Engineer&descAlignY=58&descSize=22

https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=2800&pause=900&color=22D3EE&center=true&vCenter=true&width=900&lines=Operating+LLM+agents+with+reliability+and+observability;Engineering+manufacturing+APS+and+scheduling+systems;Turning+complex+workflows+into+validated+decisions

https://github-readme-stats.vercel.app/api?username=MarcoBackman&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0F172A

https://github-readme-stats.vercel.app/api/top-langs/?username=MarcoBackman&layout=compact&theme=tokyonight&hide_border=true&bg_color=0F172A

https://streak-stats.demolab.com?user=MarcoBackman&theme=tokyonight&hide_border=true&background=0F172A

https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:0F172A,50:0EA5E9,100:8B5CF6
```

The lower page must include:

- four grouped technology rows;
- a condensed earlier-experience section with links to ModelTranslator,
  `hibernate_quiz_webapp`, and `d-star-algorithm`;
- GitHub stats, top-languages, and streak cards labeled
  `Public GitHub Snapshot`;
- a matching `capsule-render` waving footer.

- [ ] **Step 4: Run all README and GIF contract tests**

Run:

```powershell
python -m unittest tests.test_profile_readme -v
```

Expected: all tests PASS.

- [ ] **Step 5: Validate Markdown whitespace and sensitive markers**

Run:

```powershell
git diff --check
rg -n "90%|15%|beak_heamin_saipan|currently looking for a project|/commit/|ticket|factory code" README.md
```

Expected: `git diff --check` succeeds and `rg` returns no matches.

- [ ] **Step 6: Commit the README**

```powershell
git add README.md tests/test_profile_readme.py tests/__init__.py
git commit -m "docs: refresh profile for LLM AgentOps career"
```

### Task 4: Verify the rendered profile

**Files:**
- Verify: `README.md`
- Verify: `assets/llm-agentops-flow.gif`

**Interfaces:**
- Consumes: final committed README and GIF.
- Produces: evidence that local assets, remote images, links, animation, and copy satisfy the approved design.

- [ ] **Step 1: Verify every local link target**

Run a Python link scan that extracts relative Markdown and HTML image paths from
`README.md`, resolves them against the repository root, and fails if a target
does not exist.

Expected: `./assets/llm-agentops-flow.gif` resolves successfully.

- [ ] **Step 2: Verify remote image endpoints**

Check the exact URLs embedded in `README.md` for:

- both capsule-render images;
- readme-typing-svg;
- every shields.io badge;
- GitHub stats and top-languages cards;
- the streak card.

Expected: each endpoint returns an image content type. If a best-effort stats
endpoint is temporarily unavailable, confirm its syntax against official
documentation and retain accessible fallback prose.

- [ ] **Step 3: Visually inspect the complete README**

Preview the Markdown at a GitHub-like content width and confirm:

- the header title is not clipped;
- the typing text fits its canvas;
- the GIF remains readable at scaled width;
- badge rows wrap acceptably on a narrow viewport;
- Symphony precedes Taelim;
- the page remains understandable without the remote cards.

- [ ] **Step 4: Run final verification**

Run:

```powershell
git status --short
git log -4 --oneline
python -m unittest tests.test_profile_readme -v
git diff --check HEAD~2..HEAD
```

Expected: clean worktree, all tests PASS, and no diff whitespace errors.
