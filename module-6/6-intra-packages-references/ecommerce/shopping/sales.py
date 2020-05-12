from ecommerce.customer import contact  # absolute import, PEP 8 advise yhis
# relative import with:
# . - current package level
# .. - parrent package level
from ..customer import contact


def calc_tax():
    print("Calculating tax...")
    contact.get_contact()


def calc_shipping():
    print("Shipping...")
