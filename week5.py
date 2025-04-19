class ClassicBook:
    def __init__(self, title, author, year_published, genre):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.genre = genre
        self.rating = None
        self.reviews = []

    def get_summary(self):
        return f"'{self.title}' by {self.author} ({self.year_published}), Genre: {self.genre}"

    def age_of_book(self, current_year):
        return f"This book is {current_year - self.year_published} years old!"

    def add_rating(self, rating):
        if 0 <= rating <= 5:
            self.rating = rating
            return f"Rating of {rating}/5 added for '{self.title}'."
        return "Rating must be between 0 and 5."

    def add_review(self, review):
        self.reviews.append(review)
        return f"Review added: '{review}'"

    def display_reviews(self):
        if self.reviews:
            return f"Reviews for '{self.title}':\n" + "\n".join(self.reviews)
        return "No reviews available."

    def recommend_books(self):
        recommendations = {
            "Romance": ["Wuthering Heights by Emily Brontë", "Anna Karenina by Leo Tolstoy"],
            "Philosophy": ["Meditations by Marcus Aurelius", "Beyond Good and Evil by Friedrich Nietzsche"],
            "Adventure": ["Moby-Dick by Herman Melville", "The Three Musketeers by Alexandre Dumas"],
            "Mystery": ["The Hound of the Baskervilles by Arthur Conan Doyle", "Rebecca by Daphne du Maurier"],
        }
        return f"Books similar to '{self.title}': " + ", ".join(recommendations.get(self.genre, ["No recommendations available."]))


class PhilosophicalClassic(ClassicBook):
    def __init__(self, title, author, year_published, genre, philosophical_theme):
        super().__init__(title, author, year_published, genre)
        self.philosophical_theme = philosophical_theme

    def get_summary(self):
        return f"'{self.title}' by {self.author} ({self.year_published}), Genre: {self.genre}. Theme: {self.philosophical_theme}"


# Creating book instances
book1 = ClassicBook("Pride and Prejudice", "Jane Austen", 1813, "Romance")
book2 = PhilosophicalClassic("Thus Spoke Zarathustra", "Friedrich Nietzsche", 1883, "Philosophy", "The Übermensch and Eternal Recurrence")

# Displaying book details
print(book1.get_summary())
print(book2.get_summary())
print(book1.age_of_book(2025))  # Checking age of the book

# Adding ratings and reviews
print(book1.add_rating(4.5))
print(book1.add_review("A timeless classic with engaging characters!"))
print(book1.display_reviews())

# Getting book recommendations
print(book1.recommend_books())
print(book2.recommend_books())
