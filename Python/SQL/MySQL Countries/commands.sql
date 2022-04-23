USE world;

-- 1. 

-- SELECT name, languages.language, languages.percentage 
-- FROM countries
-- JOIN languages ON countries.id = languages.country_id
-- WHERE languages.language = "Slovene"
-- ORDER BY languages.percentage DESC;

-- 2.

-- SELECT countries.name, COUNT(cities.country_id) AS Number_of_Cities
-- FROM countries
-- JOIN cities ON countries.id = cities.country_id
-- GROUP BY countries.name
-- ORDER BY Number_of_Cities DESC;

-- 3.

-- SELECT name, population
-- FROM cities
-- WHERE country_code = 'MEX' AND population >= 500000
-- ORDER BY population DESC;

-- 4.

-- SELECT name, languages.language, languages.percentage 
-- FROM countries
-- JOIN languages ON countries.id = languages.country_id
-- WHERE languages.percentage >= 89
-- ORDER BY languages.percentage DESC;

-- 5.

-- SELECT name, surface_area, population
-- FROM countries
-- WHERE surface_area <= 501 AND population >= 100000;

-- 6.

-- SELECT name, government_form, capital, life_expectancy
-- FROM countries
-- WHERE government_form = 'Constitutional Monarchy' AND capital >= 200 AND life_expectancy >= 75
-- ORDER BY name ASC;

-- 7. 

-- SELECT countries.name AS country, cities.name AS city, cities.district, cities.population
-- FROM countries
-- JOIN cities ON countries.id = cities.country_id
-- WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population >= 500000;

-- 8.

-- SELECT region, COUNT(countries.name)
-- FROM countries
-- GROUP BY region
-- ORDER BY COUNT(countries.name) DESC;

 
