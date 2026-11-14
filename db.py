import json
import psycopg
from psycopg.rows import dict_row

DSN = "host=localhost port=5432 dbname=docbot user=docbot password=docbot"


def init_db() -> None:
    with psycopg.connect(DSN) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS extracted_documents (
                id BIGSERIAL PRIMARY KEY,
                source TEXT NOT NULL,
                doc_type TEXT NOT NULL,
                data JSONB NOT NULL,
                created_at TIMESTAMPTZ DEFAULT now()
            )
        """)
        conn.commit()


def save_extraction(source: str, doc_type: str, model) -> int:
    with psycopg.connect(DSN, row_factory=dict_row) as conn:
        row = conn.execute(
            "INSERT INTO extracted_documents (source, doc_type, data) "
            "VALUES (%s, %s, %s) RETURNING id",
            (source, doc_type, json.dumps(model.model_dump())),
        ).fetchone()
        conn.commit()
    return row["id"]


def list_recent(limit: int = 5):
    with psycopg.connect(DSN, row_factory=dict_row) as conn:
        return conn.execute(
            "SELECT id, source, doc_type, created_at FROM extracted_documents "
            "ORDER BY id DESC LIMIT %s",
            (limit,),
        ).fetchall()