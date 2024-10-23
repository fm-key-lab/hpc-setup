#!/bin/bash

set -euo pipefail

module purge; ml ariba

MLST_ARIBA=$1
cd $MLST_ARIBA

SLURM_LOGS=$MLST_ARIBA/.logs
mkdir -p $SLURM_LOGS

ariba pubmlstspecies | while IFS= read -r SPECIES; do
  echo "$SPECIES"
  PREFIX="$SLURM_LOGS/$(echo "$SPECIES" | tr -d ' ')"
  sbatch -o "$PREFIX.%j.out" -e "$PREFIX.%j.err" --nodes=1 --time=0:10:00 --mem=500MB --export=SPECIES="$SPECIES",MLST_ARIBA="$MLST_ARIBA" --wrap='ml ariba && ariba pubmlstget "$SPECIES" "$MLST_ARIBA/$SPECIES"'
  echo "--------------"
done