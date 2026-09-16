<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README.ko.md">한국어</a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;height=250&amp;color=0:0F172A,50:0EA5E9,100:8B5CF6&amp;text=Sung%20Jun%20%22Tony%22%20Baek&amp;fontSize=44&amp;fontColor=E2E8F0&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=LLM%20AgentOps%20Engineer&amp;descAlignY=58&amp;descSize=22" alt="Waving gradient header for Sung Jun Tony Baek, LLM AgentOps Engineer" width="100%" />
</p>

<h1 align="center">Sung Jun "Tony" Baek</h1>

<p align="center"><strong>LLM AgentOps Engineer</strong></p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;size=20&amp;duration=2800&amp;pause=900&amp;color=22D3EE&amp;center=true&amp;vCenter=true&amp;width=900&amp;lines=Operating+LLM+agents+with+reliability+and+observability;Engineering+manufacturing+APS+and+scheduling+systems;Turning+complex+workflows+into+validated+decisions" alt="Operating LLM agents with reliability and observability; engineering manufacturing APS and scheduling systems; turning complex workflows into validated decisions" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/sung-jun-tony-baek-9b505b11a" aria-label="LinkedIn">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://marcobackman.tistory.com/" aria-label="Technical blog">
    <img src="https://img.shields.io/badge/Technical%20Blog-0F172A?style=for-the-badge&amp;logo=blogger&amp;logoColor=white" alt="Technical blog" />
  </a>
  <a href="mailto:sbaek2015@my.fit.edu" aria-label="Email Sung Jun Baek">
    <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&amp;logo=gmail&amp;logoColor=white" alt="Email Sung Jun Baek" />
  </a>
</p>

<p align="center">
  <img
    src="./assets/llm-agentops-flow.gif"
    alt="Animated LLM AgentOps production trace showing guardrails, planning, tool execution, evaluation, replanning, demo telemetry, and a verified decision"
    width="100%"
  />
</p>

I specialize in **LLM AgentOps**—turning agentic prototypes into observable,
testable, cost-aware, and reliable production systems. I also build
manufacturing planning platforms where complex operational workflows must
become validated and explainable decisions.

## Agent Harnessing & Workflow Engineering

> I design Claude and Codex agent harnesses that turn open-ended development
> tasks into controlled, repeatable, and reviewable engineering workflows.

- Define scoped context and task boundaries so each agent receives the minimum
  information and authority required for its role.
- Configure tool permissions and controlled execution paths for repository,
  browser, document, and delivery workflows.
- Orchestrate plan → implementation → test → review → PR workflows with
  explicit checkpoints and recovery paths.
- Use verification gates, reviewable artifacts, and traceable handoffs to make
  outcomes reproducible and auditable.
- Separate implementation and review roles when independent validation improves
  confidence.

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

## Additional Platform Experience

### Financial Services Platform — Real-Time Fund Processing

> Software Developer at **BeaconFire Inc.**, contributing to a real-time
> fund-processing platform for financial services.

- Strengthened availability in OpenShift/Kubernetes by resolving liveness-probe
  issues, reducing recurring health-check failures from 40 per hour to zero.
- Designed multi-process, event-driven services with Kafka and AMQ/RabbitMQ
  across Azure SQL, PostgreSQL, and DynamoDB, and refactored legacy code into an
  order management system.
- Optimized database-intensive batch processing for 100,000+ orders through
  caching, batching, and indexing.
- Supported Azure disaster recovery and failover, Sumo Logic/Log4j2 monitoring,
  and Veracode vulnerability remediation.
- Established Docker/Flyway test environments and applied TDD with JUnit 5 and
  Mockito to improve deployment stability.

### Warehouse Digital Twin Service Platform

> Full-Stack Engineer at **VisionSpace**, building a hybrid-cloud digital-twin
> service platform for warehouse operations.

- Designed Java/Spring Boot microservices across on-premise and AWS
  infrastructure, with Jenkins delivery pipelines targeting EC2, ECR, and ECS.
- Built a React/TypeScript frontend and web application server for visualizing
  and interacting with dynamic digital-twin simulations.
- Developed a .NET/C# stress-testing application that simulated high-concurrency
  robotic-device traffic through MQTT, WebSocket, and AWS IoT.
- Integrated LLM, RAG, and computer-vision capabilities with the platform to
  expand intelligent search, analysis, and visual processing workflows.
- Supported production connectivity and scaling with Route 53, ACM, S3,
  security controls, and load-balanced AWS services.

## Technology focus

| LLM AgentOps | Backend & event systems |
| --- | --- |
| Claude · Codex · agent harnessing · workflow orchestration · context engineering · verification gates · LLM workflows · runtime traces · token and cost signals | Python · FastAPI · Java · Spring Boot · Kafka · RabbitMQ · PostgreSQL |

| Observability & cloud delivery | Digital twin & manufacturing |
| --- | --- |
| Prometheus · Grafana · GitHub Actions · Jenkins · Docker · Kubernetes/OpenShift · AWS · Azure | MQTT · WebSocket · AWS IoT · React · TypeScript · Oracle · APS scheduling |

## Earlier experience

- [ModelTranslator](https://github.com/TCC2021SeniorProject/ModelTranslator) — model-based IoT tooling that translates UPPAAL models into Python-oriented embedded-system workflows.
- [Hibernate quiz web app](https://github.com/MarcoBackman/hibernate_quiz_webapp) — a Spring Boot and Hibernate web application for working with relational data and protected routes.
- [D* algorithm](https://github.com/MarcoBackman/d-star-algorithm) — pathfinding exploration implemented with Python/Pygame and Java desktop UI tooling.

## Public GitHub Snapshot

**Personal — [@MarcoBackman](https://github.com/MarcoBackman)**

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=MarcoBackman&amp;theme=tokyonight" alt="MarcoBackman's public GitHub contribution statistics" height="170" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=MarcoBackman&amp;theme=tokyonight" alt="Most-used languages in MarcoBackman's public GitHub repositories" height="170" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=MarcoBackman&amp;theme=tokyonight&amp;hide_border=true&amp;background=0F172A" alt="MarcoBackman's public GitHub contribution streak" />
</p>

**Work — [@sungjunbaek-cloud](https://github.com/sungjunbaek-cloud)**

<p align="center">
  <img src="https://streak-stats.demolab.com?user=sungjunbaek-cloud&amp;theme=tokyonight&amp;hide_border=true&amp;background=0F172A" alt="sungjunbaek-cloud's public GitHub contribution streak (work account)" />
</p>

**Previous work — [@TonyBaek2023](https://github.com/TonyBaek2023)**

<p align="center">
  <img src="https://streak-stats.demolab.com?user=TonyBaek2023&amp;theme=tokyonight&amp;hide_border=true&amp;background=0F172A" alt="TonyBaek2023's public GitHub contribution streak (previous work account)" />
</p>

_Work accounts contribute to private repositories, so GitHub exposes only their contribution totals._

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;height=120&amp;section=footer&amp;color=0:0F172A,50:0EA5E9,100:8B5CF6" alt="Waving gradient footer" width="100%" />
</p>
