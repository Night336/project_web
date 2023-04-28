from typing import List
import os
import sys

from accessor.base_accessor import BaseAccessor
from data import Review

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))


class ReviewAccessor(BaseAccessor):
    def get_all_revews(self) -> List[Review]:
        return self.session.query(Review).all()

    def get_review_by_id(self, product_id: int) -> Review:
        return self.session.query(Review).get(product_id)

    def create_review(self, user_id: int, product_id: int, text: str) -> Review:
        review = Review(user_id=user_id, product_id=product_id, text=text)
        self.session.add(review)
        self.session.commit()
        self.session.refresh(review)
        return review

    def update_review(self, review_id: int, text: str) -> Review:
        review = self.session.query(Review).get(review_id)
        review.text = text

        self.session.commit()
        self.session.refresh(review)
        return review

    def delete_review(self, review_id: int) -> None:
        self.session.query(Review).filter(Review.id == review_id).delete()
        self.session.commit()
