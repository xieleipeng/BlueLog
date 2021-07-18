from faker import Faker

from models import Admin, Category
from extensions import db


def fake_admin():
	admin = Admin(
		username='admin',
		blog_title='Bulelog',
		blog_sub_title="No, I'm the real thing.",
		name='Mima',
		about='Um,......'
	)
	admin.set_password('helloflask')
	db.session.add(admin)
	db.session.commit()


fake = Faker()


def fake_categories(count=10):
	category = Category(name='Default')
	db.session.add(category)

	for i in range(count):
		category = Category(name=fake.word())
		db.session.add(category)
		try:
			db.session.commit()
		except InterruptedError:
			db.session.rollback()


