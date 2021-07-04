# Contact Form using Django + Celery

This is a contact form project, you can use in personal portfolio websites or anywhere where people will like to contact you.

When you submit the form it will save the details of the person who tried contacting you inside the database and also sends an email message both to the ower of contact form and person who tried conatcting with a personalised message.

## Tech stack:
<p align="left">
  <img src="https://img.shields.io/badge/django-092E20.svg?&style=for-the-badge&logo=django&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/python-FFD43B.svg?&style=for-the-badge&logo=python&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/celery-9DCE5C.svg?&style=for-the-badge&logo=celery&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/redis-%23B92B27.svg?&style=for-the-badge&logo=redis&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/bootstrap-563d7c.svg?&style=for-the-badge&logo=bootstrap&logoColor=white" />&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/gmail-D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />&nbsp;&nbsp;&nbsp;
</p>

</br>


## Setup :
1. Install the [requirements.txt](./requirements.txt) in a virtual env.
   ```
   pip install -r requirements.txt
   ```
   **Note**: Redis installation for Ubuntu [here](https://redis.io/topics/quickstart)


2. Update your email address in [settings.py](./PortfolioContact/settings.py) file which will be used for sending an email.

3. Update [.env](./PortfolioContact/settings.py) file by saving your email's password into it.

4. Open four terminals with the virtual env created using requirements.txt file 
    
    1. **Terminal 1** : Start Django server.
        ``` 
        python manage.py runserver
        ```
        Note : Your directory should be same as manage.py file. 
        
        ![Terminal1](https://user-images.githubusercontent.com/55273506/124386906-2e339800-dcfa-11eb-8bcc-736b50600a65.png)


    2. **Terminal 2** : Starting Redis server ie. Message Broker.
        ```
        redis-server
        ```
        Make sure you have install redis properly.
        
        ![Terminal2](https://user-images.githubusercontent.com/55273506/124386927-50c5b100-dcfa-11eb-8d9e-be0fc383ee95.png)

    
    3. **Termial 3** : Starting Redis CLI to interact with our Django Application.
        ```
        redis-cli
        ``` 
        ![Terminal3](https://user-images.githubusercontent.com/55273506/124386951-6cc95280-dcfa-11eb-836d-bec0971a6637.png)
    
    4. **Termial 4** : Running the Celery worker server i.e. connecting Celery to Redis by using below command. 
        ```
        celery -A PortfolioContact worker --loglevel=INFO
        ```
        ![Terminal4](https://user-images.githubusercontent.com/55273506/124386961-7488f700-dcfa-11eb-8c95-10b7d38198ee.png)


5. Follow the link from Terminal 1 to your local host **http://127.0.0.1:8000/** .

6. Submit the form to see the results.


## Working Screenshots:

1. Contact Form:
    
    ![ContactForm_1](https://user-images.githubusercontent.com/55273506/124387044-af8b2a80-dcfa-11eb-8563-5870fc7ed6ff.png)


2. After submitting form:

    ![ContactForm_2](https://user-images.githubusercontent.com/55273506/124387069-bfa30a00-dcfa-11eb-929e-52714a3c6a5d.png)

3. Email to owner:

    ![Email_1](https://user-images.githubusercontent.com/55273506/124387090-d2b5da00-dcfa-11eb-91df-1d2dee5d8c4e.png)



4. Email to client who submitted the form:

    ![Email_2](https://user-images.githubusercontent.com/55273506/124387096-d6e1f780-dcfa-11eb-8bb2-5954ea8dc9c8.png)



## [Akhil Bhalerao](https://github.com/iamakkkhil)
