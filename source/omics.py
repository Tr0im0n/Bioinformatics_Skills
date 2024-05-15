
import os
import pandas as pd


os.chdir(r"C:\Users\Tom\Documents\Universiteit\Bioinformatics Skills\week 5")
file_name = "DEGs.xlsx"
df = pd.read_excel(file_name)
col_names = ["gene_id", "gene", "FPKM_control", "FPKM_treated", "log2FC", "p_value"]
col_name = "log2FC"


def get_min_max():
    log2fc_max = df[col_name].max()
    log2fc_min = df[col_name].min()
    print(f"Max: {log2fc_max}\nMin: {log2fc_min}")


def get_upregulated():
    mask = df["log2FC"] > 0
    print(mask.sum())


if __name__ == "__main__":
    get_upregulated()





