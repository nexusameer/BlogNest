# BlogNest

BlogNest is a feature-rich blogging platform built using [Django](https://www.djangoproject.com/).

## Features

- User authentication (registration, login, logout)
- Create, edit, and delete blog posts
- Commenting system
- Categories and tags for posts
- Responsive design
- Admin dashboard for managing content

## Getting Started

### Prerequisites

- Python 3.9+
- pip
- (Optional) Virtualenv

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nexusameer/BlogNest.git
   cd BlogNest
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Blog: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure

```
BlogNest/
├── blog/           # Main blog app
├── users/          # User authentication and profiles
├── BlogNest/       # Project settings
├── templates/      # HTML templates
├── static/         # Static files (CSS, JS, images)
├── manage.py
└── requirements.txt
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
