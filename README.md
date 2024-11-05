# FastApiExample

Notes: 

 - I receive a strange error when posting to the /claims endpoint. The entry saves correctly but I receive the error:
 sqlalchemy.orm.exc.DetachedInstanceError: Instance <Claim at 0xffff9bdc7a40> is not bound to a Session; attribute refresh operation cannot proceed (Background on this error at: https://sqlalche.me/e/14/bhk3)

 - I would place an index on net_fees to support quick sorting.
 
 - I wanted to use a custom validator to handle validating that procedure type always began with a D but ran into issue between pydantic 1 & 2 and exactly how this is to function. In a real world environment I would look for advice from a more experienced FastAPI/SQLModel user



