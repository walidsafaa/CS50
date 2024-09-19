SELECT title FROM shows ORDER BY title;

UPDATE shows SET title = "Avatar: The Last Airbender" WHERE title LIKE "Avatar%";

UPDATE shows SET title = "Game of Thrones" WHERE title LIKE "%got%" or "Game Of%" or "Game of%";

UPDATE shows SET title = "The Bachelorette" WHERE title LIKE "the bachelorette%";

UPDATE [shows] SET title=UPPER(LEFT(title,1))+LOWER(SUBSTRING(title,2,LEN(title)))