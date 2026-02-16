<div align="center">

<img src="https://giovanni-zanotti.is-a.dev/Media/curious-traveler/hero.webp" alt="CuriousTrip Logo" width="100%" />

# 🧭 CuriousTrip - Traveler API v2.0

### High-Performance Asynchronous Travel Data Aggregator

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Asyncio](https://img.shields.io/badge/AsyncIO-Concurrency-orange?style=for-the-badge&logo=python)
![Aiohttp](https://img.shields.io/badge/Aiohttp-Client-blueviolet?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

</div>

---

## 📖 About The Project

**CuriousTrip** is a modular CLI application designed to generate comprehensive travel profiles ("Travel Cheat Sheets") in real-time. By orchestrating **9 distinct RESTful APIs**, it aggregates demographic, meteorological, financial, and cultural data into a single, cohesive report.

**What's New in v2.0:**
This version introduces a complete architectural overhaul, moving from synchronous requests to a **fully asynchronous** model using `asyncio` and `aiohttp`. This allows for concurrent data fetching, drastically reducing wait times compared to sequential execution.

### ✨ Key Features
* **⚡ Asynchronous Core:** Utilizes `asyncio.gather` to fetch data from multiple endpoints simultaneously.
* **🛡️ Fault Tolerance:** Implements robust error handling; if one API fails or times out, the application gracefully skips that section without crashing.
* **Modular Architecture:** Clean separation between API logic (`/api`), data processing, and CLI interaction.
* **Persistence:** Automatically saves generated travel profiles to local `.txt` files for offline viewing.

---

## 🎥 Live Demo

See the application in action: login, destination selection, and profile generation.

<div align="center">
  <img src="https://giovanni-zanotti.is-a.dev/Media/curious-traveler/demo-cli.gif" alt="Demo Gif" width="100%" />
</div>

---

## 📂 Project Structure

The project follows a modular design pattern to ensure maintainability and scalability.

```text
.
├── app/
│   ├── api/             # Async API integration modules (aiohttp)
│   ├── data/            # Local storage for generated travel profiles (.txt)
│   ├── tools/           # Utility scripts (file I/O, persistence)
│   ├── info_fetcher.py  # Central orchestrator (Async logic)
│   └── main.py          # Entry point & CLI Interface
├── .gitignore           # Version control exclusions
├── README.md            # Documentation
└── requirements.txt     # Dependencies
```

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the required packages:

```bash
git clone https://github.com/GiZano/CuriousTrip.git
cd CuriousTrip
pip install -r requirements.txt
```

### 2. Execution
> [!WARNING]
> **Directory Constraint:** To ensure correct relative path resolution for data saving, the application **must** be executed from within the `/app` directory.

```bash
cd app
python main.py
```

_If run from the root directory, the application may fail to locate the `/data` folder._

---

## 🔗 Integrated APIs

The "Swindle Sheet" is built by aggregating data from the following services:

| Category | API Service | Purpose |
| :--- | :--- | :--- |
| 🌍 **Geography** | **REST Countries** | Population, Capital, Region data |
| 🌦️ **Weather** | **Open-Meteo** | Real-time weather forecasts |
| 💰 **Finance** | **ExchangeRate** | Currency conversion rates |
| 🎓 **Education** | **HipoLabs** | Local University listings |
| 🍽️ **Culture** | **TheMealDB** | Local culinary suggestions |
| 🐾 **Trivia** | **Cat/Dog/Joke APIs** | Fun facts & entertainment |
| 🌌 **Space** | **NASA APOD** | Astronomy Picture of the Day |

### ⚠️ Note on NASA API
The `space_api` module uses a generic `DEMO_KEY`.
If you see an **"Oops..."** message in the Space section, the hourly demo limit has been reached. To fix this, generate a free API Key at [api.nasa.gov](https://api.nasa.gov/) and update the configuration file.

---

## 🛠️ Error Resilience Strategy

The `info_fetcher.py` orchestrator is designed to be **resilient**. Network operations are wrapped in `try-except` blocks. In the event of:
* API Timeouts
* Rate Limiting (HTTP 429)
* Service Downtime (HTTP 500)

The application will **log the error** internally and proceed to compile the rest of the report, ensuring the user always receives a partial result rather than a program crash.

---

<div align="center">

**Developed by [GiZano](https://giovanni-zanotti.is-a.dev)**

</div>
