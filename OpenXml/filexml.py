import xml.etree.ElementTree as ET

# Percorso del file XML da aprire
file_xml = "C:\\GameMultiPlatform\\SetupController\\ns_controller_properties.xml"

# Parse del file XML
tree = ET.parse(file_xml)
root = tree.getroot()

# Ora puoi lavorare con il contenuto del file XML attraverso l'oggetto root
# ad esempio, puoi accedere agli elementi e ai loro attributi

# Stampare il tag dell'elemento radice
print("Tag dell'elemento radice:", root.tag)

# Stampare gli attributi dell'elemento radice
print("Attributi dell'elemento radice:", root.attrib)

# Attraversare gli elementi figlio dell'elemento radice
# Attraversare gli elementi del file XML
for element in root.iter():
    # Stampa il tag dell'elemento
    print("Tag:", element.tag)
    
    # Stampa gli attributi dell'elemento
    if element.attrib:
        print("Attributi:")
        for attrib_name, attrib_value in element.attrib.items():
            print(f"\t{attrib_name}: {attrib_value}")