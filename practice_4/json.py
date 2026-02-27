import json

def parse_json_and_display(filename):
    """
    Parse JSON file and display interface information in a formatted table
    """
    try:
        # Read and parse the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
        
        # Display the header
        print("Interface Status")
        print("=" * 80)
        print(f"{'DN':<50} {'Description':<15} {'Speed':<8} {'MTU':<6}")
        print("-" * 80)
        
        # Extract and display interface information
        # Assuming the JSON structure from the output example
        # This structure might need adjustment based on actual JSON format
        
        # Method 1: If the data is directly a list of interfaces
        if isinstance(data, list):
            for item in data:
                dn = item.get('dn', '')
                description = item.get('description', '')
                speed = item.get('speed', '')
                mtu = item.get('mtu', '')
                print(f"{dn:<50} {description:<15} {speed:<8} {mtu:<6}")
        
        # Method 2: If data has a specific structure (like from the example)
        elif isinstance(data, dict):
            # This is a common structure for network device data
            if 'imdata' in data:
                for item in data['imdata']:
                    # Navigate through the nested structure
                    if 'l1PhysIf' in item:
                        attributes = item['l1PhysIf'].get('attributes', {})
                        dn = attributes.get('dn', '')
                        description = attributes.get('descr', '') or attributes.get('description', '')
                        speed = attributes.get('speed', 'inherit')
                        mtu = attributes.get('mtu', '9150')
                        print(f"{dn:<50} {description:<15} {speed:<8} {mtu:<6}")
            
            # Alternative structure
            elif 'interfaces' in data:
                for interface in data['interfaces']:
                    dn = interface.get('dn', '')
                    description = interface.get('description', '')
                    speed = interface.get('speed', 'inherit')
                    mtu = interface.get('mtu', '9150')
                    print(f"{dn:<50} {description:<15} {speed:<8} {mtu:<6}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Specify the JSON file name
    json_file = "sample-data.json"
    parse_json_and_display(json_file)