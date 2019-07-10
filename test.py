
from google.cloud import language

def languageAnalysis(text):
    client = language.
    document = client.document_from_text(text)

    # Sentiment
    sent_analysis = document.analyze_sentiment()

    print(dir(sent_analysis))

    sentiment = sent_analysis.sentiment

    # Entities
    ent_analysis = document.analyze_entities()
    entities = ent_analysis.entities

    return sentiment, entities

text = "Hello world, how are you"

sentiment, entities = languageAnalysis(text)
print(sentiment.score, sentiment.magnitude)
