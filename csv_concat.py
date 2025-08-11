import argparse
import csv

if __name__ == "__main__":

    # parse the argument, benchmark name
    parser = argparse.ArgumentParser(description="Run benchmarks")
    parser.add_argument("--benchmark", type=str, required=True, help="Benchmark name")
    parser.add_argument("--num_bitflip", type=int, required=True, help="Number of bitflips")
    # int array of rand seeds
    parser.add_argument("--rand_seed", type=int, required=True, help="Random seed")

    # the last size may not be full
    parser.add_argument("--ychunk_total_num", type=int, default=100, help="number of chunks to run in total")
    parser.add_argument("--debug_id", type=int, required=False, help="debug id")
    parser.add_argument("--input_dir", type=str, required=True, help="Input directory")

    args = parser.parse_args()


    if args.debug_id is not None:
        id_max = args.debug_id
    else:
        id_max = args.ychunk_total_num

    # Store all rows and header for the master CSV
    all_rows = []
    header = None

    for id in range(id_max):
        name = f"{args.input_dir}/{args.benchmark}-x{args.num_bitflip}-z{args.rand_seed}-yc{id}-{args.ychunk_total_num}.csv"
        # if file exists, append rows except header
        try:
            with open(name, 'r') as f:
                reader = csv.reader(f)
                # Get header from the first file
                if header is None:
                    header = next(reader)
                else:
                    next(reader)  # skip header for subsequent files
                
                for row in reader:
                    # append to master list
                    all_rows.append(row)
        except FileNotFoundError:
            print(f"{name} not found!")
    
    name_y_all = f"{args.input_dir}/{args.benchmark}-x{args.num_bitflip}-z{args.rand_seed}.csv"
    # write header and all rows to name_y_all
    if header is not None and all_rows:
        with open(name_y_all, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(all_rows)
        print(f"Concatenated {len(all_rows)} rows to {name_y_all}")
    else:
        print("No data found to concatenate")
