def define_env(env):
    @env.macro
    def spec_content(meta):
        topic = meta.get("topic", "No Topic")
        statement = meta.get("k8tre_statements", {}).get("spec", "No statement provided.")
        updated = meta.get("last_updated", "Unknown")
        source = meta.get("discussion", "N/A")

        return f"""
# {topic}

!!! abstract "Specification"
    {statement}

Last updated: {updated}  
Source: [GitHub Discussion]({source})
"""
