    class Nodo:
       def __init__(self, nombre = None, dpi = None, izq = None, der = None):
           self.nombre = nombre
           self.dpi = dpi
           self.izq = izq
           self.der = der

           def __str__(self):
               return "%s %s" %(self.nombre, self.dpi)

    class Arbol: 
        def __init__(self):
            self.raiz = None

            def agregar(self, elemento):
                if self.raiz == None
                self.raiz = elemento
                else:
                    aux = self.raiz 

                    padre = None 
                    while aux != None:
                        padre = aux 
                        if int(elemento.dpi)>= int (aux.dpi):
                            aux = aux.der
                        else:
                            aux = aux.izq
                        if int(elemento.dpi)>= int (padre.dpi):
                            padre.der = elemento
                        else:
                            padrer.iqz = elemento 

        def preordenar (self, elemento):
            if elemento != None:
                print (elemento)
                self.preordenar(elemento.izq)
                 self.preordenar(elemento.der)
                 print(elemento)

      def postorden (self, elemento):
          if elemento != None:
                print (elemento)
                self.postorden(elemento.izq)
                self.postorden(elemento.der)
                print(elemento)

        def inorden (self, elemento):
            if elemento != None:
                
                self.preordenar(elemento.izq)
                print (elemento)
                self.preordenar(elemento.der)

        def getRaiz(self):
            return self.raiz


        if __name__ == "__main__":
            ab=Arbol()
            while(true):
                print("---Menu---\n"+
                      "1. Agregar\n"+
                      "2. PreOrden\n"+
                      "3. PostOrden\n"+
                      "4. InOrder\n"+
                      )
                num = input("Ingrese una opcion"):

                    if num == "1":
                        nombre = input("Ingrese nombre:")
                        dpi = input ("Ingrese numero de dpi")
                        nod = Nodo(nombre, dpi)
                        ab.agregar(nod)

                   if num == "2":
                       print("Mostrar en preOrden")
                       ab.preorden(ab.getRaiz())

                    if num == "3":
                        print("Mostrar en PostOrden")
                        ab.postorden(ab.getRaiz())

                    if num == "4":
                        print("Mostrar en PostOrden")
                        ab.inorden(ab.getRaiz())