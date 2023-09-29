from typing import Union, List


# three later and corresponding one letter names
RESIDUES_NAMES = {"ALA": "A",
                  "ARG": "R",
                  "ASN": "N",
                  "ASP": "D",
                  "CYS": "C",
                  "GLN": "Q",
                  "GLU": "E",
                  "GLY": "G",
                  "HIS": "H",
                  "ILE": "I",
                  "LEU": "L",
                  "LYS": "K",
                  "MET": "M",
                  "PHE": "F",
                  "PRO": "P",
                  "SER": "S",
                  "THR": "T",
                  "TRP": "W",
                  "TYR": "Y",
                  "VAL": "V"
}

# first value is hydrophobicity index, second is pI, third is molecular mass in kDa
RESIDUES_CHARACTERISTICS = {
    "A" : []

}

def change_residues_encoding(seq: str, query: str = "one") -> str:
    pass


def get_seq_characteristic(seq: str) -> str:
    pass


def find_res_in_seq(seq: str) -> str:
    pass


def find_peptidases_sites(seq: str, peptidase: Union[str, List[str], dict] = PEPTIDASES_SITES) -> Union[str, List[str]]:
    pass


def calculate_protein_mass(seq: str) -> float:
    pass


def calculate_average_hydropathy(seq: str) -> float:
    pass


def get_mrna(seq: str) -> List[str]:
    pass


def calculate_pI(seq: str) -> float:
    pass