mad_lib = """
Dear {name},
I am {action}ing you to {other_action} you
to {action_three} your {noun}.
"""

print(mad_lib.format(name="Joel",
                     action="write",
                     other_action="inform",
                     action_three="get lost",
                     noun="face"))

# DON'T DO THIS
marker_action = "erase"
print("Markers are difficult to %s" %marker_action)
