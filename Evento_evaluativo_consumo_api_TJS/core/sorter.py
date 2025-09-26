import copy
from typing import List, Dict, Any, Optional

class Sorter:
    """Contiene algoritmos de ordenamiento sobre listas de diccionarios."""

    # --- Helpers ---
    @staticmethod
    def _get_key_value(item, key):
        val = item.get(key, None)
        if val is None:
            raise ValueError(f"Registro no contiene la clave {key}")
        try:
            return float(val)
        except Exception:
            raise ValueError(f"Valor no numérico en '{key}': {val}")
    
    @staticmethod
    def _clean_numeric_value(val):
        """Limpia y convierte un valor a float, manejando casos especiales."""
        if val is None:
            raise ValueError("Valor nulo")
        
        # Si ya es un número, devolverlo
        if isinstance(val, (int, float)):
            return float(val)
        
        # Si es string, limpiar espacios y caracteres especiales
        if isinstance(val, str):
            # Remover espacios en blanco
            cleaned = val.strip()
            
            # Manejar strings vacíos
            if not cleaned:
                raise ValueError("String vacío")
            
            # Remover caracteres no numéricos comunes (excepto punto y signo negativo)
            import re
            cleaned = re.sub(r'[^\d\.\-\+eE]', '', cleaned)
            
            # Intentar conversión
            try:
                return float(cleaned)
            except ValueError:
                raise ValueError(f"No se puede convertir '{val}' a número")
        
        # Para otros tipos, intentar conversión directa
        try:
            return float(val)
        except ValueError:
            raise ValueError(f"Tipo no soportado: {type(val)}")

    @staticmethod
    def _swap(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]

    # --- Algoritmos ---
    @staticmethod
    def bubble_sort(data, key, reverse=False):
        arr = copy.deepcopy(data)
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (Sorter._get_key_value(arr[j], key) > Sorter._get_key_value(arr[j + 1], key)) ^ reverse:
                    Sorter._swap(arr, j, j + 1)
        return arr

    @staticmethod
    def selection_sort(data, key, reverse=False):
        arr = copy.deepcopy(data)
        n = len(arr)
        for i in range(n):
            sel = i
            for j in range(i + 1, n):
                cond = Sorter._get_key_value(arr[j], key) < Sorter._get_key_value(arr[sel], key)
                if cond ^ reverse:
                    sel = j
            Sorter._swap(arr, i, sel)
        return arr

    @staticmethod
    def insertion_sort(data, key, reverse=False):
        arr = copy.deepcopy(data)
        for i in range(1, len(arr)):
            current = arr[i]
            cur_val = Sorter._get_key_value(current, key)
            j = i - 1
            while j >= 0 and ((Sorter._get_key_value(arr[j], key) > cur_val) ^ reverse):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current
        return arr

    @staticmethod
    def merge_sort(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
        def merge(left, right):
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                cond = Sorter._get_key_value(left[i], key) <= Sorter._get_key_value(right[j], key)
                if cond ^ reverse:
                    res.append(left[i]); i += 1
                else:
                    res.append(right[j]); j += 1
            res.extend(left[i:]); res.extend(right[j:])
            return res

        if len(data) <= 1:
            return copy.deepcopy(data)
        mid = len(data) // 2
        left = Sorter.merge_sort(data[:mid], key, reverse)
        right = Sorter.merge_sort(data[mid:], key, reverse)
        return merge(left, right)
    
    @staticmethod
    def quick_sort(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
        arr = copy.deepcopy(data)
        def qsort(a, lo, hi):
            if lo >= hi:
                return
            pivot = Sorter._get_key_value(a[(lo + hi) // 2], key)
            i, j = lo, hi
            while i <= j:
                while ((Sorter._get_key_value(a[i], key) < pivot) ^ reverse):
                    i += 1
                while ((Sorter._get_key_value(a[j], key) > pivot) ^ reverse):
                    j -= 1
                if i <= j:
                    Sorter._swap(a, i, j)
                    i += 1; j -= 1
            qsort(a, lo, j); qsort(a, i, hi)

        qsort(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def counting_sort(data: List[Dict[str, Any]], key: str, reverse: bool = False, decimal_mode: str = "multiply") -> List[Dict[str, Any]]:
        """
        Counting sort adaptado para manejar números decimales.
        
        Args:
            decimal_mode: 
                - "multiply": Multiplica por 100 (5.66 -> 566)
                - "round": Redondea al entero más cercano (5.66 -> 6)  
                - "truncate": Trunca decimales (5.66 -> 5)
        """
        arr = copy.deepcopy(data)
        values = []
        conversion_factor = 1
        
        # Determinar si hay decimales y calcular factor de conversión
        if decimal_mode == "multiply":
            max_decimals = 0
            for item in arr:
                raw_val = item.get(key, None)
                if raw_val is None:
                    continue
                try:
                    if isinstance(raw_val, str):
                        cleaned_val = raw_val.strip()
                        import re
                        cleaned_val = re.sub(r'[^\d\.\-\+]', '', cleaned_val)
                        float_val = float(cleaned_val) if cleaned_val else 0.0
                    else:
                        float_val = float(raw_val)
                    
                    # Contar decimales
                    decimal_str = str(float_val).split('.')
                    if len(decimal_str) > 1:
                        max_decimals = max(max_decimals, len(decimal_str[1]))
                except:
                    pass
            
            conversion_factor = 10 ** max_decimals
        
        for i, item in enumerate(arr):
            raw_val = item.get(key, None)
            if raw_val is None:
                raise ValueError(f"Registro no contiene la clave {key}")
            
            try:
                # Limpiar el valor si es string
                if isinstance(raw_val, str):
                    cleaned_val = raw_val.strip()
                    import re
                    cleaned_val = re.sub(r'[^\d\.\-\+]', '', cleaned_val)
                    float_val = float(cleaned_val) if cleaned_val else 0.0
                else:
                    float_val = float(raw_val)
                
                # Convertir según el modo seleccionado
                if decimal_mode == "multiply":
                    int_val = int(round(float_val * conversion_factor))
                elif decimal_mode == "round":
                    int_val = round(float_val)
                elif decimal_mode == "truncate":
                    int_val = int(float_val)
                else:
                    raise ValueError(f"Modo decimal no válido: {decimal_mode}")
                
                # Verificar que no sea negativo
                if int_val < 0:
                    raise ValueError(f"Counting sort no puede manejar valores negativos. Valor: '{raw_val}' -> {int_val} en posición {i}")
                
                values.append(int_val)
                
            except (ValueError, TypeError) as e:
                raise ValueError(f"Error procesando valor en posición {i}: '{raw_val}' (tipo: {type(raw_val).__name__}) - {str(e)}")
        
        if len(values) == 0:
            return arr
        
        mx = max(values)
        count = [0] * (mx + 1)
        for v in values:
            count[v] += 1
        
        # Prefijo
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        out = [None] * len(arr)
        
        for i in range(len(arr) - 1, -1, -1):
            raw_val = arr[i].get(key, None)
            # Aplicar la misma lógica de conversión
            if isinstance(raw_val, str):
                cleaned_val = raw_val.strip()
                import re
                cleaned_val = re.sub(r'[^\d\.\-\+]', '', cleaned_val)
                v_float = float(cleaned_val) if cleaned_val else 0.0
            else:
                v_float = float(raw_val)
            
            # Convertir según el modo
            if decimal_mode == "multiply":
                v = int(round(v_float * conversion_factor))
            elif decimal_mode == "round":
                v = round(v_float)
            elif decimal_mode == "truncate":
                v = int(v_float)
            
            pos = count[v] - 1
            out[pos] = arr[i]
            count[v] -= 1
            
        if reverse:
            out.reverse()
        return out

    @staticmethod
    def radix_sort(data: List[Dict[str, Any]], key: str, reverse: bool = False, decimal_mode: str = "multiply") -> List[Dict[str, Any]]:
        """Radix sort para enteros no negativos."""
        arr = copy.deepcopy(data)
        values = []
        conversion_factor = 1
        
        if decimal_mode == "multiply":
            max_decimals = 0
            for item in arr:
                raw_val = item.get(key, None)
                if raw_val is None:
                    continue
                try:
                    if isinstance(raw_val, str):
                        cleaned_val = raw_val.strip()
                        import re
                        cleaned_val = re.sub(r'[^\d\.\-\+]', '', cleaned_val)
                        float_val = float(cleaned_val) if cleaned_val else 0.0
                    else:
                        float_val = float(raw_val)
                    
                    # Contar decimales
                    decimal_str = str(float_val).split('.')
                    if len(decimal_str) > 1:
                        max_decimals = max(max_decimals, len(decimal_str[1]))
                except:
                    pass
            
            conversion_factor = 10 ** max_decimals
        
        for item in arr:
            v = Sorter._get_key_value(item, key)
            if decimal_mode == "multiply":
                v = int(round(v * conversion_factor))
            elif decimal_mode == "round":
                v = round(v)
            elif decimal_mode == "truncate":
                v = int(v)
            else:
                raise ValueError(f"Modo decimal no válido: {decimal_mode}")
            float_val = float(v)
            if float_val < 0:
                raise ValueError("Radix sort requiere enteros no negativos.")
            int_val = int(float_val)
            values.append(int_val)
        if len(values) == 0:
            return arr
        maxv = max(values)
        exp = 1
        out = arr
        while maxv // exp > 0:
            buckets = [[] for _ in range(10)]
            for item in out:
                v_float = float(Sorter._get_key_value(item, key))
                if decimal_mode == "multiply":
                    v = int(round(v_float * conversion_factor))
                elif decimal_mode == "round":
                    v = round(v_float)
                elif decimal_mode == "truncate":
                    v = int(v_float)
                else:
                    raise ValueError(f"Modo decimal no válido: {decimal_mode}")
                digit = (v // exp) % 10
                buckets[digit].append(item)
            out = [x for bucket in buckets for x in bucket]
            exp *= 10
        if reverse:
            out.reverse()
        return out

    @staticmethod
    def heap_sort(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
        arr = copy.deepcopy(data)
        n = len(arr)

        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and ((Sorter._get_key_value(arr[l], key) > Sorter._get_key_value(arr[largest], key)) ^ reverse):
                largest = l
            if r < n and ((Sorter._get_key_value(arr[r], key) > Sorter._get_key_value(arr[largest], key)) ^ reverse):
                largest = r
            if largest != i:
                Sorter._swap(arr, i, largest)
                heapify(n, largest)

        # Build heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
        # Extract
        for i in range(n - 1, 0, -1):
            Sorter._swap(arr, 0, i)
            heapify(i, 0)
        if reverse:
            arr.reverse()
        return arr

    @staticmethod
    def bucket_sort(data: List[Dict[str, Any]], key: str, reverse: bool = False, buckets_count: Optional[int] = None) -> List[Dict[str, Any]]:
        """Bucket sort para números (flotantes o enteros)."""
        arr = copy.deepcopy(data)
        n = len(arr)
        if n == 0:
            return arr
        values = [Sorter._get_key_value(x, key) for x in arr]
        minimum = min(values); maximum = max(values)
        # Evitar división por cero
        if maximum == minimum:
            return arr[::-1] if reverse else arr
        if not buckets_count:
            buckets_count = max(10, n // 2)
        buckets = [[] for _ in range(buckets_count)]
        for item in arr:
            v = Sorter._get_key_value(item, key)
            idx = int((v - minimum) / (maximum - minimum) * (buckets_count - 1))
            buckets[idx].append(item)
        sorted_arr = []
        for b in buckets:
            # Puedes usar insertion_sort para ordenar cada bucket
            sorted_b = Sorter.insertion_sort(b, key, reverse=False)
            sorted_arr.extend(sorted_b)
        if reverse:
            sorted_arr.reverse()
        return sorted_arr
    

