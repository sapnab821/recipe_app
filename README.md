<h2>Overview</h2>
<p>
This project focuses on creating a web application using the Django framework. In this project, working with Python-based Django, a full-stack web application using the Django development server will be developed. The main focus of this project will be the backend with a light touch of styling on the frontend. The final web application will be dynamic and multi-user, letting users sign up and create their own content. It’ll also have statistical dashboards, implementing new data analytics and data visualization skills.
</p>

<br>

<h2>Features</h2>
<ul>
  <li>User Authentication, for secure user login system.</li>
  <li>Recipe Management, users can create recipes and upload images.</li>
  <li>Difficulty Calculation, the application calculates the difficulty of recipes based on cooking time and number of ingredients.</li>
  <li>Users can search for recipes</li>
</ul>

<h2>Tech Used</h2>
<ul>
<li>Django (5.0.7)</li>
<li>Pillow (10.4.0)</li>
<li>Black (formatting: 24.4.2)</li>
<li>Pandas (2.2.2)</li>
<li>matplotlib (3.9.1)</li>
<li>gunicorn (22.0.0)</li>
<li>dj-database-url (2.2.0)</li>
<li>psycopg2-binary (2.9.9)</li>
<li>WhiteNoise (6.7.0)</li>
</ul>

<h2>Set Up</h2>
<ul>
<li>Clone the repository.</li>
<li>Go to the recipe-app directory and execute make install-dev.</li>
<li>Configure the database for development by editing the DATABASES settings in dev.py within the settings folder.</li>
<li>Apply migrations using make dev-migrate.</li>
<li>Create a superuser by running make dev-superuser.</li>
<li>Start the app with make dev-start and view it in your browser at http://127.0.0.1:8000.</li>
</ul>
<br>
