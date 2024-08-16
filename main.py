#!/usr/bin/env python3
from models.db import DB
from models.user import User
from models.blog import Blog
import bcrypt

# Instantiate the DB class
db = DB()

# Create a new User instance
user_1 = User(email="test@me.com", firstName="Eric", lastName="Uwi", password="passwd")
user_2 = User(email="test@me1.com", firstName="Kennedy", lastName="Merci", password="passwd")
user_3 = User(email="test@me2.com", firstName="Alice", lastName="Mukapa", password="passwd")
# Add the User instance to the session
db.new(user_1)
db.new(user_2)
db.new(user_3)

# Commit the transaction to save the User to the database
db.save()

# add blogs
blog_1 = Blog(title="drugs therapy", content="blog 1", user_id=1)
blog_2 = Blog(title="pharmacology", content="blog 2", user_id=1)
blog_3 = Blog(title="comp", content="blog 1", user_id=2)
blog_4 = Blog(title="civil", content="blog 1", user_id=3)

db.new(blog_1)
db.new(blog_2)
db.new(blog_3)
db.new(blog_4)
db.save()

print(db.all())
print(db.all(User))
print(db.all(Blog))
user = db.get(User, 2)
print(user.password)
print(db.get(Blog, 2))
print(db.get(Blog, 6))
print(db.delete(user))
print(db.all(User))
print(db.all(Blog))

