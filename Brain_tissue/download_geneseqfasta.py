import argparse
from Bio import Entrez, SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import defaultdict

def download_transcripts(list_file, email_address="", outfile="brain.fasta"): 
    """Download transcripts from a file of list identifiers"""

    Entrez.email = email_address 
    with open(list_file, "r") as fp: 
        ids = [i.strip() for i in fp.readlines()]

    handle = Entrez.efetch(db="nucleotide", 
                           id=ids,
                           retmode ="xml", 
                           strand=1)

    output = Entrez.parse(handle)
    seqs = []
    for entry in output:
        organism = entry.get("GBSeq_organism", "Unknown organism")
        print(f"Organism for {entry['GBSeq_locus']}: {organism}")
        
        feat_tbl = entry["GBSeq_feature-table"]
        num_cds = 0 
        for j in feat_tbl: 
            if j['GBFeature_key'] == "CDS": 
                num_cds += 1
                cds = j["GBFeature_location"]

                # print(cds)
                cds_loc = j['GBFeature_intervals']
                # print("Num of features: ", len(cds_loc))
                start = int(cds_loc[0]['GBInterval_from'])
                end = int(cds_loc[0]['GBInterval_to'])
                # print(start, end)
                seq = entry["GBSeq_sequence"][start - 1 : end]
        if num_cds != 1: 
            print("Error: Too many CDS found", num_cds)
        seqs.append(SeqRecord(Seq(seq), 
                              id=entry['GBSeq_locus'],
                              description=entry["GBSeq_definition"]
                              )
                    )
    handle.close()
    with open(outfile, "w") as output_handle:
        SeqIO.write(seqs, output_handle, "fasta")

def get_args(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("--list-file", type=str, action="store", 
                        help="Name of list file with identifiers to download")
    parser.add_argument("--out-file", type=str, action="store", 
                        default="mus_exp.fasta", 
                        help="Name of list file with identifiers to download")
    return parser.parse_args()

def main(): 
    args = get_args()
    download_transcripts(args.list_file, outfile=args.out_file)

if __name__=="__main__": 
    main()