# BrewBuddy

This application simplifies the management of homemade brews while also providing access to a wide range of brews crafted by other users.


## About the User <!-- This is a scaled down user persona -->
- The target audience for this application primarily consists of homebrewing enthusiasts who seek seamless management of their brewing endeavors. These users are individuals dedicated to crafting their own alcoholic beverages and desire a user-friendly solution to         streamline the organization of their homebrews.
- This app streamlines the management of brewing batches, enabling users to effortlessly document and replicate their previous brews. It also serves as a platform for users to draw inspiration from each other's brews when crafting new recipes.

## Features <!-- List your app features using bullets! Do NOT use a paragraph. No one will read that! -->
- Create brews with personalized details including name, description, image, stage, and categories.
- Access individual brew logs for each brew, allowing users to create, delete, and edit logs as required.
- Explore a variety of brews crafted by other users within the community.

## To get the App setup

1. Set up a [Firebase](https://firebase.google.com/) project with just Authentication - Here's how: [Firebase Setup & Authentication](https://www.loom.com/share/163ffe1539bb482196efa713ed6231e9)

2. Clone BrewBuddy-Server to your local machine
``` bash
git@github.com:Mason-Austin/brewbuddy-server.git
```

2. Move into directory
``` bash
cd BrewBuddy-Server
```
5. Be in the root directory and from your command line, run
``` bash
pipenv install django=='4.1.3' autopep8=='2.0.0' pylint=='2.15.5' djangorestframework=='3.14.0' django-cors-headers=='3.13.0' pylint-django=='2.5.3'
```
6. Select Python Interpreter
Open VS Code and press ⌘SHIFTP (Mac), or CtrlSHIFTP (Windows) to open the Command Palette, and select "Python: Select Interpreter".

Find the option that has:

<YOUR_FOLDER_NAME>-<RANDOM_STRING>

7. Pylint Settings for Django
   There should now be a .vscode folder in your directory. If there is not one, create it. Create/open the settings.json file and add the following lines:
``` bash
{
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--django-settings-module=brewbuddy.settings",
    ],
}
```
5. Create Base Django Tables
   Inside the .vscode create a file called launch.json. Paste the following code in that file.
``` bash
python manage.py migrate
```
5. Running the Django Server
``` bash
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true,
            "autoReload":{
                "enable": true
            }
        }
    ]
}
```
8. Run your server(You can also use F5)
``` bash
python manage.py runserver
```
10. Make sure the client side is setup as well. Enjoy!
## Relevant Links <!-- Link to all the things that are required outside of the ones that have their own section -->
- [Wireframes](https://www.figma.com/file/sDoylO5F3Bj4uGVKj9uiEZ/BrewBuddy?type=whiteboard&node-id=0-1&t=C0d58Pbr9NtLLnBS-0)
- [ERD](https://dbdiagram.io/d/Brew-Buddy-65cab807ac844320aeff0b4c)
- [Project Board](https://github.com/users/Mason-Austin/projects/5)
- [BrewBuddy-Client](https://github.com/Mason-Austin/brewbuddy-client)

<!-- ## Project Screenshots These can be inside of your project. Look at the repos from class and see how the images are included in the readme <img width="1148" alt="Your Alt" src="your-link.png"> -->

## Contributors
- [Mason Austin](https://github.com/Mason-Austin)
