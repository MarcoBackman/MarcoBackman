# Claude and Codex Agent Harnessing Design

## Goal

Add Claude and Codex agent-harnessing and development-workflow management to
both profile languages, positioning the capability as part of LLM AgentOps
rather than as a simple tool list.

## Placement

Insert a concise section after the professional summary and before Symphony:

- English: `Agent Harnessing & Workflow Engineering`
- Korean: `에이전트 하네싱 및 워크플로 엔지니어링`

Symphony and Taelim remain the first two featured project sections.

## English content

The English section must be fully English. The only Korean text permitted in
`README.md` remains the existing `한국어` language-selector label.

Describe:

- Claude and Codex agent harnesses with scoped context and task boundaries;
- tool permissions and controlled execution;
- repeatable plan, implementation, test, review, and PR workflows;
- verification gates, traceable artifacts, and explicit handoffs;
- role separation for implementation and review where appropriate.

## Korean content

Describe the same capability naturally in Korean:

- Claude·Codex 기반 에이전트 실행 환경;
- 프롬프트·컨텍스트·도구 권한·작업 범위 관리;
- 계획→구현→테스트→리뷰→PR 워크플로;
- 검증 게이트, 결과물 추적, 명시적 작업 인계;
- 구현과 리뷰 역할 분리.

## Technology focus

Add the following without removing existing skills:

- English: `Claude · Codex · agent harnessing · workflow orchestration ·
  context engineering · verification gates`
- Korean: `Claude · Codex · 에이전트 하네싱 · 워크플로 오케스트레이션 ·
  컨텍스트 엔지니어링 · 검증 게이트`

## Test contract

Tests must verify:

- both section headings;
- Claude and Codex in both documents;
- context/permission boundaries, verification gates, and traceable handoffs;
- section placement before Symphony;
- the English harnessing section contains no Hangul characters;
- existing bilingual navigation and privacy checks remain green.

## PR scope

The final change modifies only `README.md`, `README.ko.md`, and
`tests/test_profile_readme.py`. Remove this design and its implementation plan
before updating Draft PR #2.
