from sqlalchemy.exc import IntegrityError

from project import db
from project.api.models import Exercise
from project.tests.base import BaseTestCase


class TestExerciseModel(BaseTestCase):
	def test_add_exercise(self):

		exercise = Exercise(
			'Define a function called sum that takes two\
			 integers as arguments and returns their sum.', 
			'sum(2,2)', 
			'4'
		)

		db.session.add(exercise)
		db.session.commit()

		self.assertTrue(exercise.id)
		self.assertEquals(exercise.body, 'Define a function called sum that takes two\
			 integers as arguments and returns their sum.')

		self.assertEquals(exercise.test_code, 'sum(2,2)')
		self.assertEquals(exercise.test_code_solution, '4')
