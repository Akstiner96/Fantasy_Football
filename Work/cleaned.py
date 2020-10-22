{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}

from pathlib import Path
import pandas as pd


def cleaned_data():
    #define csv paths
    qb_path = Path('../data/qb_data.csv')
    rb_path = Path('../data/rb_data.csv')
    wr_path = Path('../data/wr_data.csv')
    te_path = Path('../data/te_data.csv')
    fb_path = Path('../data/fb_data.csv')
    dst_path = Path('../data/dst_data.csv')
    k_path = Path('../data/k_data.csv')
    
    #store csv's as a callable variable
    qb_clean = pd.read_csv(qb_path, index_col="Player")
    rb_clean = pd.read_csv(rb_path, index_col="Player")
    wr_clean = pd.read_csv(wr_path, index_col="Player")
    te_clean = pd.read_csv(te_path, index_col="Player")
    fb_clean = pd.read_csv(fb_path, index_col="Player")
    dst_clean = pd.read_csv(dst_path, index_col="Player")
    k_clean = pd.read_csv(k_path, index_col="Player")
    
    return qb_clean, rb_clean, wr_clean, te_clean, fb_clean, dst_clean, k_clean


qb, rb, wr, te, fb, dst, k = cleaned_data()