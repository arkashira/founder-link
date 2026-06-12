class MVPBuilder:
    def __init__(self):
        self.template = 'Basic Template'

    def build(self, user):
        return f'MVP for {user.name}'

mvp_builder = MVPBuilder()
