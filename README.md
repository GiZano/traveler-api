# 🧭 CuriousTrip - Traveler API v2.0

![Welcome Image](https://giovanni-zanotti.is-a.dev/Media/curious-traveler/hero.webp)

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)
![Asyncio](https://img.shields.io/badge/architecture-asynchronous-orange)

**The Curious Traveler** (also known as *CuriousTrip*) is a modular, high-performance command-line application designed for travel data aggregation. By orchestrating nine distinct RESTful APIs, the application generates a comprehensive "Swindle Sheet"—a curated travel profile featuring demographic, meteorological, financial, and cultural insights.

This Version 2.0 introduces a complete transition to asynchronous programming, utilizing `aiohttp` and `asyncio` to execute concurrent network requests, significantly reducing data retrieval latency.

## 🎥 Demo
Here is a quick demonstration of the portal in action, from login to registering a new volunteer:

![Demo Gif](https://giovanni-zanotti.is-a.dev/Media/curious-traveler/demo-cli.gif)

---

## 📂 Project Structure

The repository is organized following modular design principles to ensure separation of concerns between API logic, data processing, and the user interface.

```text
.
├── app/
│   ├── api/             # Asynchronous API integration modules
│   ├── data/            # Local storage for generated .txt travel profiles
│   ├── tools/           # Utility scripts (e.g., file persistence)
│   ├── info_fetcher.py  # Central orchestrator utilizing asyncio.gather
│   └── main.py          # Application entry point and CLI loop
├── .gitignore           # Configuration for version control exclusions
├── README.md            # Primary documentation
└── requirements.txt     # List of project dependencies
```

---

## 🚀 Installation & Execution

### 1. Environment Setup
Clone the repository and install the necessary dependencies via pip:

```bash
pip install -r requirements.txt
```

### 2. Execution Guidelines
> [!IMPORTANT]
> To ensure correct directory resolution and file persistence, the application **must** be executed from within the `/app` directory:

```bash
cd app
python main.py
```

**Note:** Failure to run the script from the `/app` context will result in runtime errors regarding the generation of the `/data` directory and relative file pathing.

---

## 🔗 Integrated Services & API Credits

The application aggregates data from the following providers:
* **Geographical Data**: REST Countries API
* **Meteorology**: Open-Meteo API
* **Finance**: ExchangeRate API
* **Education**: HipoLabs Universities API
* **Content & Trivia**: TheMealDB, Cat Facts, JokeAPI, NASA APOD, and Dog API.

### Note on NASA API (space_api)
The `space_api` module currently utilizes a `DEMO_KEY`. If the application returns an **Oops..."** message in the Space Photo section, it indicates that the demo credit limit has been reached. For extended use, it is mandatory to generate a personal API Key and update the configuration within the module to restore functionality.

---

## 🛠️ Error Resilience
The `info_fetcher.py` orchestrator is designed with high fault tolerance. Should an external service be unresponsive or experience a timeout, the application will gracefully omit the affected section and continue to compile the remaining data, providing an error summary in the final output.
