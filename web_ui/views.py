from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from web_ui.models import Report


class CommonMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = User.objects.all()
        return context


class LoginRequiredMixin(CommonMixin):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class OwnerPermissionRequiredMixin(CommonMixin):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        report = super().get_object()
        if report.author != self.request.user:
            raise PermissionDenied()
        return report


class ReportListView(LoginRequiredMixin, ListView):
    context_object_name = "reports"
    model = Report

    def get_queryset(self):
        author_id = self.kwargs.get('author_id', None)
        if author_id:
            return Report.objects.filter(author=author_id)
        else:
            return Report.objects.all()


class ReportSearchView(LoginRequiredMixin, ListView):
    context_object_name = "reports"
    model = Report

    def get_queryset(self):
        query = self.request.POST.get('query', None) or self.request.GET.get('query', None)
        if query:
            return Report.objects.filter(Q(title__contains=query) |
                                         Q(content__contains=query) |
                                         Q(author__username__contains=query))
        else:
            return Report.objects.all()


class ReportDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "report"
    model = Report
    queryset = Report.objects.all()


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = ['title', 'content']
    success_url = reverse_lazy('web_ui:list_report')

    def post(self, request, *args, **kwargs):
        formClass = self.get_form_class()
        form = formClass(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ReportUpdateView(OwnerPermissionRequiredMixin, UpdateView):
    model = Report
    fields = ['title', 'content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('web_ui:list_report')


class ReportDeleteView(OwnerPermissionRequiredMixin, DeleteView):
    model = Report
    success_url = reverse_lazy('web_ui:list_report')
