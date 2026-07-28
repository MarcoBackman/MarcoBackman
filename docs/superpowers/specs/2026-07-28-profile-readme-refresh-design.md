# GitHub Profile README Refresh Design

## Goal

Turn the `MarcoBackman` profile README into a polished, animated portfolio that
positions Sung Jun "Tony" Baek's recent career around LLM AgentOps, supported by
production AI-agent and manufacturing APS engineering work.

The profile should feel visually memorable within the first screen, while the
project descriptions remain specific, credible, and readable for engineering
recruiters and technical peers.

## Evidence and privacy boundaries

- Use the public LinkedIn profile as the source for role, positioning, and
  career-level context.
- Use the user's GitHub commits, inspected with explicit permission, to verify
  high-level technical contributions to Symphony and Taelim.
- Name Symphony and Taelim because the user explicitly requested them as the
  primary project highlights.
- Do not link private repositories or expose commit hashes, ticket numbers,
  branch names, file paths, database topology, customer data, factory codes, or
  other internal implementation details.
- Generalize the custom animation and architecture wording so they illustrate
  the engineering approach rather than reproduce an internal product screen.
- Omit the LinkedIn metrics of `90%` lead-time reduction and `15%` productivity
  improvement until the user confirms which project each metric belongs to.
- Present GitHub cards as a public-repository snapshot. Public card services do
  not represent the user's private professional work.

## Visual direction

### Selected direction: Aurora Manufacturing Intelligence

Use a deep navy, cyan, and violet palette that combines industrial reliability
with modern AI-platform energy.

- Base: `#0F172A`
- Cyan accent: `#22D3EE`
- Violet accent: `#8B5CF6`
- Light text: `#E2E8F0`
- Supporting blue: `#38BDF8`

The page should be visually rich but keep animation concentrated in three
places: the header, the typing line, and one custom project-flow GIF.

### Alternatives considered

1. **Industrial Blueprint** — restrained navy and steel-blue diagrams; strongest
   for a traditional enterprise tone, but less expressive than requested.
2. **Neon Agent Terminal** — black, green, and purple terminal styling; highly
   animated, but it over-emphasizes developer aesthetics and underplays the
   manufacturing domain.
3. **Aurora Manufacturing Intelligence** — balances production engineering and
   AI-agent identity; selected as the best fit.

## Content structure

The previous "Recent work" and `beak_heamin_saipan` sections are removed.

1. Animated identity header
2. Compact professional introduction and contact links
3. Custom AI-agent workflow GIF
4. Symphony project highlight
5. Taelim project highlight
6. Verified technology stack
7. Condensed earlier experience
8. Public GitHub statistics
9. Matching animated footer

## Detailed README draft

### 1. Animated identity header

Use `capsule-render` with a `waving` header, a fixed custom gradient, and a
`fadeIn` title animation.

Displayed identity:

> Sung Jun "Tony" Baek<br>
> LLM AgentOps Engineer

The generated SVG URL will use explicit colors rather than random themes so the
header and footer remain visually consistent on every visit.

### 2. Typing statement and introduction

Use `readme-typing-svg` with centered, looping lines:

> Operating LLM agents with reliability and observability<br>
> Engineering manufacturing APS and scheduling systems<br>
> Turning complex workflows into validated decisions

Proposed introduction:

> I am a software engineer specializing in LLM AgentOps: turning agentic
> prototypes into observable, testable, and reliable production systems. I also
> build manufacturing planning platforms where complex operational workflows
> must become validated and explainable decisions.

Contact badges:

- LinkedIn
- Technical blog
- Email

No generic "currently looking for a project" statement will remain.

### 3. Custom GIF: From Question to Decision

Create `assets/ai-agent-workflow.gif` as an original looping animation rather
than using a third-party stock GIF.

Storyboard:

1. A user question enters a dark terminal-style panel.
2. Five nodes illuminate in sequence:
   `QUESTION → PLAN → QUERY → VALIDATE → INSIGHT`.
3. A small trace panel shows safe, generic status messages such as
   `context ready`, `query validated`, and `report generated`.
4. The result resolves into a compact chart and a decision card.
5. The animation holds briefly, then loops smoothly.

The GIF must not contain real customer data, an internal product screenshot, or
an exact representation of the private system architecture. Target dimensions
are approximately `960 × 360`, optimized to remain legible on GitHub without a
large repository-size cost.

### 4. Symphony — LLM AgentOps for APS Analytics

Proposed lead:

> A production AI-agent platform where LLM AgentOps practices make
> natural-language analytical workflows observable, validated, cost-aware, and
> reliable for advanced planning and scheduling.

Verified contribution bullets:

- Built and refined multi-step agent behavior around planning, SQL-assisted
  analysis, validation, replanning, and report generation.
- Centralized LLM execution paths so runtime context, token usage, inference
  traces, and cost signals remain consistent across agent workflows.
- Added regression tests around prompt injection, execution context, and SQL
  tooling to protect behavior during refactoring.
- Expanded production observability with Prometheus metrics and Grafana
  dashboards spanning agent, API, database, model, session, and tool layers.
- Contributed to operational controls including usage reporting and protected
  API documentation access.

Technical focus line:

> `Python` · `FastAPI` · `LangGraph` · `LangChain` · `SQL` · `Prometheus` ·
> `Grafana` · `AWS/EKS`

### 5. Taelim — Manufacturing APS and Scheduling Engine

Proposed lead:

> A manufacturing planning engine for order allocation, machine scheduling, and
> lot composition in corrugated-packaging operations.

Verified contribution bullets:

- Improved scheduling correctness by preventing stale demand from being
  processed twice during lot composition.
- Fixed confirmed-order recomposition paths so eligible orders are not lost
  during factory-specific planning flows.
- Refactored coating-related domain rules and strengthened the integrity of
  work-in-progress and order-length data.
- Added automated QA coverage with unit and integration tests, repeatable
  datasets, and GitHub Actions workflows.
- Improved operational support through Oracle schema/index versioning,
  configurable logging, and engine-result exports.

Technical focus line:

> `Python` · `Oracle SQL` · `GitHub Actions` · `pytest` · `Scheduling` ·
> `Optimization` · `Manufacturing APS`

### 6. Verified LLM AgentOps technology stack

Use the uniform icon/badge pattern popularized by GitHub Profile README
Generator rather than an unstructured badge cloud.

Groups:

- **LLM AgentOps & Backend:** Python, FastAPI, LangChain, LangGraph
- **Data & Observability:** SQL, Oracle, PostgreSQL, Prometheus, Grafana
- **Cloud & Delivery:** AWS, Docker, Kubernetes, GitHub Actions
- **Earlier full-stack foundation:** Java, Spring, JavaScript

Only technologies supported by LinkedIn or verified project work are included.
Icons should use a consistent height and a single centered row per group.

### 7. Earlier experience

Condense the long existing project catalog into three short themes:

- Built financial-system backend features and batch/data workflows.
- Developed model-based IoT tooling that translated formal models into
  executable Python for embedded devices.
- Explored algorithms and desktop software through D* Lite, KNN range search,
  and Java GUI projects.

Keep representative public links, but remove lengthy course-project explanations
from the main profile.

### 8. Public GitHub snapshot

Use generator-style dynamic cards for:

- GitHub stats for `MarcoBackman`
- Top languages for `MarcoBackman`
- Contribution streak for `MarcoBackman`

Apply the same transparent or Tokyo Night-compatible palette to all cards.
Label the section `Public GitHub Snapshot` so it is not mistaken for a complete
view of private professional contributions.

Because the public `github-readme-stats` endpoint is best-effort, the README
must still communicate the user's strengths when cards temporarily fail.

### 9. Footer

Use a shorter `capsule-render` waving footer with the reversed section and the
same fixed gradient. The footer contains no additional copy.

## External SVG and card configuration

- `capsule-render`: `type=waving`, fixed navy/cyan/violet gradient,
  `animation=fadeIn`, matched header/footer sections.
- `readme-typing-svg`: `Fira Code`, centered, cyan text, transparent background,
  three lines, measured width to prevent clipping.
- GitHub Profile README Generator conventions: uniform social icons, grouped
  skill icons, stats, top languages, and streak cards.
- GitHub Readme Stats: use `MarcoBackman`; transparent or Tokyo Night styling;
  avoid any claim that the cards include private repositories.

## Editorial rules

- Use English for the published README.
- Lead with outcomes and engineering responsibility, then name the supporting
  technologies.
- Keep each project highlight to one lead sentence and no more than five
  contribution bullets.
- Avoid unsupported proficiency levels, performance metrics, or completion
  claims.
- Do not call Symphony merely a RAG project; describe it as a production
  multi-step AI-agent platform.
- Spell the manufacturing project `Taelim` in public-facing prose.
- Keep the animated first screen accessible by retaining meaningful text outside
  every SVG or GIF.

## Verification

- Validate all Markdown, HTML image tags, query-string escaping, and public
  links.
- Verify every remote SVG/card URL returns an image.
- Inspect the generated GIF at full size and at GitHub-like width.
- Confirm the GIF loops, text is readable, and file size is reasonable.
- Confirm the README has useful fallback text when dynamic cards are unavailable.
- Search the final diff for private URLs, commit hashes, ticket identifiers,
  internal paths, and unsupported metrics.
- Render or preview the full README before completion.
