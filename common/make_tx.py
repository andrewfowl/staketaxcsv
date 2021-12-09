
from common.Exporter import (Row, TX_TYPE_UNKNOWN, TX_TYPE_TRANSFER, TX_TYPE_SPEND, TX_TYPE_INCOME)
from settings_csv import DONATION_WALLETS


def make_spend_tx(txinfo, sent_amount, sent_currency):
    return _make_tx_sent(txinfo, sent_amount, sent_currency, TX_TYPE_SPEND)


def make_just_fee_tx(txinfo, fee_amount, fee_currency):
    return _make_tx_sent(txinfo, fee_amount, fee_currency, TX_TYPE_SPEND, empty_fee=True)


def make_transfer_out_tx(txinfo, sent_amount, sent_currency, dest_address=None):
    if DONATION_WALLETS and dest_address in DONATION_WALLETS:
        return make_spend_tx(txinfo, sent_amount, sent_currency)
    else:
        return _make_tx_sent(txinfo, sent_amount, sent_currency, TX_TYPE_TRANSFER)


def make_transfer_in_tx(txinfo, received_amount, received_currency):
    # Adjust to no fees for transfer-in transactions
    txinfo.fee = ""
    txinfo.fee_currency = ""

    if DONATION_WALLETS and txinfo.wallet_address in DONATION_WALLETS:
        return _make_tx_received(txinfo, received_amount, received_currency, TX_TYPE_INCOME)
    else:
        return _make_tx_received(txinfo, received_amount, received_currency, TX_TYPE_TRANSFER)


def make_simple_tx(txinfo, tx_type, z_index=0):
    fee_currency = txinfo.fee_currency if txinfo.fee else ""

    row = Row(
        timestamp=txinfo.timestamp,
        tx_type=tx_type,
        received_amount="",
        received_currency="",
        sent_amount="",
        sent_currency="",
        fee=txinfo.fee,
        fee_currency=fee_currency,
        exchange=txinfo.exchange,
        wallet_address=txinfo.wallet_address,
        txid=txinfo.txid,
        url=txinfo.url,
        z_index=z_index,
        comment=txinfo.comment
    )
    return row


def make_unknown_tx(txinfo):
    return make_simple_tx(txinfo, TX_TYPE_UNKNOWN)


def make_unknown_tx_with_transfer(txinfo, sent_amount, sent_currency, received_amount,
                                  received_currency, empty_fee=False, z_index=0):
    return _make_tx_exchange(
        txinfo, sent_amount, sent_currency, received_amount, received_currency, TX_TYPE_UNKNOWN,
        empty_fee=empty_fee, z_index=z_index
    )


def _make_tx_received(txinfo, received_amount, received_currency, tx_type, txid=None, empty_fee=False, z_index=0):
    txid = txid if txid else txinfo.txid
    fee = "" if empty_fee else txinfo.fee
    fee_currency = txinfo.fee_currency if fee else ""

    row = Row(
        timestamp=txinfo.timestamp,
        tx_type=tx_type,
        received_amount=received_amount,
        received_currency=received_currency,
        sent_amount="",
        sent_currency="",
        fee=fee,
        fee_currency=fee_currency,
        exchange=txinfo.exchange,
        wallet_address=txinfo.wallet_address,
        txid=txid,
        url=txinfo.url,
        z_index=z_index,
        comment=txinfo.comment
    )
    return row


def _make_tx_sent(txinfo, sent_amount, sent_currency, tx_type, empty_fee=False, z_index=0):
    fee = "" if empty_fee else txinfo.fee
    fee_currency = txinfo.fee_currency if fee else ""

    row = Row(
        timestamp=txinfo.timestamp,
        tx_type=tx_type,
        received_amount="",
        received_currency="",
        sent_amount=sent_amount,
        sent_currency=sent_currency,
        fee=fee,
        fee_currency=fee_currency,
        exchange=txinfo.exchange,
        wallet_address=txinfo.wallet_address,
        txid=txinfo.txid,
        url=txinfo.url,
        z_index=z_index,
        comment=txinfo.comment
    )
    return row


def _make_tx_exchange(txinfo, sent_amount, sent_currency, received_amount, received_currency, tx_type,
                      txid=None, empty_fee=False, z_index=0):
    txid = txid if txid else txinfo.txid
    fee = "" if empty_fee else txinfo.fee
    fee_currency = txinfo.fee_currency if fee else ""

    row = Row(
        timestamp=txinfo.timestamp,
        tx_type=tx_type,
        received_amount=received_amount,
        received_currency=received_currency,
        sent_amount=sent_amount,
        sent_currency=sent_currency,
        fee=fee,
        fee_currency=fee_currency,
        exchange=txinfo.exchange,
        wallet_address=txinfo.wallet_address,
        txid=txid,
        url=txinfo.url,
        z_index=z_index,
        comment=txinfo.comment
    )
    return row
