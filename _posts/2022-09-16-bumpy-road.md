---
layout: post
title: "The bumpy road to planet formation"
date: 2022-09-16 12:00:00
description: How pressure bumps change what we observe in protoplanetary disks
tags: paper-story dust
categories: paper-stories
related_posts: false
---

### The question

> *How do dynamically evolving gas pressure bumps affect the observational properties of protoplanetary disks? Can we observationally distinguish between planetary versus zonal flow origin of pressure bumps?*

### Context

Over the last years, large (sub-)millimeter surveys of protoplanetary disks in different star-forming regions have well constrained the demographics of disks, such as their millimeter luminosities, spectral indices, and disk radii. Additionally, several high-resolution **observations have revealed an abundance of substructures** in the disk's dust continuum. The **most prominent are ring-like structures, which are likely caused by pressure bumps trapping dust particles**. Still, the origins and characteristics of these pressure bumps need to be understood in more detail.

### Method

We perform one-dimensional **gas and dust evolution simulations**, setting up models with **varying gas pressure bump features**, including their amplitude and location, growth time, and number of bumps. We subsequently run **radiative transfer calculations to obtain synthetic images**, from which we obtain the different quantities of observations.

{% include figure.liquid path="assets/img/stadler22_bumps_images.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">
    Figure 1: Synthetic ALMA dust continuum images of various bump models. Credit: Stadler et al. (2022).
</div>

### What we found

The outermost pressure bump determines the disk's dust size across different millimeter wavelengths and the observed dust masses of disks with optically thick inner bumps (<40 au) are underestimated by up to an order of magnitude. Our modeled **dust traps need to form early** (a few ten-thousand years), **fast** (on gas viscous timescales), **and must be long-lived** (a few million years) **to be consistent with the observations** of high millimeter luminosities and low spectral indices of disks. While the **planetary bump models can reproduce these observables** irrespective of the opacity prescription, the highest opacities are needed for the dynamic bump model, which mimics zonal flows in disks, to be in line with observations.

### Conclusions and what comes next

**Our findings favor the planetary over the zonal flow origin of pressure bumps** and support the idea that planet formation should already occur in early Class 0/I stages of circumstellar disks (after a few ten- to hundred thousand years). The determination of the disk's effective size through its outermost pressure bump also delivers a possible answer to why disks in recent low-resolution surveys appear to have the same sizes across different millimeter wavelengths. The study of disk gas kinematics via molecular line observations with ALMA can help to constrain the properties of these gas pressure bumps (see [exoALMA VI]({{ '/blog/2025/exoalma-vi/' | relative_url }})).

##### **The paper:** Stadler, Gárate, Pinilla et al. (2022): *The impact of dynamic pressure bumps on the observational properties of protoplanetary disks*, Astronomy & Astrophysics 668, A104 (first author). [arXiv](https://arxiv.org/abs/2209.07931) · [DOI](https://doi.org/10.1051/0004-6361/202243338)
