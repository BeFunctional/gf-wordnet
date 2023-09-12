--# -path=.:../abstract:../common:../api
concrete ParseCat of Parse =
  NounCat - [PPartNP, UseN2, RelNP, DetNP, NumDigits],
  VerbCat - [PassV2, ReflVP, ComplVV, SlashV2V, SlashVV, SlashV2VNP, UseCopula],
  AdjectiveCat - [ReflA2,CAdvAP],
  AdverbCat - [ComparAdvAdj,ComparAdvAdjS,AdnCAdv],
  SentenceCat - [EmbedVP],
  QuestionCat,
  RelativeCat - [IdRP],
  ConjunctionCat,
  PhraseCat - [UttAP, UttVP],
  IdiomCat,
  TenseX - [SC,Temp,TTAnt,Tense,TPres,TPast,TFut,TCond,Pol,PPos,PNeg,MU],
  TenseCat,
  NamesCat,
  ParseExtendCat,
  WordNetCat,
  ConstructionCat - [Language, InLanguage, languageNP, languageCN,
                     afrikaans_Language, amharic_Language, arabic_Language,
                     bulgarian_Language, catalan_Language, chinese_Language,
                     danish_Language, dutch_Language, english_Language,
                     estonian_Language, finnish_Language, french_Language,
                     german_Language, greek_Language, hebrew_Language,
                     hindi_Language, japanese_Language, italian_Language,
                     latin_Language, latvian_Language, maltese_Language,
                     nepali_Language, norwegian_Language, persian_Language,
                     polish_Language, punjabi_Language, romanian_Language,
                     russian_Language, sindhi_Language, spanish_Language,
                     swahili_Language, swedish_Language, thai_Language,
                     turkish_Language, urdu_Language],
  DocumentationCat
  ** {

flags
  case_sensitive = off;

} ;
