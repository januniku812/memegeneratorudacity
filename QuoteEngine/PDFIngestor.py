import subprocess
import random
from typing import List
from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel
import os


class PDFIngestor(IngestorInterface):
    """Class to parse PDf files and create QuoteModel objects"""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path and return QuoteModel objects"""
        quotes_list = []
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")
        # creating a temporary file
        tmp = f'./tmp/{random.randint(0, 1000)}.txt'
        try:
            call = subprocess.call(['pdftotext', path, tmp])
            with open(tmp, 'r') as file:
                file_lines_content = file.readlines()
        except FileNotFoundError as filenotfounderr:
            print(f'Error: {filenotfounderr}')
            return quotes_list

        subprocess.run(["rm", tmp])

        for line in file_lines_content:
            line = line.strip('\n\r').strip()
            line_length = len(line)
            if line_length > 0:
                parsed_line = line.split(' - ')
                quote_model = QuoteModel(parsed_line[0], parsed_line[1])
                quotes_list.append(quote_model)

        file.close()
        os.remove(tmp)
        return quotes_list
