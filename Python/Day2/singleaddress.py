class SingleAddress:
    def _init_(self,lastname,firstname,street_address,city,state,country,postal_code):
        self.lastname=lastname
        self.firstname=firstname
        self.street=street_address
        self.city=city
        self.state=state
        self.country=country
        self.postal=postal_code
    def get_details(self):
        return self.lastname+" "+self.firstname+" "+self.street+" "+self.city+" "+self.state+" "+self.country+" "+self.postal
    