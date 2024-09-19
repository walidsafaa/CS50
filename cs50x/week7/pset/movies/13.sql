SELECT name FROM people WHERE id IN
(SELECT person_id FROM stars WHERE movie_id IN
(SELECT movies.id
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE stars.person_id IN (SELECT id FROM people WHERE name = 'Kevin Bacon' and birth = 1958)))
AND
name != 'Kevin Bacon'
ORDER BY name
