# iRIX Python tools

Some libraries to use internally.  
Don't forget to increase version number in setup.py if you make changes.  

installation

```py
pip install git+<https link_to_repo> (get it from clone dialog)
#  prompt that asks for password needs your app password
```
update

```py
pip install git+<https link_to_repo> --upgrade
```
>In order to get access to this repo you must have activated app password in bitbucket otherwise you can't >authenticate. Goto your account->Personal Secttings->Account Settings->App passwords and create new. (or just place you ssh key)

## libs

### irix_mail

Simple module to send emails over Microsoft 365. You need valid username and password of the irix_service account.

"mail_infra"
Can be used to either directly mail to infra, f.e for info mailings from cron jobs.

"send_mail"
Used to send email to anyone.

#### usage
 
```py
from infra_py_toolbox import Irix_mail

mailer = Irix_mail("myuser@domain.com","mypassword")

mailer.mail_infra("Warn", "this is the end off all things", "no clue why this happend.")

mailer.send_mail("recipient@domain.com", "my subject", "the message body")
```

### folder_cleanup

Script to remove old files from a given folder (path) with the possibility to make sure only files or folders older than x amount of days will be deleted but only when a given number of files whould survive.  

This module when called from a script in a cronjob, can be used to prevent backup folders from growing to much. Also it makes sure that if the backup job f.e stopped working we are not deleting all files over time and leaving us with no backup files at all.

Alse this module makes sure there are always enough files in a certain folder. All those parameters can be passed to constructor.

The module will raise errors not enough files would survive, or if there aren't enough files in the folder to begin with. You can catch those and f.e notify someone with this error message.

The constructor takes four parameters.
1. The path to the folder.
2. The age in days after whichg a file should get deleted. (modified date)
3. The min amount of files that should still be in this folder after the deletion.
4. The boolean if the script should also remove folders. (be careful with this, as it removes recursively)

So the modules deletes all files that are older than specified in second parameter as long as the amount of files specified in the third parameter would survive. If conditions can not be met, an exception will be thrown.

#### usage
 
installation

```py
pip install git+<https link_to_repo> (get it from clone dialog)
```
update

```py
pip install git+<https link_to_repo> --upgrade
```
usage

```py
from infra_py_toolbox import Folder_cleanup

cleaner = Folder_cleanup("/home/myBackup/somewhere", 5, 10)
try:
    cleaner.delete_old_files()
except Exception as e:
    # do something with exception f.e use irix_mail lib to pass message to infra
```


