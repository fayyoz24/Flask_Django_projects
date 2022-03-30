-- Question 1 : 
-- Select film title description and release year join category table.
-- Name column names with table name by using snake case.

SELECT
	category.name as category,
	film.title as  film_title,
	description as film_description,
	film.release_year as release_year
FROM film_category 
	JOIN film ON film_category.film_id=film.film_id
	JOIN category ON film_category.category_id=category.category_id;

-- Question 2 : 
-- Select customer and their address join country and city tables
-- Name column names with table name by using snake case.



SELECT 
	customer.first_name as customer_name,
	customer.last_name as customer_last_name,
	address.address,
	address.district,
	city.city,
	country.country
	FROM customer
	JOIN address ON customer.address_id = address.address_id
	JOIN city ON city.city_id = address.city_id
	JOIN country ON city.country_id = country.country_id


-- Question 3 : 
-- Select all payments info including staff info, customer info and rental info.
-- Name column names with table name by using snake case.

SELECT 
	film.title as film_title,
	staff.first_name as staff_first_name,
	staff.last_name as staff_last_name,
	customer.first_name as customer_first_name,
	customer.last_name as customer_last_name,
	amount,
	payment_date
	FROM payment
	JOIN staff ON payment.staff_id = staff.staff_id
	JOIN customer ON payment.customer_id = customer.customer_id
	JOIN rental ON payment.rental_id = rental.rental_id
	JOIN inventory ON rental.inventory_id = inventory.inventory_id
	JOIN film ON inventory.film_id = film.film_id


-- Question 4 : 
-- Select all the actors and films and join them
-- Name column names with table name by using snake case.
-- HINT : You need to use groupby


SELECT
	film.title AS film_title,
	actor.first_name AS actor_first_name,
	actor.last_name AS actor_last_name
FROM 
	film_actor
	JOIN actor ON film_actor.actor_id=actor.actor_id
	JOIN film ON film_actor.film_id=film.film_id
	GROUP BY actor.actor_id,film.film_id



-- Question 5 : 

-- Select all the stores with addresses and manager staff name last name.


SELECT 
	staff.first_name as staff_first_name,
	staff.last_name as staff_last_name,
	address.address,
	address.district,
	city.city,
	country.country
	FROM store
	JOIN address ON store.address_id = address.address_id
	JOIN city ON city.city_id = address.city_id
	JOIN country ON city.country_id = country.country_id
	JOIN staff ON store.manager_staff_id = staff.staff_id


-- Question 6 : 
-- In this store every worker receives 1500 $ base salary
-- After the 5000th movie, they get a bonus of 0.1 euro for every movie they rent.
-- Calculate total bonus that is received by staff members and join their names and last_names

SELECT 
	staff.first_name as staff_first_name,
	staff.last_name as staff_last_name,
	((SUM(staff.staff_id)-5000)*0.1) as bonus
	FROM payment 
	JOIN staff ON payment.staff_id = staff.staff_id
	GROUP BY staff.staff_id
