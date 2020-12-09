import java.io.*;

import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamConstants;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamReader;

public final class XML implements XMLStreamConstants {

    public static void main(String[] args) throws Exception {
        System.out.println("File: " + args[0]);
        try( FileReader srcXml = new FileReader(new File(args[0])) ) {
            new XML().parse(srcXml);
        }
    }

	private XMLInputFactory factory;

	public XML() {
		try {
			factory = XMLInputFactory.newInstance();
			factory.setProperty(XMLInputFactory.IS_REPLACING_ENTITY_REFERENCES, Boolean.FALSE);
			factory.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, Boolean.FALSE);
			factory.setProperty(XMLInputFactory.IS_COALESCING, Boolean.FALSE);
			factory.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE, Boolean.FALSE);
			factory.setProperty(XMLInputFactory.IS_VALIDATING, Boolean.FALSE);
			factory.setProperty(XMLInputFactory.SUPPORT_DTD, Boolean.FALSE);

		} catch (Exception ex) {
            ex.printStackTrace();
		}
	}

	public void parse(Reader document) throws XMLStreamException,  IOException {
		try {
			parse(factory.createXMLStreamReader(document));
		} finally {
			document.close();
		}

	}

	private void parse(XMLStreamReader streamReader) throws XMLStreamException {
		try {
            System.out.println("Start Doc");
			while (streamReader.hasNext()) {
				switch (streamReader.next()) {
				case START_ELEMENT:
					//System.out.println("Start Element: " + streamReader.getName().toString());
					break;
				case CHARACTERS:
                    //System.out.println("CHARACTERS: " + streamReader.getText());
					break;
                default:
					break;
				}
			}
		} finally {
				streamReader.close();
		}
	}

}
