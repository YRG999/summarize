from pdfminer.high_level import extract_text
from sumy.parsers.plaintext import PlaintextParser  
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summarize_pdf(file_path):
  text = extract_text(file_path)
  parser = PlaintextParser(text, Tokenizer("english")) 

  summarizer = LexRankSummarizer()
  summary = summarizer(parser.document, 10)  

  summary_text = [str(sentence) for sentence in summary]
  summary_text = " ".join(summary_text)
  
  return summary_text

pdf_file = input("Enter PDF file path\n")
print(summarize_pdf(pdf_file))
