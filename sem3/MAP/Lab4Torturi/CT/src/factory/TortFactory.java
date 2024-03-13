package factory;

import entity.Tort;
import factory.IEntityFactory;

public class TortFactory implements IEntityFactory<Tort> {

    private static final String DELIMITER = ";";

    @Override
    public Tort createEntity(String line) {
        int id=Integer.parseInt(line.split(";")[0]);
        String tip=line.split(";")[1];

        return new Tort(id,tip);
    }

    @Override
    public String toStringFactory(Tort entity) {
        return entity.getID() + DELIMITER + entity.getTip();
    }


}
