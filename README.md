<div align="center" style="font-family: charter;">

<h1>Reinforcing Action Policies by <i>Prophesying</i></h1>


<a href="https://arxiv.org/abs/xxx" target="_blank">
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
  <b>Our framework that uses a world model as a real-world–facing simulator to post-train VLA policies.</b>
    Our world model Prophet extends a video generator with history-aware mechanism and dual action conditioning, and is pretrained on large-scale robot trajectories to model action-to-video dynamics.
    The pretrained Prophet enables `prophesying' precise, physically plausible long-horizon rollouts, and can be rapidly adapted via few-shot fine-tuning to new environments, objects, and trajectories.
    Upon Prophet, we introduce the FA-GRPO with FlowScale RL algorithm to more stably and efficiently improve policies.
    Together, our training paradigm turns diverse logged data and a single pretrained world model into a unified engine for scalable, data-efficient, and safely improvable VLA systems.
</p>


</div>


## 📚 Bibtex

If you find this project or dataset helpful, please consider citing our paper:

```bibtex
@article{zhang2025vla,
    title={Reinforcing Action Policies by Prophesying},
    author={Zhang, Jiahui and Huang, Ze and Gu, Chun and Ma, Zipei and Zhang, Li},
    year={2025},
    journal={arXiv preprint arXiv:2506.22242xxxx},
}
```