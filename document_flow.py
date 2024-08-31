# document_flow.py

class Document:
    def __init__(self, title):
        self.title = title
        self.status = 'Draft'

    def update_status(self, new_status):
        valid_statuses = ['Draft', 'Review', 'Approved', 'Published']
        if new_status in valid_statuses:
            self.status = new_status
            print(f"Document '{self.title}' status updated to '{self.status}'")
        else:
            print(f"Invalid status: {new_status}")

class DocumentFlow:
    def __init__(self):
        self.documents = []

    def add_document(self, title):
        doc = Document(title)
        self.documents.append(doc)
        print(f"Document '{title}' added with status '{doc.status}'")

    def update_document_status(self, title, new_status):
        for doc in self.documents:
            if doc.title == title:
                doc.update_status(new_status)
                return
        print(f"Document '{title}' not found")

    def show_all_documents(self):
        if not self.documents:
            print("No documents available.")
            return
        print("Current Documents Status:")
        for doc in self.documents:
            print(f"Title: {doc.title}, Status: {doc.status}")

if __name__ == "__main__":
    flow = DocumentFlow()

    # Add some documents
    flow.add_document("Document 1")
    flow.add_document("Document 2")

    # Update document status
    flow.update_document_status("Document 1", "Review")
    flow.update_document_status("Document 2", "Approved")

    # Display all documents and their statuses
    flow.show_all_documents()

    # Attempting to update to an invalid status
    flow.update_document_status("Document 1", "Archived")
