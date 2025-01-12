class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self.title = title

        # Add the article to both the author and magazine
        self.author.add_article(self)
        self.magazine.add_article(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self.name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after instantiation")
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("Must be an instance of Article")
        self._articles.append(article)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set([article.magazine.category for article in self._articles]))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("Must be an instance of Article")
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set([article.author for article in self._articles]))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        contributing_authors = [author for author in authors if authors.count(author) > 2]
        return list(set(contributing_authors)) if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles()))

# Class variable to track all magazines for top_publisher
Magazine.all_magazines = []
