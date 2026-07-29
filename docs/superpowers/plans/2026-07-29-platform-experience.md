# Additional Platform Experience Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans
> to implement this plan task-by-task in the existing
> `feature/llm-agentops-profile` worktree.

**Goal:** Add LinkedIn-backed financial-services and warehouse digital-twin
platform experience while preserving Symphony and Taelim as the profile's
featured work.

**Architecture:** Extend the README's information hierarchy with one compact
career section between Taelim and Technology focus. Protect the structure and
source-backed terminology with behavior-level README tests, then update the
existing Draft PR without retaining temporary planning documents.

**Tech Stack:** GitHub Flavored Markdown, Python 3.13, `unittest`

---

### Task 1: Establish the missing-experience contract

**Files:**
- Modify: `tests/test_profile_readme.py`

- [ ] **Step 1: Add a focused README test**

Add `test_includes_financial_and_digital_twin_platform_experience` to
`ProfileReadmeTests`. It must assert:

```python
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
```

Also assert the heading order:

```python
self.assertLess(
    self.readme.index("Taelim — Manufacturing APS & Scheduling Engine"),
    self.readme.index("Additional Platform Experience"),
)
self.assertLess(
    self.readme.index("Additional Platform Experience"),
    self.readme.index("Technology focus"),
)
```

- [ ] **Step 2: Run the focused test and confirm RED**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme.ProfileReadmeTests.test_includes_financial_and_digital_twin_platform_experience -v
```

Expected: FAIL because `Additional Platform Experience` is not yet present.

- [ ] **Step 3: Commit the failing contract**

```powershell
git add tests/test_profile_readme.py
git commit -m "test: require additional platform experience"
```

### Task 2: Add the LinkedIn-backed experience

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Insert the new section after Taelim**

Add:

```markdown
## Additional Platform Experience

### Financial Services Platform — Real-Time Fund Processing

> Software Developer at **BeaconFire Inc.**, contributing to a real-time
> fund-processing platform for financial services.

- Improved availability in OpenShift/Kubernetes by resolving recurring
  liveness-probe failures.
- Built Kafka and AMQ/RabbitMQ event-driven services across Azure SQL,
  PostgreSQL, and DynamoDB.
- Refactored a legacy OMS and optimized batch processing for 100,000+ orders.
- Supported Azure disaster recovery, Sumo Logic/Log4j2 monitoring, Veracode
  remediation, and Docker/Flyway/JUnit 5 testing.

### Warehouse Digital Twin Service Platform

> Full-Stack Engineer at **VisionSpace**, building a hybrid-cloud digital-twin
> platform for warehouse operations.

- Built Java/Spring Boot microservices and a React/TypeScript visualization UI.
- Simulated robotic-device traffic with MQTT, WebSocket, AWS IoT, and a C#
  stress-testing application.
- Automated delivery to EC2, ECR, and ECS with Jenkins and Docker.
- Integrated LLM, RAG, and computer-vision capabilities with the platform.
```

Keep each subsection to four or five bullets. Preserve all existing Symphony
and Taelim wording.

- [ ] **Step 2: Expand Technology focus**

Keep the current two-table layout. Add only technologies evidenced by the new
section:

- Kafka, RabbitMQ, Kubernetes/OpenShift;
- AWS, Azure, Jenkins, Docker;
- MQTT, WebSocket, AWS IoT, React, TypeScript.

- [ ] **Step 3: Run the focused test and confirm GREEN**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme.ProfileReadmeTests.test_includes_financial_and_digital_twin_platform_experience -v
```

Expected: PASS.

- [ ] **Step 4: Run the complete suite**

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests.test_profile_readme -v
git diff --check
```

Expected: all tests PASS and no whitespace errors.

- [ ] **Step 5: Commit the README**

```powershell
git add README.md
git commit -m "docs: add financial and digital twin experience"
```

### Task 3: Verify and update Draft PR #1

**Files:**
- Verify: `README.md`
- Verify: `tests/test_profile_readme.py`
- Remove: `docs/superpowers/specs/2026-07-29-platform-experience-design.md`
- Remove: `docs/superpowers/plans/2026-07-29-platform-experience.md`

- [ ] **Step 1: Review the rendered information hierarchy**

Confirm:

- Symphony and Taelim remain the first two detailed project sections;
- the new parent section follows Taelim;
- both new subsections are concise and use source-backed claims;
- Technology focus follows the experience section;
- no private client names or invented metrics appear.

- [ ] **Step 2: Remove temporary planning documents**

Remove both design and implementation plan files, then commit:

```powershell
git add -u docs/superpowers
git commit -m "chore: keep career notes out of profile PR"
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
- net PR scope remains README, GIF generator/assets, and tests;
- temporary planning documents are absent.

- [ ] **Step 4: Push and inspect Draft PR #1**

```powershell
git push origin feature/llm-agentops-profile
gh pr view 1 --repo MarcoBackman/MarcoBackman
```

Confirm the PR remains open, draft, mergeable, and limited to the intended
profile files.
