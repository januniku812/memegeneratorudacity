from typing import List

from QuoteEngine import IngestorInterface, QuoteModel
import pandas


class CSVIngestor(IngestorInterface):
    """Class for parsing csv files"""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file at the path and return QuoteModel objects"""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        quotes_list = []
        df = pandas.read_csv(path, header=0, sep=',', error_bad_lines=False)
        # index is never used
        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes_list.append(quote)

        return quotes_list


