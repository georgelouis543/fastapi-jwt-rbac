A FastAPI App with JWT Authentication and Role-based Access Control

# **Pre-requisites:**

1. Make sure you have pgadmin4 installed on your system (if not already, please use this link to download: https://www.postgresql.org/download/).
2. Once you have installed pgadmin4, create a user and a password for your server (if you don't provide a user, the default would be postgres)
3. Please create a Database within the Postgresql server (Here's a screen-recording on how to do that: https://jam.dev/c/dba5ed09-a24b-4f42-9953-443ea84fb0f1)

# **How to Run the Project**

1. Clone the Repository to your local system
2. Add a .env file to your root folder (I have provided a .env.example file, whose variables you can use in your .env)
3. Edit the DATABASE_URL_LOCAL in your .env file in this format:
   1. Add your Database user to the URL string in place of {user} (if you are using the default user, it would be postgres)
   2. Add your password to the URL string in place of {password} (In case you entered a password with special characters, make sure you URL encode if when you are entering).
   3. Enter the database name you created in place of {db_name}.
   4. For example, if your password is test1234 and db_name is test-db, the final URL string would be: **postgresql+psycopg://postgres:test1234@127.0.0.1:5432/{db_name}**
4. Create a Virtual environment in the root folder of your project (not inside the app folder!) (please see this [link](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) on how to create virtual environments in Windows/macOS)
5. Activate the Virtual Environment 
6. Install all requirements (please ensure you have activated the virtual environment) using this command: `pip install -r requirements.txt` (pip3 if you're using macOS)
7. You can now run the app using this command: `fastapi dev app/main.py` (in a production environment this would be `fastapi run`)

# **How the App works**

1. Open the swagger UI on your browser at the address http://localhost:8000/docs
2. Register a user at the route `/auth/register`
   1. Enter a valid username, password, and a user_role (either user or admin -- this should not be the case in a production environment, but since it's the basic functionality in question, I have implemented it for simplicity)
   2. I have also added basic redundancy checks for usernames
3. You can now use The Authorize button (on the top right) to authenticate your credentials
4. Create one user with an admin role and one with user role
5. Try creating a Project at the `/project/create-projects` route
6. Try updating a project at the `/project/edit-project/{project_id}` route
7. Try deleting a project at the `/project/edit-project/{project_id}` route
8. Try doing the above for both user and admin roles (notice that only admins are allowed to perform the above actions)
9. Try viewing all existing projects at the `/project/projects` route (notice that both admins and users have access to this)

#### **Here's a video walkthrough on how this project works:** https://www.loom.com/share/4ff37445049a4e46b2b0658122209ac9