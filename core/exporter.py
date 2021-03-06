from melodies.models import Chant
from django.http import HttpResponse

import csv

class Exporter():
    '''
    The Exporter class provides a method to download a set of chants
    '''

    @classmethod
    def export_to_csv(cls, ids):
        '''
        Create a CSV file of chants
        '''

        chants = Chant.objects.filter(pk__in=ids)
        opts = chants.model._meta
        field_names = [field.name for field in opts.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=dataset.csv'
        
        writer = csv.writer(response)
        writer.writerow(field_names)
        for chant in chants:
            writer.writerow([getattr(chant, field) for field in field_names])
            
        return HttpResponse(response, content_type='text/csv')
