from nada_dsl import *

def nada_main():
    # Define two parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Function to create secret integers
    def create_secret_integer(input_name, party):
        try:
            return SecretInteger(Input(name=input_name, party=party))
        except Exception as e:
            print(f"Error creating secret integer {input_name} for {party.name}: {e}")
            return None

    # Secret integers for party1
    my_int1 = create_secret_integer("my_int1", party1)
    my_int2 = create_secret_integer("my_int2", party1)

    # Secret integers for party2
    my_int3 = create_secret_integer("my_int3", party2)
    my_int4 = create_secret_integer("my_int4", party2)

    # Check if all secret integers were created successfully
    if None in [my_int1, my_int2, my_int3, my_int4]:
        print("Failed to create some secret integers. Aborting.")
        return []

    try:
        # Perform operations
        sum_party1 = my_int1 + my_int2
        sum_party2 = my_int3 + my_int4

        # Cross-party operation
        total_sum = sum_party1 + sum_party2

        return [
            Output(sum_party1, "sum_party1", party1),
            Output(sum_party2, "sum_party2", party2),
            Output(total_sum, "total_sum", [party1, party2])
        ]
    except Exception as e:
        print(f"An error occurred during computation: {e}")
        return []

# Execute the main function if this script is run directly
if __name__ == "__main__":
    outputs = nada_main()
    for output in outputs:
        print(output)

