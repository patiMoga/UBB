package factory;

import entity.Entity;

public interface IEntityFactory<T extends Entity> {
    public T createEntity(String line);
    public String toStringFactory(T entity);
}
