package entity;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class EntityTest {

    @Test
    void getID() {
        // Arrange
        int expectedId = 42;
        Entity entity = new TestEntity(expectedId);

        // Act
        int actualId = entity.getID();

        // Assert
        assertEquals(expectedId, actualId);
    }

    // Create a subclass for testing purposes
    private static class TestEntity extends Entity {
        public TestEntity(int id) {
            super(id);
        }
    }
}
