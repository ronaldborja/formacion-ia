class HashTable:
    def __init__(self): 
        self.MAX = 100 
        self.arr = [[] for _ in range(self.MAX)]  # Usando _ para indicar una variable no usada

    def get_hash(self, key): 
        h = 0  
        for char in key: 
            h += ord(char)  
        return h % self.MAX  
    
    def __setitem__(self, key, val): 
        h = self.get_hash(key) 
        found = False
        for idx, element in enumerate(self.arr[h]): 
            if len(element) == 2 and element[0] == key:  # Verificar si la clave ya está en la lista
                self.arr[h][idx] = (key, val)  # Si la clave está, actualizar su valor
                found = True
                break
        if not found:
            self.arr[h].append((key, val))  # Si la clave no está, agregarla a la lista

    def __getitem__(self, key): 
        h = self.get_hash(key)
        for element in self.arr[h]: 
            if element[0] == key:  # Buscar la clave en la lista
                return element[1]  # Si se encuentra, devolver el valor asociado
        raise KeyError(key)  # Si la clave no se encuentra, lanzar una excepción KeyError
    
    def __delitem__(self, key): 
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]  # Eliminar la clave y su valor asociado de la lista
                return
        raise KeyError(key)  # Si la clave no se encuentra, lanzar una excepción KeyError


dicc = HashTable()
dicc["march 6"] = 130
dicc["march 6"] = 150
dicc["march 6"] = 170

print(dicc["march 6"])

