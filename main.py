from fastapi import FastAPI, HTTPException
from sqlmodel import Field, SQLModel, create_engine, Session

from typing import Optional
from typing_extensions import Annotated
import uuid

app = FastAPI()

class Claim(SQLModel, table=True):
    claim_id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    provider_npi: int = Field(alias="Provider NPI")
    submitted_procedure: str = Field(alias="submitted procedure")
    provider_fees: float = Field(alias="provider fees")
    member_coinsurance: float = Field(alias="member coinsurance")
    member_copay: float = Field(alias="member copay")
    allowed_fees: float = Field(alias="Allowed fees")
    quadrant: Optional[str]
    plan_group_number: str = Field(alias="Plan/Group #")
    subscriber_number: float = Field(alias="Subscriber#")
    net_fee: float = 0.0

DATABASE_URL = "postgresql://user:password@db/claims_db"
engine = create_engine(DATABASE_URL)

@app.post("/claims/")
def create_claim(claim: Claim):
    # Calculate net fee
    claim.net_fee = (
        claim.provider_fees + claim.member_coinsurance + claim.member_copay - claim.allowed_fees
    )
    print(claim)
    with Session(engine) as session:
        session.add(claim)
        session.commit()
    return {"claim_id": claim.claim_id, "net_fee": claim.net_fee}

@app.get("/top-providers")
def get_top_providers():
    with Session(engine) as session:
        results = session.query(Claim) \
            .order_by(Claim.net_fee.desc()) \
            .limit(10) \
            .all()
    return {"top_providers": results}