from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carro.carro import Carro
from pedidos.models import Pedido, LineaPedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from tienda.models import Producto
from carro.carro import Carro
# Create your views here.



@login_required(login_url="autenticacion/inicio_sesion")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    pedidosCarro=list()
    for key, value in carro.carro.items():
        pedidosCarro.append(LineaPedido(


            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido

        ))
    LineaPedido.objects.bulk_create(pedidosCarro)  #bulk_create ->  este memtodo hace insert into

    enviar_mail(pedido=pedido,
                pedidosCarro=pedidosCarro,
                nombreusuario=request.user.username,
                emailusuario=request.user.email
                )

    messages.success(request,"pedido hecho correctamente")
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto="Grcias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {

        "pedido":kwargs.get("pedido"),
        "pedidosCarro":kwargs.get("pedidosCarro"),
        "nombreusuario":kwargs.get("nombreusuario")

    })

    mensaje_texto=strip_tags(mensaje)
    from_email="mnikolaas@gmail.com"#correo de la pagina
    #to=kwargs.get("emailusuario") #aquien va ditigido al correo electronico
    to="nicolasmunozj0@gmail.com"
    send_mail(asunto, mensaje_texto, from_email,[to],html_message=mensaje)




def pasarela_pago(request):
    carro = Carro(request)
    productos_carro = carro.carro.values()  # Obtener los valores (productos) del diccionario del carrito
    precio_total = sum(int(item["cantidad"]) * float(item["precio"]) for item in productos_carro)
    precio_total_centavos = int(precio_total * 100)  # Convertir a centavos
    return render(request, "pago.html", {"precio_total": precio_total_centavos})



