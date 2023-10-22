from gtts import gTTS


def text_to_hindi_speech(text, output_file):
    try:
        # Create a gTTS object with the Hindi text and specify the language
        tts = gTTS(text, lang='hi')

        # Save the Hindi speech to an audio file
        tts.save(output_file)

        print(f'Success! Hindi speech saved as {output_file}')
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    hindi_text = "नमस्ते, यह एक नमूना पाठ-से-ध्वनि रूप में है।"
    output_file = "hindi_output.mp3"
    text_to_hindi_speech(hindi_text, output_file)
