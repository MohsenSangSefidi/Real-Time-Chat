# Real-Time Chat

A modern, real-time chat application built with Django, WebSockets (via Django Channels), and HTMX for a seamless single-page application experience without complex JavaScript frameworks.


## Tech Stack

**Client:** Html, Css, Htmx

**Server:** Django, Websocket 


## Features

- **Real-time messaging** using WebSockets (Django Channels)
- **HTMX-powered UI** for dynamic updates without full page reloads
- **User authentication** with Django's built-in auth system
- **Message history** with automatic scrolling to newest messages
- **Responsive design** that works on desktop and mobile

## Installation

- You can see my Project from this Link : 
https://mohsen.pythonanywhere.com/

- Also can install it locally

```
# Clone the repository
git clone https://github.com/MohsenSangSefidi/Real-Time-Chat
cd Real-Time-Chat

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver
```
## Screenshots

![App Screenshot](https://s33.picofile.com/file/8484458750/Screenshot_Real_Time_Chat.jpg)


## License

[MIT](https://choosealicense.com/licenses/mit/)

