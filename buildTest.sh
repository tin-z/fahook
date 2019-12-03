#!/bin/sh


export ARCH=$1


warn()
{
	echo "$1" >&2
  exit 1
}


if [ "$ARCH" = "arm" ]; then
  if [ ! -z $(which arm-linux-gnueabi-gcc) ];
  then
    export CC=$(which arm-linux-gnueabi-gcc)
  else
    warn "Not setting CC: can't locate arm-linux-gnueabi-gcc."
  fi
elif [ "$ARCH" = "x86" ]; then
  if [ ! -z $(which gcc) ];
  then
    export CC=$(which gcc)
    export LMFLAGS="-m32"
  else
    warn "Not setting CC: can't locate gcc."
  fi
elif [ "$ARCH" = "x64" ]; then
  if [ ! -z $(which gcc) ];
  then
    export CC=$(which gcc)
  else
    warn "Not setting CC: can't locate gcc."
  fi
else
  warn "Arch not supported.. the arch supported by are arm, x86, x64"
fi


make || exit $?

