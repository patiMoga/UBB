package factory;

import entity.Tort;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class TortFactoryTest {

    @Test
    void createEntity() {
        // Arrange
        TortFactory tortFactory = new TortFactory();
        String inputLine = "1;Chocolate";

        // Act
        Tort tort = tortFactory.createEntity(inputLine);

        // Assert
        assertEquals(1, tort.getID());
        assertEquals("Chocolate", tort.getTip());
    }

    @Test
    void toStringFactory() {
        // Arrange
        TortFactory tortFactory = new TortFactory();
        Tort tort = new Tort(1, "Chocolate");

        // Act
        String resultString = tortFactory.toStringFactory(tort);

        // Assert
        assertEquals("1;Chocolate", resultString);
    }
}
