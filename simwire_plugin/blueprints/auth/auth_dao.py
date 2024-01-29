from sqlalchemy.exc import NoResultFound, MultipleResultsFound, SQLAlchemyError
from ...models import User
from typing import Union


def load_user(username: str) -> Union[User, None]:

    try:
        user = User.query.filter_by(username=username).first()
    except NoResultFound:
        user = None
    except MultipleResultsFound:
        # Handle the case where multiple users with the same username are found
        # This should not be possible but still want to cover for it because the exception is possible.
        raise Exception("Multiple users found with the same username")
    except SQLAlchemyError as e:
        # Handle other SQLAlchemy errors
        print(f"error occurred: {e}")
        user = None

    return user
