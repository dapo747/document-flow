# document_flow.py

class Document:
    def __init__(self, title, uploader):
        self.title = title
        self.uploader = uploader
        self.status = 'Draft'

    def update_status(self, new_status):
        valid_statuses = ['Draft', 'Review', 'Approved', 'Published']
        if new_status in valid_statuses:
            self.status = new_status
            print(f"Document '{self.title}' status updated to '{self.status}'")
        else:
            print(f"Invalid status: {new_status}")

    def display_info(self):
        print(f"Title: {self.title}, Status: {self.status}, Uploaded by: {self.uploader}")

class DocumentFlow:
    def __init__(self):
        self.documents = []

    def add_document(self, title, uploader):
        doc = Document(title, uploader)
        self.documents.append(doc)
        print(f"Document '{title}' added with status '{doc.status}' by '{uploader}'")

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
            doc.display_info()

if __name__ == "__main__":
    flow = DocumentFlow()

    # Add some documents with uploader information
    flow.add_document("Document 1", "Alice")
    flow.add_document("Document 2", "Bob")

    # Update document status
    flow.update_document_status("Document 1", "Review")
    flow.update_document_status("Document 2", "Approved")

    # Display all documents and their statuses
    flow.show_all_documents()

    # Attempting to update to an invalid status
    flow.update_document_status("Document 1", "Archived")
