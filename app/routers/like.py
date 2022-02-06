from fastapi import APIRouter, status, Response, HTTPException, Depends
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/like",
    tags=["Like"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def like(like: schemas.Like, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == like.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {like.post_id} does not exist")

    like_query = db.query(models.Like).filter(models.Like.post_id == like.post_id, models.Like.user_id == current_user.id)
    like_found = like_query.first()


    if (like.direction == 1):
        if like_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} has already liked the post {like.post_id}")

        new_vote = models.Like(post_id = like.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully liked the post"}


    else:
        if not like_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Like does not Exist")
        
        like_query.delete(synchronize_session=False)    
        
        db.commit()
        return {"message": "Successfully Unliked the Post"}

