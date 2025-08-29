# creditCard
**Current Phase: 0.1**

## Technology Stack & Versions

- **Backend:** Python **3.11.6** using Flask **2.3.3**  
- **Database:** PostgreSQL **15** (migrated from MySQL)  
- **Frontend:** React Native **0.74** with Expo **51** (single codebase for iOS and Android)  
- **Package Manager:** Node.js **20.x** + npm **10.x**  
- **Authentication & Security:** bcrypt **4.0.1**, PyJWT **2.8.0**  
- **Hosting (planned):** Flask backend on AWS (EC2/Elastic Beanstalk), PostgreSQL on AWS RDS  

---

## Architecture Diagram

iOS / Android App (React Native)
↓ ↑
[ Sends API Requests ]
↓ ↑
Flask Backend (Python)
↓ ↑
[ Queries PostgreSQL Database ]
↓ ↑
Cloud Database (AWS RDS)
---

## Current Functionality

This app currently allows users to:  
1. **Create an account** with email and password (hashed and salted using bcrypt).  
2. **Log in** to their account.  
3. **Add credit cards** to their account from a predefined list.  
4. **Fetch user cards** from the backend.  

> **Note:** The app is currently a prototype. It does **not** access Apple Pay directly but simulates credit card recommendations based on stored card rewards and Merchant Category Codes (MCCs).  

---

## Database Schema

1. **Users** – stores login information (email, hashed password)  
2. **Cards** – stores card ID, name, network, and issuer  
3. **UserCards** – maps user IDs to their owned card IDs, optionally with a nickname  
4. **CardRewards** – stores card ID with MCC category rewards (e.g., 2x points for groceries)  
5. **MCCCategories** – maps MCC IDs to general categories (e.g., groceries, dining)  

---

## Development Phases

- **Phase 1:** Handle MCCs to determine optimal credit card for a purchase.  
- **Phase 2:** Create user profiles and integrate Plaid API (optional) to automatically fetch card names.  
- **Phase 3:** Deploy fully on iOS and Android using Expo.  
- **Phase 4:** Include GPS to detect MCC based on user location.  

---

## Running the Project Locally

### Backend (Flask)

```bash
# Create a virtual environment
.\venv\Scripts\activate

# Activate it
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend
set FLASK_APP=backend/flaskApp.py
set FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
flask run

# Navigate to the frontend folder
cd cardwise-app

# Install dependencies
npm install

# Start Expo
npx expo start