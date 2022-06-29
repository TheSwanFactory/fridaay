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

FRIDAAY defines a new "atomic unit" of 
abstraction for the modern data stack called Data Actions.  Each Data Action defines a semantic mapping for creating a new "frame" from existing frames (or inline data). This allows analysts and data scientists to declaratively specify their intent, empowering the underlying platform to efficiently satisfy those requirements. 

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

```
fridaay:
  do: config
  version: 0.1
 import:
   f: com.igwet.fridaay.frames
  ml: com.databricks.mlflow
  qd: com.quiltdata.packages
data:
  do: f.inline
  csv:
  - ['name", 'age']
  - ['Joe', 53]
```
      
