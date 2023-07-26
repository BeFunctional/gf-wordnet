concrete ParseMlt of Parse =
  NounMlt - [PPartNP, UseN2, RelNP, DetNP],
  VerbMlt - [PassV2, ReflVP, ComplVV, SlashVV, SlashV2V, SlashV2VNP, UseCopula],
  AdjectiveMlt - [ReflA2, CAdvAP],
  AdverbMlt - [ComparAdvAdj, ComparAdvAdjS, AdnCAdv],
  SentenceMlt - [EmbedVP],
  QuestionMlt,
  RelativeMlt,
  ConjunctionMlt,
  PhraseMlt - [UttAP, UttVP],
  IdiomMlt,
  TenseX - [CAdv,IAdv,AdV,SC,Adv],
  NamesMlt,
  ParseExtendMlt,
  WordNetMlt
  ** {

flags
  case_sensitive = off;

} ;
