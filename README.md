# PersonaForge

## Overview
**PersonaForge** is a Python-based script that generates realistic fake identities. It is designed to simulate user behavior by creating identities with various characteristics such as names, birthdays, hobbies, interests, and more. This tool is particularly useful for testing, research, or other applications where realistic user data is needed without compromising real user privacy.

---

## Features
- **Random Identity Generation:** Generates fake identities with details like name, birthday, age, email address, blood type, hobbies, interests, zodiac signs, and more.
- **Customizable Headers:** Simulates real-world user behavior using random `User-Agent` headers.
- **Secure Passwords:** Creates secure, random passwords for each generated identity.
- **Zodiac Sign Assignment:** Automatically assigns a zodiac sign based on the generated birth month.
- **Data Storage:** Saves generated identities in a JSON file for further use.
- **Error Handling:** Handles common HTTP errors and retries requests intelligently.
- **Batch Processing:** Generates multiple identities in a single run.

---

## Requirements
The script uses the following Python libraries:
- `requests` - For making HTTP requests to fetch fake identity data.
- `bs4` (BeautifulSoup) - For parsing HTML responses.
- `json` - For handling JSON data storage.
- `secrets` - For generating secure random passwords.
- `time` - For adding delays between requests.
- `pathlib` - For managing file paths.
- `random` - For generating random selections.

To install the required libraries, run:
```bash
pip install requests beautifulsoup4
```

---

## Usage
1. Clone or download the repository containing the `PersonaForge` script.
2. Ensure the required libraries are installed.
3. Run the script using Python:
    ```bash
    python main.py
    ```
4. By default, the script generates 100 fake identities and saves them in `data/fake_data.json`.

---

## Script Overview
### Classes and Methods
#### **IdentityFarmer**
- `__init__`: Initializes default data such as hobbies, interests, and categories.
- `generate_password(length=12)`: Generates a secure random password.
- `generate_random_headers()`: Creates random HTTP headers to mimic real users.
- `get_zodiac_sign(birth_month)`: Determines a zodiac sign based on the birth month.
- `get_identity()`: Fetches and parses a single fake identity from an online generator.
- `generate_multiple_identities(num=100)`: Generates multiple identities.
- `append_to_json(identities)`: Appends generated identities to a JSON file.
- `run()`: Orchestrates the identity generation and storage process.

### Example Output
The generated JSON file will contain entries like:
```json
{
    "Name": "John Doe",
    "Birthday": "May 15, 1992",
    "Age": 31,
    "Email": "johndoe@example.com",
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Blood Type": "O+",
    "Password": "4x!Qe5@rP#M",
    "Hobbies": ["Hiking", "Photography", "Writing"],
    "Interests": ["Technology", "Music", "Literature"],
    "Category": "Music",
    "Zodiac Sign": "Taurus"
}
```

---

## Notes
- The script fetches data from `fakenamegenerator.com`. Ensure you comply with their terms of service.
- If the target website blocks requests, the script handles HTTP 429 errors by pausing and retrying.

---

## Future Improvements
- Improve error handling for other types of HTTP errors.
- Extend functionality to generate identities in bulk with diverse parameters.
- Integrate with other fake data APIs for additional diversity.

---



