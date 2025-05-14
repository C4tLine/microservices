-- can_subscribe
-- depends: backend_20250505_01_AFTgp-init

ALTER TABLE public.user_channel ADD COLUMN can_subscribe boolean NOT NULL DEFAULT TRUE;
