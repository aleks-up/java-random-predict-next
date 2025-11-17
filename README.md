# java-random-predict-next

1. Восстанавливает внутренний seed Java Random по двум подряд идущим 32‑битным выходам;
2. Полностью повторяет поведение стандартного java.util.Random
3. Точно предсказывает любое количество дальнейшних значений nextInt();

📌 Пример
<code>
cracker = JavaRandomCracker.recover_seed(out1, out2)
print(cracker.next_n_ints(5))   # предсказать 5 следующих nextInt()
</code>

Где out1 и out2 — два последовательных значения nextInt() (signed 32-bit).
