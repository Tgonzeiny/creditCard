# creditCard
**Current Phase  0.1**

    Current Libraries and planned Tech stack

- The softwares backend shall be written entirely in Python.
- The software shall use a mySQL database
- The software shall use flask to handle web backend requests
- The software shall use React Native for the frontend to ensure we will not have to create two apps. More specifically it will be using expo.


    Development Plan
    
This app serves the purpose of providing the consumer with an optimal credit card for each purchase.
The current plan is for the user to provide a list of credit cards, in which the backend will query for the optimal credit card given the user's MCC and location.
For example, if the user is at or around a Mcdonalds and opens apple pay or gpay the user will be prompted with a banner saying "Use X card for this purchase".
As we logistically get closer this section will be ironed out.

The schema for the database will consist of three tables: 
1. User tables - Will consist of user and login information/email
2. Card ID - Will consist of the cardID and card type
3. User owned cards- Will consist of user id corresponding to card ID.
4. Reward information - Will consist of card ID with various MCC category rewards
5. MCC Categories - Will create a ID for MCCs that correspond with a category.


    Development Phases:
Phase 1: Will consist of pulling a given location MCC (Merchant category codes)
to decide which optimal credit card to use out of a given list

Phase 2: Will consist of creating user profiles and using previous logic to find
an optimal MCC for the given user. Including integration of PlaidAPI

Phase 3: Integration onto IoS and android.

Phase 4: GPS inclusion for mobile app to accurately determine the MCC.

    Outstanding Bugs

    Change Log