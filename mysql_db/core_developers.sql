CREATE DATABASE core_developers;
use core_developers;

CREATE TABLE developers(
  login VARCHAR(255) NOT NULL,
  core BOOLEAN
);

INSERT INTO developers
  (login, core)
VALUES
  ('chenkx1', true),
  ('chenkx2', true),
  ('chenkx3', true),
  ('chenkx4', true),
  ('chenkx5', true),
  ('chenkx6', true),
  ('chenkx7', true),
  ('chenkx8', true),
  ('chenkx9', true),
  ('chenkx10', true),
  ('chenkx11', true),
  ('murry1', false),
  ('murry2', false),
  ('murry3', false),
  ('murry4', false),
  ('murry5', false),
  ('murry6', false),
  ('murry7', false),
  ('murry8', false),
  ('murry9', false),
  ('murry10', false),
  ('murry11', false);
