# Script to calculate Gromov-Wasserstein distances,
# using algorithms in Peyre et al. ICML 2016
import os
import ot
import itertools as it
import numpy as np
import numpy.typing as npt
import pandas as pd
import ctypes
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from multiprocessing import Pool
from typing import List, Optional, Tuple

from CAJAL.lib.utilities import pj, load_dist_mat, list_sort_files, read_mp_array

'''
TODO:

- Deal with read csv header vs not cutting out points
- Option to return GW matching between points in cells as well
- Overall function that loads distances and calculates GW in one
- Tests
    - num_pts should be same in each input file and distance matrix
    - no distances should be 0 except diagonal (might not be requirement)
    - **distance matrix files should be in upper/lower triangle format
'''


# def compute_intracell_distances_one(
#         data_file: str,
#         metric: str ="euclidean",
#         return_mp: bool =True,
#         header: Optional[int | List[int]] = None) ->  npt.NDArray[np.float_] :
#     """
#     Compute the pairwise distances in the point cloud stored in a \*.csv file.
#     Return distance matrix as numpy array

#     :param data_file: file path to point cloud file (currently assumes a header line)
#         * metric (string): distance metric passed into pdist()
#         * return_mp (boolean): if True, return multiprocessing array, if False return numpy array
#         * header: If the \*.csv file has a row header labelling the columns,
#              use this field to label it, see :func:`pandas.read_csv` for details.

#     Returns:
#         A multiprocessing array, if return_mp == True; else a numpy array.
#     """
    
#     coords = pd.read_csv(data_file, header=header)
#     dist_mat = pdist(coords, metric=metric)

#     # Return either as numpy array or mp (multiprocessing) array
#     try: 
#         return_dist = squareform(dist_mat)
#     except Exception as err:
#         print(err)
#         print("Scipy raised an error while computing intracell distances in ", data_file)
#         print("Check that this file is correctly formatted.")
#         raise
        
#     if return_mp:
#         return_dist = read_mp_array(return_dist)
#     return return_dist

# def save_distances_one(data_file, distances_dir=None, file_prefix="",
#                        metric="euclidean", header=None):
#     """
#     Not currently used, kept as legacy
#     Compute the pairwise distances in the point cloud stored in the file.
#     Save each to a file in distances_dir.


#     Args:
#         data_file (string): file path to point cloud file
#                           (currently assumes a header line)
#         distances_dir (string): if None (default), return list of multiprocessing array.
#                                if filepath string, save distance matrices in this directory
#         file_prefix (string): if distances_dir is a file path, prefix each output distance
#                              file with this string
#         metric (string): distance metric passed into pdist()
#         header (boolean): passed into read_csv, whether data file has a header line

#     Returns:
#         None (creates path to distances_dir and saves files there)
#     """
#     coords = pd.read_csv(data_file, header=header)
#     dist_mat = pdist(coords, metric=metric)

#     # Return distance matrices in list, except
#     # save distance matrices to the file path of distances_dir
#     outfile = file_prefix + "_" + data_file.replace(".csv", "") + "_dist.txt" \
#         if file_prefix != "" else data_file.replace(".csv", "") + "_dist.txt"
#     np.savetxt(pj(distances_dir, outfile),
#                dist_mat, fmt='%.8f')
#     return outfile


# def compute_intracell_distances_all(
#         data_dir: str,
#         data_prefix: Optional[str] =None,
#         data_suffix: str ="csv",
#         #distances_dir=None,
#         metric: str ="euclidean",
#         return_mp: bool =True,
#         header: Optional[int | List[int]] = None):
#     """
#     Compute the pairwise distances in the point cloud stored in each file.
#     Return list of distance matrices.
    
#     Args:
#         * data_dir (string): file path to directory containing all \
#                 point cloud files (currently assumes a header line)
#         * data_prefix (string): only read files from data_dir \
#               starting with this string. None (default) uses \
#               all files
#         * metric (string): distance metric passed into pdist()
#         * return_mp (boolean): only used of distances_dir is None.\
#               If True, return multiprocessing array,\
#               if False return numpy array
#         * header: If the \*.csv file has a row header labelling the\
#               columns, use this field to label it, see\
#               :func:`pandas.read_csv` for details. 
    
#     Returns:
#         List of distance matrices. (In the future, will be a list \
#             of distance matrices or None, in the case where \
#             the distances_dir flag is enabled.)

#     """

#     # if distances_dir is not None and not os.path.exists(distances_dir):
#     #     os.makedirs(distances_dir)

#     # (TODO : Add support for a flag "distances_dir" which will enable the user
#     #  to write the list of distance matrices in addition to / rather than returning it.)
    
#     files_list = list_sort_files(data_dir, data_prefix, data_suffix=data_suffix)
    
#     # Compute pairwise distance between points in each file
#     return_list = [compute_intracell_distances_one(pj(data_dir, data_file),
#                                                metric=metric, return_mp=return_mp, header=header)
#                    for data_file in files_list]
#     check_num_pts = all([len(x) == len(return_list[0]) for x in return_list])
#     if not check_num_pts:
#         raise Exception("Point cloud data files do not have same number of points")
#     return return_list


# def load_intracell_distances(distances_dir : str,
#                                 data_prefix: str =None):
#     """
#     Load distance matrices from directory into list of numpy arrays.
    
#     Args: 
#         distances_dir (string): input directory where distance files are saved
#         data_prefix (string): only read files from distances_dir starting with this string
#     Returns:
#         list of numpy arrays containing distance matrix for each cell
#     """

#     files_list = list_sort_files(distances_dir, data_prefix)
#     return [load_dist_mat(pj(distances_dir, dist_file))
#             for dist_file in files_list]

# def load_intracell_distances_mp(distances_dir, data_prefix=None):
#     """
#     Load distance matrices from directory into list of arrays.
    
#     Args: 
#         distances_dir (string): input directory where distance files are saved
#         data_prefix (string): only read files from distances_dir starting with this string
#         return_mp (boolean): if True, return multiprocessing array, if False return numpy array
    
#     Returns:
#         list of multiprocessing arrays containing distance matrix for each cell
#     """
#     files_list = list_sort_files(distances_dir, data_prefix)
#     return [load_dist_mat(pj(distances_dir, dist_file), return_mp=return_mp)
#             for dist_file in files_list]

def _calculate_gw_preload_global(
        index_pair : Tuple[int,int],
        return_mat : bool) -> Tuple[float, Optional[npt.NDArray[np.float_]]]:
    """
    Compute GW distance and the coupling matrix between two distance matrices.
    Meant to be called within a multiprocessing pool where dist_mat_list exists globally
    
    :param index_pair: indices in the global list dist_mat_list for the first\
         and second distance matrix, respectiveley
    :param return_mat: if True, returns the coupling matrix between points
            if False, only returns GW distance
    
        i1 (int): index in the dist_mat_list for the first distance matrix
            i2 (int): index in the dist_mat_list for the second distance matrix
            return_mat (boolean): 
    Returns:
        float: GW distance
    """
    # Get distance matrices from global list (this saves memory so it's not copied in each process)
    i1, i2 = arguments
    d1 = np.frombuffer(dist_mat_list[i1])
    numpts = int(np.sqrt(d1.shape))  # mp_arrays are in vector form, we know this is a square matrix
    d1 = d1.reshape((numpts, numpts))
    d2 = np.frombuffer(dist_mat_list[i2]).reshape((numpts, numpts))
    # Compute Gromov-Wasserstein matching coupling matrix and distance
    gw, log = ot.gromov.gromov_wasserstein(
            d1, d2, ot.unif(d1.shape[0]), ot.unif(d2.shape[0]),
            'square_loss', log=True)
    if return_mat:
        return log['gw_dist'], gw
    else:
        return log['gw_dist'], None
                                                    


def _init_fn(dist_mat_list_arg, save_mat):
    """
    Initialization function sets dist_mat_list to be global in multiprocessing pool.
    Also sets other arguments because I couldn't figure out how to lazily modify an iterator
    """
    global dist_mat_list, return_mat
    dist_mat_list = dist_mat_list_arg
    return_mat = save_mat


def compute_GW_distance_matrix(
        dist_mat_list_arg : List[npt.NDArray[np.float_]],
        save_mat : bool =False,
        num_cores : int=12,
        chunk_size : int =100)-> Tuple[npt.NDArray[np.float_],
                                       Optional[List[npt.NDArray[np.float_]]]]:
                                                
                                                    
    """
    Compute the GW distance between each pair of matrices in a given list of intracell \
    distance matrices
        
    :param dist_mat_list_arg: list of multiprocessing or numpy arrays containing distance\
              matrix for each cell
    :param save_mat: if True, returns coupling matrix (matching) between points. \
                            if False, only returns GW distance
    :param num_cores: number of parallel processes to run GW in
    :param chunk_size: chunk size for the iterator of all pairs of cells. \
            Larger size is faster but takes more memory, see \
            :meth:`multiprocessing.pool.Pool.imap` for details.

    :return:
        A matrix of the GW distances between all the intracell distance matrices in \
        dist_mat_list_arg.
    """
    arguments = it.combinations(range(len(dist_mat_list_arg)), 2)
                                                    

    # if num_cores > 1:
        # Start up multiprocessing w/ list of distance matrices in global environment
    with Pool(processes=num_cores,
              initializer=_init_fn,
              initargs=(dist_mat_list_, save_mat)) as pool:
        dist_results = list(pool.imap(
            _calculate_gw_preload_global,
            arguments,
            chunksize=chunk_size))
                                                    
    e = zip(*dist_results)
    GW_dist_mat = list(next(e))
    if save_mat:
        GW_coupling_mats = list(next(e))
    else:
        GW_coupling_mats = None
    return (GW_dist_mat, GW_coupling_mats)

                                    

    
    # else:
    #     # Set dist_mat_list in global environment so can call the same functions
    #     global dist_mat_list, return_mat
    #     dist_mat_list = dist_mat_list_arg
    #     return_mat = save_mat
    #     dist_results = list(map(_calculate_gw_preload_global, arguments))
# def compute_and_save_GW_dist_mat(
#         dist_mat_list_local : List[npt.NDArray| ctypes.Array],
#         file_prefix : str,
#         gw_results_dir : str,
#         save_mat:bool =False,
#         num_cores: int =12,
#         chunk_size: int =100):
#     """
    
#     Compute the GW distance between each pair of distance matrices in vector form,
#     and write the resulting matrix of GW distances to a file.

#     Args:
#         * dist_mat_list_local (list): list of multiprocessing or numpy arrays containing intracell \
#     distance matrix for each cell
#         * file_prefix (string): name of output file to write GW distance matrix to
#         * gw_results_dir (string): path to directory to write output file to
#         * save_mat (boolean): if True, returns coupling matrix (matching) between points.\
#                             if False, only returns GW distance
#         * num_cores (int): number of parallel processes to run GW in
#         * chunk_size (int): chunk size for the iterator of all pairs of cells. \
#                  Larger size is faster but takes more memory, see \
#                  :meth:`multiprocessing.pool.Pool.imap` for details

#     Returns:
#         None (writes distance matrix of GW distances to file)
#     """
#     # Create output directory
#     if not os.path.exists(gw_results_dir):
#         os.makedirs(gw_results_dir)

#     dist_results = compute_GW_distance_matrix_preload_global(
#                       dist_mat_list_local,
#                       save_mat=save_mat,
#                       num_cores=num_cores,
#                       chunk_size=chunk_size)

#     # Save results - suffix name of output files is currently hardcoded
#     if save_mat:
#         np.savetxt(pj(gw_results_dir, file_prefix + "_gw_dist_mat.txt"),
#                    np.array([res[0] for res in dist_results]), fmt='%.8f')
#         np.savez_compressed(pj(gw_results_dir, file_prefix + "_gw_matching.npz"), *[res[1] for res in dist_results])
#     else:
#         np.savetxt(pj(gw_results_dir, file_prefix + "_gw_dist_mat.txt"), np.array(dist_results), fmt='%.8f')
