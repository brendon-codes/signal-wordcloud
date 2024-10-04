--
-- Extract Signal messages from SQLite
--
SELECT
  m.body
FROM
  messages as m
INNER JOIN
  conversations as c on c.id = m.conversationId
WHERE
  c.name = 'My Group' AND
  m.body IS NOT NULL
;
