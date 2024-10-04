# Pangram Finder - NYT Spelling Bee

## Overview

This Streamlit application is designed to help users find pangrams and valid words from the **New York Times Spelling Bee** game. The app allows users to input a set of 6 adjacent letters and a center letter, then generates all possible combinations of valid words and identifies potential pangrams (words that use all letters).

## Features

- **Input Validation:** The app validates user input to ensure exactly 6 adjacent letters and 1 center letter are entered.
- **Word Generation:** It generates all possible word combinations (length 7 to 9) from the provided letters and filters the words based on an English dictionary.
- **Pangram Finder:** The app checks for pangrams, which are words that use all the provided letters.
- **Tile Display:** Valid words and pangrams are displayed in a clean tile format using custom CSS styling.

## How It Works

1. **User Input:**
   - Users are prompted to enter 6 letters and a center letter without spaces.
   - Click the "Find Pangrams" button to process the input.

2. **Word Generation:**
   - The app generates all letter combinations of length 7 to 9, ensuring that the center letter is included in each word.
   - The app then cross-checks these combinations with a dictionary (`filtered_words.txt`) to identify valid words.

3. **Pangram Detection:**
   - The app checks for words that contain all 6 adjacent letters and the center letter (pangrams).
   
4. **Results Display:**
   - Valid words and pangrams are displayed as clickable tiles in a visually appealing layout using CSS flexbox.

## Installation

### Prerequisites

- **Python 3.x**
- **Streamlit**: You need to have Streamlit installed. You can install it using pip:
  ```bash
  pip install streamlit
  ```

### Setup

1. Clone or download this repository to your local machine.
2. Ensure you have the file `filtered_words.txt`, which contains the dictionary of valid words.
3. Run the following command to start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

- Open the Streamlit app in your browser after running the above command.
- Enter the 6 letters and the center letter into the respective input fields.
- Click the "Find Pangrams" button to view the generated words and pangrams.

## Example

1. **Input:**
   - Letters: `abcdef`
   - Center Letter: `g`

2. **Output:**
   - **Possible Pangrams:**
     - ABCDEFG
     - etc.
   - **Possible Words:**
     - ABC
     - DEF
     - Etc.

## File Structure

```bash
├── app.py               # Main Streamlit application script
├── filtered_words.txt    # Dictionary file containing valid words
└── README.md             # Readme file for the project
```

## Custom CSS

The application uses a custom CSS section to display words in a tile format. The tiles are styled to fit dynamically and display as neatly aligned boxes on the screen.

Example of the CSS:

```css
.tile-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 10px;
}

.tile {
    background-color: #04488c;
    border: 2px solid #2196F3;
    border-radius: 5px;
    padding: 8px;
    text-align: center;
    font-size: 16px;
    font-weight: bold;
    flex: 1 1 100px;
    max-width: 150px;
    height: 45px;
}
```

## License

This project is licensed under the MIT License.