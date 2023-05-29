"""Module with functions."""

def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
    else:
        primeiro = numbers[0]  # o primeiro número da soma
        for i in range(0, len(numbers)):
            if numbers[i] > primeiro:
                primeiro = numbers[i]
        numbers.remove(primeiro)
        segundo = numbers[0]
        for j in range(0, len(numbers)):
            if numbers[j] > segundo:
                segundo = numbers[j]         
        return segundo, primeiro
