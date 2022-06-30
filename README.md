# FRIDAAY
## Format Representing Interdependent Data Actions As YAML

Who needs SQL, Python, JavaScript and CSV?
Get it all done by FRIDAAY 

- Format
- Representing
- Interdependent 
- Data
- Actions
- As
- YAML

FRIDAAY defines a new "atomic unit" of abstraction for the modern data stack called Data Actions.  
Each Data Action defines a semantic mapping for creating a new "frame" from existing frames (or inline data). 
This allows analysts and data scientists to declaratively specify their intent, empowering the underlying platform to efficiently satisfy those requirements. We call this production-ready alternative to traditional exploratory notebooks a [PipeBook](https://ihack.us/2022/06/30/pipebook-yml-reimagining-notebooks-as-resilient-data-pipelines/).

Right now, business logic and data dependencies are trapped inside complex (and often incompatible) programming languages such as SQL, Python, and Scala, and APIs like Spark vs Pandas, TensorFlow vs MLFlow, etc. FRIDAAY replaces these with a simple yet extensible "programming format" based on YAML that enables:
- fine-grained orchestration
- full-fidelity no-code visual programming of data pipelines
- platform and language independence 
- reusable specification of dashboards and data apps  
- inline tests and alerting
- uniform specification of external integrations
- schema-aware autocompletion and templates 
- ad-hoc materialization and incrementalizarions
- version-controlled user-facing semantic models and metric layers
- deterministic transformations between versions and vendors
- novel interaction paradigms beyond notebooks and REPLs
- turn legacy code into structured data, so we can manage using alll our data superpowers

## Example 
```
fridaay:
  version: 0.1
  do: init
  imports:
   sql: dad-sql
  set: # global constants (COMMENT)
    NAME: pipebook_demo1
    SAPIENT: Human
     
test_data:
  doc: Sample data for test purposes
  do: sql.load
  csv.inline:
  - ['Name','Age','Weight', 'Type', 'Timestamp']
  - ['Ernie', 54, 170.5, 'Human Tech Nerd', date'2020-03-20']
  - ['Qhuinn', 7, 36.3, 'English Cocker Spaniel', date'2022-06-27']
  - ['Frolic', 2, 76.2, 'Chocolate Labrador', date'2022-06-27']
 
recent_pets:
  do: sql.select
  from: $$ # last frame
  cols:
    Name: STRING Personal Name
    Age: INTEGER.year Age
    Weight: DOUBLE.pound Current Weight
  where.all:
   - ['Type', NOT LIKE, $SAPIENT] # dereference constant
   - ['Timestamp','>', date'2022-01-01']
  save: table
```
      
