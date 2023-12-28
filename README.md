
# CatchClient A pathway to unlimited emails and a dream.

```python
>>> import catchclient
>>> # Get a new .com domain
>>> domain = catchclient.getdomain(".com")

>>> # Get the inbox of an email
>>> # Includes status, amount, email link, email time, email sender
>>> inbox = catchclient.getinbox("email1@"+domain)

>>> # Get email content
>>> if inbox['status'] == True:
>>>     email_link = inbox['emails'][0]['link']
>>>     email_content = catchclient.getemail(email_link)
```

CatchClient allows you to have `unlimited emails` under thousands of `different domains`. With an easy to use python library, you can easily utilize CatchClient in any of your projects seemlessly.

## Installing the CatchClient [latest version]


```console
$ python -m pip install git+https://github.com/podzied/catchclient
```

Supports Python 3.6 and above

## Supported Features

- 10s of thousands of top-level domains
- Constantly adding new domains to list
- Easily get access to entire inbox of email
- Quick email processing time
