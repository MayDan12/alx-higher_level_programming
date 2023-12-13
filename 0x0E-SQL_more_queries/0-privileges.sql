-- This script lists al privilegeds
-- of trhe MySQL users
SELECT *
FROM information_schema.USER_PRIVILEGES
WHERE GRANTEE = 'user_0d_1@localhost' OR GRANTEE = 'user_0d_2@localhost';
