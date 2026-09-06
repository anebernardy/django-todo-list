from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from .forms import TodoForm
from .models import Todo


class TodoListView(ListView):
    model = Todo
    context_object_name = "todo_list"
    template_name = "todo/todo_list.html"


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return Todo.objects.filter(finished_at__isnull=True)


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def post(self, request, pk):
        todo = get_object_or_404(
            Todo, 
            pk=pk,
            finished_at__isnull=True
        )
        todo.mark_as_completed()

        return redirect("todo_list")
