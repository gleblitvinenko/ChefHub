from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishSearchForm
from kitchen.models import Cook, Dish, DishType


def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Dish.objects.select_related("dish_type")
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish_list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
