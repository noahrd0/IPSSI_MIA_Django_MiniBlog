# Django Mini Blog Application

## Objective

This exercise demonstrates the development of a Django application using the Model-View-Template (MVT) architecture. The Mini Blog Application allows users to create, edit, view, and delete blog posts and comments.

## Features

- Create, edit, view, and delete blog posts.
- Add, edit, and delete comments on blog posts.
- Redirect between views and use templates that extend a common base layout.
- Test coverage to ensure the application functions as expected.

## Specifications

### Step 1: Models

#### BlogPost

- **Fields**:
  - `title`: CharField, max length: 100
  - `content`: TextField
  - `created_at`: DateTimeField, auto_now_add=True
- **Features**:
  - `__str__` method returns the post title.

#### Comment

- **Fields**:
  - `post`: ForeignKey to BlogPost (on_delete=models.CASCADE)
  - `author`: CharField, max length: 50
  - `text`: TextField
  - `created_at`: DateTimeField, auto_now_add=True
- **Features**:
  - `__str__` method returns a truncated version of the comment text.

### Step 2: Views

#### List Blog Posts

- **Template**: `post_list.html`
- **Features**:
  - Displays all blog posts with "View," "Edit," and "Delete" links.
  - Includes a "Create New Post" button.

#### View Blog Post Details

- **Template**: `post_detail.html`
- **Features**:
  - Displays a blog post and its associated comments.
  - Each comment has "Edit" and "Delete" links.
  - Includes a link to add a comment and a "Back to Blog List" button.

#### Create Blog Post

- **Template**: `create_post.html`
- **Features**:
  - Displays a form for creating a new blog post.
  - Redirects to the blog post list after creation.
  - Includes a "Cancel" button.

#### Edit Blog Post

- **Template**: `edit_post.html`
- **Features**:
  - Displays a form for editing an existing blog post.
  - Pre-fills the form with the existing blog post's data.
  - Redirects to the blog post detail view after saving changes.
  - Includes a "Cancel" button.

#### Add Comment to Blog Post

- **Template**: `add_comment.html`
- **Features**:
  - Displays a form for adding a comment to a blog post.
  - Redirects to the blog post detail view after adding a comment.
  - Includes a "Cancel" button.

#### Edit Comment

- **Template**: `edit_comment.html`
- **Features**:
  - Displays a form for editing an existing comment.
  - Pre-fills the form with the existing comment's data.
  - Redirects to the blog post detail view after saving changes.
  - Includes a "Cancel" button.

#### Delete Blog Post

- **Features**:
  - Deletes a specific blog post.
  - Redirects to the blog post list after deletion.
  - Includes a confirmation prompt.

#### Delete Comment

- **Features**:
  - Deletes a specific comment.
  - Redirects to the blog post detail view after deletion.
  - Includes a confirmation prompt.

### Step 3: Templates

Templates extend a common `base.html` template and include a navigation bar with the following links:

- Home: Redirects to the blog post list.
- Create Post: Redirects to the create post view.

### Step 4: URLs

Configure the following URLs:

- `/`: Blog post list (List view).
- `/post/<id>/`: Blog post detail (Detail view).
- `/post/create/`: Create a new blog post (Create view).
- `/post/<id>/edit/`: Edit an existing blog post (Edit view).
- `/post/<id>/add_comment/`: Add a comment to a blog post (Add Comment view).
- `/comment/<id>/edit/`: Edit an existing comment (Edit Comment view).
- `/post/<id>/delete/`: Delete a blog post (Delete Post view).
- `/comment/<id>/delete/`: Delete a comment (Delete Comment view).

### Step 5: Tests

Write 10 test cases to ensure:

- Blog posts are created, edited, and deleted correctly.
- Comments are added, edited, and deleted correctly.
- Views return expected HTTP responses.
- Templates render the correct data.
- Redirections occur as intended.

### Example Features

#### Post List (`/`):

- Blog Posts:
  1. Django Basics (View | Edit | Delete)
  2. Advanced Django Features (View | Edit | Delete)
  - [Create New Post]

#### Post Detail (`/post/<id>/`):

- Title: Django Basics
- Content: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- Comments:
  - Author: Alice, Text: Great introduction to Django! (Edit | Delete)
  - Author: Bob, Text: Very helpful! (Edit | Delete)
  - [Add Comment]
  - [Back to Blog List]

#### Add Post (`/post/create/`):

- Title: [Input Field]
- Content: [Text Area]
- [Save Post] [Cancel]

#### Add Comment (`/post/<id>/add_comment/`):

- Author: [Input Field]
- Text: [Text Area]
- [Add Comment] [Cancel]

#### Edit Post (`/post/<id>/edit/`):

- Title: Django Basics (Pre-filled in input field)
- Content: Django is a high-level Python web framework... (Pre-filled in text area)
- [Save Changes] [Cancel]

#### Edit Comment (`/comment/<id>/edit/`):

- Text: Great introduction to Django! (Pre-filled in input field)
- [Save Changes] [Cancel]

#### Delete Post Confirmation (`/post/<id>/delete/`):

- Are you sure you want to delete "Django Basics"?
- [Yes, Delete] [Cancel]

#### Delete Comment Confirmation (`/comment/<id>/delete/`):

- Are you sure you want to delete the comment by Alice: "Great introduction to Django!"?
- [Yes, Delete] [Cancel]

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or later

### Installation

1. Clone the repository:

```sh
git clone https://github.com/noahrd0/IPSSI_MIA_Django_MiniBlog.git
cd MiniBlog
```

2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

4. Apply the migrations:


```sh
python manage.py migrate
```

5. Run the development server:

```sh
python manage.py runserver
```

### Running Tests

```sh
python manage.py test
```
