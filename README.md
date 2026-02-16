# 🧭 The Curious Traveler API

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)
![Requests](https://img.shields.io/badge/library-requests-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)

**The Curious Traveler** (also known as *CuriousTrip*) is a modular, command-line Python application designed to aggregate and display comprehensive travel data. By orchestrating multiple free public REST APIs, the application allows users to input a destination country and instantly receive a curated travel profile, also known as a "Swindle Sheet". 

This project demonstrates practical skills in handling HTTP REST requests, parsing complex JSON payloads, handling exceptions for external services, and orchestrating data from diverse sources into a unified, highly readable CLI interface.

---

## ✨ Features

- **🌍 Destination Demographics**: Retrieves official name, capital, population, continent, languages, and currency.
- **🌤️ Real-time Weather**: Checks the current temperature, wind speed, and weather conditions of the destination's capital.
- **💰 Live Budget Conversion**: Converts a user-defined budget from EUR to the destination's local currency using up-to-date exchange rates.
- **🎓 Top Universities**: Suggests the top 3 universities located in the chosen country.
- **🍽️ Culinary Suggestions**: Recommends a random meal with ingredients to inspire your travel palate.
- **🎲 Entertainment & Trivia**: Delivers a random travel joke and a daily cat fact to keep things fun.
- **📸 Daily Space Imagery & Dogs**: Fetches NASA's Astronomy Picture of the Day and a random dog picture.
- **💾 Local Data Export**: Seamlessly saves the generated travel profile to a local `.txt` file within the `/app/data/` directory for future reference.

---

## 📂 Project Structure

The project follows a clean, modular architecture, separating API logic from data processing and the main CLI loop.

```text
.
├── app/
│   ├── api/
│   │   ├── budget_api.py    # ExchangeRate API integration
│   │   ├── cat_api.py       # Cat Facts API
│   │   ├── country_api.py   # REST Countries API
│   │   ├── dog_api.py       # Dog API
│   │   ├── food_api.py      # TheMealDB API
│   │   ├── joke_api.py      # JokeAPI
│   │   ├── space_api.py     # NASA APOD API
│   │   ├── uni_api.py       # HipoLabs Universities API
│   │   └── weather_api.py   # Open-Meteo API
│   ├── data/                # Generated text profiles are saved here
│   ├── tools/
│   │   └── saver.py         # Utility to write data to .txt files
│   ├── info_fetcher.py      # Orchestrator that gathers data from all APIs
│   └── main.py              # Entry point and CLI UI loop
├── .gitignore               # Ignores __pycache__, venv, and data files
├── README.md                # Project documentation
└── requirements.txt         # Project dependencies
```

---

## 🚀 Installation & Setup

1. **Clone the repository:**
```bash
   git clone https://github.com/yourusername/traveler-api.git
   cd traveler-api
```   

2. **Create and activate a virtual environment (Recommended):**
```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

---

## 💻 Usage

Run the main application script from the root directory. Make sure your `PYTHONPATH` allows for the local imports:

```bash
python app/main.py
```

**Step-by-step Execution:**
1. The app will welcome you with a retro ASCII banner.
2. You will be prompted to `Insert a country name:` (e.g., *Japan*, *Italy*).
3. Next, you will provide an available budget in EUR: `Insert the available budget (EUR):` (e.g., *500*).
4. The orchestrator will fetch all data from the various APIs and print a fully structured "CuriousTrip Swindle Sheet" to your terminal.
5. Finally, you can choose to save the output locally: `Would you like to save the sheet? (Y/N):`. If accepted, it will be saved inside `app/data/`.

---

## 🔗 APIs Orchestrated

This project successfully integrates 9 different external APIs to compile its profiles:

1. **[REST Countries API](https://restcountries.com/)** - Core geographical and demographic data.
2. **[Open-Meteo API](https://open-meteo.com/)** - Geographic coordinate-based live weather tracking.
3. **[ExchangeRate API](https://www.exchangerate-api.com/)** - Live currency exchange rates.
4. **[TheMealDB API](https://www.themealdb.com/)** - Random recipe and ingredient generation.
5. **[HipoLabs Universities API](http://universities.hipolabs.com/)** - Educational institutions list.
6. **[Cat Facts API](https://catfact.ninja/)** - Daily trivia generation.
7. **[JokeAPI](https://v2.jokeapi.dev/)** - Safe, single-string programming/general jokes.
8. **[NASA APOD API](https://api.nasa.gov/)** - Astronomy picture of the day.
9. **[Dog API](https://dog.ceo/dog-api/)** - Random dog imagery.

---

## 🛠️ Error Handling

Network requests can be unpredictable. `info_fetcher.py` handles potential failures smoothly: if a specific API goes down or times out, the application will simply skip that phase, alert the user of the missing module in an *Errors* section at the bottom of the generated sheet, and continue providing the rest of the available data. 

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check [issues page](https://github.com/GiZano/traveler-api/issues).