# Copt_ 

https://doi.org/10.5281/zenodo.14991160

## **Overview**
This project presents a **deep learning (DL) approach** to **codon optimization**, leveraging **recurrent neural networks (RNNs)** to enhance **tissue-specific protein expression**. Unlike traditional codon optimization tools that often fail to maximize protein translation efficiency, our method incorporates **cell-type-dependent codon biases**, leading to superior **recombinant protein expression** in heterologous systems.

## **Why Codon Optimization Matters**
Protein translation is a fundamental process where **mRNA templates** are decoded into **polypeptide chains** by ribosomes. However, **codon usage biases** vary across species and cell types, impacting **protein yield, stability, and function**. 

Existing **public codon optimization tools** may not always improve protein expression and can even result in **misfolding** or **reduced efficiency**, especially for **secretory proteins** used in therapeutics.

## **Our Approach**
To address these limitations, we developed an **AI-driven codon optimization model** trained on **gene expression data** from three mouse tissues:

- **Brain**
- **Liver**
- **Muscle**

Additionally, we trained models for **human and mouse secretory proteins**.

### **Key Features**
- **Deep Learning-Powered** – Uses RNNs to capture tissue-specific codon biases.
- **Tailored for Secretory Proteins** – Focuses on proteins crucial for **therapeutics, gene therapy, and vaccine manufacturing**.
- **Enhanced Expression** – Tested on firefly luciferase, enhanced green fluorescent protein (eGFP), and Gaussia luciferase, achieving **higher expression** than commercially available tools.
- **Validated in vitro** – Liver-trained models consistently outperformed other approaches.

## **Applications**
**Biopharmaceuticals & Gene Therapy** – Improves expression of therapeutic proteins.  
**Vaccine Development** – Optimizes antigens for maximal yield in **expression systems**.  
**Synthetic Biology** – Enhances recombinant protein production.  



License
This project is licensed under the MIT License.

Contributor:
👤 Sandhiya Ravi – Postdoctoral Researcher & Developer

