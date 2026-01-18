import subprocess_test

def get_top_cpu_processes(n=5):
    """Get the top n CPU-consuming processes."""
    try:
        # Run the 'ps' command to get process information sorted by CPU usage
        result = subprocess_test.run(
            ['ps', 'aux', '-sort=-%cpu'],
            stdout=subprocess_test.PIPE,
            stderr=subprocess_test.PIPE,
            text=True,
            check=True
        )

        # Split the output into lines
        lines = result.stdout.strip().split('\n')

        # Get the header and the top n processes
        header = lines[0]
        top_processes = lines[1:n+1]

        # Print the header and top processes
        print(header)
        for process in top_processes:
            print(process)

    except subprocess_test.CalledProcessError as e:
        print(f"An error occurred while trying to get process information: {e.stderr}")
if __name__ == "__main__":
    get_top_cpu_processes(5)