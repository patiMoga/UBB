package entity;

import entity.Tort;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class TortTest {

    @Test
    void getTip() {
        // Arrange
        Tort tort = new Tort(1, "Chocolate");

        // Act
        String tip = tort.getTip();

        // Assert
        assertEquals("Chocolate", tip);
    }

    @Test
    void setTip() {
        // Arrange
        Tort tort = new Tort(1, "Chocolate");

        // Act
        tort.setTip("Vanilla");

        // Assert
        assertEquals("Vanilla", tort.getTip());
    }

    @Test
    void toStringTest() {
        // Arrange
        Tort tort = new Tort(1, "Chocolate");

        // Act
        String toStringResult = tort.toString();

        // Assert
        assertEquals("Tort{id=1, tip='Chocolate'}", toStringResult);
    }
}
