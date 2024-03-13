package repository;

import entity.Entity;

import java.util.*;

public class Repo<T extends Entity> extends AbsRepo<T> {

    public Repo() {
        this.entities = new ArrayList<>();

    }

    @Override
    public void add(T entity) throws DuplicateException {
        if(!entities.contains(entity))
            entities.add(entity);
        else
            throw new DuplicateException("Deja exista entitatea!");

    }

    @Override
    public void delete(int id) {
        if(getById(id)!=null)
            entities.removeIf(entity -> entity.getID() == id);
        else
            throw new NoSuchElementException("Adaugati un id valid!");

    }

    @Override
    public T getById(int id) {
        for(T entity:entities)
        {
            if(entity.getID()==id)
            {
                return entity;
            }
        }
        return null;
    }

    @Override
    public Collection<T> getAll() {
        return new ArrayList<>(entities) ;
    }

    @Override
    public void update(T entity) {
//        for(int i = 0; i < entities.size(); i++) {
//            T existingEntity = entities.get(i);
//            if(existingEntity.getID() == entity.getID()) {
//                existingEntity.
//            }
//        }
        delete(entity.getID());
        entities.add(entity);
    }
    @Override
    public Iterator<T> iterator() {
        return new ArrayList<T>(entities).iterator();
    }
}
