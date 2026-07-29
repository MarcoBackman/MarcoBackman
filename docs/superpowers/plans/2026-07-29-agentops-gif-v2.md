# Professional LLM AgentOps Trace GIF V2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the short generic workflow GIF with a 13-second professional production-trace animation that demonstrates guardrails, planning, tool execution, evaluation, replanning, telemetry, and a verified decision.

**Architecture:** Refactor the deterministic Pillow generator into focused renderers for the header, execution graph, trace waterfall, telemetry, and decision strip. Drive every renderer from one 96-frame timeline, validate the exported GIF and README contract with `unittest`, and inspect five representative scenes at desktop and mobile widths.

**Tech Stack:** Python 3.13, Pillow 12.1, `unittest`, GitHub Flavored Markdown

## Global Constraints

- Canvas is exactly `960 × 540`.
- Source animation uses `96` frames at `140 ms` per frame for a `13,440 ms` loop.
- Optimized GIF retains at least `70` frames, loops infinitely, and is below `6,000,000` bytes.
- The animation contains no text smaller than `15 px`.
- The visual path is `REQUEST → GUARDRAIL → CONTEXT → PLAN → TOOL / SQL → EVALUATE → REPLAN → REPORT`.
- The first evaluation displays `evidence gap`; the second displays `2/2 checks pass`.
- Every synthetic metric is visually grouped under `DEMO TELEMETRY`.
- The final decision is `Prioritize 3 at-risk orders before capacity lock.`
- No private URLs, customer data, internal IDs, actual project metrics, file paths, or factory codes appear.
- The README keeps `./assets/llm-agentops-flow.gif`, uses `width="100%"`, and retains static fallback narrative.
- Preserve the existing cross-platform font fallback.

## File map

- Modify: `scripts/generate_agentops_gif.py`
  - Owns the deterministic timeline and all five focused rendering regions.
- Modify: `assets/llm-agentops-flow.gif`
  - Stores the optimized V2 animation.
- Modify: `tests/test_profile_readme.py`
  - Verifies dimensions, duration, frames, determinism, file size, semantic constants, and README integration.
- Modify: `README.md`
  - Uses responsive width and professional AgentOps alt text.

---

### Task 1: Establish the V2 contract with failing tests

**Files:**
- Modify: `tests/test_profile_readme.py`

**Interfaces:**
- Consumes: existing `generate_gif(output_path: Path) -> None`.
- Produces: executable V2 requirements that Task 2 must satisfy.

- [ ] **Step 1: Add imports for the V2 semantic contract**

Update the generator import:

```python
from scripts.generate_agentops_gif import (
    DECISION_TEXT,
    FRAME_COUNT,
    FRAME_DURATION_MS,
    HEIGHT,
    STAGES,
    WIDTH,
    generate_gif,
    load_font,
)
```

- [ ] **Step 2: Replace the old GIF contract assertions**

The generated and committed GIF tests must use:

```python
def assert_v2_gif_contract(test_case: unittest.TestCase, path: Path) -> None:
    with Image.open(path) as image:
        durations = []
        for frame_index in range(image.n_frames):
            image.seek(frame_index)
            durations.append(image.info.get("duration", 0))

        test_case.assertEqual(image.format, "GIF")
        test_case.assertEqual(image.size, (960, 540))
        test_case.assertGreaterEqual(image.n_frames, 70)
        test_case.assertEqual(image.info.get("loop"), 0)
        test_case.assertGreaterEqual(sum(durations), 12_000)


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
```

- [ ] **Step 3: Add semantic and determinism tests**

```python
def test_v2_timeline_and_semantics_are_stable(self) -> None:
    self.assertEqual((WIDTH, HEIGHT), (960, 540))
    self.assertEqual(FRAME_COUNT, 96)
    self.assertEqual(FRAME_DURATION_MS, 140)
    self.assertEqual(
        STAGES,
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
        DECISION_TEXT,
        "Prioritize 3 at-risk orders before capacity lock.",
    )


def test_generator_is_deterministic_in_one_environment(self) -> None:
    with TemporaryDirectory() as directory:
        first = Path(directory) / "first.gif"
        second = Path(directory) / "second.gif"
        generate_gif(first)
        generate_gif(second)
        self.assertEqual(first.read_bytes(), second.read_bytes())
```

- [ ] **Step 4: Add the future README integration assertions**

```python
def test_professional_gif_is_responsive_and_descriptive(self) -> None:
    self.assertIn('src="./assets/llm-agentops-flow.gif"', self.readme)
    self.assertIn('width="100%"', self.readme)
    self.assertIn(
        "guardrails, planning, tool execution, evaluation, replanning, "
        "demo telemetry, and a verified decision",
        self.readme,
    )
```

- [ ] **Step 5: Run the targeted tests and confirm RED**

Run:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme.AgentOpsGifTests -v
python -m unittest tests.test_profile_readme.ProfileReadmeTests.test_professional_gif_is_responsive_and_descriptive -v
```

Expected: FAIL because the current generator is `960 × 360`, uses 48 source
frames and five stages, and the README uses `width="960"`.

- [ ] **Step 6: Commit the failing contract**

```powershell
git add tests/test_profile_readme.py
git commit -m "test: define professional AgentOps GIF contract"
```

### Task 2: Implement the production-trace generator

**Files:**
- Modify: `scripts/generate_agentops_gif.py`
- Modify: `assets/llm-agentops-flow.gif`

**Interfaces:**
- Preserves: `load_font(size: int, bold: bool = False) -> ImageFont.ImageFont`
- Preserves: `generate_gif(output_path: Path) -> None`
- Produces: `draw_frame(frame_index: int) -> Image.Image`
- Produces: five region renderers consuming `ImageDraw`, fonts, and normalized timeline progress.

- [ ] **Step 1: Replace the timeline constants**

Use:

```python
WIDTH = 960
HEIGHT = 540
FRAME_COUNT = 96
FRAME_DURATION_MS = 140
STAGES = (
    "REQUEST",
    "GUARDRAIL",
    "CONTEXT",
    "PLAN",
    "TOOL / SQL",
    "EVALUATE",
    "REPLAN",
    "REPORT",
)
DECISION_TEXT = "Prioritize 3 at-risk orders before capacity lock."
QUESTION_TEXT = "Which orders are at risk this week?"
```

Add `SUCCESS = (52, 211, 153)` and `WARNING = (251, 191, 36)` while retaining
the approved navy/cyan/blue/violet colors.

- [ ] **Step 2: Add deterministic timeline helpers**

```python
def elapsed_ms(frame_index: int) -> int:
    return frame_index * FRAME_DURATION_MS


def progress_between(frame_index: int, start_ms: int, end_ms: int) -> float:
    current = elapsed_ms(frame_index)
    if current <= start_ms:
        return 0.0
    if current >= end_ms:
        return 1.0
    return (current - start_ms) / (end_ms - start_ms)


def is_active(frame_index: int, start_ms: int) -> bool:
    return elapsed_ms(frame_index) >= start_ms
```

- [ ] **Step 3: Implement the header renderer**

Create:

```python
def draw_header(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    title_font: ImageFont.ImageFont,
    label_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
```

It must render the title, `SAMPLE RUN`, trace/environment labels, the synthetic
question, and one status selected from:

```python
STATUS_TIMELINE = (
    (0, "RUNNING", CYAN),
    (6_200, "EVALUATING", WARNING),
    (7_600, "REPLANNING", VIOLET),
    (10_800, "VERIFIED", SUCCESS),
)
```

- [ ] **Step 4: Implement the two-row execution graph**

Create:

```python
def draw_execution_graph(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    node_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
```

Use four nodes at y=`132` and four nodes at y=`212`. Draw a vertical handoff
from `PLAN` to `TOOL / SQL`, then a right-to-left lower row. Show the amber
first evaluation from `6,200–7,600 ms`, the violet replan loop from
`7,600–9,400 ms`, and the green verified route after `9,400 ms`.

- [ ] **Step 5: Implement the trace waterfall**

Create:

```python
TRACE_ROWS = (
    ("safety.check", 1_200, 1_850),
    ("context.retrieve", 1_650, 2_400),
    ("planner.create_tasks", 2_400, 4_000),
    ("sql.validate", 4_000, 4_850),
    ("tool.execute", 4_650, 6_200),
    ("evaluator.grounding", 6_200, 7_600),
    ("planner.replan", 7_600, 9_400),
    ("report.synthesize", 10_800, 12_200),
)


def draw_trace_waterfall(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    label_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
```

Render it in the lower-left panel with readable 15px labels, proportional
duration bars, and state indicators. Use warning for the first grounding
evaluation and success after replanning.

- [ ] **Step 6: Implement telemetry and decision renderers**

Create:

```python
def draw_demo_telemetry(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    label_font: ImageFont.ImageFont,
    metric_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:


def draw_decision_strip(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    label_font: ImageFont.ImageFont,
    decision_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
```

Telemetry appears progressively after `4,000 ms` and resolves fully after
`10,800 ms`. The decision strip begins at `10,800 ms`, reaches full opacity by
`12,200 ms`, and remains visible through the final frame.

- [ ] **Step 7: Assemble frames with minimum typography**

`draw_frame()` must load:

```python
title_font = load_font(24, bold=True)
node_font = load_font(16, bold=True)
label_font = load_font(16, bold=True)
metric_font = load_font(20, bold=True)
decision_font = load_font(18, bold=True)
small_font = load_font(15)
```

No renderer may load a smaller font.

- [ ] **Step 8: Generate and test the V2 asset**

Run:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python scripts/generate_agentops_gif.py
python -m unittest tests.test_profile_readme.AgentOpsGifTests -v
```

Expected: all GIF tests PASS, asset below 6 MB.

- [ ] **Step 9: Commit the generator and asset**

```powershell
git add scripts/generate_agentops_gif.py assets/llm-agentops-flow.gif
git commit -m "feat: expand AgentOps GIF into production trace"
```

### Task 3: Update the README integration

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: `./assets/llm-agentops-flow.gif`.
- Produces: responsive GitHub rendering and meaningful fallback text.

- [ ] **Step 1: Replace the GIF image element**

Use:

```html
<img
  src="./assets/llm-agentops-flow.gif"
  alt="Animated LLM AgentOps production trace showing guardrails, planning, tool execution, evaluation, replanning, demo telemetry, and a verified decision"
  width="100%"
/>
```

- [ ] **Step 2: Run the README integration test**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme.ProfileReadmeTests.test_professional_gif_is_responsive_and_descriptive -v
```

Expected: PASS.

- [ ] **Step 3: Run the complete profile suite**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme -v
git diff --check
```

Expected: all tests PASS and no whitespace errors.

- [ ] **Step 4: Commit the README integration**

```powershell
git add README.md
git commit -m "docs: embed responsive AgentOps production trace"
```

### Task 4: Verify professional quality and PR scope

**Files:**
- Verify: `assets/llm-agentops-flow.gif`
- Verify: `README.md`
- Verify: `scripts/generate_agentops_gif.py`
- Verify: `tests/test_profile_readme.py`

**Interfaces:**
- Consumes: final V2 asset and README.
- Produces: visual and automated evidence suitable for updating draft PR #1.

- [ ] **Step 1: Export representative frames to ignored scratch space**

Create `.superpowers/gif-v2-preview/` and export frames nearest:

- `700 ms` initialization;
- `6,900 ms` evidence gap;
- `8,500 ms` replanning;
- `10,200 ms` verified evaluation;
- `12,700 ms` final decision.

Use Pillow to seek by accumulated frame durations so GIF optimization does not
change the selected scene.

- [ ] **Step 2: Inspect all five original-size frames**

Confirm:

- text does not overlap or clip;
- the two-row graph reads in the intended direction;
- amber evidence gap and violet replan are visually distinct;
- telemetry values sit under `DEMO TELEMETRY`;
- final decision is fully readable.

- [ ] **Step 3: Inspect desktop and 420px renders**

Render the GIF region at GitHub desktop width and `420 px`. Confirm primary
nodes, status, metric values, and decision remain identifiable. Record any
secondary waterfall text limitation honestly.

- [ ] **Step 4: Run final automated verification**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme -v
git diff --check origin/main..HEAD
git status --short
git diff --name-status origin/main..HEAD
```

Expected:

- all tests PASS;
- diff check is clean;
- worktree is clean;
- net PR diff contains only README, GIF, generator, and tests after the
  temporary design/plan documents are removed.

- [ ] **Step 5: Remove temporary design/plan documents before PR update**

Remove:

- `docs/superpowers/specs/2026-07-29-agentops-gif-v2-design.md`
- `docs/superpowers/plans/2026-07-29-agentops-gif-v2.md`

Commit:

```powershell
git add -u docs/superpowers
git commit -m "chore: keep GIF design notes out of profile PR"
```

- [ ] **Step 6: Push and verify draft PR #1**

```powershell
git push origin feature/llm-agentops-profile
```

Confirm PR #1 remains draft, mergeable, and contains only the intended net
profile files.
