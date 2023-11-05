# Python Flask Template

This project provides a template for a Python web application using Flask, with pre-configured tooling for code linting, formatting, testing, and deployment. It's ideal for developers looking to jumpstart their Flask application development with best practices in mind.

## Features

- **Flask Application**: A lightweight WSGI web application framework for quick development of dynamic websites.
- **Unit Testing**: Integrated with `pytest` for writing and executing test cases, ensuring code correctness.
- **Code Linting**: Uses `flake8` to enforce coding style and standards.
- **Pre-commit Hooks**: Pre-commit hooks run `flake8` and `black` to ensure code quality and consistency before each commit.
- **Docker Support**: Containerize your application for development and deployment with the provided Dockerfile.
- **GitHub Actions Workflow**: Automated testing and linting with GitHub Actions to facilitate continuous integration.
- **Automatic Semantic Versioning**: Automated version tagging and release management with semantic versioning standards.
- **Code Formatting**: `black` is configured for consistent code formatting across the codebase.
- **Type Checking**: Static type checking with `mypy` to catch potential type-related bugs.

## Getting Started

These instructions will help you set up your project locally. For live deployment notes, scroll down to [Deployment](#deployment).

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12
- Git

### Installation

To get a local copy up and running, follow these simple steps:

```bash
# Clone the repository
git clone https://github.com/SanderMoon/PythonFlaskTemplate.git
```
```bash
# Navigate to the repository directory
cd PythonFlaskTemplate
```
```bash
# Install pre-commit hooks
pre-commit install
```
```bash
# Create a virtual environment (Optionial)
python3.12 -m venv venv
```
```bash
# Activate the virtual environment (Optional)   
source venv/bin/activate
# OR
venv\Scripts\activate.bat
```
```bash
# Install dependencies
pip install -r requirements.txt
```

### Usage

To start the application locally, run:

```bash
flask run
```

Navigate to `http://127.0.0.1:5000/` to see your application in action.

Or you can run it in VSCode using the provided launch configuration.

## Running Tests

To run tests, use the following command:

```bash
pytest
```

## Deployment

To deploy this project, you can build a Docker container using the provided Dockerfile, or deploy directly to a hosting service that supports Python applications.

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [GitHub Actions](https://github.com/features/actions) - Automated workflows.
- [Docker](https://www.docker.com/) - Containerization platform.

## Versioning

We use SemVer for versioning. For the versions available, see the [releases on this repository](https://github.com/SanderMoon/PythonFlaskTemplate/releases).

## Authors

- **Sander Moon** - *Initial work* - [SanderMoon](https://github.com/SanderMoon)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
