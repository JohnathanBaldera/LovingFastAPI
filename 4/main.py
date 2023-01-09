from fastapi import FastAPI


#The Description Passed to the FastAPI Object Supports Markdown
DESCRIPTION = """
## Special Thanks

- The Austin Python Meetup Organizers
- Amicus
- BlackLocus
- Striveworks
"""

# All of this information is available to added to the Docs
app = FastAPI(title="The Austin Python Meetup",
              description=DESCRIPTION,
              version="1.0.0",
              terms_of_service="I <3 MLOps",
              contact={
                  "name": "Johnathan Baldera",
                  "url": "https://github.com/JohnathanBaldera"
              },
              license_info={
                  "name": "MIT License",
                  "url": "https://opensource.org/licenses/MIT"
              })


@app.get("/")
async def root():
    return {"message": "Goodbye Austin Meet Up"}

@app.get("/users", tags=["Users"])
async def get_users():
    return {"user" : "Johnathan Baldera"}

@app.post("/users", tags=["Users"])
async def create_users():
    pass

@app.patch("/users", tags=["Users"])
async def update_users():
    pass

@app.delete("/users", tags=["Users"])
async def delete_users():
    pass

@app.get("/jobs", tags=["Jobs"])
async def get_items():
    return {"job" : ["Software Engineer", "Data Scientist", "Proposal Writer"]}
