from gtts import gTTS

marathi_text = "मराठीत लिहिण्याचं सोपं आहे."
output_file = "marathi_output.mp3"

# Create a gTTS object with Marathi text and the language code 'mr'
tts = gTTS(marathi_text, lang='mr')

# Save the Marathi speech to an audio file
tts.save(output_file)
