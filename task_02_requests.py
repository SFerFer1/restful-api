#!/usr/bin/python3
import requests
import csv
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(f"Title: {post['title']}")
        else:
            print("Hubo un error al obtener los posts.")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        post_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:

            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            

            writer.writeheader()
            

            writer.writerows(post_data)
        
        print("Datos guardados en 'posts.csv'.")
    else:
        print(f"Error al obtener los posts. Código de estado: {response.status_code}")

fetch_and_print_posts()
fetch_and_save_posts()