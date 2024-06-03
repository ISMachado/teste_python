import pandas as pd
from sqlalchemy.orm import Session
from database import engine, Data
from datetime import datetime, timedelta

def fetch_data(session: Session, start_date: str):
    query = session.query(Data).filter(
        Data.timestamp.between(f"{start_date}T00:00:00Z", f"{start_date}T23:59:59Z")
    )
    df = pd.read_sql(query.statement, session.bind)
    return df

def transform_data(df: pd.DataFrame):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')
    return df.resample('10T').agg(['mean', 'min', 'max', 'std'])

def load_data(session: Session, df: pd.DataFrame):
    for index, row in df.iterrows():
        data_entry = Data(
            timestamp=index,
            wind_speed=row[('wind_speed', 'mean')],
            power=row[('power', 'mean')],
            ambient_temperature=row[('ambient_temperature', 'mean')]
        )
        session.add(data_entry)
    session.commit()

def main():
    session = Session(bind=engine)
    try:
        start_date = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')
        df = fetch_data(session, start_date)
        transformed_df = transform_data(df)
        load_data(session, transformed_df)
    finally:
        session.close()

if __name__ == "__main__":
    main()
