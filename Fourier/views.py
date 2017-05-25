'''
UDFJC FT
Control web para Hide64
'''
from django.shortcuts import render, HttpResponse
import base64, os  
from django.shortcuts import render_to_response

'''Pagina de inicio del app'''
def index(request):
    return render(request, 'Fourier/index.html', {})

'''Funcion de carga de imagen para encriptar a base 64'''
def load_image(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file-5'], str(request.FILES['file-5']))
        encrypt(request.FILES['file-5'], str(request.FILES['file-5']))
        fileBase64 = open('uploads/'+str(request.FILES['file-5'])+'_base64.txt','rb')
        namefile = str(request.FILES['file-5'])+'_base64.txt'
        base64 = fileBase64.read() 
        return render_to_response('Fourier/encrypt.html', {'base64':base64, 'file':namefile,})
    return render(request, 'Fourier/index.html', {})
 
'''Control para carga de archivos al repo'''
def handle_uploaded_file(file, filename):
    if not os.path.exists('uploads/'):
        os.mkdir('uploads/') 
    with open('uploads/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

'''funcion de encripcion de imagenes'''
def encrypt(file, filename):
    image = open('uploads/'+filename,'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    text_base64 = open('uploads/'+filename+'_base64.txt','wb')
    text_base64.write(image_64_encode)    
    return 

'''descarga de archivo'''
def get_file(request):
    namefile = request.GET['file']
    fileBase64 = open('uploads/'+namefile,'rb') 
    base64 = fileBase64.read()
    response = HttpResponse(base64, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=' + namefile
    return response 

'''Carga de txt al repo'''
def load_txt(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file-4'], str(request.FILES['file-4']))
        decrypt(request.FILES['file-4'], str(request.FILES['file-4']))
        fileImg= open('uploads/'+str(request.FILES['file-4'])+'_decode64.jpg','rb')
        namefile = str(request.FILES['file-4'])+'_decode64.jpg'
        img = fileImg.read() 
        return render_to_response('Fourier/decrypt.html', {'img':img, 'file':namefile,}) 
    return render(request, 'Fourier/index.html', {})     

'''funcion para desencriptar b64->imagen'''
def decrypt(file, filename):
    with open('uploads/'+filename,'rb') as file_base64:
        text_encode = file_base64.read()
    image_64_decode = base64.b64decode(text_encode)     
    image_result = open('uploads/'+filename+'_decode64.jpg','wb')
    image_result.write(image_64_decode)
    return

'''funcion para descargar la imagen decodificada'''
def get_Img(request):
    namefile = request.GET['file']
    fileBase64 = open('uploads/'+namefile,'rb') 
    base64 = fileBase64.read()
    response = HttpResponse(base64, content_type='image/gif')
    response['Content-Disposition'] = 'attachment; filename=' + namefile
    return response 