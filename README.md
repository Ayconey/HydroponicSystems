# HydroponicSystems
![HydroponicSystem](gardening.jpg)
API for creating and managing hydroponic systems by users.

Users can:

- Register
- Log in
- Create/Update/Delete their hydroponic systems.
- Add/Update/Delete measurement data from their existing hydroponic systems.
- Retrieve information about their systems and measurements.

# Accessing the Application
The application can be downloaded or accessed through the browser at [Here](http://project-hydro.mateuszsobiech.com:8000/) .
## Local Installation
1. Download the GitHub repository.
2. If you don't have Docker Desktop, download it.
3. Run Docker Desktop.
4. Open the console in the project's root folder (where the docker-compose file is located).
5. In the console, type: docker-compose up.

After this step, a PostgreSQL database should be set up at localhost:5432 along with the API application at localhost:8000.

# Description of Endpoints
The entire description is provided under localhost.
## Login and Registration
User authentication and authorization are done using dj_rest_auth.

- Registration is at the endpoint: localhost:8000/auth/registration/.
To create an account, you need to provide a unique username, (optional) email, and password twice. After successful registration, you receive an authentication token.
- Login is at the endpoint: localhost:8000/auth/login/. To log in, you need to provide the username, email (optional), and password.
## Hydroponic System
- List of user's hydroponic systems and adding a new system: localhost:8000/hydro/hydro-systems/
- Updating, deleting, displaying system details along with the 10 latest measurements: localhost:8000/hydro/hydro-systems/[your system's id]/
## Measurements
- Adding measurements to your system and displaying all measurements: localhost:8000/hydro/hydro-systems/[your system's id]/measurements/
- Deleting and updating a measurement from your system: localhost:8000/hydro/measurements/[your measurement's id]/
## Documentation
Documention is at localhost:8000/api-docs/ .
