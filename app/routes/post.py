from fastapi import HTTPException, Depends, status, Response, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from typing import List, Optional
from sqlalchemy import func

router = APIRouter(prefix="/posts", tags=["post"])


# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])  # JOIN
def get_posts(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
    limit: int = 3,
    skip: int = 0,
    search: Optional[str] = "",
):
    # RETREIVING DATA
    # # posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all() Get All items with owner id
    posts = (
        db.query(models.Post)
        .filter(models.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )  # QUERY PARAMETER

    # JOIN
    result = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Post.id == models.Vote.post_id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )

    return result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    new_posts = models.Post(
        owner_id=current_user.id, **post.dict()
    )  # Create With User id
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return new_posts


@router.get("/latest")
def get_latest_post(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    # post = my_posts[len(my_posts)-1]
    # return {"detail": post}
    post = db.query(models.Post)
    return {"data": "latest post"}


# @router.get("/{id}", response_model=schemas.Post)
@router.get("/{id}", response_model=List[schemas.PostOut])  # JOIN
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    posts = db.query(models.Post).filter(models.Post.id == id).first()

    # JOIN
    # result = (
    #     db.query(models.Post.title, models.User.email)
    #     .join(models.User, models.Post.owner_id == models.User.id)
    #     .filter(models.Post.id == id)
    #     .first()
    # )
    result = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Post.id == models.Vote.post_id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.id == id)
        .all()
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    if result.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )
    return result


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    deleted_query = db.query(models.Post).filter(models.Post.id == id)
    deleted_post = deleted_query.first()
    if not deleted_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exists",
        )

    if deleted_post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )
    deleted_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(
    id: int,
    post: schemas.PostBase,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    posts_query = db.query(models.Post).filter(models.Post.id == id)

    updated_post = posts_query.first()

    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exists",
        )

    if updated_post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )

    posts_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return posts_query.first()
