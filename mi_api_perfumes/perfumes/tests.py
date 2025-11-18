from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient 
from django.contrib.auth import get_user_model
from perfumes.models import Marca, Perfume, Carrito, Pedido, ItemCarrito 

User = get_user_model()

class EcommerceFlowTests(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register') 
        self.login_url = reverse('login')
        self.perfume_list_url = reverse('perfume-list')
        self.carrito_list_url = reverse('carrito-list')
        self.pedido_list_url = reverse('pedido-list')
        
        # Crear datos iniciales (Marca y Perfume)
        self.marca = Marca.objects.create(nombre='Givenchy', pais_origen='Francia')
        self.perfume = Perfume.objects.create(nombre='Irresistible', marca=self.marca, precio=100.00)

    #REGISTRO DE USUARIO

    def test_1_registro_usuario(self):
        data = {
            'username': 'juli123',
            'email': 'juli@mail.com',
            'password': 'Auto123',
            'first_name': 'Julian',
            'last_name': 'Arenas'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='juli123').exists())

    #LOGIN DE USUARIO (Requiere registro previo)

    def test_2_login_usuario(self):
        self.client.post(self.register_url, {
            'username': 'luci',
            'email': 'luci@mail.com',
            'password': '789'
        }, format='json')
        
        # 2. Probar el login
        response = self.client.post(self.login_url, {
            'username': 'luci',
            'password': '789'
        }, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('detail' in response.data) 

    #LISTADO DE PRODUCTOS (Lectura Pública)

    def test_3_listado_productos_publico(self):
        response = self.client.get(self.perfume_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    #AGREGAR PRODUCTO AL CARRITO (Requiere login)
    
    def test_4_agregar_producto_al_carrito(self):
        user_test = User.objects.create_user(username='test_c', password='123')
        self.client.force_authenticate(user=user_test) # Forzamos el login
        
        carrito, created = Carrito.objects.get_or_create(usuario=user_test)
        
        data = {
            'carrito': carrito.pk,
            'perfume': self.perfume.pk,
            'cantidad': 2
        }
        
        response = self.client.post(reverse('itemcarrito-list'), data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ItemCarrito.objects.count(), 1) 
        

    # CREACIÓN DE PEDIDO DESDE EL CARRITO

    def test_5_generar_pedido(self):
        user_test = User.objects.create_user(username='test_p', password='123')
        self.client.force_authenticate(user=user_test)
        
        # Crear Carrito y agregar un producto
        carrito = Carrito.objects.create(usuario=user_test)
        ItemCarrito.objects.create(carrito=carrito, perfume=self.perfume, cantidad=2)
        
        # Crear el Pedido
        pedido_data = {
            'usuario': user_test.pk,
            'total': 200.00, 
            'direccion_envio': 'Calle Salta 318'
        }
        
        response = self.client.post(self.pedido_list_url, pedido_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Pedido.objects.filter(usuario=user_test).exists())

