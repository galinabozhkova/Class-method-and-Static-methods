from MovieWorld.customer import Customer


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if customer not in self.customers and len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for el in self.customers:
            if el.id == customer_id:
                for dvd in el.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{el.name} has already rented {dvd.name}"
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.is_rented:
                            return "DVD is already rented"
                        if dvd.age_restriction > el.age:
                            return f"{el.name} should be at least {dvd.age_restriction} to rent this movie"
                    el.rented_dvds.append(dvd)
                    dvd.is_rented = True
                    return f"{el.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for el in self.customers:
            if el.id == customer_id:
                for dvd in el.rented_dvds:
                    if dvd.id == dvd_id:
                        el.rented_dvds.remove(dvd)
                        dvd.is_rented = False
                        return f"{el.name} has successfully returned {dvd.name}"
            return f"{el.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += repr(customer) + "\n"
        for dvd in self.dvds:
                result += repr(dvd) + "\n"
        return result


