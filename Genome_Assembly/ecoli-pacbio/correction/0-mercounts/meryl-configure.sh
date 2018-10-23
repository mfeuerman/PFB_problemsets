#!/bin/sh


#  Path to Canu.

syst=`uname -s`
arch=`uname -m | sed s/x86_64/amd64/`

bin="/Users/admin/canu/$syst-$arch/bin"

if [ ! -d "$bin" ] ; then
  bin="/Users/admin/canu"
fi

#  Report paths.

echo ""
echo "Found perl:"
echo "  " `which perl`
echo "  " `perl --version | grep version`
echo ""
echo "Found java:"
echo "  " `which java`
echo "  " `java -showversion 2>&1 | head -n 1`
echo ""
echo "Found canu:"
echo "  " $bin/canu
echo "  " `$bin/canu -version`
echo ""


#  Environment for any object storage.

export CANU_OBJECT_STORE_CLIENT=
export CANU_OBJECT_STORE_NAMESPACE=ecoli
export CANU_OBJECT_STORE_PROJECT=




/Users/admin/canu/Darwin-amd64/bin/meryl -C k=16 threads=4 memory=8 \
  count segment=1/01 ../../ecoli.seqStore \
> ecoli.ms16.config.01.out 2>&1
exit 0
