# Software Engineering Job Listing Application

This project is a web application developed using Django's MVT (Model-View-Template) architecture. It is designed to showcase software engineering job opportunities and provides users with the ability to filter and search through job listings.

## Features

- **Job Listings:** Displays software engineering job opportunities with details such as job title, location, and salary range.
- **Advanced Filtering:** Users can filter jobs based on various criteria, ensuring they find the positions most relevant to their skills and preferences.
- **Search Functionality:** A robust search feature that allows users to quickly find job listings that match specific keywords.
- **Responsive Design:** Built with HTML and Tailwind CSS, the application offers a modern and responsive user interface across all devices.
- **Complex Django Functions:** Several complex Django functions have been implemented to handle data processing and business logic, ensuring a smooth and efficient user experience.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (default with Django, can be replaced with PostgreSQL, MySQL, etc.)

## Installation

1. **Clone the repository:**
   ```bash
    git clone https://github.com/yourusername/software-engineering-job-listing.git
    cd software-engineering-job-listing
   ```
2. **Create a virtual environment:**
   ```bash
    python3 -m venv env
    source env/bin/activate
   ```
3. **Install the dependencies:**
   ```bash
    pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
    python manage.py migrate
   ```
5. **Apply migrations:**
   ```bash
    python manage.py runserver
   ```
6. **Access the application:**
   Open your browser and go to
   ```bash
    http://127.0.0.1:8000/
   ```

## Usage

- **Home Page:** Browse the list of software engineering jobs.
- **Search Jobs:** Enter keywords in the search bar to quickly find relevant job opportunities.
- **Filter Jobs:** Use the filtering options to narrow down job listings based on criteria like location, job type, or salary range.

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/zisanurhaque/swe_jobs/blame/main/LICENSE) file for details.

## Contact

For any inquiries, please contact [Zisanur Haque](https://zisanurhaque.vercel.app/).
