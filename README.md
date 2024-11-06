### Send Emails via M365 from Python

This module provides a simple way to send emails via Microsoft 365. You need a valid Microsoft 365 username (email address) and password.

The `send_mail` method is used to send an email to any recipient. You can also pass a list of recipients here ["recipient1@example.com", "recipient2@example.com"]

The host defaults to `smtp.office365.com`, and the port defaults to `587`, but you can specify your own in the constructor if needed.

#### Usage

Install via pip:

    pip install git+https://github.com/hadoken79/py_send_m365.git

```python
from py_send_m365 import M365Mail

# Create an instance, providing optional host and port if needed
mailer = M365Mail("myuser@domain.com", "mypassword", host="smtp.example.com", port=587)

# Send an email
mailer.send_mail("recipient@domain.com", "My Subject", "The message body")


