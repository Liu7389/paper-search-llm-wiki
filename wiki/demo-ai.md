---
id: demo-ai
title: 示範：人工智慧各子領域頂會論文
sources: [S16, S12, S13, S14, S11, S6]
---
# 示範：人工智慧各子領域的頂會論文（每篇附網址）

方法：在 OpenAlex 先找到會議本身（source），再用「會議 + 關鍵字」篩選、依引用數排序，最後逐一核對網址可開。[S16]

## 影像辨識（CVPR）
- 2016, *Deep Residual Learning for Image Recognition*, https://doi.org/10.1109/cvpr.2016.90 [S16]
- 2018, *Learning Transferable Architectures for Scalable Image Recognition*, https://doi.org/10.1109/cvpr.2018.00907 [S16]

## 資訊檢索 IR（SIGIR）
- 2024, *The Power of Noise: Redefining Retrieval for RAG Systems*, https://doi.org/10.1145/3626772.3657834 [S16]
- 2024, *Fine-Tuning LLaMA for Multi-Stage Text Retrieval*, https://doi.org/10.1145/3626772.3657951 [S16]

## LLM（ACL）
- 2023, *Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models*, https://doi.org/10.18653/v1/2023.acl-long.147 [S16]
- 2024, *Large Language Models are not Fair Evaluators*, https://doi.org/10.18653/v1/2024.acl-long.511 [S16]

## RAG（EMNLP、ACL）
- 2023, *Active Retrieval Augmented Generation*（EMNLP）, https://aclanthology.org/2023.emnlp-main.495/ [S16]
- 2024, *DRAGIN: Dynamic Retrieval Augmented Generation based on the Real-time Information Needs of Large Language Models*（ACL）, https://doi.org/10.18653/v1/2024.acl-long.702 [S16]

## 網路（SIGCOMM）
- 2020, *Understanding Operational 5G: A First Measurement Study on Its Coverage, Performance and Energy Consumption*, https://doi.org/10.1145/3387514.3405882 [S16]
- 2020, *PINT: Probabilistic In-band Network Telemetry*, https://doi.org/10.1145/3387514.3405894 [S16]

## 資安（IEEE S&P）
- 2021, *Machine Unlearning*, https://doi.org/10.1109/sp40001.2021.00019 [S16]
- 2020, *HopSkipJumpAttack: A Query-Efficient Decision-Based Attack*, https://doi.org/10.1109/sp40000.2020.00045 [S16]

## Agent（AAMAS）
- 2020, *Learning Transferable Cooperative Behavior in Multi-Agent Teams*, https://dl.acm.org/doi/10.5555/3398761.3398967 [S16]
- 2021, *Contrasting Centralized and Decentralized Critics in Multi-Agent Reinforcement Learning*, https://doi.org/10.65109/jcle4281 [S16]

## 量子（量子機器學習，NeurIPS）
- 2022, *Escaping from the Barren Plateau via Gaussian Initializations in Deep Variational Quantum Circuits*, https://proceedings.neurips.cc/paper_files/paper/2022/hash/7611a3cb5d733e628081431445cb01fd-Abstract.html [S16]
- 2022, *Power and Limitations of Single-Qubit Native Quantum Neural Networks*, https://papers.neurips.cc/paper_files/paper/2022/file/b250de41980b58d34d6aadc3f4aedd4c-Paper-Conference.pdf [S16]
- 量子沒有公認的資訊類頂會，這裡以 NeurIPS 的量子機器學習論文示範。[S13][S14]

## 注意事項
- 只搜關鍵字不限會議時，RAG 全文 72,637 筆、標題 6,690 筆，且前兩名是 arXiv 預印本。[S12]
- arXiv 不經同儕審查，要找頂會正式版本。[S11]
- 同一篇論文可能有預印本與正式版兩筆紀錄，引用頂會正式版。[S12]
- 挑一篇頂會論文當種子，再做 backward／forward 滾雪球。[S6]
