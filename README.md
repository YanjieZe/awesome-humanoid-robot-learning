# Awesome-Humanoid-Robot-Learning  [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

**Basic Info.** This repo collects academic papers about **humanoid robot learning**.  They are mainly categorized by the tasks they focus on. The papers with **real robot experiments** are preferred in this list. The papers with **open-sourced code** are added with a star🌟.

Feel free to pull a request for new papers/codes about humanoid robot learning.

- [Awesome-Humanoid-Robot-Learning](#awesome-humanoid-robot-learning)
  - [Loco-Manipulation and Whole-Body-Control](#loco-manipulation-and-whole-body-control)
  - [Manipulation](#manipulation)
  - [Teleoperation](#teleoperation)
  - [Locomotion and Navigation](#locomotion-and-navigation)
  - [Hardware Design](#hardware-design)
  - [Simulation Benchmark](#simulation-benchmark)
  - [Physics-Based Character Animation](#physics-based-character-animation)
  - [Human Motion Analysis and Synthesis](#human-motion-analysis-and-synthesis)

---

## Loco-Manipulation and Whole-Body-Control
- [arXiv 2025.04](https://arxiv.org/abs/2504.14305), Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning, [website](https://almi-humanoid.github.io/)
- [arXiv 2025.03](https://arxiv.org/abs/2503.12533), Being-0: A Humanoid Robotic Agent with Vision-Language Models and Modular Skills, [website](https://beingbeyond.github.io/being-0/)
- 🌟 [arXiv 2025.03](https://arxiv.org/abs/2503.05652), BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities, [websie](https://behavior-robot-suite.github.io/)
- [arXiv 2025.03](https://arxiv.org/abs/2503.04613), Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
- [arXiv 2025.02](https://arxiv.org/abs/2502.20061), HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery
- 🌟 [arXiv 2025.02](https://arxiv.org/abs/2502.13013), **HOMIE**: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit, [website](https://homietele.github.io/) / [github](https://github.com/OpenRobotLab/OpenHomie)
- [arXiv 2025.02](https://arxiv.org/abs/2502.12152), Learning Getting-Up Policies for Real-World Humanoid Robots, [website](https://humanoid-getup.github.io/)
- [arXiv 2025.02](https://arxiv.org/abs/2502.08378), Learning Humanoid Standing-up Control across Diverse Postures
- [arXiv 2025.02](https://arxiv.org/abs/2502.03206), **HugWBC**: A Unified and General Humanoid Whole-Body Controller
for Fine-Grained Locomotion, [website](https://hugwbc.github.io/)
- [arXiv 2025.02](https://arxiv.org/abs/2502.03132), **SPARK**: A Toolbox for Safe Humanoid Autonomy and Teleoperation, [website](https://intelligent-control-lab.github.io/spark/)
- [arXiv 2025.02](https://agile.human2humanoid.com/), **ASAP**: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills, [website](https://agile.human2humanoid.com/)
- [arXiv 2025.02](https://arxiv.org/abs/2502.01465), **Embrace Collisions**: Humanoid Shadowing for Deployable Contact-Agnostics Motions, [website](https://project-instinct.github.io/)
- [arXiv 2024.12](https://arxiv.org/abs/2412.15166), Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
- [arXiv 2024.12](https://arxiv.org/abs/2412.14172), Learning from Massive Human Videos for Universal Humanoid Pose Control, [website](https://usc-gvl.github.io/UH-1/)
- [arXiv 2024.12](https://arxiv.org/abs/2412.13196), **ExBody2**: Advanced Expressive Humanoid Whole-Body Control, [website](https://exbody2.github.io/)
- [arXiv 2024.12](https://arxiv.org/abs/2412.07773), **Mobile-TeleVision**: Predictive Motion Priors for Humanoid Whole-Body Control, [website](https://mobile-tv.github.io/)
- [arXiv 2024.11](https://arxiv.org/abs/2411.03532), A Behavior Architecture for Fast Humanoid Robot Door Traversals, [video](https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy)
- [arXiv 2024.11](https://arxiv.org/abs/2411.01349), The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control
- [arXiv 2024.10](https://arxiv.org/abs/2410.23234), EMOTION: Expressive Motion Sequence Generation for Humanoid Robots with In-Context Learning
- [arXiv 2024.10](https://arxiv.org/abs/2410.21229), HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots, [website](https://hover-versatile-humanoid.github.io/)
- [arXiv 2024.10](https://arxiv.org/abs/2410.12773), Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions, [website](https://ut-austin-rpl.github.io/Harmon/)
- [arXiv 2024.10](https://arxiv.org/abs/2410.05681), Whole-Body Dynamic Throwing with Legged Manipulators
- [arXiv 2024.09](https://arxiv.org/abs/2409.20514), Opt2Skill: Imitating Dynamically-feasible Whole-Body Trajectories for Versatile Humanoid Loco-Manipulation, [Website](https://opt2skill.github.io/)
- [2024.08](https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/), VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters, [website](https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/)
- [arXiv 2024.07](https://arxiv.org/abs/2407.12381), Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation, [video](https://www.youtube.com/watch?v=OyXojqRasHU) / [website](https://hucebot.github.io/flow_multisupport_website/)
- [arXiv 2024.06](https://arxiv.org/abs/2406.14655v1), HYPERmotion: Learning Hybrid Behavior Planning for Autonomous Loco-manipulation, [website](https://hy-motion.github.io/)
- 🌟 [arXiv 2024.06](https://arxiv.org/abs/2406.10454), HumanPlus: Humanoid Shadowing and Imitation from Humans, [website](https://humanoid-ai.github.io/) / [code](https://github.com/MarkFzp/humanplus)
- [arXiv 2024.06](https://arxiv.org/abs/2406.06005), WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts, [website](https://lecar-lab.github.io/wococo/)
- 🌟 [arXiv 2024.06](https://arxiv.org/abs/2406.08858), OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning, [website](https://omni.human2humanoid.com/) / [code](https://github.com/LeCAR-Lab/human2humanoid)
- 🌟 [arXiv 2024.03](https://arxiv.org/abs/2403.04436), Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation, [website](https://human2humanoid.com/) / [code](https://github.com/LeCAR-Lab/human2humanoid)
- 🌟 [arXiv 2024.02](https://arxiv.org/abs/2402.16796), Expressive Whole-Body Control for Humanoid Robots, [website](https://expressive-humanoid.github.io/) / [code](https://github.com/chengxuxin/expressive-humanoid)
- [arXiv 2023.10](https://arxiv.org/abs/2310.03191), Sim-to-Real Learning for Humanoid Box Loco-Manipulation


## Manipulation
- [arXiv 2025.03](https://arxiv.org/abs/2503.24361), Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation, [website](https://co-training.github.io/)
- [arXiv 2025.03](https://arxiv.org/abs/2503.14734), GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
- [arXiv 2025.03](https://arxiv.org/abs/2503.12725), Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions
- [arXiv 2025.03](https://arxiv.org/abs/2503.13441), Humanoid Policy ~ Human Policy, [website](https://human-as-robot.github.io/)
- arXiv 2025.02， Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids, [website](https://toruowo.github.io/recipe/)
- [arXiv 2025.02](https://arxiv.org/abs/2502.02858), **Dexterous Safe Control** for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
- [arXiv 2025.01](https://arxiv.org/abs/2501.04595), MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data
- [arXiv 2024.12](https://arxiv.org/abs/2412.10631), ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition, [website](https://nataliya.dev/armada)
- [arXiv 2024.12](https://arxiv.org/abs/2412.00396), ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning
- [arXiv 2024.11](https://arxiv.org/abs/2411.04005), Object-Centric Dexterous Manipulation from Human Motion Data, [website](https://cypypccpy.github.io/obj-dex.github.io/)
- [arXiv 2024.11](https://arxiv.org/abs/2411.02214), DexHub and DART: Towards Internet-Scale Robot Data Collection, [website](https://dexhub.ai/project)
- [arXiv 2024.11](https://arxiv.org/abs/2411.00704), Learning to Look Around: Enhancing Teleoperation and Learning with a Human-like Actuated Neck
- 🌟 [arXiv 2024.10](https://arxiv.org/abs/2410.10803), Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies, [website](https://humanoid-manipulation.github.io/) / [code](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy)
- 🌟 [arXiv 2024.10](https://arxiv.org/abs/2410.24221), EgoMimic: Scaling Imitation Learning via Egocentric Video, [website](https://egomimic.github.io/) / [code](https://github.com/SimarKareer/EgoMimic)
- [arXiv 2024.10](https://arxiv.org/abs/2410.18964), Learning to Look: Seeking Information for Decision Making via Policy Factorization, [website](https://robin-lab.cs.utexas.edu/learning2look/)
- [arXiv 2024.10](https://arxiv.org/abs/2410.11792), OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation, [website](https://ut-austin-rpl.github.io/OKAMI/)
- [2024.09](https://openreview.net/forum?id=55tYfHvanf), Bimanual Dexterity for Complex Tasks, [website](https://bidex-teleop.github.io/)
- 🌟 [arXiv 2024.08](https://arxiv.org/abs/2408.11805), ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation, [website](https://ace-teleop.github.io/) / [code](https://github.com/ACETeleop/ACETeleop)
- 🌟 [arXiv 2024.07](https://arxiv.org/abs/2407.01512), Open-TeleVision: Teleoperation with Immersive Active Visual Feedback, [website](https://robot-tv.github.io/) / [code](https://github.com/OpenTeleVision/TeleVision)
- 🌟 [arXiv 2024.07](https://arxiv.org/abs/2407.03162), Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning, [website](https://dingry.github.io/projects/bunny_visionpro.html) / [code](https://github.com/Dingry/BunnyVisionPro)
- 🌟 [arXiv 2024.04](https://arxiv.org/abs/2404.16823), Learning Visuotactile Skills with Two Multifingered Hands, [website](https://toruowo.github.io/hato/) / [code](https://github.com/toruowo/hato)
- 🌟 [arXiv 2024.03](https://arxiv.org/abs/2403.07788), DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation, [website](https://dex-cap.github.io/) / [code](https://github.com/j96w/DexCap)
- [1999](https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613(99)01327-3), Is imitation learning the route to humanoid robots?

## Teleoperation
- 🌟 [arXiv 2025.02](https://arxiv.org/abs/2502.13013), HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit, [code](https://github.com/OpenRobotLab/OpenHomie)
- [arXiv 2024.12](https://arxiv.org/abs/2412.07773), Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control
- 🌟 [arXiv 2024.10](https://arxiv.org/abs/2410.10803), Generalizable Humanoid Manipulation with 3D Diffusion Policies, [website](https://humanoid-manipulation.github.io/) / [code](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy)
- 🌟 [arXiv 2024.08](https://arxiv.org/abs/2408.11805), ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation, [website](https://ace-teleop.github.io/) / [code](https://github.com/ACETeleop/ACETeleop)
- 🌟 [arXiv 2024.07](https://arxiv.org/abs/2407.03162), Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning, [website](https://dingry.github.io/projects/bunny_visionpro.html) / [code](https://github.com/Dingry/BunnyVisionPro)
- 🌟 [arXiv 2024.07](https://arxiv.org/abs/2407.01512), Open-TeleVision: Teleoperation with Immersive Active Visual Feedback, [website](https://robot-tv.github.io/) / [code](https://github.com/OpenTeleVision/TeleVision)
- 🌟 [arXiv 2024.06](https://arxiv.org/abs/2406.10454), HumanPlus: Humanoid Shadowing and Imitation from Humans, [website](https://humanoid-ai.github.io/) / [code](https://github.com/MarkFzp/humanplus)
- 🌟 [arXiv 2024.06](https://arxiv.org/abs/2406.08858), OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning, [website](https://omni.human2humanoid.com/) / [code](https://github.com/LeCAR-Lab/human2humanoid)
- [arXiv 2024.03](https://arxiv.org/abs/2403.04436), Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation, [website](https://human2humanoid.com/)
- 🌟 [arXiv 2023.09](https://arxiv.org/abs/2309.01952), Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation, [website](https://ut-austin-rpl.github.io/TRILL/) / [code](https://github.com/UT-Austin-RPL/TRILL)
- [arXiv 2023.01](https://arxiv.org/abs/2301.04317), Teleoperation of Humanoid Robots: A Survey, [webpage](https://humanoid-teleoperation.github.io/)
- [arXiv 2022.03](https://arxiv.org/abs/2203.06972), iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots, [Science Robotics](https://www.science.org/doi/10.1126/scirobotics.adh3834) / [github](https://github.com/ami-iit/paper_dafarra_2024_science-robotics_icub3-avatar-system)


## Locomotion and Navigation
- [arXiv 2025.03](https://arxiv.org/abs/2503.00923), HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion, [website](https://simonlinsx.github.io/HWC_Loco/)
- [arXiv 2025.03](https://arxiv.org/abs/2503.09010), HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots
- [arXiv 2025.03](https://arxiv.org/abs/2503.09015), Natural Humanoid Robot Locomotion with Generative Motion Prior
- [arXiv 2025.03](https://arxiv.org/abs/2503.00692), Learning Perceptive Humanoid Locomotion over Challenging Terrain
- [arXiv 2025.02](https://arxiv.org/abs/2502.16230), Learning Humanoid Locomotion with World Model Reconstruction
- [arXiv 2025.02](https://arxiv.org/abs/2502.17219), Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning
- [arXiv 2025.02](https://arxiv.org/abs/2502.14814), **VB-Com**: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception, [website](https://renjunli99.github.io/vbcom.github.io/) 
- [arXiv 2025.02](https://arxiv.org/abs/2502.10363), BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds, [website](https://why618188.github.io/beamdojo/)
- [arXiv 2024.12](https://arxiv.org/abs/2412.04453), **NaVILA**: Legged Robot Vision-Language-Action Model for Navigation, [website](https://navila-bot.github.io/)
- [arXiv 2024.11](https://arxiv.org/abs/2411.14386), Learning Humanoid Locomotion with Perceptive Internal Model
- 🌟 [arXiv 2024.11](https://arxiv.org/abs/2411.01919), Real-Time Polygonal Semantic Mapping for Humanoid Robot Stair Climbing, [code](https://github.com/BTFrontier/polygon_mapping)
- 🌟 [arXiv 2024.10](https://arxiv.org/abs/2410.11825), Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies, [website](https://lipschitz-constrained-policy.github.io/) / [code](https://github.com/zixuan417/smooth-humanoid-locomotion)
- [arXiv 2024.10](https://arxiv.org/abs/2410.03654), Learning Humanoid Locomotion over Challenging Terrain, [website](https://humanoid-challenging-terrain.github.io/)
- [2024.10](https://openreview.net/forum?id=O0oK2bVist), Adapting Humanoid Locomotion over Challenging Terrain via Two-Phase Training, [website](https://sites.google.com/view/adapting-humanoid-locomotion/two-phase-training)
- [2024.10](https://openreview.net/forum?id=wH7Wv0nAm8), Bi-Level Motion Imitation for Humanoid Robots, [website](https://sites.google.com/view/bmi-corl2024)
- [arXiv 2024.08](https://arxiv.org/abs/2408.14472), Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning
- [arXiv 2024.06](https://arxiv.org/abs/2406.10759), Humanoid Parkour Learning, [website](https://humanoid4parkour.github.io/)
- [arXiv 2024.02](https://arxiv.org/abs/2402.19469), Humanoid Locomotion as Next Token Prediction, [website](https://humanoid-next-token-prediction.github.io/)
- [arXiv 2024.02](https://arxiv.org/abs/2402.18294), Whole-body Humanoid Robot Locomotion with Human Reference, [website](https://greatsjk.github.io/Adam-PNDbotics/)
- [arXiv 2024.01](https://arxiv.org/abs/2401.16889), Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control
- [arXiv 2023.09](https://arxiv.org/abs/2309.12784), Learning to Walk and Fly with Adversarial Motion Priors
- [arXiv 2023.07](https://arxiv.org/abs/2307.10142), Benchmarking **Potential Based Rewards** for Learning Humanoid Locomotion, 
- [arXiv 2023.03](https://arxiv.org/abs/2303.03381), Real-World Humanoid Locomotion with Reinforcement Learning, [website](https://learning-humanoid-locomotion.github.io/)
- [arXiv 2023.02](https://arxiv.org/abs/2302.09450), Robust and Versatile Bipedal Jumping Control through Reinforcement Learning

## Hardware Design
- [arXiv 2025.04](https://arxiv.org/abs/2504.13165), RUKA: Rethinking the Design of Humanoid Hands with Learning, [website](https://ruka-hand.github.io/)
- [arXiv 2025.04](https://arxiv.org/abs/2504.04259), ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning, [website](https://www.orcahand.com/)
- [arXiv 2025.03](https://arxiv.org/abs/2503.22459), Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
- 🌟 [arXiv 2025.02](https://arxiv.org/abs/2502.00893), **ToddlerBot**: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation, [website](https://toddlerbot.github.io/) / [github](https://github.com/hshi74/toddlerbot)
- [arXiv 2025.01](https://arxiv.org/abs/2501.05204), Design and Control of a Bipedal Robotic Character
- 2024.11, Zeroth Bot, [Github](https://github.com/zeroth-robotics/zeroth-bot)
- 🌟 [arXiv 2024.09](https://arxiv.org/abs/2409.19795), The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics, [website](http://www.generalroboticslab.com/blogs/blog/2024-09-29-dukehumanoidv1/index.html) / [code](https://github.com/generalroboticslab/dukeHumanoidHardwareControl)
- 🌟 [arXiv 2024.07](https://arxiv.org/abs/2407.21781), Berkeley Humanoid: A Research Platform for Learning-based Control, [website](https://berkeley-humanoid.com/) / [code](https://github.com/HybridRobotics/isaac_berkeley_humanoid)
- [2024.07](https://la.disneyresearch.com/publication/design-and-control-of-a-bipedal-robotic-character/), Design and Control of a Bipedal Robotic Character, [youtube](https://youtu.be/7_LW7u-nk6Q?si=DTpHYW_fCOST26tR)
- [arXiv 2021.04](https://arxiv.org/abs/2104.09025), The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors
- [arXiv 2019.04](https://arxiv.org/abs/1904.03815), Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation, [website](https://berkeleyopenarms.github.io/)

## Simulation Benchmark
- 🌟 2025.01, MuJoCo Playground, [github](https://github.com/google-deepmind/mujoco_playground) / [website](https://playground.mujoco.org/)
- [arXiv 2024.12](https://arxiv.org/abs/2412.17730), **Mimicking-Bench**: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking, [website](https://mimicking-bench.github.io/)
- 🌟 [arXiv 2024.12](https://arxiv.org/abs/2412.13211), **ManiSkill-HAB**: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks, [website](https://arth-shukla.github.io/mshab/)
- arXiv 2024.12, **Genesis**: A Generative and Universal Physics Engine for Robotics and Beyond, [code](https://github.com/Genesis-Embodied-AI/Genesis) / [website](https://genesis-embodied-ai.github.io/)
- [arXiv 2024.10](https://arxiv.org/abs/2410.24185), DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning, [website](https://dexmimicgen.github.io/)
- 🌟 [arXiv 2024.10](https://arxiv.org/abs/2410.00425), ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI, [website](https://www.maniskill.ai/home) / [code](https://github.com/haosulab/ManiSkill)
- 🌟 [arXiv 2024.07](https://arxiv.org/abs/2407.07788), BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark, [website](https://chernyadev.github.io/bigym/) / [code](https://github.com/chernyadev/bigym)
- 🌟 [arXiv](https://arxiv.org/abs/2407.10943), GRUtopia: Dream General Robots in a City at Scale, [website](https://github.com/OpenRobotLab/GRUtopia)
- 🌟 [arXiv 2024.06](https://arxiv.org/abs/2406.02523), RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots, [website](https://robocasa.ai/) / [code](https://github.com/robocasa/robocasa)
- 🌟 [arXiv 2024.04](https://arxiv.org/abs/2404.05695), Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer, [website](https://sites.google.com/view/humanoid-gym/) / [code](https://github.com/roboterax/humanoid-gym)
- 🌟 [arXiv 2024.03](https://arxiv.org/abs/2403.10506), HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation, [website](https://humanoid-bench.github.io/) / [code](https://github.com/carlosferrazza/humanoid-bench)

## Physics-Based Character Animation

- 🌟 [arXiv 2025.03](https://arxiv.org/abs/2503.19901) / CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization, [website](https://liangpan99.github.io/TokenHSI/)
- 🌟 [arXiv 2025.02](https://arxiv.org/abs/2502.20390), InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions, [website](https://sirui-xu.github.io/InterMimic/), [code](https://github.com/Sirui-Xu/InterMimic)
- 🌟 [arXiv 2024.09](https://arxiv.org/abs/2409.14393), MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting, [website](https://research.nvidia.com/labs/par/maskedmimic/)
- [arXiv 2023.06](https://arxiv.org/abs/2306.09532), Hierarchical Planning and Control for Box Loco-Manipulation
- 🌟 [arXiv 2023.09](https://arxiv.org/abs/2309.07918), Unified Human-Scene Interaction via Prompted Chain-of-Contacts, [website](https://xizaoqu.github.io/unihsi/)
- 🌟 [arXiv 2023.05](https://arxiv.org/abs/2305.06456), Perpetual Humanoid Control for Real-time Simulated Avatars, [code](https://github.com/ZhengyiLuo/PHC)



## Human Motion Analysis and Synthesis
- [arXiv 2025.04](https://arxiv.org/abs/2504.10414), HUMOTO: A 4D Dataset of Mocap Human Object Interactions, [website](https://jiaxin-lu.github.io/humoto/)
- arXiv 2025.04, Climber Force and Motion Estimation from Video, [website](https://rihat99.github.io/climb_force/)
- [arXiv 2025.03](https://arxiv.org/abs/2503.21268), ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate

--- 
# Contact
If you have questions/suggestions, feel free to email Yanjie Ze.
