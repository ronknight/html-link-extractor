<h1 align="center">🔗 <a href="https://github.com/ronknight/html-link-extractor">HTML Link Extractor</a></h1>

<h4 align="center">📄 A Python-based tool to extract all hyperlinks from an HTML file using BeautifulSoup.</h4>

<p align="center">
  <a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
  <a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
  <a href="https://github.com/ronknight/html-link-extractor/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
  <a href="https://github.com/ronknight/html-link-extractor/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
  <a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
  <a href="https://github.com/ronknight/html-link-extractor/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
  <a href="https://github.com/ronknight/html-link-extractor/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-Ronknight%20-red"></a>
</p>

<p align="center">
  <a href="#project-overview">Project Overview</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#visualization">Visualization</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## 📘 Project Overview

HTML Link Extractor is a simple Python script that extracts all hyperlinks from an HTML file using the BeautifulSoup library. The extracted links are printed to the console and optionally saved to a text file for further use.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ronknight/html-link-extractor.git
   cd html-link-extractor
   ```

2. **Install Dependencies**:
   Ensure Python 3.x is installed on your system. Then, install the required library:
   ```bash
   pip install beautifulsoup4
   ```

---

## 🚀 Usage

1. Place your HTML file in the project directory. Rename it to `input.html` or adjust the file name in `app.py`.

2. Run the script:
   ```bash
   python app.py
   ```

3. Output:
   - Extracted links are displayed in the console.
   - A file named `extracted_links.txt` is created in the project directory containing the extracted links.

---

## 📊 Visualization

```mermaid
graph TD
A[User Input: HTML File] -->|Loaded by Script| B[BeautifulSoup Parses HTML]
B --> C[Extracts <a> Tags with href]
C --> D[Print Links to Console]
C --> E[Save Links to extracted_links.txt]
```

---

## ⚠️ Disclaimer

This tool is intended for educational purposes and does not validate or sanitize the extracted links. Use responsibly and ensure compliance with applicable laws and regulations when processing third-party HTML files.