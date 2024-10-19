from config.db import get_connection

def main():
    conn = get_connection()
    # Use a conexão aqui
    print("Conexão estabelecida com sucesso!")

if __name__ == "__main__":
    main()
