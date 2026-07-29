# LLM AgentOps Production Trace GIF V2 Design

## Goal

Replace the short, generic workflow animation with a professional production
trace console that demonstrates what LLM AgentOps work looks like in practice:
guardrails, context assembly, planning, tool execution, evaluation, replanning,
observability, and a grounded decision.

The animation remains illustrative. It must not reproduce an internal product
screen, customer data, private architecture, or actual performance metrics.

## Visual direction

Use an enterprise observability-console aesthetic rather than a decorative
pipeline diagram.

- Canvas: `960 × 540`
- Target loop duration: `12.5–14 seconds`
- Target source frames: approximately `96–108`
- Target file size: under `6 MB`
- Palette:
  - Background: `#0F172A`
  - Panel: `#162038`
  - Primary cyan: `#22D3EE`
  - Supporting blue: `#38BDF8`
  - Violet: `#8B5CF6`
  - Success green: `#34D399`
  - Warning amber: `#FBBF24`
  - Text: `#E2E8F0`
  - Muted: `#94A3B8`

Animation should be deliberate and restrained: progressive state changes,
waterfall bars, status transitions, and a single replan loop. Avoid excessive
glow, random particles, arcade-like motion, or rapidly flashing elements.

## Scenario

Use one clearly synthetic manufacturing-planning question:

> Which orders are at risk this week?

The final synthetic decision is:

> Prioritize 3 at-risk orders before capacity lock.

Every telemetry panel must be labeled `DEMO TELEMETRY` so its values cannot be
mistaken for real Symphony results.

## Layout

### Header band

Show:

- `LLM AGENTOPS // PRODUCTION TRACE`
- `SAMPLE RUN`
- `trace: demo-run-0241`
- `environment: production-like demo`
- animated status chip: `RUNNING → EVALUATING → REPLANNING → VERIFIED`

### Execution graph

Use two rows of four readable nodes:

```text
REQUEST → GUARDRAIL → CONTEXT → PLAN
                                  ↓
REPORT  ← REPLAN    ← EVALUATE ← TOOL / SQL
```

The normal path lights in cyan. The first evaluation turns amber and routes
through a visible violet `REPLAN` loop. The second evaluation turns green and
continues to `REPORT`.

Supporting labels:

- Guardrail: `policy pass`
- Context: `3 sources ready`
- Plan: `3 tasks`
- Tool / SQL: `read-only query`
- Evaluate, first pass: `evidence gap`
- Replan: `add capacity check`
- Evaluate, second pass: `2/2 checks pass`
- Report: `grounded response`

### Lower-left: execution trace waterfall

Show progressive rows with a duration bar and status:

1. `safety.check`
2. `context.retrieve`
3. `planner.create_tasks`
4. `sql.validate`
5. `tool.execute`
6. `evaluator.grounding`
7. `planner.replan`
8. `report.synthesize`

Durations are synthetic and visual only. The waterfall should make parent/child
execution order obvious without showing internal file paths or service names.

### Lower-right: demo telemetry

Show large, readable values:

- `Latency 3.42s`
- `Tokens 1,842`
- `Est. cost $0.018`
- `Validation 2/2 PASS`
- `Evidence 3 sources`

Show smaller operational badges:

- `READ-ONLY SQL`
- `POLICY PASS`
- `TRACE COMPLETE`

### Decision strip

At the end of the loop, reveal:

- Heading: `VERIFIED DECISION`
- Decision: `Prioritize 3 at-risk orders before capacity lock.`
- Supporting label: `grounded · policy-safe · observable`

## Timeline

1. `0.0–1.2s` — console initializes and the sample question appears.
2. `1.2–2.4s` — request, guardrail, and context stages complete.
3. `2.4–4.0s` — planner produces three tasks.
4. `4.0–6.2s` — read-only SQL/tool execution fills the trace waterfall.
5. `6.2–7.6s` — evaluation turns amber with `evidence gap`.
6. `7.6–9.4s` — violet replan loop adds a capacity check.
7. `9.4–10.8s` — second evaluation passes in green.
8. `10.8–12.2s` — report and demo telemetry resolve.
9. `12.2–13.4s` — verified decision holds long enough to read before reset.

## Typography and responsive readability

- Use the existing cross-platform monospace font resolver.
- Main title: at least `24 px`.
- Node labels: at least `16 px`, bold.
- Metric values: at least `18 px`, bold.
- Supporting text: at least `15 px`.
- Do not add any body text smaller than `15 px`.
- At a `420 px` rendered width, the primary node labels, status, telemetry
  values, and final decision must remain identifiable. Secondary waterfall
  durations may be less prominent.

## Generator architecture

Keep the asset reproducible in `scripts/generate_agentops_gif.py`.

Recommended code boundaries:

- timeline constants and scene thresholds;
- color and font helpers;
- header/status rendering;
- execution-graph rendering;
- trace-waterfall rendering;
- telemetry rendering;
- decision-strip rendering;
- frame assembly and optimized GIF export.

Use deterministic interpolation and synthetic data only. No randomness,
network calls, timestamps, or environment-dependent text.

## README integration

- Keep the asset path `./assets/llm-agentops-flow.gif`.
- Change the image width to `100%` so it scales with GitHub's content column.
- Update the alt text to mention guardrails, planning, tool execution,
  evaluation, replanning, telemetry, and a verified decision.
- Keep the static LLM AgentOps narrative immediately below the GIF.

## Test contract

Update `tests/test_profile_readme.py` to verify:

- GIF format;
- `960 × 540` dimensions;
- infinite loop;
- at least `70` optimized frames;
- summed frame duration of at least `12,000 ms`;
- file size below `6,000,000` bytes;
- generator fallback font behavior;
- README references the same asset with `width="100%"`;
- README alt text includes the professional AgentOps concepts.

## Verification

- Run the complete profile test suite.
- Regenerate the asset twice and confirm deterministic output on the same
  environment.
- Inspect representative frames from initialization, first evaluation,
  replanning, verified evaluation, and final decision.
- Inspect the animation at original size, GitHub desktop width, and `420 px`.
- Confirm the final decision remains visible for at least one second.
- Confirm no actual project metrics, customer data, private URLs, internal IDs,
  or implementation paths appear.
