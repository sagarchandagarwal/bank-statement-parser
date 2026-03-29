"""
bank-statement-parser
~~~~~~~~~~~~~~~~~~~~~
Parse Indian bank PDF statements into structured transaction data.

Supported banks:
  - HDFC Bank (savings/current)
  - HDFC Credit Card
  - SBI Bank
  - SBI Credit Card
  - Yes Bank
  - Yes Credit Card
  - RBL Bank
  - RBL Credit Card
  - IndusInd Credit Card
  - One Credit Card
  - Standard Chartered Bank

Basic usage::

    from bank_statement_parser import parse, list_supported_banks

    result = parse("statement.pdf")
    # result = {
    #   "bank_type": "HDFC Bank",
    #   "transactions": [...],
    #   "account_info": ""
    # }

    # With a password-protected PDF:
    result = parse("statement.pdf", password="mypassword")

    print(list_supported_banks())
"""

from bank_statement_parser.parsers.detector import detect_and_parse

__version__ = "0.1.0"
__all__ = ["parse", "detect_and_parse", "list_supported_banks"]

_SUPPORTED_BANKS = [
    "HDFC Bank",
    "HDFC Credit Card",
    "SBI Bank",
    "SBI Credit Card",
    "Yes Bank",
    "Yes Credit Card",
    "RBL Bank",
    "RBL Credit Card",
    "IndusInd Credit Card",
    "One Credit Card",
    "Standard Chartered Bank",
]


def parse(filepath: str, password: str = None) -> dict:
    """Parse a bank statement PDF and return structured transaction data.

    Args:
        filepath: Absolute or relative path to the PDF file.
        password: Optional password for encrypted PDFs.

    Returns:
        A dict with keys:
            - ``bank_type`` (str): Human-readable bank/card name.
            - ``transactions`` (list[dict]): List of transactions, each with
              keys ``serial``, ``date``, ``description``, ``debit``,
              ``credit``, ``balance``.
            - ``account_info`` (str): Account metadata (may be empty).

    Raises:
        Exception: If the PDF is password-protected and no/wrong password
                   is given, or if the bank format is unsupported.
        ValueError: If no transactions could be extracted.
    """
    result = detect_and_parse(filepath, password=password)
    if result is None:
        raise ValueError(
            "Could not parse any transactions. "
            "The bank format may not be supported, or the PDF may be password-protected."
        )
    return result


def list_supported_banks() -> list:
    """Return a list of supported bank/card names."""
    return list(_SUPPORTED_BANKS)
