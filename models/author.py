
class Author:
    def __init__(self, id, name):
        self.name = name
        self.id = id
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Id must be of type int")
        self._id = value
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        if not hasattr(self, '_name'):
            self._name = value
        else:
            raise AttributeError("Name cannot be changed after instantiation")
    @classmethod
       # inserting a new article 
    def create_article(cls, cursor, title, content, author_id, magazine_id):
        cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)", (title, content, author_id, magazine_id))
        article_id = cursor.lastrowid
        return cls(article_id, title, content, author_id, magazine_id)

    @classmethod
    
    def get_title(cls, cursor):
        cursor.execute("SELECT title FROM articles")
        titles = cursor.fetchall()
        return [title[0] for title in titles] if titles else None


    def get_author(self, cursor):
       
        cursor.execute("SELECT name FROM authors WHERE id = ?", (self._author_id,))
        author_name = cursor.fetchone()
        return author_name[0] if author_name else None


    def get_magazine(self, cursor):
       
        cursor.execute("SELECT name FROM magazines WHERE id = ?", (self._magazine_id,))
        magazine_name = cursor.fetchone()
        return magazine_name[0] if magazine_name else None
        
        
        

    def __repr__(self):
        return f'<Author {self.name}>'
