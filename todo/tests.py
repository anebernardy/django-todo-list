from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import TodoForm
from .models import Todo


class TodoFormTests(TestCase):
    def test_rejects_past_deadline_when_creating_task(self):
        yesterday = timezone.localdate() - timedelta(days=1)

        form = TodoForm(
            data={
                "title": "Overdue task",
                "deadline": yesterday,
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("deadline", form.errors)

    def test_accepts_future_deadline(self):
        tomorrow = timezone.localdate() + timedelta(days=1)

        form = TodoForm(
            data={
                "title": "Future task",
                "deadline": tomorrow,
            }
        )

        self.assertTrue(form.is_valid())


class TodoUpdateTests(TestCase):
    def test_allows_editing_task_while_keeping_past_deadline(self):
        yesterday = timezone.localdate() - timedelta(days=1)

        todo = Todo.objects.create(
            title="Old task",
            deadline=yesterday,
        )

        response = self.client.post(
            reverse("todo_update", args=[todo.pk]),
            data={
                "title": "Updated old task",
                "deadline": yesterday,
            },
        )

        self.assertRedirects(response, reverse("todo_list"))

        todo.refresh_from_db()

        self.assertEqual(todo.title, "Updated old task")
        self.assertEqual(todo.deadline, yesterday)

    def test_blocks_editing_completed_task(self):
        today = timezone.localdate()

        todo = Todo.objects.create(
            title="Completed task",
            deadline=today,
            finished_at=today,
        )

        response = self.client.get(
            reverse("todo_update", args=[todo.pk])
        )

        self.assertEqual(response.status_code, 404)


class TodoCompleteTests(TestCase):
    def test_completes_task_with_post_request(self):
        today = timezone.localdate()

        todo = Todo.objects.create(
            title="Pending task",
            deadline=today,
        )

        response = self.client.post(
            reverse("todo_complete", args=[todo.pk])
        )

        self.assertRedirects(response, reverse("todo_list"))

        todo.refresh_from_db()

        self.assertEqual(todo.finished_at, today)

    def test_does_not_complete_task_with_get_request(self):
        today = timezone.localdate()

        todo = Todo.objects.create(
            title="Pending task",
            deadline=today,
        )

        response = self.client.get(
            reverse("todo_complete", args=[todo.pk])
        )

        self.assertEqual(response.status_code, 405)

        todo.refresh_from_db()

        self.assertIsNone(todo.finished_at)
