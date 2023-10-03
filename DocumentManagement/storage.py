from DocumentManagement.category import Category
from DocumentManagement.document import Document
from DocumentManagement.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for el in self.categories:
            if el.id == category_id:
                el.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for el in self.topics:
            if el.id == topic_id:
                el.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        for el in self.documents:
            if el.id == document_id:
                el.edit(new_file_name)

    def object_if_is_in(self, idto, list_of_items):
        for el in list_of_items:
            if el.id == idto:
                return el

    def delete_category(self, category_id):
        category = self.object_if_is_in(category_id, self.categories)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.object_if_is_in(topic_id, self.topics)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.object_if_is_in(document_id, self.documents)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                return el

    def __repr__(self):
        return "\n".join([repr(el) for el in self.documents])
