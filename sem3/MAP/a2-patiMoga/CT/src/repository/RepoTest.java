package repository;

import entity.Entity;
import entity.Tort;
import org.junit.jupiter.api.Test;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

class RepoTest {

    @Test
    void add() {
        Repo<Tort> repo = new Repo<>();
        Tort entity1 = new Tort(1,"HAHAH");
        assertDoesNotThrow(() -> repo.add(entity1));
        assertTrue(repo.getAll().contains(entity1));
        assertThrows(DuplicateException.class, () -> repo.add(entity1)); // Ensure adding duplicate throws DuplicateException
    }

    @Test
    void delete() throws DuplicateException {
        int idToDelete=1;

        Repo<Tort> repo = new Repo<>();
        Tort entity1 = new Tort(1,"HAHAH");
        Tort entity2 = new Tort(2,"BAHAH");
        repo.add(entity1);
        repo.add(entity2);
        repo.delete(idToDelete);
        Collection<Tort> remainingEntities = repo.getAll();

        assertTrue(remainingEntities.stream().noneMatch(entity -> entity.getID() == idToDelete));

        assertEquals(1, remainingEntities.size());

        NoSuchElementException exception = assertThrows(NoSuchElementException.class,
                () -> repo.delete(4));
        assertEquals("Adaugati un id valid!", exception.getMessage());
    }

    @Test
    void getById() throws DuplicateException {
        Repo<Tort> repo = new Repo<>();
        Tort entity1 = new Tort(1,"HAHAH");
        Tort entity2 = new Tort(2,"BHAH");
        repo.add(entity1);
        repo.add(entity2);

        // Act
        Entity resultEntity = repo.getById(1);

        // Assert
        assertEquals(entity1, resultEntity);
        assertNull(repo.getById(3)); // Ensure getting non-existent entity returns null
    }

    @Test
    void getAll() throws DuplicateException {
        // Arrange
        Repo<Tort> repo = new Repo<>();
        Tort entity1 = new Tort(1,"HAHAH");
        Tort entity2 = new Tort(1,"BAHAH");
        repo.add(entity1);
        repo.add(entity2);

        Collection<Tort> allEntities = repo.getAll();
        assertTrue(allEntities.contains(entity1));
        assertTrue(allEntities.contains(entity2));
    }

    @Test
    void update() throws DuplicateException {
        Repo<Tort> repo = new Repo<>();
        Tort tort = new Tort(1, "Chocolate");
        Tort tort1 = new Tort(1, "VANI");
        repo.add(tort);
        repo.update(1,"VANI");
        assertEquals(tort.getTip(),tort1.getTip());


    }

    @Test
    void iterator() throws DuplicateException {
        // Arrange
        Repo<Tort> repo = new Repo<>();
        Tort entity1= new Tort(1,"HAHAH");
        Tort entity2 = new Tort(2,"BAHAH");
        repo.add(entity1);
        repo.add(entity2);

        Iterator<Tort> iterator = repo.iterator();

        assertTrue(iterator.hasNext());
        assertEquals(entity1, iterator.next());
        assertTrue(iterator.hasNext());
        assertEquals(entity2, iterator.next());
        assertFalse(iterator.hasNext());
    }
}
