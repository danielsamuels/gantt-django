from django.views.generic import ListView
from django.utils.timezone import now
from django.db.models import Min, Max

from .helpers import JSONResponseMixin, LoginRequired
from .models import TimelineItem, Organisation, User

import calendar
import datetime


class Data(LoginRequired, JSONResponseMixin, ListView):

    model = Organisation

    def get_context_data(self):
        # Return the users, the timeline items and the date range required(?).

        users = [{
            'id': user.pk,
            'name': user.__unicode__(),
            'image': '/static/img/daniel.png'
        } for user in self.request.user.organisation.user_set.all()]

        timeline_items_qs = TimelineItem.objects.filter(
            project__organisation=self.request.user.organisation,
        )

        timeline_items = [
            {
                'user': item.user.pk,
                'project': item.project.__unicode__(),
                'start_date': item.start_date.strftime('%d/%m/%Y'),
                'end_date': item.end_date.strftime('%d/%m/%Y'),
                'description': item.description,
                'days': (item.end_date - item.start_date).days
            }
            for item
            in TimelineItem.objects.filter(
                project__organisation=self.request.user.organisation,
            )
        ]

        aggregate = timeline_items_qs.aggregate(Min('start_date'), Max('end_date'))

        return {
            'users': users,
            'timeline_items': timeline_items,
            'start_date': aggregate['start_date__min'].strftime('%d/%m/%Y'),
            'end_date': aggregate['end_date__max'].strftime('%d/%m/%Y')
        }
