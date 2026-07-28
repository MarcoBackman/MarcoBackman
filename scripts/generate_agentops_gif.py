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
    return ImageFont.load_default()


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
