class Group:
    def __init__(self):
        group_id = 0
        members = []
        leaders = []
        reports = []
        join_requests = []
        size = 0

    def add_member(self, user, adder):
        # adder is the user try to add someone
        # this is a check to make sure the adder is an admin
        # returns True if user successfully added, False otherwise
        if adder in self.members:
            self.members.append(user)
            return True
        elif adder in self.leaders:
            self.members.append(user)
            return True
        else:
            return False

    def add_leader(self, user, adder):
        # adder is the leader trying to add someone
        if adder in self.leaders:
            self.leaders.append(user)
            return True
        else:
            return False

    def add_report(self, report):
        self.reports.append(report)

    def is_leader(self, user):
        # checks if the given user is a leader of the group
        if user in self.leaders:
            return True
        else:
            return False

    def is_member(self, user):
        # checks if the given user is a member of the group
        if user in self.members:
            return True
        else:
            return False

    def request_to_join(self, user):
        # Adds the user to a list of users who wish to join
        self.join_requets.append(user)

    def rm_report(self, report):
        # Removes report from reports
        while reports.count(report) > 0:
            self.reports.remove(report)
        return True