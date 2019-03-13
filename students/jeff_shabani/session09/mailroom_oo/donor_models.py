#!/usr/bin/env python3

from collections import OrderedDict
from operator import itemgetter
from pathlib import Path

# from students.jeff_shabani.session09.write_a_letter import write_a_letter

"""
Framework accessing multiple donors.
"""

# Jeff Shabani
# March 1st, 2019
# Python 210, Session 9
# donors.py

class Donor():
    donors = {}
    donations = list()

    def __init__(self, name=''):
        self.name = name
        self.donation = []

    def add_donor(self, answer, amount):
        """
        Adds a donor to the donors list
        :param answer: name
        :param amount: amount to donate
        :return: updated donors dictionary
        """
        self.donations.append(amount)
        self.donors[answer] = self.donations

    def write_a_letter(self, name, amount):
        return f'Dear {name},\n\nThank you for your kind donation of ${amount:,.0f}\n\n' \
            f'Rest assured that these funds will be put to optimal use.\n\n' \
            f'Best regards,\n' \
            f'The Charitable Charities Team'

    def write_a_single_letter(self, answer, amount):
        """
        writes and saves a single letter as a txt file
        :param answer: the donor name entered
        :param amount: the amount to be entered
        :return: text file and path object
        """
        with open(f'{answer}.txt', 'wt') as letter:
            letter.write(self.write_a_letter(answer, amount))
        letter_path = f'{Path.cwd()}//{answer}.txt'
        return Path(letter_path).exists()

    def view_donor_names(self):
        [print(name) for name in self.donors]


class DonorCollection(Donor):

    donors = {'William B': [120, 130, 50],
              'Sammy Maudlin': [500, 125, 670, 1000],
              'Bobby Bittman': [10],
              'Skip Bittman': [75, 125, 19],
              'Ashley Lashbrooke': [10000, 15000]}

    def __init__(self, name=''):
        self.name = name
        self.donation = 0
        super().__init__()

    def view_donor_names(self):
        [print(name) for name in self.donors]

    def create_new_donors_dict(self):
        """
        dictionay comprehension of donors with sum, len, and average of values.
        """
        new_donors = {k: (sum(v), len(v), (len(v) / len(v))) for k, v in self.donors.items()}
        return OrderedDict(sorted(new_donors.items(), key=itemgetter(1), reverse=True))

    def write_letters_to_all_donors(self):
        for donor, total in self.create_new_donors_dict().items():
            with open(f'{donor}.txt', 'wt') as letter:
                letter.write(Donor.write_a_letter(self, donor, total[0]))

    def create_report(self):
        header = f'{"Name".ljust(20)}{"| Total Donations".rjust(20)}{"| # of Donations".rjust(20)}' \
            f'{"| Average Donation".rjust(20)}'
        print(header)
        print('-' * len(header))

        # get donors and totals from new_donors dictionary
        for k, v in self.create_new_donors_dict().items():
            print(f'{str(k).ljust(20)}{str(v[0]).rjust(20)}{str(v[1]).rjust(20)}{str(v[2]).rjust(20)}')
