import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from config.create_tables import create_tables

from gql.mutation import Mutation
from gql.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()

create_tables()

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"message": "server running"}