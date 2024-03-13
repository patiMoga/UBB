package repository;

import entity.Entity;

import java.util.Collection;

public interface IRepository<T extends Entity> extends Iterable<T> {
    void add(T entity) throws DuplicateException;
    void delete(int id);
    T getById(int id);
    Collection<T> getAll();
    void update(T entity);
}


