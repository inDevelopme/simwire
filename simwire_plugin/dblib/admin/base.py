from sqlalchemy.exc import NoResultFound, MultipleResultsFound, SQLAlchemyError

from .interface import IAdmin
from simwire_plugin.models.user import User


# Admin class that will implement the interface
class AdminBase(IAdmin):

    def __init__(self):
        pass

    def get_user_by_id(self, user_id: int) -> User:

        user = None
        try:
            user = User.query.get(user_id)
        except NoResultFound as e:
            print(f"Error: No Results found for {str(user_id)}, {e}")
        except MultipleResultsFound as e:
            print(f"Error: Multiple Results found for {str(user_id)}, {e}")
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return user

    def get_user_by_username(self, username: str) -> [User, None]:
        user = None
        try:
            user = User.query.filter_by(username=username).first()
        except NoResultFound as e:
            print(f"Error: No Results found for {username}, {e}")
        except MultipleResultsFound as e:
            print(f"Error: Multiple Results found for {username}, {e}")
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return user
