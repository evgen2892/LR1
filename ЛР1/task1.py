
from abc import ABC, abstractmethod

class PhysicalObject(ABC):
    """
    Физический объект.

    Атрибуты:
        name: Непустое название.
        mass_kg: Масса (кг), > 0.
        volume_m3: Объём (m^3), >= 0.
    Doctest:
    >>> class _Stone(PhysicalObject):
    ...     def move_to(self, x: float, y: float, z: float) -> None: ...
    ...     def apply_force(self, newton: float, seconds: float) -> None: ...
    ...     def describe(self) -> str: ...
    ...
    >>> s = _Stone("stone", 1.0, 0.1)
    >>> (s.name, s.mass_kg, s.volume_m3)
    ('stone', 1.0, 0.1)
    >>> _Stone("", 1.0, 0.1)
    Traceback (most recent call last):
    ...
    ValueError: name must be a non-empty string
    """

    def __init__(self, name: str, mass_kg: float, volume_m3: float) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if mass_kg <= 0:
            raise ValueError("mass_kg must be > 0")
        if volume_m3 < 0:
            raise ValueError("volume_m3 must be >= 0")

        self.name: str = name
        self.mass_kg: float = float(mass_kg)
        self.volume_m3: float = float(volume_m3)

    @abstractmethod
    def move_to(self, x: float, y: float, z: float) -> None:
        """
        Переместить объект в точку.

        Args:
            x: Координата X.
            y: Координата Y.
            z: Координата Z.

        Returns:
            None
        """
        ...

    @abstractmethod
    def apply_force(self, newton: float, seconds: float) -> None:
        """
        Приложить силу.
        Args:
            newton: Сила (Н).
            seconds: Время (с), > 0 (валидация в реальной реализации).
        Returns:
            None
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Описание объекта.

        Returns:
            Текстовое описание.
        """
        ...


class Container(ABC):
    """
    Контейнер/ёмкость.

    Атрибуты:
        capacity_l: Вместимость (л), > 0.
        current_l: Текущий объём (л), 0..capacity_l.
        is_sealed: Герметичность.
    """

    def __init__(self, capacity_l: float, current_l: float, is_sealed: bool) -> None:
        if capacity_l <= 0:
            raise ValueError("capacity_l must be > 0")
        if not (0 <= current_l <= capacity_l):
            raise ValueError("current_l must be between 0 and capacity_l")

        self.capacity_l: float = float(capacity_l)
        self.current_l: float = float(current_l)
        self.is_sealed: bool = bool(is_sealed)

    @abstractmethod
    def fill(self, amount_l: float) -> float:
        """
        Наполнить контейнер.
        Args:
            amount_l: Объём (л), > 0 (валидация в реальной реализации).
        Returns:
            Новый current_l (л).
        """
        ...

    @abstractmethod
    def drain(self, amount_l: float) -> float:
        """
        Слить из контейнера.
        Args:
            amount_l: Объём (л), > 0 (валидация в реальной реализации).
        Returns:
            Новый current_l (л).
        """
        ...
    @abstractmethod
    def seal(self, sealed: bool) -> None:
        """
        Установить герметичность.

        Args:
            sealed: True/False.
        Returns:
            None
        """
        ...
class PoweredDevice(ABC):
    """
    Устройство с питанием.
    Атрибуты:
        model: Непустая модель.
        max_power_w: Макс. мощность (Вт), > 0.
        is_on: Включено ли устройство.
    """

    def __init__(self, model: str, max_power_w: float, is_on: bool) -> None:
        if not isinstance(model, str) or not model.strip():
            raise ValueError("model must be a non-empty string")
        if max_power_w <= 0:
            raise ValueError("max_power_w must be > 0")

        self.model: str = model
        self.max_power_w: float = float(max_power_w)
        self.is_on: bool = bool(is_on)

    @abstractmethod
    def turn_on(self) -> None:
        """
        Включить.

        Returns:
            None
        """
        ...

    @abstractmethod
    def turn_off(self) -> None:
        """
        Выключить.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_power(self, power_w: float) -> None:
        """
        Установить мощность.

        Args:
            power_w: Мощность (Вт), 0..max_power_w (валидация в реальной реализации).

        Returns:
            None
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
