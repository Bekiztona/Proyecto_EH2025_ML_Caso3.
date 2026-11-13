from pathlib import Path
import duckdb
import pyreadstat

def load_and_join(discrimination_path, person_path, staging_dir="outputs/staging"):
    """Read SAV files, stage as Parquet, then join using DuckDB.

    SAV decoding initially requires memory. Parquet staging lets DuckDB scan
    columnar files for the join rather than registering two full pandas frames.
    """
    staging = Path(staging_dir)
    staging.mkdir(parents=True, exist_ok=True)
    disc, meta_disc = pyreadstat.read_sav(discrimination_path, apply_value_formats=False)
    disc_path = staging / "discriminacion.parquet"
    disc.to_parquet(disc_path, index=False)
    del disc
    person, meta_person = pyreadstat.read_sav(person_path, apply_value_formats=False)
    person_parquet = staging / "persona.parquet"
    person.to_parquet(person_parquet, index=False)
    del person
    con = duckdb.connect()
    sql = f"""
    SELECT d.*, p.s01a_02, p.s01a_03, p.s01a_09, p.s01a_08, p.s01a_10
    FROM read_parquet('{disc_path.as_posix()}') d
    LEFT JOIN read_parquet('{person_parquet.as_posix()}') p
      ON CAST(d.folio AS VARCHAR) = CAST(p.folio AS VARCHAR)
     AND CAST(d.nro AS INTEGER) = CAST(p.nro AS INTEGER)
    """
    joined = con.execute(sql).df()
    return joined, meta_disc, meta_person
