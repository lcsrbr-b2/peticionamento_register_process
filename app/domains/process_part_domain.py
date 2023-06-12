from dataclasses import dataclass

@dataclass
class ProcessPartDomain:
    process_id: int
    cpf_cnpj: str
    name: str 
    role: int