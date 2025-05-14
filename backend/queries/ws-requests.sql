-- name: GetUserByID :one
SELECT "id", "username", "given_name", "family_name", "enabled"
FROM "public"."user"
WHERE "id"=$1
;

-- name: CreateUser :exec
INSERT INTO "public"."user"
("id", "username", "given_name", "family_name", "enabled")
VALUES($1, $2, $3, $4, $5)
;

-- name: ChanListByUserID :many
SELECT "channel"."id", "channel"."channel", "channel"."title", "channel"."default"
FROM "public"."channel"
JOIN "public"."user_channel" ON "user_channel"."chan_id" = "channel"."id"
WHERE "user_channel"."user_id"=$1 AND "user_channel"."can_subscribe"='t';
;

-- name: UserListByChanID :many
SELECT "user"."id", "user"."username", "user"."given_name", "user"."family_name", "user"."enabled"
FROM "public"."user"
JOIN "public"."user_channel" ON "user_channel"."user_id" = "user"."id"
WHERE "user_channel"."chan_id"=$1
;

-- name: UserCanSubscribe :one
SELECT EXISTS (
    SELECT 1 
    FROM "public"."channel" c
    LEFT JOIN "public"."user_channel" uc ON uc."chan_id" = c."id" AND uc."user_id" = $1
    WHERE c."channel" = $2 
    AND (uc."can_subscribe" = true OR (uc."user_id" IS NULL AND c."default" = true))
) AS "can_subscribe";

-- name: UserCanPublish :one
SELECT EXISTS (
    SELECT 1 
    FROM "public"."channel" c
    JOIN "public"."user_channel" uc ON uc."chan_id" = c."id" AND uc."user_id" = $1
    WHERE c."channel" = $2 
    AND uc."can_publish" = true
) AS "can_publish";

-- name: SubscribeUserToChannel :exec
INSERT INTO user_channel (user_id, chan_id, can_publish)
SELECT $1, c.id, $3
FROM channel c
WHERE c.channel = $2
ON CONFLICT (user_id, chan_id) DO NOTHING;
