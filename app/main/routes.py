from flask import render_template, redirect, url_for, flash, request
# pyrefly: ignore [missing-import]
from flask_login import login_required, current_user
from app import db
from app.main import main
from app.main.forms import KitapForm, IncelemeForm
from app.models import Kitap, Inceleme

@main.route('/')
@login_required
def index():
    # Only list books added by the current user
    kitaplar = Kitap.query.filter_by(user_id=current_user.id).order_by(Kitap.eklendigi_tarih.desc()).all()
    return render_template('main/index.html', kitaplar=kitaplar)

@main.route('/kitap/ekle', methods=['GET', 'POST'])
@login_required
def kitap_ekle():
    form = KitapForm()
    if form.validate_on_submit():
        yeni_kitap = Kitap(
            baslik=form.baslik.data,
            yazar=form.yazar.data,
            yayin_yili=form.yayin_yili.data,
            user_id=current_user.id
        )
        db.session.add(yeni_kitap)
        db.session.commit()
        flash('Kitap başarıyla eklendi.', 'success')
        return redirect(url_for('main.index'))
    return render_template('main/kitap_ekle.html', form=form)

@main.route('/kitap/<int:id>', methods=['GET', 'POST'])
@login_required
def kitap_detay(id):
    kitap = Kitap.query.get_or_404(id)
    form = IncelemeForm()
    
    if form.validate_on_submit():
        yeni_inceleme = Inceleme(
            icerik=form.icerik.data,
            puan=int(form.puan.data),
            user_id=current_user.id,
            kitap_id=kitap.id
        )
        db.session.add(yeni_inceleme)
        db.session.commit()
        flash('İncelemeniz başarıyla eklendi.', 'success')
        return redirect(url_for('main.kitap_detay', id=kitap.id))
        
    # Ortak yorum mantığı: Aynı başlık ve yazara sahip tüm kitapların yorumları
    ortak_incelemeler = Inceleme.query.join(Kitap).filter(
        Kitap.baslik == kitap.baslik,
        Kitap.yazar == kitap.yazar
    ).order_by(Inceleme.olusturulma_tarihi.desc()).all()
        
    return render_template('main/kitap_detay.html', kitap=kitap, form=form, ortak_incelemeler=ortak_incelemeler)

@main.route('/kitap/<int:id>/sil', methods=['POST'])
@login_required
def kitap_sil(id):
    kitap = Kitap.query.get_or_404(id)
    # Check if the book belongs to the current user
    if kitap.user_id != current_user.id:
        flash('Bu kitabı silme yetkiniz yok.', 'danger')
        return redirect(url_for('main.index'))
    
    db.session.delete(kitap)
    db.session.commit()
    flash('Kitap başarıyla silindi.', 'success')
    return redirect(url_for('main.index'))

@main.route('/profil')
@login_required
def profil():
    toplam_kitap = len(current_user.kitaplar)
    toplam_inceleme = len(current_user.incelemeler)
    incelemeler = Inceleme.query.filter_by(user_id=current_user.id).order_by(Inceleme.olusturulma_tarihi.desc()).all()
    
    return render_template('main/profil.html', 
                           toplam_kitap=toplam_kitap, 
                           toplam_inceleme=toplam_inceleme, 
                           incelemeler=incelemeler)
