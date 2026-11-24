class Solution:

    def isValid(self, s: str) -> bool:

        pila = []

        pares = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for caracter in s:

            if caracter in pares:

                if not pila or pila[-1] != pares[caracter]:
                    return False

                pila.pop()

            else:
                pila.append(caracter)

        return len(pila) == 0