SELECT title FROM movies WHERE id IN (
SELECT movies.id FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE stars.person_id = (SELECT id FROM people WHERE name = 'Bradley Cooper'))
AND id IN (SELECT movies.id FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE stars.person_id = (SELECT id FROM people WHERE name = 'Jennifer Lawrence'))