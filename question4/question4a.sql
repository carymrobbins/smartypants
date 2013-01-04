CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) UNIQUE
);

CREATE TABLE contact (
    id SERIAL PRIMARY KEY,
    email VARCHAR(256),
    company_id INTEGER REFERENCES company (id)
);

CREATE INDEX idx_contact_company_id ON contact (company_id);
