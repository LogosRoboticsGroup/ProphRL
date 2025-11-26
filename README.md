<div align="center" style="font-family: charter;">

<h1>Reinforcing Action Policies by <i>Prophesying</i></h1>


<a href="https://arxiv.org/abs/2511.20633" target="_blank">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-PorphRL-red?logo=arxiv" height="20" />
</a>
<a href="https://LogosRoboticsGroup.github.io/ProphRL/" target="_blank">
    <img alt="Website" src="https://img.shields.io/badge/🌎_Website-ProphRL-blue.svg" height="20" />
</a>

<div>
    <span>Jiahui Zhang</span><sup>1 3 *</sup>,
    <span>Ze Huang</span><sup>1 3 *</sup>,
    <span>Chun Gu</span><sup>1 2 3</sup>,
    <span>Zipei Ma</span><sup>1 2</sup>,
    </span>
    <a href="https://lzrobots.github.io/" target="_blank">Li Zhang</a><sup>1 2 3</sup></span>
</div>

<div>
    <sup>1</sup>School of Data Science, Fudan University&emsp;
    <sup>2</sup>Shanghai Innovation Institute&emsp;
    <sup>3</sup>Logos Robotics&emsp;
</div>

<img src="docs/resources/teaser.png" width="100%"/>
<p align="justify" style="font-style: italic;">
  <b>ProphRL uses a world model as a real-world–facing simulator to post-train VLA policies.</b>
    Our world model Prophet extends a video generator with history-aware mechanism and dual action conditioning, and is pretrained on large-scale robot trajectories to model action-to-video dynamics.
    The pretrained Prophet enables `prophesying' precise, physically plausible long-horizon rollouts, and can be rapidly adapted via few-shot fine-tuning to new environments, objects, and trajectories.
    Upon Prophet, we introduce the FA-GRPO with FlowScale RL algorithm to more stably and efficiently improve policies.
    Together, our training paradigm turns diverse logged data and a single pretrained world model into a unified engine for scalable, data-efficient, and safely improvable VLA systems.
</p>


</div>

## 📝 Abstract

Vision–Language–Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer.

We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation model pretrained across large-scale, heterogeneous robot data to learn reusable action–outcome dynamics. Prophet can be few-shot adapted to new robots, objects, and environments, yielding a rollout-ready simulator.

Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute **ProphRL**, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5–17% success gains on public benchmarks and 24–30% gains on real robots across different VLA variants.


## 📚 Bibtex

If you find this project or dataset helpful, please consider citing our paper:

```bibtex
@article{zhang2025prophrl,
    title={Reinforcing Action Policies by Prophesying},
    author={Zhang, Jiahui and Huang, Ze and Gu, Chun and Ma, Zipei and Zhang, Li},
    year={2025},
    journal={arXiv preprint arXiv:2511.20633},
}
```