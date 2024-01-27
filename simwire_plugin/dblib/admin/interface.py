from abc import ABC, abstractmethod


# interface for Admin Class
class IAdmin(ABC):

    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass

    @abstractmethod
    def get_user_by_username(self, username: str):
        pass
