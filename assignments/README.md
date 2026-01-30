# Assignments

![Assignments](https://img.shields.io/badge/Assignments-PFDA%20Course-blue) ![Python](https://img.shields.io/badge/Language-Python%203.8%2B-green) ![Format](https://img.shields.io/badge/Format-Jupyter%20Notebook-orange)

This folder contains all course assignments for the Professional Foundations in Data Analytics: Web Services and Applications course.

---

## 📁 Directory Structure

```
assignments/
├── assignment1/
│   ├── assignment2-carddraw.ipynb          # Main assignment notebook
│   ├── *.png                               # Card image assets (52 files)
│   └── README.md                           # Assignment documentation
└── README.md                               # This file
```

---

## Assignment 1: Poker Hand Evaluation & Card Drawing API

![Status](https://img.shields.io/badge/Status-Complete-brightgreen) ![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow)

**File:** `assignment1/assignment2-carddraw.ipynb`

### Overview
This assignment focuses on integrating with external APIs, processing JSON data, and implementing poker hand evaluation logic. Students work with the Deck of Cards API to draw playing cards and evaluate poker hand rankings.

### Learning Objectives
Upon completion, students will be able to:

- ✅ Make HTTP requests to REST APIs using the `requests` library
- ✅ Parse and process JSON responses from web services
- ✅ Work with image data (downloading and storing files locally)
- ✅ Implement complex business logic (poker hand evaluation)
- ✅ Use pandas DataFrames for data manipulation and analysis
- ✅ Handle card values, suits, and poker hand rankings
- ✅ Write functions with proper documentation and error handling

### Key Concepts Covered

| Concept | Description |
|---------|-------------|
| **REST APIs** | Understanding HTTP requests, endpoints, query parameters |
| **JSON Parsing** | Extracting and processing data from API responses |
| **File I/O** | Downloading and saving card images locally |
| **Data Structures** | Using dictionaries, lists, and DataFrames for data organization |
| **Poker Logic** | Hand ranking (High Card, Pair, Two Pair, Three of a Kind, Straight, Flush, Full House, Four of a Kind, Straight Flush) |
| **Game Simulation** | Running multiple rounds and tracking scores |

### Requirements

**Technical Requirements:**
- Python 3.8 or higher
- Libraries: `requests`, `pandas`, `numpy`, `PIL/Pillow`
- Internet connection for API calls
- Jupyter Notebook or JupyterLab environment

**Installation:**
```bash
pip install requests pandas numpy pillow
```

### Project Structure

The notebook is organized into these main sections:

1. **Setup & Imports** (Lines 1-50)
   - Import necessary libraries
   - Define card value mappings

2. **API Functions** (Lines 51-100)
   - `deck_new()` — Create a new shuffled deck
   - `deck_draw()` — Draw cards from the deck

3. **Card Processing** (Lines 101-200)
   - `evaluate_hand()` — Analyze and rank poker hands
   - Image downloading and local storage

4. **Game Logic** (Lines 201-371)
   - Main game loop comparing two poker hands
   - Score tracking and round results

### Assignment Tasks

1. **API Integration**
   - Successfully connect to the Deck of Cards API
   - Draw cards from a shuffled deck
   - Handle API responses correctly

2. **Hand Evaluation**
   - Classify poker hand types correctly
   - Assign appropriate scoring (1 = High Card, 14 = Royal Flush)
   - Implement tie-breaker logic for same-ranked hands

3. **Game Implementation**
   - Run multiple rounds (5 rounds in this version)
   - Track scores for two players
   - Display results for each round and final scores

4. **Code Quality**
   - Write clean, readable code
   - Add comments explaining complex logic
   - Use meaningful variable names
   - Handle potential errors gracefully

### Expected Output

```
Player A's Hand:
Final Evaluation for Player A: [Hand Type] (Score: [X], Tie Breaker Score: [Y])
Player B's Hand:
Final Evaluation for Player B: [Hand Type] (Score: [X], Tie Breaker Score: [Y])
[Winner announcement or tie]

Final Score: Player A: [X], Player B: [Y]
```

### Poker Hand Rankings

| Rank | Hand Type | Points | Description |
|------|-----------|--------|-------------|
| 1 | High Card | 1 | No matching cards |
| 2 | One Pair | 2 | Two cards of same value |
| 3 | Two Pair | 3 | Two different pairs |
| 4 | Three of a Kind | 4 | Three cards of same value |
| 5 | Straight | 5 | Five cards in sequence |
| 6 | Flush | 6 | Five cards of same suit |
| 7 | Full House | 7 | Three of a kind + pair |
| 8 | Four of a Kind | 8 | Four cards of same value |
| 9 | Straight Flush | 9 | Straight in same suit |

### Debugging Tips

- **KeyError on card values:** Ensure `card_value_map` includes all possible values ('2'-'9', '0' for 10, 'J', 'Q', 'K', 'A')
- **API errors:** Check internet connection and verify the deck API is accessible
- **Image download failures:** Ensure write permissions in the notebook directory
- **Hand ranking issues:** Review the poker hand logic against official poker rankings

### How to Run

1. Open the notebook in Jupyter:
   ```bash
   jupyter notebook assignments/assignment1/assignment2-carddraw.ipynb
   ```

2. Install dependencies if needed:
   ```bash
   pip install requests pandas numpy pillow
   ```

3. Execute cells sequentially (Shift+Enter or Run All)

4. Review output and verify correct hand rankings

### Submission Checklist

- [ ] All code cells execute without errors
- [ ] Hand evaluation logic is implemented correctly
- [ ] Both players' hands are evaluated and compared
- [ ] Final scores are calculated and displayed
- [ ] Card images are downloaded successfully
- [ ] Code includes comments and documentation
- [ ] Variable names are clear and descriptive

### Resources

- **Deck of Cards API:** https://deckofcardsapi.com/
- **Poker Hand Rankings:** https://www.pokernews.com/poker-hands.htm
- **Python Requests Library:** https://docs.python-requests.org/
- **Pandas Documentation:** https://pandas.pydata.org/docs/

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError: No module named 'requests' | Run `pip install requests` |
| API connection errors | Check internet connection; verify API endpoint is accessible |
| KeyError on suit/value | Review card parsing logic; ensure card codes format matches expectations |
| Image save errors | Check directory permissions; verify write access |
| Hand ranking incorrect | Trace through hand evaluation logic; compare with poker rankings table |

### Grading Rubric

| Criteria | Points | Notes |
|----------|--------|-------|
| API Integration | 20 | Successfully draws cards, handles responses |
| Hand Evaluation | 30 | Correctly identifies hand types and ranks |
| Code Quality | 20 | Clean, documented, follows conventions |
| Game Logic | 20 | Proper scoring, multiple rounds, correct output |
| **Total** | **100** | |

---

## Additional Notes

- Each assignment builds on previous concepts
- Review course materials and lectures before starting
- Test your code incrementally as you write
- Use print statements and debugging tools to verify logic
- Don't hesitate to consult the resources provided

---

**Last Updated:** January 2026  
**Course:** Professional Foundations in Data Analytics: Web Services and Applications
