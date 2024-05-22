import azure.functions as func
import logging
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="sentiment")
def sentiment(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.params.get("text")
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req.params.get("text")

    if text:
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
        sentiment = "positive" if scores["compound"] > 0 else "negative"
        return func.HttpResponse(sentiment)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )