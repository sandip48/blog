from post.models import Post
import random
from faker import Faker
images = ["post/desktop-1366x768.jpg",
         "post/dell_vostro_3401_10th_gen_1.jpg",
         "post/background-3104413 (1).jpg",]
         
def insert_fake_data_in_post():
        fake = Faker()
        for i in range(40):
                Post.objects.create(
                        title=fake.sentence(),
                        content=fake.paragraph(nb_sentences=20),
                        image=random.choice(images),
                )