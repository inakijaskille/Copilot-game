"""
Mission control system for space crew assignments.
Manages crew member information and mission assignments.
"""

# List of crew members with their names and roles
crew_members = [
    {"name": "Commander Sarah Chen", "role": "Mission Commander"},
    {"name": "Dr. James Mitchell", "role": "Chief Engineer"},
    {"name": "Lt. Maria Rodriguez", "role": "Pilot"},
    {"name": "Dr. Yuki Tanaka", "role": "Medical Officer"}
]


def assign_mission(crew_member, mission):
    """
    Assign a mission to a crew member.
    
    Args:
        crew_member (dict): Dictionary containing crew member info
        mission (str): The mission description
        
    Returns:
        dict: Updated crew member dictionary with assigned mission
    """
    # Create a copy to avoid modifying original data
    updated_member = crew_member.copy()
    updated_member["assigned_mission"] = mission
    return updated_member


def main():
    """
    Main program that runs the mission control system.
    Assigns missions and displays crew information.
    """
    # Mission assignment
    mission_assignments = {
        0: "System Check and Maintenance",
        1: "Power Core Diagnostics",
        2: "Orbital Trajectory Verification",
        3: "Medical Inventory Review"
    }
    
    print("=" * 50)
    print("SPACE STATION MISSION CONTROL")
    print("=" * 50)
    print()
    
    # Loop through crew members and assign missions
    for index, crew_member in enumerate(crew_members):
        mission = mission_assignments[index]
        assigned_crew = assign_mission(crew_member, mssion)
        
        # Display crew member information and assignment
        print(f"Crew Member {index + 1}:")
        print(f"  Name: {assigned_crew['name']}")
        print(f"  Role: {assigned_crew['role']}")
        print(f"  Mission: {assigned_crew['assigned_mission']}")
        print()


# Execute main program
if __name__ == "__main__":
    main()
