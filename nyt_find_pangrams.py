import streamlit as st
import itertools

# Function to get words from a dictionary file
def get_words_from_dictionary():
    """Load words from a dictionary file and return as a set."""
    with open('filtered_words.txt', 'r') as file:
        dictionary_words = set(word.strip().lower() for word in file.readlines())
    return dictionary_words

# Function to generate all possible letter combinations
def generate_combinations(letters, center_letter):
    """
    Generate all combinations of letters with lengths between 7 and 9
    ensuring that the center letter is included in each combination. 
    Repeated letters are allowed.
    """
    all_combinations = []
    for length in range(7, 10):
        for comb in itertools.product(letters, repeat=length):
            word = ''.join(comb)
            if center_letter in word:
                all_combinations.append(word)
    
    return all_combinations

# Function to find valid words from the combinations
def find_valid_words(combinations, dictionary_words):
    """Find valid words from the combinations that exist in the dictionary."""
    return [word for word in combinations if word in dictionary_words]

# Function to find pangrams from the combinations
def find_pangrams(all_letters, combinations):
    """
    Find pangrams from the list of combinations that contain all the letters.
    """
    pangrams = []
    sorted_letters = sorted(all_letters)
    
    for word in combinations:
        if sorted(sorted(set(word))) == sorted_letters:
            pangrams.append(word)
    
    return pangrams

def main():
    st.title("Pangram Finder-NYT Spelling Bee")

    # Inject the CSS for tile display
    st.markdown("""
    <style>
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
            text-align: middle;
            font-size: 16px;
            font-weight: bold;
            flex: 1 1 100px;
            max-width: 150px;
            height: 45px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Input for 6 letters and center letter
    letters = st.text_input("Enter the 6 letters adjacent to the center (without spaces):").lower()
    center_letter = st.text_input("Enter the center letter:").lower()

    # Button to start processing
    if st.button("Find Pangrams"):
        # Check input validity
        if len(letters) != 6 or len(center_letter) != 1:
            st.error("Please provide exactly 6 letters and 1 center letter.")
        else:
            # Load dictionary words
            dictionary_words = get_words_from_dictionary()

            # Combine letters
            all_letters = letters + center_letter

            # Generate combinations and find valid words
            combinations = generate_combinations(all_letters, center_letter)
            valid_words = find_valid_words(combinations, dictionary_words)

            # Check for pangrams
            pangrams = find_pangrams(all_letters, valid_words)

            # Display pangrams
            if pangrams:
                if len(pangrams) == 1:
                    st.text("Possible Correct Pangram:")
                else:
                    st.text("Possible Correct Pangrams:")

                # Display pangrams in a tile format
                pangram_tiles = "".join([f"<div class='tile'>{word.upper()}</div>" for word in pangrams])
                st.markdown(f"<div class='tile-container'>{pangram_tiles}</div>", unsafe_allow_html=True)
            else:
                st.warning("There are no valid pangrams in English for these letters.")

            # Display valid words
            st.text("Possible Correct Words in The Game:")

            # Display valid words in a tile format
            valid_word_tiles = "".join([f"<div class='tile'>{word.upper()}</div>" for word in valid_words])
            st.markdown(f"<div class='tile-container'>{valid_word_tiles}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()