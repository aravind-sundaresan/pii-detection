from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider

# Create configuration containing engine name and models
configuration = {
    "nlp_engine_name": "spacy",
    "models": [{"lang_code": "en", "model_name": "en_core_web_trf"}]
}

# Create NLP engine based on configuration
provider = NlpEngineProvider(nlp_configuration=configuration)
nlp_engine = provider.create_engine()

# Pass the created NLP engine and supported_languages to the AnalyzerEngine
analyzer = AnalyzerEngine(
    nlp_engine=nlp_engine, 
    supported_languages=["en"]
)

# Call analyzer to get results
results = analyzer.analyze(text="My name is John Doe. My phone number is 212-555-5555.",
                           entities=["PERSON", "PHONE_NUMBER"],
                           language='en')

for entity in results:
    print(entity)
