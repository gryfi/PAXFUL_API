import os
import django
import argparse

os.environ.setdefault('DJANGO_SETTINGS_MODULE','PAXFUL_REST.settings')
django.setup()
import random
from BOOK_REST.models import Book,Author
from faker import Faker


fakegen = Faker()
"""
# An arbitrary book list to create sample Book object entries from
"""
books_list = ['War and Peace','Anna Karenina','To Kill a Mockingbird','The Great Gatsby',\
            'One Hundred Years of Solitude','Crime and Punishment','A Passage to India',\
            'Invisible Man','Don Quixote','Beloved']
"""

# An author add function create an author object,save and then return for use in creating a Book object
here we use faker package to create name field samples from creating an Author object

"""
def add_Author():
    author = Author.objects.get_or_create(name = fakegen.name())[0]
    author.save()
    return author

"""
# function for populating DB with author and book objects.
"""
def populate(N=10):
    for entry in range(N):
        author = add_Author()
        if entry == 2:
            book = Book.objects.get_or_create(title=random.choice(books_list), author=author)
            book = Book.objects.get_or_create(title=random.choice(books_list), author=author)
        else:
            book = Book.objects.get_or_create(title=random.choice(books_list), author=author)


"""
#argument_parser for DB sample data filling and deleting script
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Populate App Database with Sample Data')
    parser.add_argument(
    '-delete',
    action='store',
    default=False,
    help="select for deleting all data or populating")
    parser.add_argument(
    '-Nsamples',
    action='store',
    default=False,
    help="Number of Sample Entries")
    args = parser.parse_args()
    delete = args.delete
    n_samples = int(args.Nsamples)

    if not delete:
        print("Filling DB with sample Data !")
        if not n_samples:
            populate()
        else:
            populate(n_samples)
        print("DB filled with sample Data")
    else:
        print("Deleting any data in Database")
        Book.objects.all().delete()
        Author.objects.all().delete()
        print("Deleted data in Database")
