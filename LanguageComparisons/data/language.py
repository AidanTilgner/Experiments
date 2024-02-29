from dataclasses import dataclass
from typing import Tuple, Dict

@dataclass
class LanguageMetrics:
    lexical_diversity: float
    syntactic_complexity: float
    phonemic_inventory: float
    semantic_range: float
    pragmatic_flexibility: float
    language_typology_features: float
    interlingual_homophony: float
    number_of_morphemes: float

    def __init__(
        self,
        lexical_diversity: float,
        syntactic_complexity: float,
        phonemic_inventory: float,
        semantic_range: float,
        pragmatic_flexibility: float,
        language_typology_features: float,
        interlingual_homophony: float,
        number_of_morphemes: float,
    ):
        self.lexical_diversity = lexical_diversity
        self.syntactic_complexity = syntactic_complexity
        self.phonemic_inventory = phonemic_inventory
        self.semantic_range = semantic_range
        self.pragmatic_flexibility = pragmatic_flexibility
        self.language_typology_features = language_typology_features
        self.interlingual_homophony = interlingual_homophony
        self.number_of_morphemes = number_of_morphemes

    def get_expressiveness_score(self) -> float:
        factors = [
            self.lexical_diversity,
            self.syntactic_complexity,
            self.phonemic_inventory,
            self.semantic_range,
            self.pragmatic_flexibility,
            self.language_typology_features,
            self.interlingual_homophony,
        ]

        score = sum(factors) / len(factors)
        return score
    
    def get_expressiveness_metrics(self) -> Dict[str, float]:
        return {
            "Lexical Diversity": self.lexical_diversity,
            "Syntactic Complexity": self.syntactic_complexity,
            "Phonemic Inventory": self.phonemic_inventory,
            "Semantic Range": self.semantic_range,
            "Pragmatic Flexibility": self.pragmatic_flexibility,
            "Language Typology Features": self.language_typology_features,
            "Interlingual Homophony": self.interlingual_homophony,
        }

@dataclass
class LanguageSources:
    sources: Tuple[str, str]

    def __init__(self, sources: Tuple[str, str]):
        self.sources = sources

    def add_source(self, source: str, source_for: str):
        self.source = source
        self.source_for = source_for

@dataclass
class Language:
    name: str
    metrics = LanguageMetrics
    sources = LanguageSources

    def __init__(
        self,
        name: str,
        metrics: LanguageMetrics,
        sources: LanguageSources,
    ):
        self.name = name
        self.metrics = metrics
        self.sources = sources
    
