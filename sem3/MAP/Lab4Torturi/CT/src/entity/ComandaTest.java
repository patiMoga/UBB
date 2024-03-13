package entity;
import entity.Comanda;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ComandaTest {

    @Test
    void getTorturi() {
        // Arrange
        List<String> torturi = Arrays.asList("Chocolate", "Vanilla", "Strawberry");
        Comanda comanda = new Comanda(1, torturi, "2023-12-31");

        // Act
        List<String> resultTorturi = comanda.getTorturi();

        // Assert
        assertEquals(torturi, resultTorturi);
    }

    @Test
    void getData() {
        // Arrange
        List<String> torturi = Arrays.asList("Chocolate", "Vanilla", "Strawberry");
        Comanda comanda = new Comanda(1, torturi, "2023-12-31");

        // Act
        String resultData = comanda.getData();

        // Assert
        assertEquals("2023-12-31", resultData);
    }


}
