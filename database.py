import mysql.connector
from mysql.connector import Error
import hashlib
from datetime import datetime
import os
import sys
import pandas as pd

class Database:

    def __init__(self):

        self.conn = None
        self.cursor = None

        self.connect()

        if self.cursor is not None:
            self.create_tables()

    # ==========================================
    # CONNECT
    # ==========================================

    def connect(self):

        try:

            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="080510",
                database="finance_ai"
            )

            if self.conn.is_connected():

                self.cursor = self.conn.cursor()

                print("Database Connected")

        except Error as e:

            print("Database Error:", e)

            self.conn = None
            self.cursor = None

    # ==========================================
    # CREATE TABLES
    # ==========================================

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS users(

            id INT AUTO_INCREMENT PRIMARY KEY,

            fullname VARCHAR(100),

            username VARCHAR(50) UNIQUE,

            email VARCHAR(100) UNIQUE,

            password VARCHAR(255),

            created_at DATETIME

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS transactions(

            id INT AUTO_INCREMENT PRIMARY KEY,

            user_id INT,

            date DATE,

            category VARCHAR(100),

            type VARCHAR(20),

            amount DOUBLE,

            description TEXT,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE

        )

        """)

        self.conn.commit()

    # ==========================================
    # HASH PASSWORD
    # ==========================================

    def hash_password(self, password):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    # ==========================================
    # REGISTER
    # ==========================================

    def register_user(
        self,
        fullname,
        username,
        email,
        password
    ):

        if self.cursor is None:
            return False

        password = self.hash_password(password)

        sql = """
        INSERT INTO users(
            fullname,
            username,
            email,
            password,
            created_at
        )
        VALUES(%s,%s,%s,%s,%s)
        """

        values = (
            fullname,
            username,
            email,
            password,
            datetime.now()
        )

        try:

            self.cursor.execute(sql, values)

            self.conn.commit()

            return True

        except Error as e:

            print(e)

            return False

    # ==========================================
    # LOGIN
    # ==========================================

    def login_user(
        self,
        username,
        password
    ):

        if self.cursor is None:
            return None

        password = self.hash_password(password)

        sql = """
        SELECT *
        FROM users
        WHERE username=%s
        AND password=%s
        """

        try:

            self.cursor.execute(
                sql,
                (
                    username,
                    password
                )
            )

            return self.cursor.fetchone()

        except Error as e:

            print(e)

            return None
    # ==========================================
    # ADD TRANSACTION
    # ==========================================

    def add_transaction(
        self,
        user_id,
        date,
        category,
        trans_type,
        amount,
        description
    ):

        if self.cursor is None:
            return False

        sql = """
        INSERT INTO transactions(
            user_id,
            date,
            category,
            type,
            amount,
            description
        )
        VALUES(%s,%s,%s,%s,%s,%s)
        """

        try:

            self.cursor.execute(
                sql,
                (
                    user_id,
                    date,
                    category,
                    trans_type,
                    amount,
                    description
                )
            )

            self.conn.commit()

            return True

        except Error as e:

            print(e)

            return False

    # ==========================================
    # GET TRANSACTIONS
    # ==========================================

    def get_transactions(self, user_id):

        if self.cursor is None:
            return []

        sql = """
        SELECT *
        FROM transactions
        WHERE user_id=%s
        ORDER BY date DESC
        """

        self.cursor.execute(sql, (user_id,))

        return self.cursor.fetchall()

    # ==========================================
    # UPDATE TRANSACTION
    # ==========================================

    def update_transaction(
        self,
        trans_id,
        date,
        category,
        trans_type,
        amount,
        description
    ):

        if self.cursor is None:
            return False

        sql = """
        UPDATE transactions
        SET
            date=%s,
            category=%s,
            type=%s,
            amount=%s,
            description=%s
        WHERE id=%s
        """

        try:

            self.cursor.execute(
                sql,
                (
                    date,
                    category,
                    trans_type,
                    amount,
                    description,
                    trans_id
                )
            )

            self.conn.commit()

            return True

        except Error as e:

            print(e)

            return False

    # ==========================================
    # DELETE TRANSACTION
    # ==========================================

    def delete_transaction(self, trans_id):

        if self.cursor is None:
            return False

        try:

            self.cursor.execute(
                "DELETE FROM transactions WHERE id=%s",
                (trans_id,)
            )

            self.conn.commit()

            return True

        except Error as e:

            print(e)

            return False

    # ==========================================
    # DASHBOARD
    # ==========================================

    def total_income(self, user_id):

        self.cursor.execute(
            """
            SELECT IFNULL(SUM(amount),0)
            FROM transactions
            WHERE user_id=%s
            AND type='Income'
            """,
            (user_id,)
        )

        return self.cursor.fetchone()[0]

    def total_expense(self, user_id):

        self.cursor.execute(
            """
            SELECT IFNULL(SUM(amount),0)
            FROM transactions
            WHERE user_id=%s
            AND type='Expense'
            """,
            (user_id,)
        )

        return self.cursor.fetchone()[0]

    def balance(self, user_id):

        return self.total_income(user_id) - self.total_expense(user_id)

    # ==========================================
    # CLOSE
    # ==========================================

    def close(self):

        if self.cursor is not None:
            self.cursor.close()

        if self.conn is not None:
            self.conn.close()
# ==========================================
# GET TRANSACTIONS
# ==========================================

def get_transactions(self, user_id):

    if self.cursor is None:
        return []

    sql = """
    SELECT *
    FROM transactions
    WHERE user_id=%s
    ORDER BY date DESC
    """

    self.cursor.execute(sql, (user_id,))
    return self.cursor.fetchall()

# ==========================================
# UPDATE TRANSACTION
# ==========================================

def update_transaction(
    self,
    trans_id,
    date,
    category,
    trans_type,
    amount,
    description
):

    if self.cursor is None:
        return False

    sql = """
    UPDATE transactions
    SET
        date=%s,
        category=%s,
        type=%s,
        amount=%s,
        description=%s
    WHERE id=%s
    """

    try:
        self.cursor.execute(
            sql,
            (date, category, trans_type, amount, description, trans_id)
        )

        self.conn.commit()
        return True

    except Error as e:
        print(e)
        return False
    
# ==========================================
# DELETE TRANSACTION
# ==========================================

def delete_transaction(self, trans_id):

    if self.cursor is None:
        return False

    try:
        self.cursor.execute(
            "DELETE FROM transactions WHERE id=%s",
            (trans_id,)
        )

        self.conn.commit()
        return True

    except Error as e:
        print(e)
        return False
    
# ==========================================
# DASHBOARD
# ==========================================

def total_income(self, user_id):

    self.cursor.execute("""
        SELECT IFNULL(SUM(amount),0)
        FROM transactions
        WHERE user_id=%s AND type='Income'
    """, (user_id,))

    return self.cursor.fetchone()[0]


def total_expense(self, user_id):

    self.cursor.execute("""
        SELECT IFNULL(SUM(amount),0)
        FROM transactions
        WHERE user_id=%s AND type='Expense'
    """, (user_id,))

    return self.cursor.fetchone()[0]


def balance(self, user_id):
    return self.total_income(user_id) - self.total_expense(user_id)

# ==========================================
# CLOSE
# ==========================================

def close(self):

    if self.cursor is not None:
        self.cursor.close()

    if self.conn is not None:
        self.conn.close()