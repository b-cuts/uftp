#!/bin/sh

###############################################################################
# Quickly make a source distribution that should work on ALL POSIX systems
# that have a bourne shell
###############################################################################

#Reference For POSIX Commands
#http://manuals.ts.fujitsu.com/file/8867/posix_k.pdf

#where am i really from?
PROG=`readlink -f $0`
LOCATION=`dirname $PROG`
cd ${LOCATION} #make sure we are in the right place

VERSION=`grep '#define VERSIONSTR' uftp.h | awk '{print $5}' | tr -d '\n'`

#create a scatch space
mkdir -p ${LOCATION}/.tmp/uftp-${VERSION}

#filter out hidden src/version control dirs
pax -w -x ustar -s '!^.*/\..*$!!' . > ${LOCATION}/.tmp/out.tar

#now that hidden src control files have been removed re-archive
cd ${LOCATION}/.tmp/uftp-${VERSION}
pax -r -f ${LOCATION}/.tmp/out.tar
cd $LOCATION/.tmp

#compression utilities are not guaranteed, although i haven't seen a system
#without gzip or bzip2 in a long time.
pax -w -x ustar uftp-${VERSION} > ${LOCATION}/uftp-${VERSION}.tar

cd ${LOCATION}

#clean up
rm -rf ${LOCATION}/.tmp
