# ROADMAP

## known issues

- `qsv.yml` pinned to early version because cluster GLIBC < 2.35
- `dash-bio` isn't correctly set up to use jupyter
- `micromamba` issues when creating path using prefix (`-p`) instead of name (`-n`)

## software

### Gviz

- https://bioconductor.org/packages/release/bioc/vignettes/Gviz/inst/doc/Gviz.html

### pairix

- https://github.com/4dn-dcic/pairix

### sanger-pathogens/Artemis

Artemis is a free genome viewer and annotation tool that allows visualization of sequence features and the results of analyses within the context of the sequence, and its six-frame translation

- https://github.com/sanger-pathogens/Artemis
- http://sanger-pathogens.github.io/Artemis/

### `bioawk`

- https://github.com/vsbuffalo/bioawk-tutorial
- https://github.com/lh3/bioawk

### FigTree

- https://github.com/rambaut/figtree/releases
- http://tree.bio.ed.ac.uk/software/figtree/

### `vcferr`

- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11109540/

### Spark and Spark SQL CLI

- https://spark.apache.org/news/spark-4.0.0-preview2.html
- https://spark.apache.org/docs/4.0.0-preview2/sql-distributed-sql-engine-spark-sql-cli.html

### `vcfgl`: A flexible genotype likelihood simulator for VCF/BCF files

- https://www.biorxiv.org/content/10.1101/2024.04.09.586324v1
- https://github.com/isinaltinkaya/vcfgl

### CLARK

- http://clark.cs.ucr.edu

### CoreCruncher

- https://github.com/lbobay/CoreCruncher

### `iTol`

- https://github.com/TongZhou2017/itol.toolkit

### simuG: a general-purpose genome simulator

- https://github.com/yjx1217/simuG

### BBMap: BBMap short read aligner, and other bioinformatic tools.

- https://sourceforge.net/projects/bbmap/

### `csvquote`

- https://github.com/dbro/csvquote/releases/tag/v0.1.5

### `gotree`

- https://github.com/evolbioinfo/gotree

### `haptools`: Haptools is a collection of tools for simulating and analyzing genotypes and phenotypes while taking into account haplotype and ancestry information.

- https://haptools.readthedocs.io/en/stable/index.html

### Cairo

```bash
cd $GROUP_HOME
mkdir -p cairo/1.18.2
cd cairo/1.18.2
wget https://www.cairographics.org/releases/cairo-1.18.2.tar.xz
tar xf cairo-1.18.2.tar.xz
rm -f cairo-1.18.2.tar.xz

# Installation Instructions
# =========================

# Requirements
# ------------
# As well as the requirements listed in README, the meson build also requires:
#   meson (http://mesonbuild.com)
#   ninja (http://ninja-build.org)

# Basic Installation
# ------------------
#   meson setup $builddir
#   ninja -C $builddir
#   ninja -C $builddir install

# where $builddir is the name of the directory where the build artifacts
# will be written to.

# Some of the common options that can be used with "meson setup" include:

# Set the install prefix.
#   --prefix=<path>

# Set the build type. Some common build types include "debug" and "release"
#   --buildtype=<buildtype>

# Compiler and linker flags can be set with the CFLAGS and LDFLAGS
# environment variables.

# Configuring cairo backends
# --------------------------
# After running "meson build", "meson configure" can be used to display
# or modify the build configuration.

# eg

#  Display configuration:
#     meson configure $builddir

#  Enable pdf and disable ps:
#     meson configure $builddir -Dpdf=enabled -Dps=disabled

# The "-D" options can also be used with "meson setup"

# Tests
# -----
# Refer to test/README
```

```bash
cd $GROUP_HOME
mkdir -p cairo/1.17.13
cd cairo/1.17.13
wget https://www.cairographics.org/releases/rcairo-1.17.13.tar.gz
tar xf rcairo-1.17.13.tar.gz
rm -f rcairo-1.17.13.tar.gz
```
