package factory;

import entity.Comanda;

import java.util.Arrays;
import java.util.List;

public class ComandaFactory implements IEntityFactory<Comanda> {
    @Override
    public Comanda createEntity(String line) {
        String[] parts = line.split(";", 3);
        int id = Integer.parseInt(parts[0]);
        List<String> torturi = Arrays.asList(parts[1].split(","));
        String data= parts[2];
        return new Comanda(id,torturi,data);

    }

    @Override
    public String toStringFactory(Comanda entity) {
        StringBuilder sb = new StringBuilder();

        sb.append(entity.getID()).append(";");

        sb.append(String.join(",", entity.getTorturi())).append(";");

        sb.append(entity.getData());

        return sb.toString();
    }
}
