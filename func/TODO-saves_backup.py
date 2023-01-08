Queste funzione deve chiamare il load_device per caricare i file di template e di device così da sapere dove sono le cartelle di saves e states
Le cartelle di saves e di states sono prese dai valori rispettivi di saves e states
Deve copiarsi queste cartelle in devices/<friendly_name>/backups
Deve salvare nel file ./retroman.cfg l'id del device e quando è stata fatto il suo ultimo backup