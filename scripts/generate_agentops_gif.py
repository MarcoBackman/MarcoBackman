from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 960
HEIGHT = 540
FRAME_COUNT = 96
FRAME_DURATION_MS = 140

BACKGROUND = (8, 15, 31)
BACKGROUND_END = (18, 15, 43)
PANEL = (18, 29, 51)
PANEL_RAISED = (23, 38, 64)
GRID = (22, 36, 59)
LINE = (53, 70, 94)
TEXT = (226, 232, 240)
MUTED = (148, 163, 184)
CYAN = (34, 211, 238)
BLUE = (56, 189, 248)
VIOLET = (139, 92, 246)
SUCCESS = (52, 211, 153)
WARNING = (251, 191, 36)

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
STAGE_SUBTITLES = (
    "business question",
    "policy + safety",
    "retrieve evidence",
    "create tasks",
    "validate + execute",
    "grounding check",
    "request evidence",
    "decision ready",
)
STAGE_START_MS = (300, 1_200, 1_850, 2_400, 4_000, 6_200, 7_600, 10_800)

DECISION_TEXT = "Prioritize 3 at-risk orders before capacity lock."
QUESTION_TEXT = "Which orders are at risk this week?"

STATUS_TIMELINE = (
    (0, "RUNNING", CYAN),
    (6_200, "EVALUATING", WARNING),
    (7_600, "REPLANNING", VIOLET),
    (10_800, "VERIFIED", SUCCESS),
)

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

REGULAR_FONT_CANDIDATES = (
    Path("C:/Windows/Fonts/consola.ttf"),
    Path("/System/Library/Fonts/Menlo.ttc"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
    Path("/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf"),
    Path("DejaVuSansMono.ttf"),
)
BOLD_FONT_CANDIDATES = (
    Path("C:/Windows/Fonts/consolab.ttf"),
    Path("/System/Library/Fonts/Menlo.ttc"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"),
    Path("/usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf"),
    Path("DejaVuSansMono-Bold.ttf"),
)


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = BOLD_FONT_CANDIDATES if bold else REGULAR_FONT_CANDIDATES
    for candidate in candidates:
        try:
            return ImageFont.truetype(str(candidate), size)
        except OSError:
            continue
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def mix(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    amount: float,
) -> tuple[int, int, int]:
    amount = max(0.0, min(1.0, amount))
    return tuple(round(a + (b - a) * amount) for a, b in zip(left, right))


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


def draw_background(draw: ImageDraw.ImageDraw) -> None:
    for y in range(HEIGHT):
        draw.line(
            (0, y, WIDTH, y),
            fill=mix(BACKGROUND, BACKGROUND_END, y / (HEIGHT - 1)),
        )
    for x in range(0, WIDTH, 32):
        draw.line((x, 0, x, HEIGHT), fill=GRID, width=1)
    for y in range(0, HEIGHT, 32):
        draw.line((0, y, WIDTH, y), fill=GRID, width=1)


def text_width(
    draw: ImageDraw.ImageDraw,
    value: str,
    font: ImageFont.ImageFont,
) -> int:
    bounds = draw.textbbox((0, 0), value, font=font)
    return bounds[2] - bounds[0]


def draw_badge(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    value: str,
    font: ImageFont.ImageFont,
    color: tuple[int, int, int],
    padding_x: int = 10,
) -> int:
    x, y = xy
    width = text_width(draw, value, font) + padding_x * 2
    draw.rounded_rectangle(
        (x, y, x + width, y + 26),
        radius=8,
        fill=mix(PANEL, color, 0.12),
        outline=mix(LINE, color, 0.75),
        width=2,
    )
    draw.text((x + padding_x, y + 5), value, font=font, fill=color)
    return width


def draw_header(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    title_font: ImageFont.ImageFont,
    label_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
    draw.text(
        (32, 20),
        "LLM AGENTOPS // PRODUCTION TRACE",
        font=title_font,
        fill=TEXT,
    )
    draw_badge(draw, (779, 18), "SAMPLE RUN", small_font, BLUE)

    current = elapsed_ms(frame_index)
    status_label = STATUS_TIMELINE[0][1]
    status_color = STATUS_TIMELINE[0][2]
    for start_ms, label, color in STATUS_TIMELINE:
        if current >= start_ms:
            status_label = label
            status_color = color

    draw.text((32, 56), "trace: demo-run-0241", font=small_font, fill=MUTED)
    draw.text(
        (238, 56),
        "environment: production-like demo",
        font=small_font,
        fill=MUTED,
    )
    status_width = text_width(draw, status_label, small_font) + 26
    draw_badge(
        draw,
        (WIDTH - 32 - status_width, 51),
        status_label,
        small_font,
        status_color,
        padding_x=13,
    )

    draw.rounded_rectangle(
        (32, 84, 928, 112),
        radius=8,
        fill=(13, 25, 45),
        outline=LINE,
        width=1,
    )
    draw.text((44, 90), "QUESTION", font=label_font, fill=CYAN)
    draw.text((146, 90), QUESTION_TEXT, font=small_font, fill=TEXT)


def draw_arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    progress: float,
    color: tuple[int, int, int],
) -> None:
    draw.line((*start, *end), fill=LINE, width=3)
    progress = max(0.0, min(1.0, progress))
    current = (
        round(start[0] + (end[0] - start[0]) * progress),
        round(start[1] + (end[1] - start[1]) * progress),
    )
    if progress > 0:
        draw.line((*start, *current), fill=color, width=4)
        draw.ellipse(
            (current[0] - 3, current[1] - 3, current[0] + 3, current[1] + 3),
            fill=color,
        )
    if progress >= 1:
        if end[0] < start[0]:
            points = ((end[0], end[1]), (end[0] + 8, end[1] - 5), (end[0] + 8, end[1] + 5))
        elif end[0] > start[0]:
            points = ((end[0], end[1]), (end[0] - 8, end[1] - 5), (end[0] - 8, end[1] + 5))
        else:
            points = ((end[0], end[1]), (end[0] - 5, end[1] - 8), (end[0] + 5, end[1] - 8))
        draw.polygon(points, fill=color)


def stage_color(frame_index: int, stage_index: int) -> tuple[int, int, int]:
    current = elapsed_ms(frame_index)
    if stage_index == 5:
        if 6_200 <= current < 9_400:
            return WARNING
        if current >= 9_400:
            return SUCCESS
    if stage_index == 6 and current >= 7_600:
        return VIOLET
    if stage_index == 7 and current >= 10_800:
        return SUCCESS
    return CYAN


def draw_execution_graph(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    node_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
    node_width = 196
    node_height = 64
    top_y = 122
    bottom_y = 202
    x_positions = (32, 256, 480, 704)
    boxes = (
        (x_positions[0], top_y),
        (x_positions[1], top_y),
        (x_positions[2], top_y),
        (x_positions[3], top_y),
        (x_positions[3], bottom_y),
        (x_positions[2], bottom_y),
        (x_positions[1], bottom_y),
        (x_positions[0], bottom_y),
    )

    for index in range(len(boxes) - 1):
        x, y = boxes[index]
        next_x, next_y = boxes[index + 1]
        if index == 3:
            start = (x + node_width // 2, y + node_height)
            end = (next_x + node_width // 2, next_y)
        else:
            start = (
                x + node_width if next_x > x else x,
                y + node_height // 2,
            )
            end = (
                next_x if next_x > x else next_x + node_width,
                next_y + node_height // 2,
            )
        connector_start = STAGE_START_MS[index]
        connector_end = STAGE_START_MS[index + 1]
        connector_color = stage_color(frame_index, index + 1)
        draw_arrow(
            draw,
            start,
            end,
            progress_between(frame_index, connector_start, connector_end),
            connector_color,
        )

    recheck_progress = progress_between(frame_index, 7_600, 9_400)
    replan_center_x = boxes[6][0] + node_width // 2
    evaluate_center_x = boxes[5][0] + node_width // 2
    loop_y = bottom_y - 7
    draw.line(
        (
            replan_center_x,
            bottom_y,
            replan_center_x,
            loop_y,
            evaluate_center_x,
            loop_y,
            evaluate_center_x,
            bottom_y,
        ),
        fill=mix(LINE, VIOLET, recheck_progress),
        width=2,
    )
    if recheck_progress > 0:
        cursor_x = round(
            replan_center_x + (evaluate_center_x - replan_center_x) * recheck_progress
        )
        draw.ellipse(
            (cursor_x - 3, loop_y - 3, cursor_x + 3, loop_y + 3),
            fill=VIOLET,
        )
    if is_active(frame_index, 7_600):
        draw.text((409, 183), "2ND PASS", font=small_font, fill=VIOLET)

    current = elapsed_ms(frame_index)
    for index, ((x, y), stage, subtitle) in enumerate(
        zip(boxes, STAGES, STAGE_SUBTITLES)
    ):
        active = is_active(frame_index, STAGE_START_MS[index])
        color = stage_color(frame_index, index)
        border = color if active else LINE
        fill = mix(PANEL, color, 0.16 if active else 0.0)

        if index == 5 and 6_200 <= current < 9_400:
            subtitle = "evidence gap"
        elif index == 5 and current >= 9_400:
            subtitle = "2/2 checks pass"

        draw.rounded_rectangle(
            (x, y, x + node_width, y + node_height),
            radius=12,
            fill=fill,
            outline=border,
            width=3 if active else 2,
        )
        draw.ellipse(
            (x + 13, y + 16, x + 21, y + 24),
            fill=color if active else LINE,
        )
        draw.text(
            (x + 31, y + 10),
            stage,
            font=node_font,
            fill=TEXT if active else MUTED,
        )
        draw.text(
            (x + 14, y + 37),
            subtitle,
            font=small_font,
            fill=color if active else MUTED,
        )


def draw_trace_waterfall(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    label_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
    panel = (32, 282, 632, 467)
    draw.rounded_rectangle(panel, radius=14, fill=PANEL, outline=LINE, width=2)
    draw.text((48, 296), "EXECUTION TRACE", font=label_font, fill=BLUE)
    draw.text((479, 297), "0 ms", font=small_font, fill=MUTED)
    draw.text((570, 297), "13.4 s", font=small_font, fill=MUTED)

    label_x = 48
    bar_left = 234
    bar_right = 606
    row_top = 321
    row_step = 17
    total_ms = FRAME_COUNT * FRAME_DURATION_MS
    current = elapsed_ms(frame_index)

    cursor_x = round(bar_left + (bar_right - bar_left) * min(current / total_ms, 1.0))
    draw.line((cursor_x, row_top - 2, cursor_x, 457), fill=mix(LINE, CYAN, 0.7), width=1)

    for row_index, (name, start_ms, end_ms) in enumerate(TRACE_ROWS):
        y = row_top + row_index * row_step
        draw.text((label_x, y), name, font=small_font, fill=TEXT)
        start_x = round(bar_left + (bar_right - bar_left) * start_ms / total_ms)
        end_x = round(bar_left + (bar_right - bar_left) * end_ms / total_ms)
        draw.rounded_rectangle(
            (start_x, y + 3, end_x, y + 12),
            radius=4,
            fill=(38, 52, 75),
        )

        if current < start_ms:
            progress = 0.0
            color = LINE
        elif current < end_ms:
            progress = (current - start_ms) / (end_ms - start_ms)
            color = CYAN
        else:
            progress = 1.0
            color = SUCCESS

        if name == "evaluator.grounding":
            if 6_200 <= current < 9_400:
                color = WARNING
            elif current >= 9_400:
                color = SUCCESS
        elif name == "planner.replan" and current >= start_ms:
            color = VIOLET

        filled_end = round(start_x + (end_x - start_x) * progress)
        if progress > 0:
            draw.rounded_rectangle(
                (start_x, y + 3, filled_end, y + 12),
                radius=4,
                fill=color,
            )
        marker = "○"
        if start_ms <= current < end_ms:
            marker = "●"
        elif current >= end_ms:
            marker = "✓"
        draw.text((610, y), marker, font=small_font, fill=color)


def draw_demo_telemetry(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    label_font: ImageFont.ImageFont,
    metric_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
    panel = (648, 282, 928, 467)
    draw.rounded_rectangle(panel, radius=14, fill=PANEL, outline=LINE, width=2)
    draw.text((664, 296), "DEMO TELEMETRY", font=label_font, fill=VIOLET)

    metrics = (
        ("LATENCY", "3.42s", 4_000, 664, 326),
        ("TOKENS", "1,842", 4_650, 798, 326),
        ("COST", "$0.018", 6_200, 664, 378),
        ("VALIDATION", "2/2 PASS", 9_400, 798, 378),
        ("EVIDENCE", "3 SOURCES", 10_800, 664, 430),
    )
    current = elapsed_ms(frame_index)
    for label, value, reveal_ms, x, y in metrics:
        visible = current >= reveal_ms
        color = SUCCESS if label in {"VALIDATION", "EVIDENCE"} and visible else CYAN
        draw.text((x, y), label, font=small_font, fill=MUTED)
        draw.text(
            (x, y + 18),
            value if visible else "—",
            font=metric_font,
            fill=color if visible else LINE,
        )


def draw_decision_strip(
    draw: ImageDraw.ImageDraw,
    frame_index: int,
    label_font: ImageFont.ImageFont,
    decision_font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
    reveal = progress_between(frame_index, 10_800, 12_200)
    border = mix(LINE, SUCCESS, reveal)
    fill = mix(PANEL, (17, 62, 57), reveal * 0.52)
    draw.rounded_rectangle(
        (32, 478, 928, 524),
        radius=12,
        fill=fill,
        outline=border,
        width=2,
    )
    if reveal <= 0:
        draw.text((48, 493), "DECISION", font=label_font, fill=MUTED)
        draw.text(
            (174, 493),
            "Waiting for verified evidence",
            font=small_font,
            fill=LINE,
        )
        return

    draw.text(
        (48, 493),
        "VERIFIED DECISION",
        font=label_font,
        fill=mix(MUTED, SUCCESS, reveal),
    )
    draw.text(
        (250, 491),
        DECISION_TEXT,
        font=decision_font,
        fill=mix(MUTED, TEXT, reveal),
    )
    check_x = 902
    draw.ellipse(
        (check_x - 10, 491, check_x + 10, 511),
        fill=mix(PANEL_RAISED, SUCCESS, reveal),
    )
    draw.text((check_x - 5, 492), "✓", font=small_font, fill=BACKGROUND)


def draw_frame(frame_index: int) -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw_background(draw)

    title_font = load_font(24, bold=True)
    node_font = load_font(16, bold=True)
    label_font = load_font(16, bold=True)
    metric_font = load_font(20, bold=True)
    decision_font = load_font(18, bold=True)
    small_font = load_font(15)

    draw_header(draw, frame_index, title_font, label_font, small_font)
    draw_execution_graph(draw, frame_index, node_font, small_font)
    draw_trace_waterfall(draw, frame_index, label_font, small_font)
    draw_demo_telemetry(draw, frame_index, label_font, metric_font, small_font)
    draw_decision_strip(draw, frame_index, label_font, decision_font, small_font)
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
