from faker import Faker

fake=Faker()
class FakerUtility:
    def __init__(self):
        self.faker = Faker()

    def create_random_user_name(self):
        """Generate a random username"""
        return self.faker.user_name()

    def create_random_password(self):
        """Generate a random password"""
        return self.faker.password()

    def create_random_full_name(self):
        """Generate a random full name"""
        return self.faker.name()

    def create_random_email_address(self):
        """Generate a random email address"""
        return self.faker.email()
