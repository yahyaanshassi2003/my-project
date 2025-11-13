from flask import request, flash, redirect, url_for, render_template
from database.db import get_db

def list_ideas():
    db = get_db()
    ideas = db.execute('SELECT * FROM ideas ORDER BY created_at DESC').fetchall()
    return render_template('index.html', ideas=ideas)

def add_idea():
    if request.method == 'POST':
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        if not title:
            flash('Title is required.', 'error')
            return redirect(url_for('ideas.add'))
        db = get_db()
        db.execute('INSERT INTO ideas (title, description) VALUES (?, ?)', (title, description))
        db.commit()
        flash('Idea added successfully!', 'success')
        return redirect(url_for('ideas.index'))
    return render_template('add.html')

def edit_idea(idea_id):
    db = get_db()
    idea = db.execute('SELECT * FROM ideas WHERE id = ?', (idea_id,)).fetchone()
    if not idea:
        flash('Idea not found.', 'error')
        return redirect(url_for('ideas.index'))
    if request.method == 'POST':
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        if not title:
            flash('Title is required.', 'error')
            return redirect(url_for('ideas.edit', idea_id=idea_id))
        db.execute('UPDATE ideas SET title=?, description=? WHERE id=?', (title, description, idea_id))
        db.commit()
        flash('Idea updated successfully!', 'success')
        return redirect(url_for('ideas.index'))
    return render_template('edit.html', idea=idea)

def delete_idea(idea_id):
    db = get_db()
    db.execute('DELETE FROM ideas WHERE id=?', (idea_id,))
    db.commit()
    flash('Idea deleted successfully!', 'success')
    return redirect(url_for('ideas.index'))
