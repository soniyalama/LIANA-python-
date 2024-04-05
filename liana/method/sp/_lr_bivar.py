from __future__ import annotations

from anndata import AnnData
import pandas as pd
from typing import Optional

from liana.method.sp._SpatialBivariate import SpatialBivariate
from liana._docs import d
from liana._constants import Keys as K, DefaultValues as V

class SpatialLR(SpatialBivariate):
    """ A child class of SpatialBivariate for ligand-receptor analysis. """
    def __init__(self):
        super().__init__(x_name='ligand', y_name='receptor')

    @d.dedent
    def __call__(self,
                 adata: AnnData,
                 local_name: str = 'cosine',
                 global_name: (None | str | list) = None,
                 resource_name: str = V.resource_name,
                 resource: Optional[pd.DataFrame] = V.resource,
                 interactions: list = V.interactions,
                 expr_prop: float = 0.05,
                 n_perms: (None | int) = None,
                 mask_negatives: bool = False,
                 seed: int = V.seed,
                 add_categories: bool = False,
                 use_raw: Optional[bool] = V.use_raw,
                 layer: Optional[str] = V.layer,
                 connectivity_key = K.connectivity_key,
                 inplace = True,
                 obsm_added='local_scores',
                 lr_sep=V.lr_sep,
                 verbose: Optional[bool] = V.verbose,
                 ):
        """
        Local ligand-receptor interaction metrics and global scores.

        Parameters
        ----------
        %(adata)s
        %(local_name)s
        %(global_name)s
        %(resource_name)s
        %(resource)s
        %(interactions)s
        %(expr_prop)s
        %(n_perms)s
        %(mask_negatives)s
        %(seed)s
        %(add_categories)s
        %(use_raw)s
        %(layer)s
        %(connectivity_key)s
        %(inplace)s
        obsm_added: str
            Key in `adata.obsm` where the local scores are stored.
        %(lr_sep)s
        %(verbose)s

        Returns
        -------
        If `inplace` is `True`, the results are added to `mdata` and `None` is returned.
        Note that `obsm`, `varm`, `obsp` and `varp` are copied to the output `AnnData` object.
        When an MuData object is passed, `obsm`, `varm`, `obsp` and `varp` are copied to `.mod`.
        When `mdata` is an AnnData object, `obsm`, `varm`, `obsp` and `varp` are copied to `.obsm`.
        `AnnData` objects in `obsm` will not be copied to the output object.

        If `inplace` is `False`, the results are returned.
        """

        lr_res, local_scores = super().__call__(
            mdata=adata,
            local_name=local_name,
            global_name=global_name,
            connectivity_key=connectivity_key,
            resource_name=resource_name,
            resource=resource,
            interactions=interactions,
            nz_threshold=expr_prop,
            n_perms=n_perms,
            mask_negatives=mask_negatives,
            add_categories=add_categories,
            x_mod=True,
            y_mod=True,
            x_use_raw=use_raw,
            x_layer=layer,
            seed=seed,
            verbose=verbose,
            xy_sep=lr_sep,
            inplace=False,
            complex_sep='_'
            )

        return self._handle_return(adata, lr_res, local_scores, obsm_added, inplace)

lr_bivar = SpatialLR()
