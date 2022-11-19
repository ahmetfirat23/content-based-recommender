import streamlit as st
import speech_recognition as sr
import pandas as pd
from transformers import pipeline
from sklearn.metrics.pairwise import linear_kernel


def listen():
    btn.button("I am listening you 👂", disabled=True, type="primary")
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source=source, duration=0.02)
        try:
            audio = r.listen(source=source, timeout=2, phrase_time_limit=5)
        except sr.WaitTimeoutError as e:
            print(str(e))
            first.write("Listening has timed out, please try again.")
            return

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = r.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    respond(response)


def respond(response):
    if not response["success"]:
        print(response["error"])
        first.write("Speech recognition service not available right now. Please try again later.")
    if response["error"] == "Unable to recognize speech":
        print(response["error"])
        first.write(response["error"] + ". Please try again.")
    else:
        predict(response["transcription"])


def predict(text):
    first.text("You said: " + text)
    result = classifier(text, candidate_labels=list(genres))
    results = pd.DataFrame(result)
    b = results.T
    b.columns = results.labels
    b = b.drop(index=["sequence", "labels"])
    b = b[corr_df.columns.to_list()]
    new_corr_df = corr_df.copy()
    new_corr_df["score"] = linear_kernel(corr_df, b)
    new_corr_df = new_corr_df.sort_values(by=["score"], ascending=False)
    output = df.iloc[new_corr_df.index[:20]]#.sort_values(by=["Release Year"], ascending=False)
    st.dataframe(output[["Release Year", "Title", "Genre"]])
    return


df = pd.read_csv("augmented_genres.csv")
corr_df = pd.read_csv("corr_df.csv")
genres = corr_df.columns.to_list()
classifier = pipeline("zero-shot-classification")

st.title("Movie Recommender")
st.text("Tell me what kind of movie you want and I will recommend you some movies.")
btn = st.empty()
btn.button("Click me to talk", on_click=listen, disabled=False, type="primary")
first = st.empty()
