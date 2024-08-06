from datetime import datetime, timedelta
from django.contrib.auth.models import User
from task.models import all_the_tasks  
import random

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def create_data():
    now = datetime.now()
    future = now + timedelta(days=15)
    past = now - timedelta(days=1)    

    titles = [
        "Complete Django project", "Write blog post", "Grocery shopping", 
        "Read book", "Exercise", "Meeting with team", "Doctor's appointment",
        "Client presentation", "Call with parents", "Plan weekend trip",
        "Finish online course", "Organize desk", "Backup files", 
        "Update resume", "Clean house", "Pay bills", "Water plants",
        "Buy birthday gift", "Fix the sink", "Visit friend", 
        "Watch movie", "Cook dinner", "Laundry", "Research project", 
        "Take dog for a walk", "Learn a new recipe", "Meditate", 
        "Prepare presentation", "Attend workshop", "Write code",
        "Fix bugs", "Read articles", "Update blog", "Practice guitar", 
        "Plan budget", "Buy new phone", "Check emails", "Call support", 
        "Review PR", "Plan marketing strategy", "Design logo", 
        "Prepare report", "File taxes", "Read news", "Take out trash", 
        "Repair bike", "Shop for clothes", "Attend webinar", "Join meetup"
    ]

    # Fetch all users
    users = list(User.objects.all())

    tasks = []
    for i in range(50):
        task = {
            "user": random.choice(users), 
            "title": random.choice(titles),
            "date_time_target": random_date(past, future),
            "description": f"Description for task {i + 1} is this that the description is temporarily made by me to show the task man here there.",
            "complete": random.choice([True, False])
        }
        tasks.append(task)


    for task in tasks:
        all_the_tasks.objects.create(**task)

