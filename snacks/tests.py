from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack

class SnackTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(usertitle='testuser', password='pass')
        testuser1.save()

        test_Snack = Snack.objects.create(title='figs', purchaser=testuser1,description='organic sun dried figs.')
        test_Snack.save()

    def test_Snacks_model(self):
        Snack = Snack.objects.get(id=1)
        actual_purchaser = str(Snack.purchaser)
        actual_title = str(Snack.title)
        actual_description = str(Snack.description)
        self.assertEqual(actual_purchaser,'testuser')
        self.assertEqual(actual_title, 'figs')
        self.assertEqual(actual_description,'organic sun dried figs.')
