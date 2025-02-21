from app import create_app, db
from app.models.text_content import TextContent

app = create_app()

with app.app_context():
    # Test verileri ekle
    db.session.add(TextContent(user_id=1, content='Merhaba, bu bir test içeriğidir.'))
    db.session.add(TextContent(user_id=1, content='Flask ile API geliştiriyorum.'))
    db.session.add(TextContent(user_id=2, content='Başka bir kullanıcının içeriği.'))
    db.session.commit()
    print('Test verileri eklendi.')