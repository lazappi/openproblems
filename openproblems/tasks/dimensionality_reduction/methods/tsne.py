from ....tools.decorators import method
from ....tools.utils import check_version
from .preprocessing import preprocess_logCPM_1kHVG

import scanpy as sc


@method(
    method_name="“t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCPM, 1kHVG)",
    paper_name="Visualizing Data using t-SNE",
    paper_url="https://lvdmaaten.github.io/publications/papers/JMLR_2008.pdf",
    paper_year=2008,
    code_url="https://scikit-learn.org/stable/modules/generated/"
    "sklearn.manifold.TSNE.html#sklearn.manifold.TSNE",
    code_version=check_version("MulticoreTSNE"),
    image="openproblems-python-extras",
)
def tsne_logCPM_1kHVG(adata):
    adata = preprocess_logCPM_1kHVG(adata)
    sc.tl.tsne(adata, use_rep="X_input", n_pcs=50)
    adata.obsm["X_emb"] = adata.obsm["X_tsne"]
    return adata
