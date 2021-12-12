from database_connection import get_database_connection


def drop_tables(connection):
    """Tuhoaa tietokantataulun mikäli sellainen löytyy

    Args:
        connection: Connection-olio tietokantayhteyttä varten
    """

    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists budget;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulun

    Args:
        connection: Connection-olio tietokantayhteyttä varten
    """
    
    cursor = connection.cursor()

    cursor.execute('''
        create table budget (
            item_id int primary key,
            amount float,
            item_type int,
            desc text
        );
    ''')

    connection.commit()


def initialize_database():
    """Tietokannan alustus
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()