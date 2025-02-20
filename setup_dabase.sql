CREATE USER gov_transparency_hub_api WITH PASSWORD 'secret' LOGIN;

GRANT ALL PRIVILEGES ON ALL TABLES 
IN SCHEMA public TO gov_transparency_hub_api;