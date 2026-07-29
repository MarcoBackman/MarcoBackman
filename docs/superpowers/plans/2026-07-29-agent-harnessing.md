# Claude and Codex Agent Harnessing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans
> in the existing `feature/llm-agentops-profile` worktree.

**Goal:** Add fully English and naturally Korean descriptions of Claude/Codex
agent harnessing and workflow management without weakening the existing
LLM AgentOps and featured-project hierarchy.

**Architecture:** Add behavior-level bilingual content tests first. Insert one
compact section before Symphony in each README and extend the corresponding
technology-focus cells. Slice the English section in tests to prevent Hangul
from leaking into its body while preserving the Korean language-selector label.

**Tech Stack:** GitHub Flavored Markdown, Python 3.13, `unittest`

---

### Task 1: Define the harnessing content contract

**Files:**
- Modify: `tests/test_profile_readme.py`

- [ ] **Step 1: Add the English harnessing test**

Create `test_english_profile_describes_agent_harnessing_in_english`:

```python
heading = "## Agent Harnessing & Workflow Engineering"
self.assertIn(heading, self.readme)
section = self.readme[
    self.readme.index(heading):self.readme.index(
        "## Symphony — LLM AgentOps for APS Analytics"
    )
]
self.assertLess(self.readme.index(heading), self.readme.index("## Symphony"))
for expected in (
    "Claude",
    "Codex",
    "context and task boundaries",
    "tool permissions",
    "verification gates",
    "traceable handoffs",
):
    self.assertIn(expected, section)
self.assertNotRegex(section, r"[가-힣]")
```

- [ ] **Step 2: Add the Korean harnessing test**

Create `test_korean_profile_describes_agent_harnessing_and_workflows`:

```python
heading = "## 에이전트 하네싱 및 워크플로 엔지니어링"
self.assertIn(heading, self.korean_readme)
section = self.korean_readme[
    self.korean_readme.index(heading):self.korean_readme.index(
        "## Symphony — APS 분석을 위한 LLM AgentOps"
    )
]
self.assertLess(
    self.korean_readme.index(heading),
    self.korean_readme.index("## Symphony"),
)
for expected in (
    "Claude",
    "Codex",
    "컨텍스트",
    "도구 권한",
    "검증 게이트",
    "작업 인계",
):
    self.assertIn(expected, section)
```

- [ ] **Step 3: Verify technology-focus coverage**

In the same tests, assert:

```python
self.assertIn("agent harnessing", self.readme)
self.assertIn("workflow orchestration", self.readme)
self.assertIn("에이전트 하네싱", self.korean_readme)
self.assertIn("워크플로 오케스트레이션", self.korean_readme)
```

- [ ] **Step 4: Run focused tests and confirm RED**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme.ProfileReadmeTests -v
```

Expected: FAIL because neither harnessing section exists.

- [ ] **Step 5: Commit the failing contract**

```powershell
git add tests/test_profile_readme.py
git commit -m "test: require bilingual agent harnessing content"
```

### Task 2: Implement both harnessing sections

**Files:**
- Modify: `README.md`
- Modify: `README.ko.md`

- [ ] **Step 1: Add the fully English section**

Insert after the English summary and before Symphony:

```markdown
## Agent Harnessing & Workflow Engineering

> I design Claude and Codex agent harnesses that turn open-ended development
> tasks into controlled, repeatable, and reviewable engineering workflows.

- Define scoped context and task boundaries so each agent receives the minimum
  information and authority required for its role.
- Configure tool permissions and controlled execution paths for repository,
  browser, document, and delivery workflows.
- Orchestrate plan → implementation → test → review → PR workflows with
  explicit checkpoints and recovery paths.
- Use verification gates, traceable artifacts, and explicit handoffs to make
  outcomes reproducible and auditable.
- Separate implementation and review roles when independent validation improves
  confidence.
```

- [ ] **Step 2: Add the natural Korean section**

Insert after the Korean summary and before Symphony:

```markdown
## 에이전트 하네싱 및 워크플로 엔지니어링

> Claude와 Codex 기반 에이전트 하네스를 설계해 개방형 개발 작업을 통제
> 가능하고 반복 가능하며 검토 가능한 엔지니어링 워크플로로 전환합니다.

- 역할별 프롬프트, 컨텍스트, 작업 범위를 분리합니다.
- 저장소, 브라우저, 문서, 배포 작업의 도구 권한과 실행 경로를 관리합니다.
- 계획 → 구현 → 테스트 → 리뷰 → PR 워크플로를 검증 지점과 복구 경로로
  오케스트레이션합니다.
- 검증 게이트, 추적 가능한 결과물, 명시적 작업 인계로 재현성을 높입니다.
- 독립 검증이 필요한 작업은 구현과 리뷰 역할을 분리합니다.
```

- [ ] **Step 3: Extend both technology-focus tables**

Prepend:

- English LLM AgentOps cell: `Claude · Codex · agent harnessing · workflow
  orchestration · context engineering · verification gates`
- Korean LLM AgentOps cell: `Claude · Codex · 에이전트 하네싱 · 워크플로
  오케스트레이션 · 컨텍스트 엔지니어링 · 검증 게이트`

- [ ] **Step 4: Run focused and complete tests**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme.ProfileReadmeTests -v
python -m unittest tests.test_profile_readme -v
git diff --check
```

Expected: all tests PASS.

- [ ] **Step 5: Commit the content**

```powershell
git add README.md README.ko.md
git commit -m "docs: add Claude and Codex harnessing experience"
```

### Task 3: Clean up and update Draft PR #2

**Files:**
- Remove: `docs/superpowers/specs/2026-07-29-agent-harnessing-design.md`
- Remove: `docs/superpowers/plans/2026-07-29-agent-harnessing.md`

- [ ] **Step 1: Review language purity and information hierarchy**

Confirm:

- the English section contains only English;
- Korean appears in English only in the language selector;
- both sections occur before Symphony;
- Symphony and Taelim retain their existing relative order;
- claims describe process and controls without unsupported metrics.

- [ ] **Step 2: Remove temporary planning documents**

Use `apply_patch`, then commit:

```powershell
git add -u docs/superpowers
git commit -m "chore: keep harnessing notes out of PR"
```

- [ ] **Step 3: Run final verification**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme -v
git diff --check origin/main..HEAD
git status --short
git diff --name-status origin/main..HEAD
```

- [ ] **Step 4: Push and inspect Draft PR #2**

Push `feature/llm-agentops-profile`, update the PR summary, and confirm PR #2 is
open, draft, mergeable, and passing available checks.
