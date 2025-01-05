import assemblyai as aai
import pandas as pd
from transformers import pipeline


aai.settings.api_key = ""

transcriber = aai.Transcriber()

transcript = transcriber.transcribe("./English in a Minute_ Party Animal.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")


text_to_summarize = transcript.text
print(text_to_summarize)

text_list = [
    text_to_summarize,
    # Add more texts as needed
]

# Create a DataFrame from the list of strings
df = pd.DataFrame(text_list, columns=["text"])

# Add an empty column named "summary"
df["summary"] = ""

# Function to summarize text (can be placed outside the loop for efficiency)
def summarize_text(text, max_length=100, truncation=True):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, truncation=truncation)[0]['summary_text']
    return summary

# Loop through each row and summarize the text
for index, row in df.iterrows():
    text = row["text"]
    summary = summarize_text(text)
    df.at[index, "summary"] = summary

# Display the structure of the DataFrame (optional)
print("DataFrame Structure (after adding summary):")
print(df.info())

# Display the first few rows of the DataFrame (optional)
print("\nFirst few rows of the DataFrame (including summary):")
print(df.head())

# Save the DataFrame to a new Excel file (optional)
df.to_excel('summaries_from_strings.xlsx', index=False)

