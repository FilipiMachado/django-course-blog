from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    """ def form_valid(self, form):
        form.save()
        return super().form_valid(form) """
    
    """ def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        }) """

    """ def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        }) """


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['message'] = "This Works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"

    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context """


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context['review'] = selected_review
        return context """


""" def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    }) """


""" def thank_you(request):
    return render(request, "reviews/thank_you.html") """
