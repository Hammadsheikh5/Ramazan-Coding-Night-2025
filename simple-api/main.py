# Import necessary modules
from fastapi import FastAPI  # FastAPI framework for building APIs
import random  # Random module to select a random item from a list

# Initialize FastAPI application
app = FastAPI()

# ==============================
# Side Hustle Ideas and Money Quotes Data
# ==============================

# A list of side hustle ideas that users can get randomly
side_hustle = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
]

# A list of motivational quotes about money
money_quotes = [
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don’t happen. You create them. – Chris Grosser",
    "Don’t stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]

# ==============================
# API Endpoints
# ==============================

@app.get("/side_hustles")
def get_side_hustles(apiKey: str):
    """
    ✅ Endpoint to return a random side hustle idea.
    
    - Requires an API key for access.
    - If the API key is incorrect, returns an error message.
    - If the API key is valid, returns a random side hustle.
    """
    if apiKey != "123456":  # Simple API key validation
        return {"error": "Invalid API key"}
    
    return {"side_hustle": random.choice(side_hustle)}  # Select a random side hustle


@app.get("/money_quotes")
def get_money_quotes():
    """
    ✅ Endpoint to return a random money-related quote.
    
    - No authentication is required.
    - Simply selects a random quote from the predefined list.
    """
    return {"money_quote": random.choice(money_quotes)}  # Select a random quote


@app.get("/greet")
def greet():
    """
    ✅ Simple greeting endpoint.
    
    - Returns a welcome message from the FastAPI application.
    """
    return {"message": "Hello, from a FastAPI endpoint!"}  # Response message

