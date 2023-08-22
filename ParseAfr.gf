concrete ParseAfr of Parse =
  NounAfr - [PPartNP, UseN2, RelNP, DetNP, NumDigits],
  VerbAfr - [PassV2, ReflVP, ComplVV, SlashVV, SlashV2V, SlashV2VNP, UseCopula],
  AdjectiveAfr - [ReflA2, CAdvAP],
  AdverbAfr - [ComparAdvAdj, ComparAdvAdjS, AdnCAdv],
  SentenceAfr - [EmbedVP],
  QuestionAfr,
  RelativeAfr,
  PhraseAfr - [UttAP, UttVP],
  IdiomAfr,
  TenseX - [CAdv,IAdv,AdV,SC,Adv],
  NamesAfr,
  ParseExtendAfr,
  WordNetAfr,
  DocumentationAfr
  ** {

flags
  case_sensitive = off;

} ;
