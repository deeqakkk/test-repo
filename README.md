# Custom Integration Framework
___

This repository is meant for developing a custom integration framework, where third-party developers/orgs can develop apps, and can integrate with another org (like google calendar can be integration to slack) to enhance the UX. 

## How to run the Project
1. This project is deployed on: http://grynow.ap-south-1.elasticbeanstalk.com/
2. If you want to run it locally, there can be two ways:
   1. First, you need to clone the code.
   2. Then you need .env file which would be shared on request.
   3. Now, If you have docker installed, simply run below command.
       > $ docker-compose up --build
   4. If you don't have docker, follow the given steps.
      1. > $ pip install -r requirements.txt
      2. > $ python3 app.py
      3. You can make changes in .env if you feel so.
   5. To check if the server is running or not, either click [here](http://localhost:8080/test) or run the given command:
        > $ curl http://localhost:8080/test
        

## Docs
I have added Swagger Documentation as well, [local docs](http://localhost:8080/api-docs), [production docs](http://grynow.ap-south-1.elasticbeanstalk.com/api-docs/)


## Create a third party custom app

If you want to create a third party custom app, you can do that by making a POST request at `http://grynow.ap-south-1.elasticbeanstalk.com/apps/create`
with given dummy request body
```JSON
[{
    "name": "App 1",
    "description": "This is the first custom app.",
    "category": "Category 1",
    "images": [
        "<img_url>",
        "<img_url>"
    ],
    "display_image": "<img_url>",
    "form_fields": [
        {
            "label": "Field 1",
            "type": "text",
            "required": true,
            "meta": {
                "max_length": 90,
                "min_length": 5
            },
            "name": "name",
            "placeholder": "Enter name"
        },
        {
            "label": "Field 2",
            "type": "number",
            "name": "age",
            "required": false,
            "helper_text": "Input a number in this field"
        }
    ],
    "published": true,
    "app_info": {
        "developer": "Developer 1"
    }
}]
```

## Other Functionalities

1. Get All Custom Apps + User Apps
    > $ http://grynow.ap-south-1.elasticbeanstalk.com/apps/
    
2. Configure a custom app for yourself.
    > $ http://grynow.ap-south-1.elasticbeanstalk.com/apps/create
    

