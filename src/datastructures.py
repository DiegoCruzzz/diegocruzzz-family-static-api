
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.family = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if 'id' in member and any(existing_member['id'] == member['id'] for existing_member in self.family):
            raise ValueError(f"El ID {member['id']} ya existe en la familia.")

        if 'id' not in member:
            member['id'] = self._generateId()
            while any(existing_member['id'] == member['id'] for existing_member in self.family):
                member['id'] = self._generateId()
        self.family.append(member)

    def delete_member(self, id):
        self.family = [member for member in self.family if member['id'] != id]

    def get_member(self, id):
        for member in self.family:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        return self.family