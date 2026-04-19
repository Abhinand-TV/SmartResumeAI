from langdetect import detect

def is_english(text):
    try:
        return detect(text) == "en"
    except:
        return False