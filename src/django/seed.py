import os
import time
import sys
import random
import json
import logging
sys.path.append('/django')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hobbyist.settings")
import django
django.setup()

from django import db
from django.contrib.auth import get_user_model
from hobbyist.api import models, views


def seed_projects():

    projects = [
        {"title": "Alert light on adjustable height desks",
            "description": "My desk has adjustable height! Great, except I forget to use it. I want the table to automatically adjust every hour so I'm forced to stand.",
            "karma": 11
         },
        {"title": "Hobbyist - a platform for hobby-project collabs",
            "description": "Wow this is meta. Anyway, I could use some help developing this site. Looking for people who know React + Redux, hold the Redux. I also need users, but who doesn't amirite.",
            "karma": 234},
        {"title": "Monitoring system for hurricanes", "description": "I have like 200 barometer sensors for arduinos, don't ask how I got them. But I thought 'hey this is cool, I could build something with this'. Will start project with one member and a good idea, please leave a comment on what I should do :)",
         "karma": 32},
        {"title": "Smart mirror, facial recognition and voice control",
            "description": "I basically want to feel like Iron Man every morning. That's it.",
            "karma": 99},
        {"title": "WYSIWYG angular application", "description": "We all know the feeling of writing YET ANOTHER ANGULAR APPLICATION and those damn components and all that boilerplate code ARGH. Let's make this better, we can do it. Prefer people with 32 years experience in Angular 12.",
         "karma": -3},
    ]

    for item in projects:
        rand_user = random.choice(get_user_model().objects.all())
        new_item = models.Project(
            title=item['title'], description=item['description'], karma=item['karma'], owner=rand_user)
        new_item.save()

        for i in range(random.randint(0, 3)):
            if i > 0:
                rand_user = random.choice(
                    get_user_model().objects.exclude(pk=rand_user.pk))
                new_item.participants.add(rand_user)


def seed_users():
    users = [
        {"name": "Charles Babbage",
            "bio": "A mathematician, philosopher, inventor and mechanical engineer. Built first computer"},
        {"name": "Linus Torvalds", "bio": "Principal developer of the Linux kernel, which became the kernel for operating systems such as the Linux operating systems, Android, and Chrome OS. Also, Git."},
        {"name": "Grace Hopper", "bio": "Popularized the idea of machine-independent programming languages, which led to the development of COBOL. I think programming languages should be more like English; human readable."},
        {"name": "Satoshi Nakamoto",
            "bio": "Author of bitcoin white-paper, and pioneer of blockchain databases."}
    ]

    for user in users:
        User = get_user_model()
        User.objects.create_user(
            username=user['name'], bio=user['bio'], email="", password="qwe", kudos=random.randint(0, 500))


def seed_project_comments():
    comments = [
        "this project looks great, good job, proud of you",
        "have you considered the flux-capacitor problem? looks like a cool project!",
        "first",
        "I'll have you know I am specialized in gorilla warfare",
        "don't take this personally, but I don't like it... I LOVE IT!",
    ]

    for item in comments:
        rand_proj = random.choice(models.Project.objects.all())
        rand_user = random.choice(get_user_model().objects.all())
        new_item = models.ProjectComment(
            project=rand_proj, commenter=rand_user, text=item)
        new_item.save()


def seed():
    User = get_user_model()
    User.objects.create_superuser(
        username='root', email='', password='qwe')

    seed_users()
    seed_projects()
    seed_project_comments()


logging.info("Starting seed")
start_time = time.monotonic()
seed()
elapsed_time = time.monotonic() - start_time
logging.info("Seeding complete")
logging.info(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
