Questa funzione deve prendere la lista globale della libreria attualmente caricata che si tova in devices/nomelibreria/nomelibreria.cfg
deve vedere quali roms sono marchiate come "sync" e copiarle sul device attualmente caricato se non ci sono già
deve inoltre segnarsi sul gamelist.xml del sistema relativo alla rom copiata quando è stata copiata e su che dispositivo, ad esempio:

<path>Pokemon blu.gb</path>
    <sync=device_name>11/12/2022</sync>

Se la data non è presente significa che questa rom è stata marchiata come sync ma ancora non è stata syncata
Inoltre se il file della rom, ad esempio Pokemon blu.gb, ha una data di modifica maggiore della data di sync,
questo file dovrà essere copiato nuovamente sul device sovrascrivendo il precedente e la data dovrà essere aggiornata.

