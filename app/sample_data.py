import random
from .models import Blog, Category, Tag, User  # Replace 'yourapp' with your Django app name

def create_3d_blogs():
    category = Category.custom.first()  # You can filter by name if needed
    tags = Tag.objects.all()
    users = User.objects.all()

    image_paths = [
        "blog/images/3d1.jpg",
        "blog/images/3d2.jpg",
        "blog/images/3d3.jpg",
    ]

    titles = [
        "Amazing 3D Art in the Wild",
        "Next-Level Blender Projects",
        "3D Modeling: From Concept to Reality"
    ]

    texts = [
        "Explore how 3D artists are transforming imagination into digital reality with stunning realism.",
        "Take a look at the most detailed Blender projects crafted by top-tier designers.",
        "A full breakdown of how 3D models are used in modern design, games, and simulations."
    ]

    for i in range(6):
        blog = Blog.objects.create(
            title=titles[i],
            text=texts[i],
            image=image_paths[i],
            category=category,
            status=Blog.StatusEnum.PUBLISHED
        )
        # Add random tags and likes
        blog.tags.set(random.sample(list(tags), k=min(len(tags), 3)))
        blog.like.set(random.sample(list(users), k=min(len(users), 2)))
        blog.seen.set(random.sample(list(users), k=min(len(users), 5)))

        blog.save()
        print(f"Created blog: {blog.title}")
