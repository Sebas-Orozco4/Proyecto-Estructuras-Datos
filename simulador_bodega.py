
# ==========================================
# PROYECTO: SISTEMA DE DESPACHO DE BODEGA
# ESTRUCTURA DE DATOS: COLA FIFO
# INTEGRANTES:
# Sebastian Orozco Duque
# Miguel Angel Sepulveda
# ==========================================


# 1. CREACION DE LOS NODOS

class Nodo:

    def __init__(self, pedido):
        self.pedido = pedido
        self.siguiente = None


# 2. CREACION DE LA COLA

class Cola:

    def __init__(self, N):

        self.frente = None
        self.final = None
        self.tamano = 0

        self.capacidadMax = (N % 4) + 3


    # 3. AGREGAR PEDIDO (ENQUEUE)

    def agregar(self, pedido):

        if self.tamano >= self.capacidadMax:
            print("OVERFLOW: La bodega esta llena.")
            return

        nuevo = Nodo(pedido)

        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo

        else:
            self.final.siguiente = nuevo
            self.final = nuevo

        self.tamano += 1

        print("Pedido agregado correctamente.")


    # 4. DESPACHAR PEDIDO (DEQUEUE)

    def atender(self):

        if self.frente is None:
            print("UNDERFLOW: No hay pedidos pendientes.")
            return

        pedido = self.frente.pedido

        self.frente = self.frente.siguiente

        self.tamano -= 1

        if self.frente is None:
            self.final = None

        print("Pedido despachado:", pedido)


    # 5. CONSULTAR SIGUIENTE PEDIDO (FRONT)

    def consultar(self):

        if self.frente is None:
            print("No hay pedidos pendientes.")

        else:
            print("Siguiente pedido:", self.frente.pedido)


    # 6. MOSTRAR TODOS LOS PEDIDOS

    def mostrar(self):

        if self.frente is None:
            print("La cola esta vacia.")
            return

        actual = self.frente

        print("\nPEDIDOS PENDIENTES:")

        while actual is not None:

            print(actual.pedido)

            actual = actual.siguiente

        print("Total de pedidos:", self.tamano)


# 7. PROGRAMA PRINCIPAL

N = 13

bodega = Cola(N)

print("Capacidad maxima:", bodega.capacidadMax)

while True:

    print("\n===== SISTEMA DE DESPACHO =====")
    print("1. Registrar pedido")
    print("2. Despachar pedido")
    print("3. Consultar siguiente pedido")
    print("4. Mostrar pedidos pendientes")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        pedido = input("Ingrese el codigo del pedido: ")

        bodega.agregar(pedido)

    elif opcion == "2":

        bodega.atender()

    elif opcion == "3":

        bodega.consultar()

    elif opcion == "4":

        bodega.mostrar()

    elif opcion == "5":

        print("Cerrando sistema de bodega...")
        break

    else:

        print("Opcion no valida.")
