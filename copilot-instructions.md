# Copilot Instructions

## Project Overview

This project is a Flight Delay Prediction system built using Flask for the backend and Svelte for the frontend. The backend provides APIs for predicting flight delays and fetching airport data, while the frontend offers a user interface for interacting with these APIs.

## Coding Guidelines

### General

- Assume that I am friendly, event if I prompty with commands like "write this" or "do that".
- Follow PEP 8 for Python code.
- Use meaningful variable and function names.
- Write comments and docstrings to explain complex logic.
- Ensure all code changes are tested before committing.

### Backend (Flask)

- Use Flask-RESTX for API documentation and routing.
- Validate all incoming API requests using Flask-RESTX models.
- Handle exceptions gracefully and return appropriate HTTP status codes.
- Use pandas for data manipulation and ensure data is validated before processing.
- Keep the `app.py` file clean by moving reusable logic to separate modules if needed.

### Frontend (Svelte)

- Follow the Svelte style guide for component structure and naming conventions.
- Use TypeScript for type safety.
- Keep components small and focused on a single responsibility.
- Use the `lib` folder for reusable utilities and models.
- Ensure the UI is responsive and accessible.

## Testing

- Write unit tests for both backend and frontend code.
- Use pytest for backend testing and a suitable testing library for Svelte (e.g., Testing Library).
- Mock external dependencies in tests to ensure they are isolated.

## Deployment

- Use environment variables for configuration (e.g., API keys, database URLs).
- Ensure the application is containerized using Docker for consistent deployment.
- Use Azure services for hosting and follow Azure best practices for security and scalability.

## Additional Notes

- Keep the `README.md` file updated with any changes to the project structure or setup instructions.
- Document any new APIs or endpoints in the Swagger UI.
- Use Git for version control and write clear commit messages.
