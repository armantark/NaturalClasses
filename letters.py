from classes import *

letters = {
    "p": {
        CONS,
        ORAL,
        STOP,
        BILAB,
        LABIAL,
        VOICELESS,
        ANTERIOR,
        TENUIS,
        PLOSIVE,
        NONCON
        },
    "b": {
        CONS,
        ORAL,
        STOP,
        BILAB,
        LABIAL,
        VOICED,
        ANTERIOR,
        PLOSIVE,
        NONCON
    },
    "pʰ": {
        CONS,
        ORAL,
        STOP,
        BILAB,
        LABIAL,
        VOICELESS,
        ANTERIOR,
        ASP,
        PLOSIVE,
        NONCON
    },
    "bʰ": {
        CONS,
        ORAL,
        STOP,
        BILAB,
        LABIAL,
        VOICED,
        ANTERIOR,
        ASP,
        PLOSIVE,
        NONCON
    },
    "p'": {
        CONS,
        ORAL,
        BILAB,
        LABIAL,
        VOICELESS,
        ANTERIOR,
        EJECT,
        NONPULM,
        PLOSIVE
    },
    "m": {
        CONS,
        NASAL,
        BILAB,
        LABIAL,
        VOICED,
        ANTERIOR,
        STOP
    },
    "ʙ": {
        CONS,
        ORAL,
        TRILL,
        BILAB,
        LABIAL,
        VOICED,
        ANTERIOR,
        VIBRANT
    },
    "ɸ": {
        CONS,
        ORAL,
        FRIC,
        BILAB,
        VOICELESS,
        LABIAL,
        ANTERIOR,
        CON,
        OBST
    },
    "β": {
        CONS,
        ORAL,
        FRIC,
        BILAB,
        VOICED,
        LABIAL,
        ANTERIOR,
        CON,
        OBST
    },
    "w": {
        CONS,
        ORAL,
        VOICED,
        LABIAL,
        BILAB,
        VELAR,
        ANTERIOR,
        APPROX,
        SEMI,
        CON,
        VOCOID,

    },
    "ʍ": {

    },
    "ɱ": {

    },
    "ⱱ": {

    },
    "f": {
        CONS,
        VOICELESS,
        NONSON,
        LABIAL,
        LABDENT,
        ANTERIOR,
        CON,
        STRIDENT,
        OBST
    },
    "v": {
        CONS,
        VOICED,
        NONSON,
        LABDENT,
        LABIAL,
        ANTERIOR,
        CON,
        STRIDENT,
        OBST
    },
    "ʋ": {

    },
    "t": {
        CONS,
        PLOSIVE,
        STOP,
        VOICELESS,
        ALV,
        CORONAL,
        ANTERIOR
    },
    "d": {

    },
    "t'": {

    },
    "tʰ": {

    },
    "dʰ": {

    },
    "n": {

    },
    "r": {

    },
    "ɾ": {

    },
    "θ": {

    },
    "ð": {

    },
    "s": {

    },
    "z": {

    },
    "∫": {

    },
    "ʒ": {

    },
    "ɬ": {

    },
    "ɮ": {

    },
    "ɹ": {

    },
    "l": {

    },
    "ʈ": {

    },
    "ɖ": {

    },
    "ʈʰ": {

    },
    "ɖʰ": {

    },
    "ɳ": {

    },
    "ɽ": {

    },
    "ʂ": {

    },
    "ʐ": {

    },
    "ɻ": {

    },
    "ɭ": {

    },
    "c": {

    },
    "ɟ": {

    },
    "ɲ": {

    },
    "ç": {

    },
    "ʝ": {

    },
    "ɕ": {

    },
    "ʑ": {

    },
    "j": {

    },
    "ʎ": {

    },
    "k": {
        CONS,
        STOP,
        PLOSIVE,
        DORSAL,
        NONCON,
        VOICELESS,
        NONSON,
        VELAR
    },
    "g": {
        CONS,
        STOP,
        PLOSIVE,
        DORSAL,
        NONCON,
        VOICED,
        NONSON,
        VELAR
    },
    "k'": {
        CONS,
        STOP,
        PLOSIVE,
        DORSAL,
        NONCON,
        VOICELESS,
        NONSON,
        VELAR,
        NONPULM,
        EJECT
    },
    "kʰ": {
        CONS,
        STOP,
        PLOSIVE,
        DORSAL,
        NONCON,
        VOICELESS,
        NONSON,
        VELAR,
        ASP
    },
    "gʰ": {
        CONS,
        STOP,
        PLOSIVE,
        DORSAL,
        NONCON,
        VOICED,
        NONSON,
        VELAR,
        ASP
    },
    "ŋ": {

    },
    "x": {

    },
    "ɣ": {

    },
    "ɰ": {

    },
    "ʟ": {

    },
    "q": {

    },
    "ɢ": {

    },
    "ɴ": {

    },
    "ʀ": {

    },
    "χ": {

    },
    "ʁ": {

    },
    "ħ": {

    },
    "ʕ": {

    },
    "ʔ": {
        CONS,
        VOICELESS,
        NONSON,
        UNDEFINED
    },
    "h": {
        CONS,
        VOICELESS,
        NONSON,
        UNDEFINED
    },
    "ɦ": {

    },
    "i": {
        VOWEL,
        FRONT,
        HIGH,
        CLOSE,
        TENSE,
        SYLLABIC,
        UNROUND
    },
    "y": {
        VOWEL,
        FRONT,
        HIGH,
        CLOSE,
        TENSE,
        SYLLABIC,
        ROUND
    },
    "ɨ": {

    },
    "ʉ": {

    },
    "ɯ": {
        VOWEL,
        BACK,
        HIGH,
        CLOSE,
        TENSE,
        SYLLABIC,
        UNROUND
    },
    "u": {
        VOWEL,
        BACK,
        HIGH,
        CLOSE,
        TENSE,
        SYLLABIC,
        ROUND
    },
    "ɪ": {
        VOWEL,
        FRONT,
        NEARHIGH,
        CLOSE,
        LAX,
        SYLLABIC,
        UNROUND
    },
    "ʏ": {
        VOWEL,
        FRONT,
        NEARHIGH,
        CLOSE,
        LAX,
        SYLLABIC,
        ROUND
    },
    "ʊ": {
        VOWEL,
        BACK,
        NEARHIGH,
        CLOSE,
        LAX,
        SYLLABIC,
        ROUND
    },
    "e": {
        VOWEL,
        FRONT,
        CLOSEMID,
        MID,
        TENSE,
        SYLLABIC,
        UNROUND
    },
    "ø": {
        VOWEL,
        FRONT,
        CLOSEMID,
        MID,
        TENSE,
        SYLLABIC,
        ROUND
    },
    "ɘ": {

    },
    "ɵ": {

    },
    "ɤ": {
        VOWEL,
        BACK,
        MID,
        CLOSEMID,
        LAX,
        SYLLABIC,
        UNROUND
    },
    "o": {
        VOWEL,
        BACK,
        MID,
        CLOSEMID,
        LAX,
        SYLLABIC,
        ROUND
    },
    "ə": {
        VOWEL,
        CENTRAL,
        MID,
        LAX,
        SYLLABIC,
        UNROUND
    },
    "ɛ": {
        VOWEL,
        FRONT,
        OPENMID,
        MID,
        LAX,
        SYLLABIC,
        UNROUND
    },
    "œ": {

    },
    "ɜ": {

    },
    "ɞ": {

    },
    "ʌ": {
        VOWEL,
        FRONT,
        OPENMID,
        MID,
        LAX,
        SYLLABIC,
        UNROUND
    },
    "ɔ": {
        VOWEL,
        FRONT,
        OPENMID,
        MID,
        LAX,
        SYLLABIC,
        ROUND
    },
    "æ": {
        VOWEL,
        FRONT,
        LOW,
        LAX,
        SYLLABIC,
        UNROUND,
    },
    "a": {
        VOWEL,
        FRONT,
        LOW,
        TENSE,
        SYLLABIC,
        UNROUND
    },
    "ɶ": {

    },
    "ɑ": {
        VOWEL,
        BACK,
        LOW,
        TENSE,
        SYLLABIC,
        UNROUND
    },
    "ɒ": {

    },
    "ɐ": {

    },
    "ʘ": {

    },
    "ǀ": {

    },
    "ǃ": {

    },
    "ǂ": {

    },
    "ǁ": {

    },
    "ɓ": {

    },
    "ɗ": {

    },
    "ʄ": {

    },
    "ɠ": {

    },
    "ʛ": {

    },
    "ɥ": {

    },
    "ʜ": {

    },
    "ʢ": {

    },
    "ʡ": {

    },
    "ɺ": {

    },
    "ɧ": {

    },
    "ts": {

    },
    "dz": {

    },
    "t∫": {
        DELAY,
        STRIDENT,
        NONSON,
        CONS,
        VOICELESS,
    },
    "dʒ": {
        DELAY,
        STRIDENT,
        NONSON,
        CONS,
        VOICED,
    },
    "pf": {

    },
    "bv": {

    }
}