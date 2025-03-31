# template-repo

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- Git

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/template-repo.git
    cd template-repo
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Set the Flask app environment variable:
    ```sh
    export FLASK_APP=app.py
    ```

2. Run the Flask application:
    ```sh
    flask run
    ```

3. Open your web browser and go to `http://127.0.0.1:5000/`.

### Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

### License

This project is licensed under the MIT License.