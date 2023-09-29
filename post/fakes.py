from post.models import Post
import random
from faker import Faker
from accounts.models import User
images = ["post/Screenshot_2023-08-07_165536.png",
          "post/dwayne-johnson-black-adam.webp"]
         
def insert_fake_data_in_post():

        fake = Faker()
        users=User.objects.all()
        for i in range(40):
                Post.objects.create(
                        title=fake.sentence(),
                        content=fake.paragraph(nb_sentences=20),
                        image=random.choice(images),
                        user=random.choice(users),
                )
                