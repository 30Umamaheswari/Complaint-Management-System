# Complaint Management System

The **Complaint Management System** is a user-friendly Python application developed using the Streamlit framework. It allows users to submit complaints with ease, perform basic validations on the entered data, and receive email confirmation upon successful submission. This system is designed for managing and tracking user complaints effectively.

## Features

- **User-Friendly Interface:** The application provides a clean and intuitive user interface for submitting complaints.

- **Email Confirmation:** Upon successful complaint submission, users receive an email confirmation for their records.

- **Email Validation:** The system validates user email addresses to ensure they are in the correct format.

- **Minimum Character Requirement:** A complaint must contain a minimum of 120 characters to ensure that users provide detailed information.


## Usage

1. Configure Gmail for Email Notifications:
   - Replace `"Sender_Mail_id"` with your Gmail email address in `app.py`.
   - Replace `"Password"` with your Gmail password. Be cautious with storing your password in the code; consider using environment variables for security.

2. Start the application:

   ```bash
   streamlit run app.py
   ```

3. Access the application in your web browser using the provided URL.

4. Fill in the following details:
   - **User Name**
   - **Email Id (Must be a valid email address)**
   - **Complaint (Minimum of 120 characters)**

5. Click the "Submit" button to submit your complaint. You will receive an email confirmation indicating that your complaint has been successfully submitted.

## Application Customization

- Customize the background image:
  - Replace the URL in the `page_bg_image` variable in `app.py` to change the background image.

```python
page_bg_image = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("your-background-image-url-here");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
background-position: center;
}
</style>
```

## Contributing

Contributions to this project are welcome. If you have ideas for improvements or find any issues, please open an issue or create a pull request.

