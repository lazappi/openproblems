from ....tools.decorators import method
from ....tools.utils import check_version
from anndata import AnnData

import scanpy as sc


def _ivis_preprocess(adata: AnnData) -> AnnData:
    sc.pp.normalize_per_cell(adata)
    sc.pp.log1p(adata)

    sc.pp.highly_variable_genes(adata, n_top_genes=3000)
    adata = adata[:, adata.var["highly_variable"]].copy()
    sc.tl.pca(adata)

    return adata


@method(
    method_name="Ivis (CPU)",
    paper_name="Structure-preserving visualisation of "
    "high dimensional single-cell datasets",
    paper_url="https://www.nature.com/articles/s41598-019-45301-0",
    paper_year=2019,
    code_url="https://github.com/beringresearch/ivis",
    code_version=check_version("ivis"),
    image="openproblems-python-extras",
)
def ivis(adata: AnnData) -> AnnData:
    from ivis import Ivis

    adata = _ivis_preprocess(adata)

    # parameters taken from:
    # https://bering-ivis.readthedocs.io/en/latest/
    # scanpy_singlecell.html#reducing-dimensionality-using-ivis
    ivis = Ivis(
        k=15,
        model="maaten",
        n_epochs_without_progress=5,
        verbose=False,
        embedding_dims=2,
    )
    adata.obsm["X_emb"] = ivis.fit_transform(adata.obsm["X_pca"])

    return adata
