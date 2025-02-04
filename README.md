### Send Emails via M365 from Python

This module provides a simple way to send emails via Microsoft 365. You need a valid Microsoft 365 user (email address) and password.

The `send_mail` method is used to send an email to any recipient. You can also pass a list of recipients here ["recipient1@example.com", "recipient2@example.com"]

The host defaults to `smtp.office365.com`, and the port defaults to `587`, but you can specify your own in the constructor if needed. 

#### Usage

from py_send_m365 import M365Mail

## Create an instance, providing optional host and port if needed

    mailer = M365Mail("myuser@domain.com", "mypassword", host="smtp.example.com", port=587)

## Send an email

    mailer.send_mail("recipient@domain.com", "My Subject", "The html <br><i>message</i> body")


## Send as

If you have allowed sending from other addresses for your user in m365, you can pass a custom from address. 

    mailer.send_mail("recipient@domain.com", "My Subject", "The html <br><i>message</i> body", "my-allowed-sender@domain.com")


