from app.extensions import db
from app.models.text_content import TextContent

def save_text(content, user_id):
    new_text = TextContent(content=content, user_id=user_id)
    db.session.add(new_text)
    db.session.commit()
    return new_text

def get_user_texts(user_id):
    return TextContent.query.filter_by(user_id=user_id).all()