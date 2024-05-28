# TECHNICAL WRITING 101 USER GUIDE
#### Video Demo:  <https://youtu.be/38mMam4gLWg>

## Description
You need a username and a password to access the Technical Writing 101 web application. Once logged in, you can enjoy educational content about the three most common mistakes in technical writing and test your knowledge with a quiz. Enjoy!

## How to Use This Website
1. Register a unique username and a password with the application.
2. Log in with your username and password.
3. Click **How To** to read the webpages and view the educational videos.
4. Click **Quiz** to take the interactive quiz.
5. Learn more by clicking **References** and following the links on the page.
6. Click **Contact** if you have more questions about technical writing.

## Overview of the Web Application
The application is about common mistakes in technical writing and is comprised of one static CSS (`styles.css`) file, ten HTML files, two Python files, one requirements text (`requirements.txt`) file, and a user database (`user.db`) file. The CSS file is the source of all the layout and text styles within the various webpages. This style sheet is centralized into one file so that the webmaster only needs to manipulate a single page to change all the styles within the ten HTML files, enabling easy updating and a more consistent look and feel across the website.

### Core HTML Files
The application comprises ten HTML files, each serving a distinct function:
- `login.html` greets you with a login page requiring a username and a password. If you do not have a username or password, you must register to gain access.
- `register.html` provides the HTML form where you input your username and password. If registration fails, the `apology.html` file generates an error message.
- `apology.html` returns an apology if errors occur during the registration and login process, such as "typed wrong password," "username already exists," "password confirmation does not match," and "must provide a username and password."
- `quiz.html` tests your knowledge of the application's educational content with multiple-choice and fill-in-the-blank questions. The JavaScript code embedded in `quiz.html` uses a "for loop," allowing the webmaster to easily create new questions by reusing the code that triggers the responses for correct or incorrect answers.

### Supplementary HTML Files
The application is supplemented by six additional HTML files, each serving specific purposes:
- `challenge.html` contains sample solutions to the two editing challenges at the bottom of `quiz.html.`
- `howto.html` provides educational material on fixing the top three technical writing mistakes by using present tense, employing an active voice, and crafting shorter and more meaningful sentences.
- `index.html` serves as the homepage, defining the top three technical writing mistakes.
- `layout.html` delivers the headers for the other pages, including the title and menu buttons.
- `references.html` lists the following reference books: The Chicago Manual of Style, Microsoft Writing Style Guide, and Google Developer Documentation Style Guide.
- `contacts.html` contains the name, address, phone number, email, and fax number of a fictitious technical writer responsible for the website's content.

## Key Structural Dependencies of the Web Application
The Python code in `app.py` is the backbone of the HTML files and it does the following:
- Contains all the routes between the webpages, the logic behind error message generation, and session cookie management.
- Updates the `user.db` file dynamically.
- Allows you to log out.

The `requirements.txt` file provides a list of libraries needed to run the application. For example, Flask is one library listed in the `requirements.txt` file. Flask handles the routing of URLs and processing of user inputs. These user inputs and URL routes, managed by Flask, enable navigation and webpage interaction by dynamically rendering appropriate responses based on defined HTML templates. Additionally, Flask serves HTML files that can include embedded JavaScript code, such as in the `quiz.html` file, which enhances the user experience by providing real-time interactivity on the client side.

These dependencies are essential for the application's operation, and understanding them is crucial for maintaining, updating, and troubleshooting the application.


