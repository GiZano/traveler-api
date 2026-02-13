# 🧭 The Curious Traveler

## 📝 Description

**The Curious Traveler** is a command-line Python application designed to aggregate and display comprehensive travel data. By integrating multiple free public APIs, the application allows users to input a destination country and instantly receive a curated travel profile. This profile includes demographic information, real-time weather conditions, live currency conversion, culinary suggestions, and daily entertainment trivia. 

The project serves as a practical demonstration of handling HTTP REST requests, parsing complex JSON payloads, and orchestrating data from diverse external sources into a unified, highly readable interface.

---

## 📋 Development Phases

### Phase 1 — Setup and Initial Fetch

1. Prompt the user to input a country name in English (e.g., `Italy`, `Japan`, `Brazil`).
2. Utilize the **REST Countries API** to retrieve information regarding the specified country:
   * `https://restcountries.com/v3.1/name/{country_name}`
3. From the API response, extract and display:
   * Official country name
   * Capital city
   * Population
   * Continent
   * Spoken languages
   * Currency used

> **Tip:** The response is returned as a list. You will need to access the first element (e.g., `data[0]`).

---

### Phase 2 — Weather Conditions

1. From the REST Countries response, extract the geographic coordinates of the capital city (locate the `capitalInfo` → `latlng` field).
2. Utilize these coordinates to query the **Open-Meteo API** for current weather data:
   * `https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true`
3. Extract and display:
   * Current temperature
   * Wind speed
   * Weather condition: If the `weathercode` field equals 0, display "☀️ Clear sky"; otherwise, display "☁️ Cloudy/Variable".

---

### Phase 3 — Budget Conversion

1. From the REST Countries response, identify the local currency code (e.g., `JPY` for Japan, `BRL` for Brazil).
2. Use the **ExchangeRate API** to retrieve the current exchange rate relative to the Euro:
   * `https://open.er-api.com/v6/latest/EUR`
3. Prompt the user to input a travel budget in Euros (e.g., `500`).
4. Calculate and display the equivalent value of the budget in the destination's local currency.

---

### Phase 4 — Culinary Suggestion

1. Query **TheMealDB** to fetch a random recipe:
   * `https://www.themealdb.com/api/json/v1/1/random.php`
2. Extract and display:
   * Dish name
   * Category (e.g., Seafood, Dessert)
   * The first 5 ingredients (fields are named `strIngredient1`, `strIngredient2`, etc.)
   * Link to the recipe instructions (using `strSource` or `strYoutube`)

> **Note:** TheMealDB returns international recipes, so the dish may not originate from the selected country. Present this simply as a "Chef's Suggestion".

---

### Phase 5 — Daily Trivia

1. Use the **Cat Facts API** to fetch a random cat fact:
   * `https://catfact.ninja/fact`
2. Use the **JokeAPI** to fetch a random joke:
   * `https://v2.jokeapi.dev/joke/Any?lang=en&type=single`
3. Display both items under a "Travel Entertainment" section.

---

### Phase 6 — The Final Output Card

Assemble all the aggregated data into a clean, highly readable command-line interface output. The application should print a structured card similar to the following format:

    ╔══════════════════════════════════════════╗
    ║        TRAVEL PROFILE - CURIOUSTRIP      ║
    ╠══════════════════════════════════════════╣
    
    📍 DESTINATION
       Country: Japan
       Capital: Tokyo
       Continent: Asia
       Population: 125,836,021
       Languages: Japanese
       Currency: Japanese yen (JPY)
    
    🌤️ WEATHER IN TOKYO
       Temperature: 12°C
       Wind: 15 km/h
       Conditions: ☀️ Clear sky
    
    💰 BUDGET
       500 EUR = 78,500 JPY
    
    🍽️ CHEF'S SUGGESTION
       Dish: Sushi
       Category: Seafood
       Ingredients: Rice, Nori, Salmon, Avocado, Soy Sauce
    
    🐱 TRIVIA
       "Cats sleep for 70% of their lives."
    
    😂 TRAVEL JOKE
       "Why did the computer go to the doctor? Because it had a virus!"
    
    ╚══════════════════════════════════════════╝

---

### Phase 7 — BONUS Features 

 Following enhancements to implement:

* **🔁 Application Loop:** Upon displaying the card, prompt the user to search for another country or exit the application.
* **📸 Space Imagery:** Append the Astronomy Picture of the Day to the card using the **NASA APOD API** (`https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`). Display the title and the image URL.
* **🐶 Random Dog:** Replace (or accompany) the cat fact with a link to a random dog image using the **Dog API** (`https://dog.ceo/api/breeds/image/random`).
* **🎓 Universities:** Query the **Hipolabs Universities API** to print the top 3 universities located in the chosen country.
* **💾 Data Export:** Save the generated travel profile to a `.txt` file named after the country (e.g., `profile_japan.txt`).

---

## ⚠️ Best Practices & Tips

* **Work iteratively:** Implement and thoroughly test one phase at a time before proceeding to the next.
* **Inspect the payload:** Utilize `print(data)` or `print(data.keys())` to explore the structure of the JSON responses if you are unsure of their contents.
* **Handle timeouts gracefully:** If a specific API is unresponsive, do not stall; proceed with the others and revisit it later.
* **Code organization:** While creating explicit functions is not strictly necessary for this script (sequential execution is acceptable), you are highly encouraged to organize your code modularly if you feel comfortable doing so.

**Safe travels! 🧳**