from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated


class AssinaturaAPIView(APIView):

# permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        if 'nome' in request.GET:
            statusNome = request.GET['nome']
            assinatura = Assinatura.objects.filter(nome__contains=statusNome)
            serializer = AssinaturaSerializer(assinatura, many=True)
            return Response(serializer.data)

        elif pk == '':
            assinatura = Assinatura.objects.all()
            serializer = AssinaturaSerializer(assinatura, many=True)
            return Response(serializer.data)
        else:
            assinatura = Assinatura.objects.get(id=pk)
            serializer = AssinaturaSerializer(assinatura)
            return Response(serializer.data)

    def post(self, request):
        serializer = AssinaturaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        assinatura = Assinatura.objects.get(id=pk)
        serializer = AssinaturaSerializer(assinatura, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        assinatura = Assinatura.objects.get(id=pk)       
        assinatura.delete()
        return Response({"msg": "Apagado com sucesso"})


#///////////////////////////////////////////////////////////////////
class UsuariosAPIView(APIView):

# permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        if 'nome' in request.GET:
            statusNome = request.GET['nome']
            usuarios = Usuarios.objects.filter(nome__contains=statusNome)
            serializer = UsuariosGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        elif 'user' in request.GET:
            statusUser = request.GET['user']
            usuarios = Usuarios.objects.filter(idUser=statusUser)
            serializer = UsuariosGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        elif pk == '':
            usuarios = Usuarios.objects.all()
            serializer = UsuariosGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        else:
            usuarios = Usuarios.objects.get(id=pk)
            serializer = UsuariosGETSerializer(usuarios)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        usuarios = Usuarios.objects.get(id=pk)
        serializer = UsuariosSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        usuarios = Usuarios.objects.get(id=pk)       
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})
#///////////////////////////////////////////////////////////////////
class CategoriaAPIView(APIView):

# permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        if 'nome' in request.GET:
            statusNome = request.GET['nome']
            categoria = Categoria.objects.filter(nome__contains=statusNome)
            serializer = CategoriaSerializer(categoria, many=True)
            return Response(serializer.data)

        elif pk == '':
            categoria = Categoria.objects.all()
            serializer = CategoriaSerializer(categoria, many=True)
            return Response(serializer.data)
        else:
            categoria = Categoria.objects.get(id=pk)
            serializer = CategoriaSerializer(categoria)
            return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        categoria = Categoria.objects.get(id=pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        categoria = Categoria.objects.get(id=pk)       
        categoria.delete()
        return Response({"msg": "Apagado com sucesso"})
#///////////////////////////////////////////////////////////////////
class FilmesAPIView(APIView):

# permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        if 'nome' in request.GET:
            statusNome = request.GET['nome']
            filmes = Filmes.objects.filter(nome__contains=statusNome)#nome_contains = se os nomes conterem o que voce digitar ele vai pegar todos os nomes que tem o que vc digitou
            serializer = FilmesGETSerializer(filmes, many=True)
            return Response(serializer.data)
        elif 'categoria' in request.GET:
            statusCategoria = request.GET['categoria']
            filmes = Filmes.objects.filter(idCategoriaFK=statusCategoria)
            serializer = FilmesGETSerializer(filmes, many=True)
            return Response(serializer.data)
        elif pk == '':
            filmes = Filmes.objects.all()
            serializer = FilmesGETSerializer(filmes, many=True)
            return Response(serializer.data)
        else:
            filmes = Filmes.objects.get(id=pk)
            serializer = FilmesGETSerializer(filmes)
            return Response(serializer.data)

    def post(self, request):
        serializer = FilmesSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        filmes = Filmes.objects.get(id=pk)
        serializer = FilmesSerializer(filmes, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        filmes = Filmes.objects.get(id=pk)       
        filmes.delete()
        return Response({"msg": "Apagado com sucesso"})
#///////////////////////////////////////////////////////////////////
class FavoritosAPIView(APIView):

# permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        if 'filme' in request.GET:
            statusFilme = request.GET['filme']
            favoritos = Favoritos.objects.filter(idFilmeFk=statusFilme)
            serializer = FavoritosGETSerializer(favoritos, many=True)
            return Response(serializer.data)
        elif 'usuario' in request.GET:
            statusUsuario= request.GET['usuario']
            favoritos = Favoritos.objects.filter(idUsuarioFK=statusUsuario)
            serializer = FavoritosGETSerializer(favoritos, many=True)
            return Response(serializer.data)
        elif pk == '':
            favoritos = Favoritos.objects.all()
            serializer = FavoritosGETSerializer(favoritos, many=True)
            return Response(serializer.data)
        else:
            favoritos = Favoritos.objects.get(id=pk)
            serializer = FavoritosGETSerializer(favoritos)
            return Response(serializer.data)

    def post(self, request):
        serializer = FavoritosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        favoritos = Favoritos.objects.get(id=pk)
        serializer = FavoritosSerializer(favoritos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        favoritos = Favoritos.objects.get(id=pk)       
        favoritos.delete()
        return Response({"msg": "Apagado com sucesso"})


