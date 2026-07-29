# Korean Profile README Design

## Goal

Provide a complete Korean profile at `README.ko.md`, linked bidirectionally with
the English profile, while incorporating verified details from Tony's LinkedIn
and two supplied resume PDFs.

## Document structure

- `README.md` remains the default English GitHub profile.
- `README.ko.md` is the Korean counterpart.
- Both files start with a centered language switch:
  `English | 한국어`.
- The Korean document reuses the existing capsule header, badges, local
  AgentOps GIF, GitHub statistics, streak card, and footer.
- The English typing animation remains unchanged because its current font
  service is not guaranteed to render Korean glyphs.

## Korean information hierarchy

1. Korean professional summary;
2. Symphony;
3. Taelim;
4. financial-services platform;
5. warehouse digital-twin platform;
6. technology focus;
7. earlier engineering experience;
8. education and credentials;
9. public GitHub snapshot.

Symphony and Taelim remain the first two featured project sections.

## Resume-backed additions

Use a curated set of concrete, defensible details:

- digital twin:
  - hybrid on-premise/AWS microservices;
  - 5,000+ AWS IoT messages per second;
  - Jenkins deployment reduction from three hours to fifteen minutes;
  - MQTT/WebSocket device simulation;
  - LLM, RAG, VectorDB, and computer-vision integration;
- financial services:
  - one million record lookup reduced from sixty seconds to two seconds;
  - recurring liveness-probe failures reduced from forty per hour to zero;
  - event-driven fund processing with Kafka, AMQ/RabbitMQ, Kinesis, and
    multiple databases;
- foundation:
  - Republic of Korea Navy IT infrastructure and administrative application
    development;
  - Robolink embedded robotics work with C, sensors, motors, UART, and Zigbee;
- education and credentials:
  - B.S. in Computer Science, Florida Institute of Technology;
  - SQL Developer, Data Architecture Semi-Professional, Network Manager Level
    2, Microsoft 365 Fundamentals, and OPIc AL.

Do not import every resume metric. Avoid claims that would overwhelm the
profile or conflict with the current AgentOps narrative.

## Conflict policy

- Use LinkedIn for current titles and employment dates.
- Use the newer Korean resume for project-level technical details.
- Use the English resume as corroboration for older financial-platform work.
- Describe VisionSpace as `풀스택 엔지니어 · AI 플랫폼 개발 리딩` to preserve
  both the public title and the documented leadership scope.

## Privacy and confidentiality

Do not copy:

- phone numbers;
- street address;
- birth date or age;
- resume-only personal email addresses;
- financial customer names or enterprise customer names;
- private project URLs.

The existing public profile email and public links may remain in shared badges.

## Test contract

Tests must verify:

- bidirectional language links;
- Korean file existence and major section order;
- all four major platform/project sections;
- selected resume-backed metrics;
- Navy, Robolink, education, and credentials;
- absence of address, birth date, and the phone number shown in the resumes;
- continued English profile behavior.

## PR scope

The final follow-up PR should add `README.ko.md` and modify only `README.md` and
`tests/test_profile_readme.py`. Remove this design, its implementation plan, and
all rendered PDF intermediates before pushing.
