package repository;

import entity.Entity;

import java.util.Collection;

public interface IRepository<T extends Entity> extends Iterable<T> {
    public void add(T entity) throws DuplicateException;
    public void delete(int id);
    public T getById(int id);
    public Collection<T> getAll();
    public void update(int id,String string);


}
