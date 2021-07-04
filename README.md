# Contact Form using Django + Celery

This is a contact form project, you can use in personal portfolio websites or anywhere where people will like to contact you.

When you submit the form it will save the details of the person who tried contacting you inside the database and also sends an email message both to the ower of contact form and person who tried conatcting with a personalised message.

## Tech stack:
<p align="left">
  <img src="https://img.shields.io/badge/django-092E20.svg?&style=for-the-badge&logo=django&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/python-4B8BBE.svg?&style=for-the-badge&logo=python&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/celery-9DCE5C.svg?&style=for-the-badge&logo=celery&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/redis-%23B92B27.svg?&style=for-the-badge&logo=redis&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/bootstrap-563d7c.svg?&style=for-the-badge&logo=bootstrap&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/gmail-D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />&nbsp;&nbsp;&nbsp;
</p>

</br>

**Note**: Redis installation for Ubuntu [here](https://redis.io/topics/quickstart)


## Setup :
1. Install the [requirements.txt](./requirements.txt) in a virtual env.
   ```
   pip install -r requirements.txt
   ```

2. Update your email address in [settings.py](./PortfolioContact/settings.py) file which will be used for sending an email.

3. Update [.env](./PortfolioContact/settings.py) file by saving your email's password into it.

4. Open four terminals with the virtual env created using requirements.txt file 
    
    1. **Terminal 1** : Start Django server.
        ``` 
        python manage.py runserver
        ```
        Note : Your directory should be same as manage.py file. 

        ![Terminal_1](https://iili.io/oxsFQn.md.png)


    2. **Terminal 2** : Starting Redis server ie. Message Broker.
        ```
        redis-server
        ```
        Make sure you have install redis properly.

        ![Terminal_2](https://iili.io/oxsj6J.md.png)
    
    3. **Termial 3** : Starting Redis CLI to interact with our Django Application.
        ```
        redis-cli
        ``` 
        ![Terminal_3](https://iili.io/oxsOaR.md.png)
    
    4. **Termial 4** : Running the Celery worker server i.e. connecting Celery to Redis by using below command. 
        ```
        celery -A PortfolioContact worker --loglevel=INFO
        ```
        ![Terminal_4](https://iili.io/oxsevp.md.png)


5. Follow the link from Terminal 1 to your local host **http://127.0.0.1:8000/** .

6. Submit the form to see the results.


## Working Screenshots:

1. Contact Form:
    
    ![ContactForm_1](https://iili.io/oxPkKv.md.png)


2. After submitting form:

    ![ContactForm_2](https://iili.io/oxPOiJ.md.png)

3. Email to owner:

    ![Email_1](https://iili.io/oxP8Sp.md.png)


4. Email to client who submitted the form:

    ![Email_2](https://iili.io/oxPiVs.md.png)


## [Akhil Bhalerao](https://github.com/iamakkkhil)
