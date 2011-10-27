DROP TABLE things;

CREATE TABLE things (
    id serial PRIMARY KEY,
    name character varying(255)
);

INSERT INTO things (name) VALUES ('puppies');
INSERT INTO things (name) VALUES ('kittens');
INSERT INTO things (name) VALUES ('butterflies');
INSERT INTO things (name) VALUES ('ninja stars');
