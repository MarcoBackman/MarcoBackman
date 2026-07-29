# Korean Profile README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans
> to implement this plan task-by-task in the existing
> `feature/llm-agentops-profile` worktree.

**Goal:** Add a complete, resume-backed Korean profile README with
bidirectional language navigation while preserving the English profile as the
default GitHub landing page.

**Architecture:** Extend the README test fixture to load both language files,
then define navigation, content, ordering, metric, and privacy contracts before
creating `README.ko.md`. Reuse all visual assets and external cards from the
English profile; translate the narrative and add curated resume-backed details.

**Tech Stack:** GitHub Flavored Markdown, Python 3.13, `unittest`

---

### Task 1: Define the bilingual profile contract

**Files:**
- Modify: `tests/test_profile_readme.py`

- [ ] **Step 1: Load the Korean README in the fixture**

Add a temporary existence guard so RED is an assertion failure rather than a
file-read error:

```python
korean_path = ROOT / "README.ko.md"
cls.korean_readme = (
    korean_path.read_text(encoding="utf-8") if korean_path.exists() else ""
)
```

Keep this guard after GREEN so a missing localized file produces readable test
failures for every affected contract.

- [ ] **Step 2: Add navigation and structure tests**

Create `test_links_english_and_korean_profiles_bidirectionally`:

```python
self.assertIn('href="./README.ko.md"', self.readme)
self.assertIn('href="./README.md"', self.korean_readme)
self.assertIn('href="./README.ko.md"', self.korean_readme)
```

Create `test_korean_profile_preserves_featured_project_order`:

```python
self.assertIn("LLM AgentOps 엔지니어", self.korean_readme)
self.assertLess(self.korean_readme.index("Symphony"), self.korean_readme.index("Taelim"))
self.assertLess(
    self.korean_readme.index("Taelim"),
    self.korean_readme.index("금융 서비스 플랫폼"),
)
self.assertLess(
    self.korean_readme.index("금융 서비스 플랫폼"),
    self.korean_readme.index("물류창고 디지털 트윈"),
)
```

- [ ] **Step 3: Add resume-backed content tests**

Create `test_korean_profile_includes_curated_resume_evidence` and assert:

```python
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
    self.assertIn(expected, self.korean_readme)
```

- [ ] **Step 4: Add privacy tests**

Create `test_korean_profile_excludes_resume_only_personal_data`:

```python
self.assertNotIn("주소:", self.korean_readme)
self.assertNotIn("생년월일", self.korean_readme)
self.assertNotIn("1995년 11월 29일", self.korean_readme)
for private_client in ("DriveWealth", "Navy Federal", "OMRON", "현대 무벡스"):
    self.assertNotIn(private_client, self.korean_readme)
self.assertNotRegex(
    self.korean_readme,
    r"(?:\+?1[-.\s]?)?\d{3}[-.\s]\d{3}[-.\s]\d{4}",
)
```

- [ ] **Step 5: Run the new tests and confirm RED**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme.ProfileReadmeTests -v
```

Expected: FAIL because `README.ko.md` and language links do not exist.

- [ ] **Step 6: Commit the failing contract**

```powershell
git add tests/test_profile_readme.py
git commit -m "test: define bilingual profile contract"
```

### Task 2: Create the Korean profile

**Files:**
- Add: `README.ko.md`
- Modify: `README.md`

- [ ] **Step 1: Add a language switch to both documents**

Use this HTML at the top of both files:

```html
<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README.ko.md">한국어</a>
</p>
```

- [ ] **Step 2: Reuse visual identity**

Copy the capsule-render header/footer, typing SVG, social badges, local
AgentOps GIF, GitHub statistics, and streak card. Translate meaningful alt text
into Korean while leaving URLs and service parameters unchanged.

- [ ] **Step 3: Write the Korean professional narrative**

Use:

- `LLM AgentOps 엔지니어` as the main positioning;
- a Korean summary focused on observable and reliable LLM agents plus
  mission-critical platform engineering;
- Korean Symphony and Taelim sections matching the English claims;
- `추가 플랫폼 경력` containing:
  - `금융 서비스 플랫폼 — 실시간 펀드 처리`;
  - `물류창고 디지털 트윈 서비스 플랫폼`.

- [ ] **Step 4: Add curated resume evidence**

Digital-twin bullets must include:

- hybrid on-premise/AWS Java/Spring Boot microservices;
- 5,000+ AWS IoT messages per second;
- Jenkins deployment reduction from three hours to fifteen minutes;
- React/TypeScript visualization;
- MQTT/WebSocket device simulation;
- LLM, RAG, VectorDB, and computer vision.

Financial-platform bullets must include:

- one million records reduced from sixty seconds to two seconds;
- liveness-probe failures reduced from forty per hour to zero;
- Kafka, AMQ/RabbitMQ, Kinesis, DynamoDB, PostgreSQL, and Azure SQL;
- Docker, JOOQ, Flyway, JUnit 5, and TDD.

- [ ] **Step 5: Add foundation and credentials**

Include:

- Republic of Korea Navy IT infrastructure/application work;
- Robolink embedded robotics work;
- ModelTranslator and existing public projects;
- Florida Institute of Technology B.S. in Computer Science;
- SQLD, DAsP, Network Manager Level 2, Microsoft 365 Fundamentals, and OPIc AL.

- [ ] **Step 6: Run focused tests and confirm GREEN**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme.ProfileReadmeTests -v
```

Expected: all profile tests PASS.

- [ ] **Step 7: Run the complete suite**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme -v
git diff --check
```

Expected: all tests PASS and no whitespace errors.

- [ ] **Step 8: Commit the bilingual profile**

```powershell
git add README.md README.ko.md
git commit -m "docs: add Korean profile README"
```

### Task 3: Verify and update Draft PR #2

**Files:**
- Verify: `README.md`
- Verify: `README.ko.md`
- Verify: `tests/test_profile_readme.py`
- Remove: `docs/superpowers/specs/2026-07-29-korean-profile-design.md`
- Remove: `docs/superpowers/plans/2026-07-29-korean-profile.md`
- Remove: `tmp/pdfs/`

- [ ] **Step 1: Review Korean content**

Confirm:

- natural Korean rather than literal machine translation;
- major project and career hierarchy matches the approved design;
- metrics retain their units and source meaning;
- no resume-only contact, address, birth, or client data appears;
- all shared images have meaningful alt text.

- [ ] **Step 2: Remove temporary materials**

Delete rendered PDF intermediates after verifying their resolved path is inside
the worktree. Remove the design and plan with `apply_patch`, then commit:

```powershell
git add -u docs/superpowers
git commit -m "chore: keep Korean profile notes out of PR"
```

- [ ] **Step 3: Run final verification**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme -v
git diff --check origin/main..HEAD
git status --short
git diff --name-status origin/main..HEAD
```

Expected:

- all tests pass;
- worktree is clean;
- the follow-up PR adds `README.ko.md` and modifies `README.md` and tests;
- no temporary PDF or planning files remain.

- [ ] **Step 4: Push and inspect Draft PR #2**

```powershell
git push origin feature/llm-agentops-profile
gh pr view 2 --repo MarcoBackman/MarcoBackman
```

Confirm PR #2 remains open, draft, mergeable, and passes available checks.
