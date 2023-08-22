abstract ParseExtend = Extend - [iFem_Pron, youPolFem_Pron, weFem_Pron, youPlFem_Pron, theyFem_Pron, GenNP, DetNPMasc, DetNPFem, FocusAP, N2VPSlash, A2VPSlash,
                                 CompVP, InOrderToVP, PurposeVP, ComplGenVV, ReflRNP, ReflA2RNP, UncontractedNeg, AdvIsNPAP, ExistCN, NominalizeVPSlashNP,
                                 PiedPipingQuestSlash, PiedPipingRelSlash],
                       Numeral - [num], Punctuation ** {

fun gen_Quant : Quant ;       -- English often skips the article
                              -- when in Swedish and Bulgarian definite
                              -- article is needed. This is usually
                              -- for things in general.

    UttAP  : Pron -> AP  -> Utt ;  -- Similar to UttAP  in the RGL but takes agreement from a pronoun
    UttVPS : Pron -> VPS -> Utt ;  -- Similar to UttVPS in the RGL but takes agreement from a pronoun

    -- A version of PhrUtt which adds a punctuation mark
fun PhrUttMark : PConj -> Utt -> Voc -> Mark -> Phr ;

    -- These are nicer names for RelfA2RNP and ReflRNP
fun ReflA2 : A2 -> RNP -> AP ;
    ReflVPSlash : VPSlash -> RNP -> VP ;

    -- CNN is a version of CN category where the number is already
    -- fixed but the quantifier is still missing.
    -- This is useful mostly for coordination.
cat CNN ;
fun BaseCNN : Num -> CN -> Num -> CN -> CNN ;
    DetCNN  : Quant -> Conj -> CNN -> NP ;

    ReflPossCNN : Conj -> CNN -> RNP ;
    PossCNN_RNP : Quant -> Conj -> CNN -> RNP -> RNP ;

-- Extensions to numerals

    -- The following two functions build numerals like
    -- `two more` or `five less`.
fun NumLess : Num -> Num ;
    NumMore : Num -> Num ;

fun num : Sub1000000000000 -> Numeral ;

    -- Some cardinals like `many` permit modifications with AdA,
    -- i.e. `too many`, `very many`.
fun UseACard    : ACard -> Card ;
    UseAdAACard : AdA -> ACard -> Card ;

fun -- Version of RelNP from the RGL but without comma
    RelNP : NP -> RS -> NP ;

    -- the same as the RGL's RelNP, just renamed
    -- for consistency with ExtAdvNP for instance.
    ExtRelNP : NP -> RS -> NP ;

    -- make it possible insert comma between adjective and adverb
fun ExtAdvAP : AP -> Adv -> AP ;

    -- Use N2 as a plain N. The RGL has UseN2 but this doesn't
    -- allow us to use N2 in compound nouns.
fun BareN2 : N2 -> N ;

    -- A generalization of the CAdv API from the RGL
    -- which permits negation, i.e. `no more efficient than ..`.
    -- The argument of the CAdv is now an arbitrary complement.
fun ComparAdv : Pol -> CAdv -> Adv -> Comp -> Adv ;
    CAdvAP    : Pol -> CAdv -> AP  -> Comp -> AP ;

    AdnCAdv : Pol -> CAdv -> AdN ;

    -- the word `enough` has a special syntax in English
    -- when it is used with adjectives,
    -- i.e. `smart enough to find the solution`.
fun EnoughAP  : AP -> Ant -> Pol -> VP -> AP ;
    EnoughAdv : Adv -> Adv ;

    -- TimeNP is really overgenerating and is only a temporary
    -- place holder. It is used when a noun phrase describing
    -- time is used as an adverb.
fun TimeNP : NP -> Adv ;

    -- Sometimes one adverb modifies another. I am not sure
    -- if this is a regular pattern or the function must be revised.
fun AdvAdv : Adv -> Adv -> Adv ;

    -- gender specific version of whatSg_IP.
fun whatSgFem_IP : IP ;
    whatSgNeut_IP : IP ;

    -- reexport Extra.that_RP here since the rest of the Extra module
    -- is not used in the Parse grammar.
fun that_RP : RP ;

    -- generalize several function that take infinitive VP as argument
    -- to also support anteriority and polarity.
fun EmbedVP     : Ant -> Pol -> Pron -> VP  -> SC ;
    ComplVV     : VV  -> Ant -> Pol -> VP -> VP ;
    SlashVV     : VV  -> Ant -> Pol -> VPSlash -> VPSlash ;
    SlashV2V    : V2V -> Ant -> Pol -> VP -> VPSlash ;
    SlashV2VNP  : V2V -> NP  -> Ant -> Pol -> VPSlash -> VPSlash ;
    InOrderToVP : Ant -> Pol -> Pron -> VP  -> Adv ;
    CompVP      : Ant -> Pol -> Pron -> VP  -> Comp ;
    UttVP       : Ant -> Pol -> Pron -> VP  -> Utt ;

    -- reciprocal verbs i.e.
    -- `We love each other` or `We love one another`.
fun RecipVPSlash   : VPSlash -> VP ;
    RecipVPSlashCN : VPSlash -> CN -> VP ;

    -- A clause which uses copula but the complement
    -- is shifted to the front.
fun FocusComp : Comp -> NP -> Cl ;

}
