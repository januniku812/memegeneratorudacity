class QuoteModel():
    def __init__(self, body, author):
        """Create new QuoteModel"""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return str with "body text" - author."""
        return f"{self.body} - {self.author}"
