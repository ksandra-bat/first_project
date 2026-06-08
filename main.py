from dotenv import load_dotenv
import os

# Загружаем переменные из локального файла .env
load_dotenv()

def print_author():
	author=os.getenv("AUTHOR")
	print(f"Автор проекта: {author}")

if __name__=="__main__":
	print_author()
