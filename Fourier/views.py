from django.shortcuts import render, HttpResponse
import base64, os 
from .form import imagen
from django.shortcuts import render_to_response

def index(request):
    return render(request, 'Fourier/index.html', {})

def load_image(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file-5'], str(request.FILES['file-5']))
        encrypt(request.FILES['file-5'], str(request.FILES['file-5']))
        fileBase64 = open('uploads/'+str(request.FILES['file-5'])+'_base64.txt','rb')
        namefile = str(request.FILES['file-5'])+'_base64.txt'
        base64 = fileBase64.read()
        SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
        return render_to_response('Fourier/encrypt.html', {'base64':base64, 'file':namefile,})
    return render(request, 'Fourier/index.html', {})
 
def handle_uploaded_file(file, filename):
    if not os.path.exists('uploads/'):
        os.mkdir('uploads/')
 
    with open('uploads/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def encrypt(file, filename):
    image = open('uploads/'+filename,'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    text_base64 = open('uploads/'+filename+'_base64.txt','wb')
    text_base64.write(image_64_encode)    
    return 

def get_file(request):
    namefile = request.GET['file']
    fileBase64 = open('uploads/'+namefile,'rb') 
    base64 = fileBase64.read()
    response = HttpResponse(base64, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=' + namefile
    return response 
