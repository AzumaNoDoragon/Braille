# Text Transcription to Braille

This project was developed as part of a booklet for a college project. I decided to adapt the booklet to Braille and, while researching existing software, I noticed that many did not specify whether the Braille used was for Brazilian Portuguese (pt-BR). Additionally, I found differences in Braille dot patterns between various software.  

To ensure accurate transcription, even without full revision, I created this mapping based on a Brazilian Braille alphabet found online.  

## Features

- **Transcription of lowercase and uppercase letters**: Supports accented letters and special characters like cedilla.  
- **Support for numbers and symbols**: Includes numbers, basic mathematical operators, punctuation, and special symbols.  
- **File output**: The transcription is performed and saved in a `.txt` file for easy access and review.  

## How to Use

1. **Run the script**:

    Make sure the `transcription.txt` file contains the text you want to transcribe. Then, run the Python script:

    ```bash
    python Braille.py
    ```

2. **Output**:

    ```bash
    Original Text:
    (The original text will be displayed here)

    Braille Text:
    (The transcribed Braille text will be displayed here)
    ```

    The transcribed Braille text will be saved in the `transcribed.txt` file.  

## Limitations

This project was developed using a Braille alphabet found online. However, **I am not a Braille expert**, so there may be inaccuracies in the transcription. Below are some areas that need revision:

- **Uppercase letters**: The correct way to use the uppercase indicator needs to be confirmed.  
- **Character variations**: I am not entirely sure how and when to use accent variations and other modifiers in Braille.  
- **Special symbols**: The interpretation and mapping of symbols like mathematical operators and punctuation may not be correct.  

**Note:** I strongly recommend that this project be reviewed by someone with Braille expertise to correct any errors and improve transcription accuracy.  

## Contributions

Contributions are welcome! If you have experience with Braille and would like to help improve this project, feel free to open an issue or submit a pull request.  
