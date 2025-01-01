import requests
from bs4 import BeautifulSoup
import json
import string
import secrets
import time
from pathlib import Path
import random

class IdentityFarmer:
    """
    A class for farming realistic fake identities.
    """

    def __init__(self):
        """
        Initialize the IdentityFarmer.
        """
        self.hobbies = [
            "Reading", "Hiking", "Cooking", "Traveling", "Gaming", "Photography", 
            "Gardening", "Painting", "Cycling", "Writing", "Swimming", "Dancing",
            "Bird Watching", "Astronomy", "Collecting", "Knitting", "Sculpting", "Fishing"
        ]
        self.interests = [
            "Technology", "Science", "History", "Politics", "Music", "Sports", 
            "Art", "Literature", "Movies", "Travel", "Philosophy", "Economics"
        ]
        self.categories = {
            "Political": ["Conservative", "Liberal", "Moderate", "Socialist", "Libertarian"],
            "Regional": [
                "Addis Ababa", "Afar", "Amhara", "Benishangul-Gumuz", "Dire Dawa", 
                "Gambela", "Harari", "Oromia", "Sidama", "Somali", 
                "Southern Nations, Nationalities, and Peoples' Region (SNNPR)", 
                "South West Ethiopia Peoples' Region (SWEP)"
            ],
            "Sports": ["Soccer", "Basketball", "Tennis", "Golf", "Swimming", "Cycling", "Baseball", "Hockey", "Rugby", "Volleyball", "Track and Field"],
            "Music": ["Rock", "Pop", "Jazz", "Classical", "Hip Hop", "Electronic", "Country", "Reggae", "Blues", "Metal"],
            "Hobbies": self.hobbies,
            "Interests": self.interests,
            "Education": ["High School", "College", "Graduate School", "Vocational Training", "Self-Taught"],
            "Occupation": ["Engineer", "Doctor", "Teacher", "Artist", "Scientist", "Businessperson", "Student", "Retired", "Military"],
            "Lifestyle": ["Urban", "Suburban", "Rural", "Minimalist", "Adventurer", "Homebody"],
            "Cultural": ["Western", "Eastern", "Indigenous", "Latin American", "African", "Middle Eastern", "South Asian"]
        }
        self.zodiac_signs = {
            "January": ["Capricorn", "Aquarius"],
            "February": ["Aquarius", "Pisces"],
            "March": ["Pisces", "Aries"],
            "April": ["Aries", "Taurus"],
            "May": ["Taurus", "Gemini"],
            "June": ["Gemini", "Cancer"],
            "July": ["Cancer", "Leo"],
            "August": ["Leo", "Virgo"],
            "September": ["Virgo", "Libra"],
            "October": ["Libra", "Scorpio"],
            "November": ["Scorpio", "Sagittarius"],
            "December": ["Sagittarius", "Capricorn"]
        }
    
    def generate_password(self, length=12):
        """
        Generate a secure random password.

        Args:
            length (int): Length of the password (default is 12).

        Returns:
            str: Randomly generated password.
        """
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
                return password
    
    def generate_random_headers(self):
        """
        Generate random user-agent headers to mimic real user behavior.

        Returns:
            dict: Dictionary containing User-Agent header.
        """
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        ]
    
        return {
            'User-Agent': secrets.choice(user_agents),
            'Custom-Header': 'Your custom header value here'
        }

    def get_zodiac_sign(self, birth_month):
        """
        Get the zodiac sign based on the birth month.

        Args:
            birth_month (str): The month of birth.

        Returns:
            str: Zodiac sign.
        """
        return random.choice(self.zodiac_signs.get(birth_month, ["Unknown"]))

    def get_identity(self):
        """
        Get a realistic fake identity.

        Returns:
            dict: Dictionary containing fake identity details.
        """
        url = "https://www.fakenamegenerator.com/gen-male-er-us.php"
        headers = self.generate_random_headers()
        
        while True:
            try:
                r = requests.get(url=url, headers=headers)
                r.raise_for_status()  
                soup = BeautifulSoup(r.content, 'html.parser')
    
                name = soup.find('h3').text.strip()
    
                dd_elements = soup.find_all('dd')
    
                birthday = dd_elements[4].text.strip()
                parts = birthday.split()
                if len(parts) >= 3:
                    birth_month = parts[0] 
                else:
                    birth_month = "Unknown"
    
                age = int(dd_elements[5].text.split()[0])
                if age < 18 or age > 35:
                    continue  
    
                email_address = dd_elements[7].text.strip().split()[0]
    
                random_password = self.generate_password()
    
                user_agent = headers['User-Agent']
    
                blood_type = dd_elements[19].text.strip()
    
                avatar_hobbies = random.sample(self.hobbies, k=3)
                avatar_interests = random.sample(self.interests, k=3)

                category = random.choice(list(self.categories.keys()))

                zodiac_sign = self.get_zodiac_sign(birth_month)
    
                return {
                    "Name": name,
                    "Birthday": birthday,
                    "Age": age,
                    "Email": email_address,
                    "User Agent": user_agent,
                    "Blood Type": blood_type,
                    "Password": random_password,
                    "Hobbies": avatar_hobbies,
                    "Interests": avatar_interests,
                    "Category": category,
                    "Zodiac Sign": zodiac_sign
                }
            except requests.exceptions.HTTPError as e:
                print(f"HTTP error occurred: {e.response.status_code}")
                if e.response.status_code == 429:
                    time.sleep(10)  
                else:
                    return None 
            except Exception as e:
                print(f"An error occurred: {e}")
                return None

    def generate_multiple_identities(self, num=100):
        """
        Generate multiple realistic fake identities.

        Args:
            num (int): Number of identities to generate.

        Returns:
            list: List of dictionaries containing fake identity details.
        """
        identities = []
        for _ in range(num):
            identity = self.get_identity()
            if identity:
                identities.append(identity)
            time.sleep(random.uniform(1, 3)) 
        return identities

    def append_to_json(self, identities):
        """
        Append identities to a JSON file.

        Args:
            identities (list): List of dictionaries containing identity details.
        """
        file_path = 'data/fake_data.json'
        try:
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = []
        
        data.extend(identities)
    
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def run(self):
        """
        Run the identity generation process.
        """
        num_identities = 100
        identities = self.generate_multiple_identities(num=num_identities)
        self.append_to_json(identities)
        print(f"{num_identities} identities saved in fake_data.json")

if __name__ == '__main__':
    identity_farmer = IdentityFarmer()
    identity_farmer.run()
