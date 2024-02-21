class Producto:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_producto(self):
        pass

class Libro(Producto):
    def __init__(self, titulo, autor, genero):
        super().__init__(titulo, autor)
        self.genero = genero
    
    def mostrar_producto(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}"

class Pelicula(Producto):
    def __init__(self, titulo, autor, director):
        super().__init__(titulo, autor)
        self.director = director
    
    def mostrar_producto(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Director: {self.director}"

class Disco(Producto):
    def __init__(self, titulo, autor, artista):
        super().__init__(titulo, autor)
        self.artista = artista
    
    def mostrar_producto(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Artista: {self.artista}"

# Instancias de libros
libro1 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
libro3 = Libro("1984", "George Orwell", "Ciencia ficción")

# Instancias de películas
pelicula1 = Pelicula("El Padrino", "Mario Puzo", "Francis Ford Coppola")
pelicula2 = Pelicula("La La Land", "Damien Chazelle", "Damien Chazelle")
pelicula3 = Pelicula("Parasite", "Bong Joon-ho", "Bong Joon-ho")

# Instancias de discos
disco1 = Disco("Thriller", "Michael Jackson", "Michael Jackson")
disco2 = Disco("Dark Side of the Moon", "Pink Floyd", "Pink Floyd")
disco3 = Disco("Back in Black", "AC/DC", "AC/DC")

# Mostrar información de cada producto
print("Libros:")
print(libro1.mostrar_producto())
print(libro2.mostrar_producto())
print(libro3.mostrar_producto())

print("\nPelículas:")
print(pelicula1.mostrar_producto())
print(pelicula2.mostrar_producto())
print(pelicula3.mostrar_producto())

print("\nDiscos:")
print(disco1.mostrar_producto())
print(disco2.mostrar_producto())
print(disco3.mostrar_producto())
