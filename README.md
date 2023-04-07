


# Casting Agency API
## Motivation for the project
The Casting Agency API was created as part of the Udacity Full Stack Web Developer Nanodegree Capstone Project. The project aims to demonstrate the skills and knowledge gained throughout the course, particularly in developing and deploying web applications using Flask and SQLAlchemy.


## Project dependencies
The project has the following dependencies:

* Python 3.7 or higher
* Flask 2.0.1 or higher
* Flask-Migrate 3.1.0 or higher
* Flask-Cors 3.0.10 or higher
* SQLAlchemy 1.4.26 or higher
* psycopg2-binary 2.9.1 or higher
* pytest 6.2.5 or higher
* coverage 6.2 or higher

## Documentation of API behavior and RBAC controls
The Casting Agency API is a RESTful API that allows users to perform CRUD operations on movies and actors. It has the following endpoints:

## GET /actors
* Returns a list of actors.
* Requires the `read:actors` permission.
* Returns status code 200 and a JSON object with a `success` key and an `actors` key containing an array of actors on success.
* Sample request: `curl https://my-casting-agency-api.com/actors -H "Authorization: Bearer <access_token>"`

## POST /actors
* Adds a new actor to the database.
* Requires the `create:actors` permission.
* Returns status code 200 and a JSON object with a `success` key and an `actor` key containing the name of the added actor on success.
* Sample request: `curl -X POST https://my-casting-agency-api.com/actors -H "Authorization: Bearer <access_token>" -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 35, "gender": "Male"}'`

## PATCH /actors/{actor_id}
Updates an existing actor in the database.
* Requires the `update:actors` permission.
* Returns status code 200 and a JSON object with a `success` key and an `actor` key containing the updated actor's details on success.
* Sample request: `curl -X PATCH https://my-casting-agency-api.com/actors/1 -H "Authorization: Bearer <access_token>" -H "Content-Type: application/json" -d '{"name": "Jane Doe"}'`

## DELETE /actors/{actor_id}
Deletes an existing actor from the database.
* Requires the `delete:actors` permission.
* Returns status code 200 and a JSON object with a `success` key and an `actor` key containing the name of the deleted actor on success.
* Sample request: `curl -X DELETE https://my-casting-agency-api.com/actors/1 -H "Authorization: Bearer <access_token>"`

## GET /movies
* Returns a list of `movies`.
* Requires the `read:movies` permission.
* Returns status code 200 and a JSON object with a `success` key and a `movies` key containing an array of movies on success.
* Sample request: `curl https://my-casting-agency-api.com/movies -H "Authorization: Bearer <access_token>"`

## POST /movies
Adds a new movie to the database.
* Requires the *create:movies* permission.
* Returns status code 200 and a JSON object with a `success` key and a `movie` key containing the title of the added movie on success.
Sample request: `curl -X POST http://localhost:5000/movies -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" -d '{"title": "The Shawshank Redemption", "release_date": "1994-10-14"}'`



## Instructions to set up authentication

### to set up an authentication toy will need to login through this link.
link: https://iamn.us.auth0.com/authorize?audience=fsnd&response_type=token&client_id=XBzjkx6BmwQgU1xwHZCG4Hvg2qE4KcaU&redirect_uri=https://fsnd-capstone.onrender.com/login-success

get token from here.


but the issue is how would you assign role and permissions to newly signedup users.

so for this reason i already created three users with three different roles and permissions.

here is their details:

email = hasawit538@mitigado.com    password = @test123      role = Casting Assistant    token = eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRhbWNjNlM1VElaUl9vMXl5Tk4xdiJ9.eyJpc3MiOiJodHRwczovL2lhbW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0MmU4YTAzMzU5NWQwNTgwZWUzMmNjNSIsImF1ZCI6ImZzbmQiLCJpYXQiOjE2ODA3NzcwODcsImV4cCI6MTY4MDg2MzQ4NywiYXpwIjoiWEJ6amt4NkJtd1FnVTF4d0haQ0c0SHZnMnFFNEtjYVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.JF9AWyqXh_T6gxD56bL8RRllehkHptBlO0pn5Pl-KWuBG7UKg6NKbiYLtGXCUa4TyOs8IAWUzwTbC9A_8ys2HlB-TAOD0xoEUDTj1BX7jObI7u_G1AvqxfdR4t2Iz6PiprMph4-4DV3dZ_kzhv4gozPZzjgJVAfx8m2S5-XnIzGoqR6_r1_usOupkDAS13y_CuVv2nh7sA4EQV34CnDihRw7S-5Mm9vzPa1tbS_3E5DQjCvbcxXZXko2Mf2cXysQ3NNnbZza8OWCK7cSaiPm93edT3IX_1GYZlLkXVxClIeJytmbw8doVI8fXnQ6F-pfBTkMjqnCkzQ4YERtU0gdzQ


email = vohes12958@mitigado.com   password = @test213     role = Casting Director     token = eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRhbWNjNlM1VElaUl9vMXl5Tk4xdiJ9.eyJpc3MiOiJodHRwczovL2lhbW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0MmU4YmI2NTNlOWZiMjQ5Mjg4NzVkNyIsImF1ZCI6ImZzbmQiLCJpYXQiOjE2ODA3NzcxNTAsImV4cCI6MTY4MDg2MzU1MCwiYXpwIjoiWEJ6amt4NkJtd1FnVTF4d0haQ0c0SHZnMnFFNEtjYVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.QnHmgXfz5WPMUpl0MmLnBq-9BItK2FPWK2w8Al0X6GHRl8DFVZ3iW0Rgllb0Z-r5PBjXQ-x4tLkXTCBP7FLbzM-NgML0BAypbNwE4-5CIdm3KQHVpBef-tAvt1HqAcoe0DIlPT1h0QZ5fTGu5VEHhbvBNvPAqMPoEEngN3-qDrrbqqjgjgX1J0_jE3xVOaMcGC73LG8kvuj10CAHbdEPyi47DsuOCS4J6zjLX4bZlcr1hl9dnhS0EuNfTAx0OH5K43n7Dc0DMe_6_THSrmwpzzls6ewpUMMrVrxE3RHGq8X0PrBLXW-f8XIQiU6DHPEuWeaZvcIs4Qe1P2fJsOsNmw


email = hesowar704@dogemn.com      password = @test321     role = Executive Producer    token = eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRhbWNjNlM1VElaUl9vMXl5Tk4xdiJ9.eyJpc3MiOiJodHRwczovL2lhbW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0MmU4YzcxNTNlOWZiMjQ5Mjg4NzVmYiIsImF1ZCI6ImZzbmQiLCJpYXQiOjE2ODA3NzcyNDUsImV4cCI6MTY4MDg2MzY0NSwiYXpwIjoiWEJ6amt4NkJtd1FnVTF4d0haQ0c0SHZnMnFFNEtjYVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.EoTMY4GBxOnhjVVe5TjfKVZRP822EpUBF7gh9LOKZWlsJtr_mGAHRcsWfhqpj1zyP6k05bstbSQ85JYHMZuc9hCqDipDJAbd4einyIt7QJLLdc7bfnCRVSnWB_Mip-Yns4zPAGkOqqEdy1CMMmzS20v_Jpcve7jfusz0hbrhjqLEYjx4J-oK-tEiUeNpwe9hgLrfDKVOP0V7vlZnVYpFMTHLUFyMABY7vfXhmNuwpVqQMMXdK36CvoC4mTAUAQVxPI9jWFMQLb9jso5US3wKMyoqR2SRmopixgiJG7M1nd9fYhLEJZ1e5sbztd_Q_L3HWRgOxIz1V2UQfByrfvpFQQ

## these are .env
#### LiveURL = https://fsnd-capstone.onrender.com/


### AUTH0_DOMAIN="iamn.us.auth0.com"
### API_AUDIENCE="fsnd"
### ALGORITHMS=["RS256"]

### DATABASE_URL="postgresql://usman:MfoTvJXbYJnN4vHBEdWDocwGWObnaWRN@dpg-cgn6mpfdvk4k0104a04g-a.singapore-postgres.render.com/fsnd"

### ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRhbWNjNlM1VElaUl9vMXl5Tk4xdiJ9.eyJpc3MiOiJodHRwczovL2lhbW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0MmU4YTAzMzU5NWQwNTgwZWUzMmNjNSIsImF1ZCI6ImZzbmQiLCJpYXQiOjE2ODA3NzcwODcsImV4cCI6MTY4MDg2MzQ4NywiYXpwIjoiWEJ6amt4NkJtd1FnVTF4d0haQ0c0SHZnMnFFNEtjYVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.JF9AWyqXh_T6gxD56bL8RRllehkHptBlO0pn5Pl-KWuBG7UKg6NKbiYLtGXCUa4TyOs8IAWUzwTbC9A_8ys2HlB-TAOD0xoEUDTj1BX7jObI7u_G1AvqxfdR4t2Iz6PiprMph4-4DV3dZ_kzhv4gozPZzjgJVAfx8m2S5-XnIzGoqR6_r1_usOupkDAS13y_CuVv2nh7sA4EQV34CnDihRw7S-5Mm9vzPa1tbS_3E5DQjCvbcxXZXko2Mf2cXysQ3NNnbZza8OWCK7cSaiPm93edT3IX_1GYZlLkXVxClIeJytmbw8doVI8fXnQ6F-pfBTkMjqnCkzQ4YERtU0gdzQ'

### DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRhbWNjNlM1VElaUl9vMXl5Tk4xdiJ9.eyJpc3MiOiJodHRwczovL2lhbW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0MmU4YmI2NTNlOWZiMjQ5Mjg4NzVkNyIsImF1ZCI6ImZzbmQiLCJpYXQiOjE2ODA3NzcxNTAsImV4cCI6MTY4MDg2MzU1MCwiYXpwIjoiWEJ6amt4NkJtd1FnVTF4d0haQ0c0SHZnMnFFNEtjYVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.QnHmgXfz5WPMUpl0MmLnBq-9BItK2FPWK2w8Al0X6GHRl8DFVZ3iW0Rgllb0Z-r5PBjXQ-x4tLkXTCBP7FLbzM-NgML0BAypbNwE4-5CIdm3KQHVpBef-tAvt1HqAcoe0DIlPT1h0QZ5fTGu5VEHhbvBNvPAqMPoEEngN3-qDrrbqqjgjgX1J0_jE3xVOaMcGC73LG8kvuj10CAHbdEPyi47DsuOCS4J6zjLX4bZlcr1hl9dnhS0EuNfTAx0OH5K43n7Dc0DMe_6_THSrmwpzzls6ewpUMMrVrxE3RHGq8X0PrBLXW-f8XIQiU6DHPEuWeaZvcIs4Qe1P2fJsOsNmw'

### PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRhbWNjNlM1VElaUl9vMXl5Tk4xdiJ9.eyJpc3MiOiJodHRwczovL2lhbW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0MmU4YzcxNTNlOWZiMjQ5Mjg4NzVmYiIsImF1ZCI6ImZzbmQiLCJpYXQiOjE2ODA3NzcyNDUsImV4cCI6MTY4MDg2MzY0NSwiYXpwIjoiWEJ6amt4NkJtd1FnVTF4d0haQ0c0SHZnMnFFNEtjYVUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.EoTMY4GBxOnhjVVe5TjfKVZRP822EpUBF7gh9LOKZWlsJtr_mGAHRcsWfhqpj1zyP6k05bstbSQ85JYHMZuc9hCqDipDJAbd4einyIt7QJLLdc7bfnCRVSnWB_Mip-Yns4zPAGkOqqEdy1CMMmzS20v_Jpcve7jfusz0hbrhjqLEYjx4J-oK-tEiUeNpwe9hgLrfDKVOP0V7vlZnVYpFMTHLUFyMABY7vfXhmNuwpVqQMMXdK36CvoC4mTAUAQVxPI9jWFMQLb9jso5US3wKMyoqR2SRmopixgiJG7M1nd9fYhLEJZ1e5sbztd_Q_L3HWRgOxIz1V2UQfByrfvpFQQ'


