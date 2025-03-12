import streamlit as st
import json

# File to store the library data
LIBRARY_FILE = "library.json"

# Load the library from a file
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save the library to a file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Load books at start
library = load_library()

# Streamlit UI
st.title("📚 Personal Library Manager")

# Sidebar Menu
menu = st.sidebar.radio("📌 Menu", ["Add Book", "Remove Book", "Search Book", "Display Books", "Statistics"])

if menu == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author Name")
    year = st.number_input("Enter Publication Year", min_value=1500, max_value=2025, step=1)
    genre = st.text_input("Enter Genre")
    read_status = st.checkbox("Mark as Read")

    if st.button("Add Book"):
        book = {
            "title": title,
            "author": author,
            "year": int(year),
            "genre": genre,
            "read": read_status
        }
        library.append(book)
        save_library(library)
        st.success("✅ Book Added Successfully!")

elif menu == "Remove Book":
    st.subheader("🗑️ Remove a Book")
    titles = [book["title"] for book in library]
    if titles:
        selected_title = st.selectbox("Select Book to Remove", titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_title]
            save_library(library)
            st.success("✅ Book Removed Successfully!")
    else:
        st.warning("📭 No books available to remove!")

elif menu == "Search Book":
    st.subheader("🔍 Search for a Book")
    search_query = st.text_input("Enter Title or Author Name")
    if st.button("Search"):
        results = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        if results:
            for book in results:
                status = "✅ Read" if book["read"] else "❌ Unread"
                st.write(f"📖 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            st.warning("❌ No matching books found!")

elif menu == "Display Books":
    st.subheader("📚 Your Library")
    if library:
        for i, book in enumerate(library, start=1):
            status = "✅ Read" if book["read"] else "❌ Unread"
            st.write(f"{i}. 📖 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.warning("📭 No books in the library!")

elif menu == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {read_books} ({percentage_read:.2f}%)")
