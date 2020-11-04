import os
import tempfile

import anndata
import scprep

from . import utils

URL = (
    "https://ndownloader.figshare.com/files/24566651?private_link=e3921450ec1bd0587870"
)


@utils.loader
def load_zebrafish(test=False):
    """Download zebrafish data from figshare."""
    with tempfile.TemporaryDirectory() as tempdir:
        filepath = os.path.join(tempdir, "zebrafish.h5ad")
        scprep.io.download.download_url(URL, filepath)
        adata = anndata.read_h5ad(filepath)
        utils.filter_genes_cells(adata)

    if test:
        utils.subsample_even(adata, n_obs=500, even_obs="lab")
        utils.filter_genes_cells(adata)
        adata = adata[:, :100]
        utils.filter_genes_cells(adata)
    return adata
