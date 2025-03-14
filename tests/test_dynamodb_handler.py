import unittest
from api.dynamodb_handler import retrieve_documents

class TestDynamoDBHandler(unittest.TestCase):

    def test_retrieve_documents(self):
        """Prueba la recuperación de documentos desde DynamoDB."""
        document_type = "analitica"
        limit = 3
        result = retrieve_documents(document_type, limit)
        
        self.assertIsInstance(result, list, "El resultado debe ser una lista de documentos o vacía.")
        if result:
            self.assertIn("document_type", result[0], "Cada documento debe tener un tipo definido.")

if __name__ == "__main__":
    unittest.main()
