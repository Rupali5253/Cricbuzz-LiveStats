-- ===========================================
-- Cricbuzz Live Analytics Database Schema
-- ===========================================

CREATE TABLE IF NOT EXISTS matches (

    match_id INTEGER PRIMARY KEY,
    series_id INTEGER,

    series_name VARCHAR(255),
    match_desc VARCHAR(100),
    match_format VARCHAR(50),
    match_type VARCHAR(50),

    start_date TIMESTAMP,
    end_date TIMESTAMP,

    state VARCHAR(50),
    state_title VARCHAR(50),
    status TEXT,

    team1_id INTEGER,
    team1 VARCHAR(100),

    team2_id INTEGER,
    team2 VARCHAR(100),

    ground VARCHAR(255),
    city VARCHAR(100),
    timezone VARCHAR(100),

    curr_bat_team_id INTEGER,

    team1_runs INTEGER,
    team1_wickets INTEGER,
    team1_overs DECIMAL(5,2),

    team2_runs INTEGER,
    team2_wickets INTEGER,
    team2_overs DECIMAL(5,2)
);

CREATE TABLE IF NOT EXISTS match_history (

    history_id SERIAL PRIMARY KEY,

    fetch_time TIMESTAMP,

    match_id INTEGER,

    team1 VARCHAR(100),
    team2 VARCHAR(100),

    team1_runs INTEGER,
    team1_wickets INTEGER,
    team1_overs DECIMAL(5,2),

    team2_runs INTEGER,
    team2_wickets INTEGER,
    team2_overs DECIMAL(5,2),

    status TEXT,

    CONSTRAINT unique_history UNIQUE (

        match_id,

        team1_runs,
        team1_wickets,
        team1_overs,

        team2_runs,
        team2_wickets,
        team2_overs,

        status

    )

);
CREATE TABLE match_history (

    history_id SERIAL PRIMARY KEY,

    fetch_time TIMESTAMP,

    match_id BIGINT,

    team1 VARCHAR(100),
    team2 VARCHAR(100),

    team1_runs INTEGER,
    team1_wickets INTEGER,
    team1_overs NUMERIC,

    team2_runs INTEGER,
    team2_wickets INTEGER,
    team2_overs NUMERIC,

    status VARCHAR(200)
);