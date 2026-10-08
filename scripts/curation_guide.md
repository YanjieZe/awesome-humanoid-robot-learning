# Curation Guide

How to decide whether an arXiv candidate belongs in README.md and where it goes.
Used by both manual backfills and the daily arXiv routine.

## Include

Technical papers whose main subject is **humanoid robots** (or simulated humanoid
characters) and which use or enable **learning-based** methods. Examples:

- RL / imitation / VLA / foundation-model policies for humanoid locomotion,
  whole-body control, loco-manipulation, motion tracking, teleoperation
- Humanoid dexterous / bimanual manipulation where the platform is a humanoid
- Motion retargeting, human-to-humanoid data pipelines, egocentric human data for humanoids
- Humanoid sim-to-real, state estimation, navigation, perception for control
- Humanoid hardware papers (full robots, hands, actuators designed for humanoids)
- Simulators / benchmarks / datasets targeting humanoids
- Physics-based character animation (simulated humanoid characters, motion imitation)
- Human motion generation / capture / HOI reconstruction that is clearly aimed at
  driving humanoids or physics-based characters

Papers with **real-robot experiments** are preferred; a sim-only paper is fine if it
is a solid learning-method contribution.

## Exclude

- "Humanoid" used only in passing (general manipulation, quadrupeds, arms, drones)
- Social HRI user studies, psychology of humanoid appearance, ethics/policy essays
- LLM "humanoid agents", chatbots, virtual avatars with no motion/control content
- Pure classical control (MPC/QP/ZMP) with no learning component, **unless** it is a
  strong whole-body control / retargeting paper the community would want (when unsure, exclude)
- Market reports, short position papers, non-English papers
- Surveys: include only if they are specifically about humanoid robot learning

## Sections

Pick the single best section; add a second only when the paper is clearly about both.

1. Loco-Manipulation and Whole-Body-Control — WBC, motion tracking, whole-body
   loco-manipulation, humanoid athletic skills, retargeting, humanoid foundation models / VLAs with whole-body control
2. Manipulation — upper-body / dexterous / bimanual manipulation on a humanoid
3. Teleoperation — teleop systems and data collection interfaces
4. Locomotion — walking, running, parkour, terrain, fall recovery
5. Navigation — goal reaching, vision-language navigation for humanoids
6. State Estimation — odometry, contact / torque / pose estimation
7. Sim-to-Real — papers whose core contribution is the sim-to-real transfer method
8. Hardware Design — robot / hand / actuator design
9. Simulation Benchmark — simulators, benchmarks, datasets, evaluation suites
10. Physics-Based Character Animation — simulated characters, graphics venues
11. Human Motion Analysis and Synthesis — human motion generation / capture / HOI

## Entry format

```
- [arXiv YYYY.MM](https://arxiv.org/abs/<id>), <Title>, [website](<url>)
```

- `YYYY.MM` comes from the arXiv ID (2605.xxxxx -> 2026.05).
- Keep the official title; collapse whitespace; turn LaTeX like `$Ψ_0$` into `Ψ₀`.
- Add `, [website](...)` only if a project page URL appears in the abstract or comment.
- Prefix `🌟` only if a code URL (e.g. github.com) appears in the abstract or comment.
- If the comment says the paper was accepted (e.g. "Accepted to CoRL 2026"), use that
  venue instead of `arXiv YYYY.MM`, e.g. `[CoRL 2026](https://arxiv.org/abs/<id>)`.
- Insert newest first within a section; same month -> higher arXiv ID first.
