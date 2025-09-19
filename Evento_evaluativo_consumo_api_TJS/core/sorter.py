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
    def counting_sort(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
        """Counting sort: requiere enteros no negativos. Ordena por clave entera."""
        # Convertir a enteros
        arr = copy.deepcopy(data)
        values = []
        for item in arr:
            v = Sorter._get_key_value(item, key)
            if not float(v).is_integer() or v < 0:
                raise ValueError("Counting sort requiere enteros no negativos.")
            values.append(int(v))
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
            v = int(Sorter._get_key_value(arr[i], key))
            pos = count[v] - 1
            out[pos] = arr[i]
            count[v] -= 1
        if reverse:
            out.reverse()
        return out

    @staticmethod
    def radix_sort(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
        """Radix sort para enteros no negativos."""
        arr = copy.deepcopy(data)
        values = []
        for item in arr:
            v = Sorter._get_key_value(item, key)
            if not float(v).is_integer() or v < 0:
                raise ValueError("Radix sort requiere enteros no negativos.")
            values.append(int(v))
        if len(values) == 0:
            return arr
        maxv = max(values)
        exp = 1
        out = arr
        while maxv // exp > 0:
            buckets = [[] for _ in range(10)]
            for item in out:
                v = int(Sorter._get_key_value(item, key))
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
    

