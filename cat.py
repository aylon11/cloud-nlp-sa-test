from google.cloud import language_v1

def classify_text(text_content):
    """
    Classifying Content in a String

    Args:
      text_content The text content to analyze.
    """

    client = language_v1.LanguageServiceClient()
    # text_content = "That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows."

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    content_categories_version = (
        language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2
    )
    response = client.classify_text(
        request={
            "document": document,
            "classification_model_options": {
                "v2_model": {"content_categories_version": content_categories_version}
            },
        }
    )
    # Loop through classified categories returned from the API
    for category in response.categories:
        # # Get the name of the category representing the document.
        # # See the predefined taxonomy of categories:
        # # https://cloud.google.com/natural-language/docs/categories
        # print("Category name: {}".format(category.name))
        # # Get the confidence. Number representing how certain the classifier
        # # is that this category represents the provided text.
        # print("Confidence: {}".format(category.confidence))
        return category.name, category.confidence

    return None, None
