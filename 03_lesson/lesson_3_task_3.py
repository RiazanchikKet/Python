from address import Address
from mailing import Mailing

postal_item = Mailing(
    Address(45678, "Москва", "Патриаршие пруды", 87, 54),
    Address(23456, "Рязань", "Красноармейцев", 89, 679), 116, 649684038564)

from_item = f"{postal_item.from_address.index}, \
{postal_item.from_address.city}, {postal_item.from_address.street}, \
{postal_item.from_address.home} - {postal_item.from_address.flat}"

to_item = f"{postal_item.to_address.index}, {postal_item.to_address.city}, \
{postal_item.to_address.street}, {postal_item.to_address.home} - \
{postal_item.to_address.flat}"

print(f"Отправление {postal_item.track} из {from_item}  в \
{to_item}. Стоимость {postal_item.cost} рублей.")
