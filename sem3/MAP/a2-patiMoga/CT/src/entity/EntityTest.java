package entity;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class EntityTest {

    @Test
    void getID() {
        int id = 123;
        Entity entity = new ConcreteEntity(id);
        int result = entity.getID();

        assertEquals(id, result);
    }

    @Test
    void modify() {
        int id = 123;
        Entity entity = new ConcreteEntity(id);

        entity.modify("some string");
        assertTrue(true);
    }
    private static class ConcreteEntity extends Entity {
        public ConcreteEntity(int id) {
            super(id);
        }
    }
}
