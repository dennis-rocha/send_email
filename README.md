# send_email

## How to Use

To use the `send_email` service in your project, import it with:

```python
from send_email import send_email
```

The service requires three environment variables:

1. **`SEND_FROM`**: Your Gmail address.
2. **`SEND_TO`**: The recipient's email address.
3. **`PASS_SEND_EMAIL`**: Your Gmail app password.

Provide the title and body of the email, then call `send_email(title, body)`. After a few seconds, check the terminal for "Send email success" for successful sending or "Failed to send email: error..." for unsuccessful attempts.

## Requirements

To send emails, you'll need an app password. Generate one by following these steps:

1. Visit [Google Account - App Passwords](https://myaccount.google.com/apppasswords).
2. Select the name of your app.
3. Click on "Create".
4. Copy the generated password and save it as an environment variable.


## Authors

- [@dennis-rocha](https://www.github.com/dennis-rocha)
