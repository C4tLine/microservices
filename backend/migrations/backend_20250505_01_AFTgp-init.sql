-- Init
-- depends: 

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS public."user"
(
    id uuid NOT NULL,
    username character varying(50) COLLATE pg_catalog."default" NOT NULL DEFAULT ''::character varying,
    given_name character varying(50) COLLATE pg_catalog."default" NOT NULL DEFAULT ''::character varying,
    family_name character varying(50) COLLATE pg_catalog."default" NOT NULL DEFAULT ''::character varying,
    enabled boolean NOT NULL DEFAULT false,
    CONSTRAINT user_pkey PRIMARY KEY (id),
    CONSTRAINT user_username_key UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS public.channel
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    channel character varying(50) COLLATE pg_catalog."default" NOT NULL DEFAULT ''::character varying,
    title character varying(255) COLLATE pg_catalog."default" NOT NULL DEFAULT ''::character varying,
    "default" boolean NOT NULL DEFAULT false,
    CONSTRAINT channel_pkey PRIMARY KEY (id),
    CONSTRAINT channel_channel_key UNIQUE (channel)
);

CREATE TABLE IF NOT EXISTS public.user_channel
(
    user_id uuid NOT NULL,
    chan_id bigint NOT NULL,
    can_publish boolean NOT NULL DEFAULT false,
    CONSTRAINT user_chat_pkey PRIMARY KEY (user_id, chan_id),
    CONSTRAINT user_chat_chan_id_fkey FOREIGN KEY (chan_id)
        REFERENCES public.channel (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT user_chat_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
);
