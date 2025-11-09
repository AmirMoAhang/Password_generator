# Password_generator

![gif](./src/Streamlit/images/vid.gif)

Welcome to the Password Generator project coded by python. Project implemented by both OOP approach and functional approach. A gui is created for this project based on streamlit.


The password generator creates:
1. Random Passwords
2. Memorable Password
3. Pin Codes

## How it works

The password generator uses Python's `random` and `string` modules to generate passwords based on user preferences. The generator consists of three distinct functions, each representing a different type of password generation:

1. `generate_random_password` creates a random password with specified length, and includes numbers and/or special characters based on your preference.
2. `generate_memorable_password` generates a password composed of a number of random words selected from an English language corpus. You can specify the separator and whether the words should be capitalized.
3. `generate_pin` produces a numeric pin code of a specified length.


## Requirements

- Python 3.7+
- NLTK (Natural Language Toolkit)
- streamlit
- pyperclip

To install **NLTK**, use pip:

```bash
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:

```python
import nltk
nltk.download('words')
```

to install **streamlit** and **pyperclip** use pip:

```bash
pip install streamlit
pip install pyperclip
```

## Running the Project

Ensure that you have all the required dependencies installed. You can then set your `PYTHONPATH`, navigate to the 'src' directory and run the project using the following commands:

```bash
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory/src"
python src/Functional_approach/main.py
```

If you want to experience GUI, you can run `run.py` file in `src/streamlit` with sreamlit as below:
```bash
streamlit run run.py
```


## User Inputs

By editing the values in the functions, you can specify the length of the password for each type of password to generate. You can also decide whether to include numbers or symbols for the random password generator, or the number of words and if words should be capitalized for the memorable password generator. 
