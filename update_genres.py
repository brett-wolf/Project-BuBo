import requests
from bubo_db_connect import get_connection

API_URL = "https://api.watchmode.com/v1/genres/?apiKey=HmlwmzryJDuTfgiSb8i5Fl6C6j5Q8wxUkC4D0ZDV"
def update_genres():
    response = requests.get(API_URL)
    response.raise_for_status()
    genres = response.json()  # assume this returns a list of {id, name}

    with get_connection() as conn:
        with conn.cursor() as cur:
            for genre in genres:
                # Insert only if genre id doesn’t already exist
                cur.execute("""
                    INSERT INTO genres (genre_id, name, tmdb_id)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (genre_id) DO NOTHING;
                """, (genre["id"], genre["name"], genre["tmdb_id"]))
        conn.commit()

if __name__ == "__main__":
    update_genres()