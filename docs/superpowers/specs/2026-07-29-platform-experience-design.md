# Additional Platform Experience Design

## Goal

Add the two omitted LinkedIn-backed career areas—financial-services platform
engineering and warehouse digital-twin platform engineering—without weakening
the profile's primary LLM AgentOps positioning or its Symphony/Taelim emphasis.

## Source boundaries

The content is grounded in Tony's LinkedIn Experience entries for:

- BeaconFire Inc., Software Developer, July 2022–May 2024;
- VisionSpace, Full-Stack Engineer, October 2024–September 2025.

Use only claims stated in those entries or explicitly supplied by Tony. Do not
invent business outcomes, customer names, platform adoption metrics, or
warehouse performance figures.

## Information hierarchy

Keep the current order:

1. LLM AgentOps positioning and animated production trace;
2. Symphony;
3. Taelim;
4. new `Additional Platform Experience`;
5. Technology focus;
6. Earlier experience and public GitHub snapshot.

This preserves Symphony and Taelim as the featured projects while showing
career breadth before the technology summary.

## New section

Create one parent heading and two level-three entries.

### Financial Services Platform — Real-Time Fund Processing

Identify the role as BeaconFire Inc. and describe:

- a real-time fund-processing platform in financial services;
- OpenShift/Kubernetes availability work, including eliminating recurring
  liveness-probe failures;
- Kafka and AMQ/RabbitMQ event-driven services across Azure SQL, PostgreSQL,
  and DynamoDB;
- OMS legacy refactoring and batch processing of more than 100,000 orders;
- Azure disaster recovery, Sumo Logic/Log4j2 monitoring, Veracode remediation,
  and Docker/Flyway/JUnit 5/Mockito quality practices.

### Warehouse Digital Twin Service Platform

Identify the role as VisionSpace and describe:

- a warehouse digital-twin service platform on hybrid on-premise/AWS
  infrastructure;
- Java/Spring Boot microservices and a React/TypeScript visualization UI;
- MQTT/WebSocket/AWS IoT robotic-device simulation and C# stress testing;
- Jenkins delivery to EC2, ECR, and ECS;
- integration with LLM, RAG, and computer-vision capabilities.

## Technology focus

Expand the existing compact tables without adding a long skills inventory:

- platform engineering: Kafka, RabbitMQ, Kubernetes/OpenShift;
- cloud and delivery: AWS, Azure, Jenkins, Docker;
- real-time/digital twin: MQTT, WebSocket, AWS IoT, React, TypeScript.

## Test contract

The README test must verify:

- the new parent section occurs after Taelim and before Technology focus;
- both platform headings and employer names are present;
- the core financial-platform technologies and `100,000+` scale are present;
- the core digital-twin technologies are present;
- existing Symphony-before-Taelim ordering remains unchanged.

## PR scope

Only `README.md` and `tests/test_profile_readme.py` should remain as net new
changes for this revision. Remove this design and its implementation plan
before updating the existing Draft PR.
