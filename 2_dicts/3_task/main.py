import re

def format_phone(phone_number: str) -> str:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    phone_number = re.sub(r"\D", "", phone_number)
    formatted_phone_number = re.sub(
        r"(89|79|9)(\d{2})(\d{3})(\d{2})(\d{2})",
        r"8 (9\2) \3-\4-\5", phone_number
    )

    return formatted_phone_number
