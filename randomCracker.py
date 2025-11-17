A = 0x5DEECE66D
C = 0xB
MASK = (1 << 48) - 1


class JavaRandomCracker:
    def __init__(self, seed: int):
        """Инициализация с внутренним 48-битным seed."""
        self.seed = seed & MASK

    @staticmethod
    def recover_seed(out1: int, out2: int) -> 'JavaRandomCracker | None':
        """Восстановление внутреннего seed по двум последовательным nextInt()"""
        s1_hi = out1 << 16
        for low in range(1 << 16):
            seed = s1_hi | low
            if ((seed * A + C) & MASK) >> 16 == (out2 & 0xffffffff):
                return JavaRandomCracker(seed)
        return None

    def next_int(self) -> int:
        """Следующий nextInt(), возвращает signed 32-bit int и обновляет состояние."""
        self.seed = (self.seed * A + C) & MASK
        value = self.seed >> 16
        if value >= (1 << 31):
            value -= (1 << 32)
        return value

    def next_n_ints(self, n: int) -> list[int]:
        """Возвращает список следующих n nextInt()"""
        return [self.next_int() for _ in range(n)]


# --- пример использования ---
cracker = JavaRandomCracker.recover_seed(-996005244, 239579678)
if cracker:
    print(cracker.next_n_ints(10))  # получаем следующие 10 значений
