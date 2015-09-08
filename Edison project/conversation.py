# -*- coding: utf-8 -*-
import time
import calendar
import datetime
import telegram

#----------------------------------------------------------------------
# gReflections, a translation table used to convert things you say
#    into things the computer says back, e.g. "I am" --> "you are"
#----------------------------------------------------------------------
gReflections = {
  "sono"   : "sei",
  "ero"  : "eri",
  "io"    : "tu",
  "Vorrei"  : "vorresti",
  "io ho"  : "tu hai",
  "i'll"  : "you will",
  "mio"  : "tuo",
  "sei"  : "sono",
  "tu hai": "io ho",
  "you'll": "I will",
  "tuo"  : "mio",
  "il tuo"  : "il mio",
  "te"  : "me",
  "me"  : "te"
}


gDayEn = {
  "0"  : "Monday",
  "1"  : "Tuesday",
  "2"  : "Wednesday",
  "3"  : "Thursday",
  "4"  : "Friday",
  "5"  : "Saturday",
  "6"  : "Sunday"
}


gDayIta = {
  "0"  : "Lunedì",
  "1"  : "Martedi",
  "2"  : "Mercoledì",
  "3"  : "Giovedì",
  "4"  : "Venerdì",
  "5"  : "Sabato",
  "6"  : "Domenica"
}

gWeatherIta = {
  "sunny"  : "soleggiato",
  "fair"  : "bello",
  "cloudy"  : "nuvoloso",
  "partly"  : "parzialmente",
  "rainy"  : "piovoso",
  "shower"  : "acquazzoni",
  "snow"  : "nevicate"
}





gMonthIta = {
  "1"  : "Gennaio",
  "2"  : "Febbraio",
  "3"  : "Marzo",
  "4"  : "Aprile",
  "5"  : "Maggio",
  "6"  : "Giugno",
  "7"  : "Luglio",
  "8"  : "Agosto",
  "9"  : "Settembre",
  "10"  : "Ottobre",
  "11"  : "Novembre",
  "12"  : "Dicembre",
}


#----------------------------------------------------------------------
# gPats, the main response table.  Each element of the list is a
#  two-element list; the first is a regexp, and the second is a
#  list of possible responses, with group-macros labelled as
#  %1, %2, etc.  
#----------------------------------------------------------------------
gPats = [
  [r'ho bisogno (.*)',
  [ "Perchè hai bisogno %1?",
    "Ti potrebbe veramente servire avere %1?",
    "Sei sicuro di aver bisogno di %1?"]],
  
  [r'perchè tu non ([^\?]*)\??',
  [  "Tu pensi veramente che io non %1?",
    "Forse eventualmente io %1.",
    "Vuoi vermamente che io %1?"]],
  
  [r'perchè io non posso ([^\?]*)\??',
  [  "Tu pensi che dovresti essere in grado di %1?",
    "Se tu potessi %1, che cosa faresti?",
    "Non saprei -- perchè tu non %1?",
    "Hai veramente provato?"]],
  
  [r'non posso (.*)',
  [  "Come fai a sapere che non puoi %1?",
    "Forse potresti %1 se ci provassi.",
    "Che cosa significa per te %1?"]],
  
  [r'sono (.*)',
  [  "Sei venuto da me perchè tu sei %1?",
    "Da quanto tempo sei %1?",
    "Che impressione ti fa essere %1?"]],
  
  [r'I\'?m (.*)',
  [  "How does being %1 make you feel?",
    "Do you enjoy being %1?",
    "Why do you tell me you're %1?",
    "Why do you think you're %1?"]],
  
  [r'sei ([^\?]*)\??',
  [  "Che importanza ha se io sono %1?",
    "Preferiresti che io non fossi %1?",
    "Forse tu pensi che io sia %1?.",
    "Potrei essere %1 -- che ne dici?"]],
  
  [r'che cosa (.*)',
  [  "Perchè me lo chiedi?",
    "Come potrebbe aiutarti una risposta a questa tua domanda?",
    "A cosa stai pensando?"]],
  
  [r'come (.*)',
  [  "Tu che cosa ne pensi?",
    "Forse potresti risponderti da solo.",
    "Che cosa stai veramente chiedendo?"]],
  
  [r'perchè(.*)',
  [  "Questa è la verità?",
    "Che alrte ragioni hai?",
    "Quella ragione è la più importante di tutte??",
    "Se %1, Che altro c'è da fare?"]],
  
  [r'(.*) scusa (.*)',
  [  "Tant volte chiedere scusa non è necessario.",
    "Come ti senti quando chiedi scusa?"]],
  
  [r'ciao(.*)',
  [  "Ciao... mi fa piacere che tu sia passato oggi.",
    "Ciao, come stai oggi?"]],
  
  [r'penso che (.*)',
  [  "Hai dei dubbi su %1?",
    "Veramente pensi così?",
    "Ma ne sei sicuro %1?"]],
  
  [r'(.*) amico (.*)',
  [  "Raccontami qualcosa.",
    "quando pensi ad un amico, che cosa ti viene in mente?",
    "perchè non mi parli della amicizia?"]],
  
  [r'sì',
  [  "Mi sembri piuttosto sicuro.",
    "OK, ma potresti elaborare un po' meglio il concetto?"]],
  
  [r'(.*) computer(.*)',
  [  "Parli veramente di me?",
    "Ti sembra strano parlare ad un computer?",
    "Come ti fanno sentire i computer?",
    "Sembri spaventato dai computer?"]],
  
  [r'è (.*)',
  [  "tu pensi che sia %1?",
    "Forse è %1 -- che cosa ne pensi?",
    "Se fosse %1, che cosa faresti?",
    "Sarà veramente %1."]],
  
  [r'è (.*)',
  [  "mi sembri sicuro.",
    "Se io ti dicessi che probabilmente non è %1, come ti sentiresti?"]],
  
  [r'potresti ([^\?]*)\??',
  [  "Che cosa ti fa pensare che io non potrei %1?",
    "Se io potessi %1, che cosa succederebbe?",
    "Perchè mi chiedi se io posso %1?"]],
  
  [r'potrei ([^\?]*)\??',
  [  "Forse tu non vuoi %1.",
    "Vorresti essere capace di %1?",
    "Se tu potessi %1, che cosa faresti?"]],
  
  [r'tu sei (.*)',
  [  "Perchè tu pensi che io sia %1?",
    "Ti farebbe piacere se io fossi %1?",
    "Forse tu vorresti che io fossi %1.",
    "Forse tu stai parlando di te stesso?"]],
  
  
  [r'io non (.*)',
  [  "Veramente tu non %1?",
    "Perchè tu non %1?",
    "Vorresti %1?"]],
  
  [r'sto (.*)',
  [  "Bene, Raccontami di più su questo.",
    "Ti capita spesso di stare %1?",
    "Quando ti capita di stare %1?",
    "Quando stai %1, che cosa fai?"]],
  
  [r'ho (.*)',
  [  "Perchè tu mi dici che tu hai %1?",
    "Hai veramente %1?",
    "Ora che tu hai %1, che cosa capiterà?"]],
  
  [r'vorrei (.*)',
  [  "Mi potresti spiegare perchè tu vorresti %1?",
    "Perchè tu vorresti %1?",
    "Chi altri sa che tu vorresti %1?"]],
  
  [r'cè (.*)',
  [  "tu pensi veramente che ci sia %1?",
    "è probabile che ci sia %1.",
    "Ti piacerebbe se ci fosse %1?"]],
  
  [r'mio (.*)',
  [  "capisco, il tuo %1.",
    "Perchè tu dici che il tuo %1?",
    "Quando pensi al tuo %1, Come ti senti?"]],
  
  [r'tu (.*)',
  [  "Dovremmo parlare di te, non di me.",
    "Perchè parli di me?",
    "Perchè ti interessa che cosa io sono %1?"]],
    
  [r'perchè (.*)',
  [  "Dimmi tu il perchè %1?",
    "Perchè tu pensi che %1?" ]],
    
  [r'voglio (.*)',
  [  "che cosa significa per te volere %1?",
    "Perchè vuoi %1?",
    "Che cosa faresti se tu avessi %1?",
    "Se tu avessi %1, poi, che cosa faresti?"]],
  
  [r'pippa(.*)',
  [  "è à ò ù ì"]],

  [r'(.*) mamma(.*)',
  [  "Parlami di tua madre.",
    "In che rapporti sei con tua madre?",
    "Che cosa ti fa pensare tua mamma?",
    "Come si relaziona questo con il tuo umore oggi?",
    "Delle buone relazioni in famiglia sono importanti."]],
  
  [r'(.*) papà (.*)',
  [  "Parlami di tuo padre.",
    "Come ti fa sentire tuo padre?",
    "Che cosa ne pensi di tuo padre?",
    "Il tuo stato d'animo oggi è in relazione con i rapporti che hai con tuo padre?",
    "Hai delle difficoltà a mostrare i sentimenti che provi per la tua famiglia?"]],

  [r'(.*) bimbo(.*)',
  [  "Quando eri un bimbo, avevi tanti amici?",
    "Qual'è il tuo ricordo favorito dell'infanzia?",
    "Ti ricordi di qualche bella storia di infanzia?",
    "Capitava che altri bambini ti dessero fastidio?",
    "Pensi che la tua esperienza infantile sia in relazione con il tuo stato d'animo oggi??"]],
    
  [r'(.*)\?',
  [  "Perchè mi chiedi questo?",
    "per favore, pensa se sei in grado di rispondere a quesa domanda.",
    "Forse la risposta è dentro di te.",
    "Perchè non ne parli?"]],
  
  [r'fine',
  [  "Grazie di avere chiacchierato con me.",
    "addio.",
    "Grazie, il conto è di 150 euro.  Buona giornata!"]],
  
  [r'(.*)',
  [ "Per favore, dimmi di più.",
    "Cambiamo argomento... Dimmi della tua famiglia.",
    "Potesti elaborare il concetto?",
    "Perchè dici %1?",
    "Capisco.",
    "Molto interessante.",
    "%1.",
    "Capisco, e che cosa ti dice tutto ciò?",
    "Come ti fa sentire?",
    "Come ti senti quando dici questo?"]]
  ]


