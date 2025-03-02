from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def save(self):
        pass


class PDFDocument(Document):
    def save(self):
        return "PDF документ сохранен."


class WordDocument(Document):
    def save(self):
        return "Word документ сохранен."


class ExcelDocument(Document):
    def save(self):
        return "Excel документ сохранен."


class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "PDF":
            return PDFDocument()
        elif doc_type == "Word":
            return WordDocument()
        elif doc_type == "Excel":
            return ExcelDocument()
        else:
            raise ValueError(f"Неизвестный тип документа: {doc_type}")


def main():
    document_types = ["PDF", "Word", "Excel"]

    for doc_type in document_types:
        document = DocumentFactory.create_document(doc_type)
        print(document.save())

if __name__ == "__main__":
    main()