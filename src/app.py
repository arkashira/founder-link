import argparse
from src.user import User, user_repository
from src.mvp_builder import mvp_builder

def create_account(name, email):
    user = User(id=len(user_repository.data) + 1, name=name, email=email)
    user_repository.create(user)
    return user

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--email', required=True)
    args = parser.parse_args()
    user = create_account(args.name, args.email)
    mvp = mvp_builder.build(user)
    print(f'Account created for {user.name}')
    print(f'MVP: {mvp}')

if __name__ == '__main__':
    main()
