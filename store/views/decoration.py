from django.shortcuts import render
from django.views import View
from store.models import Decoration
class DecorationView(View):
    def get(self,request):
        member=request.session.get('customer')
        decoration=Decoration.get_decoration_by_member(member)
        print(decoration)
        return render(request,'decoration.html',{'decoration':decoration})