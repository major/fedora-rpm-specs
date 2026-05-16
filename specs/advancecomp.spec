Name:           advancecomp
Version:        2.6
Release:        %autorelease
Summary:        Recompression utilities for .png, .mng, .zip and .gz files

# Source file headers all specify GPL-2.0-or-later, except:
#
#   The bundled and forked 7z (7-Zip code) in 7z/ is under the “LGPL” license.
#   Based on https://www.7-zip.org/license.txt, and the absence of any mention
#   of license changes in https://www.7-zip.org/history.txt, 7-Zip has always
#   been licensed under LGPL-2.1-or-later, specifically; we thus assume this is
#   the intended specific license for the contents of the 7z/ directory. None
#   of the sources that would be covered by the “unRAR license restriction” or
#   the BSD-3-Clause license for LZFSE are present in this fork.
#
# However, in version 1.17, the COPYING file was updated to GPLv3, with a
# changelog message (in HISTORY and elsewhere) of “Changes to GPL3.” We
# interpret this as an overall license of GPL-3.0-only.
License:        GPL-3.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
# Additionally, the following bundled libraries are removed in %%prep and do
# not contribute to the licenses of the binary RPMs:
# - Apache-2.0: zopfli/
# - MIT: libdeflate/
SourceLicense:  %{license} AND Apache-2.0 AND MIT
URL:            https://www.advancemame.it/
%global forgeurl https://github.com/amadvance/advancecomp
Source:         %{forgeurl}/archive/v%{version}/advancecomp-%{version}.tar.gz

BuildRequires:  dos2unix

BuildRequires:  autoconf
BuildRequires:  automake

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

# System library supported by upstream
BuildRequires:  zlib-devel

# Unbundled downstream
BuildRequires:  pkgconfig(libdeflate) >= 1.19
BuildRequires:  zopfli-devel

# The point of the 2.6 release was to upgrade the bundled libdeflate; enforce
# this on the unbundled libdeflate.
Requires:       libdeflate >= 1.19

# From 7z/README:
#
#   This directory contains some source files from the
#   7z archive utility. (www.7-zip.org)
#
#   All the files in this directory was originally released
#   with the LGPL license.
#
#   All the modifications made on the original files must
#   be considered Copyright (C) 2002 Andrea Mazzoleni and
#   released under the LGPL license.
#
# It is not clear which version was forked. Because 7-Zip does not provide a
# library, and because the implementation is modified, there is no possibility
# of unbundling. Note that this was forked from the original 7-Zip, not from
# p7zip.
Provides:      bundled(7zip)

%description
AdvanceCOMP contains recompression utilities for your .zip archives,
.png images, .mng video clips and .gz files.

The official site of AdvanceCOMP is:

  https://www.advancemame.it

This package contains:
  advzip - Recompression and test utility for zip files
  advpng - Recompression utility for png files
  advmng - Recompression utility for mng files
  advdef - Recompression utility for deflate streams in .png, .mng and .gz files


%prep
%autosetup

dos2unix --keepdate doc/*.txt

# Patch out bundled libdeflate
rm --recursive --verbose libdeflate
sed --regexp-extended --in-place '/libdeflate[\/_]/d' Makefile.am
# Fix up #include paths. The find-then-modify pattern keeps us from discarding
# mtimes on any sources that do not need modification.
find . -type f -exec gawk \
    '/^[[:blank:]]*#include.*libdeflate/ { print FILENAME; nextfile }' \
    '{}' '+' |
  xargs --no-run-if-empty --verbose sed --regexp-extended --in-place \
      's@^([[:blank:]]*#include.*)libdeflate/@\1@'

# Patch out bundled zopfli
rm --recursive --verbose zopfli
sed --regexp-extended --in-place \
    --expression '/zopfli[\/_]/d' \
    --expression 's/((\(7z_SOURCES\)|WindowOut\.h).*)[[:blank:]]*\\/\1/' \
    Makefile.am
# Fix up #include paths. The find-then-modify pattern keeps us from discarding
# mtimes on any sources that do not need modification.
find . -type f -exec gawk \
    '/^[[:blank:]]*#include.*zopfli/ { print FILENAME; nextfile }' \
    '{}' '+' |
  xargs --no-run-if-empty -t sed --regexp-extended --in-place \
      --expression 's@^([[:blank:]]*#include.*)zopfli/@\1@'


%conf
autoreconf --force --install --verbose

# Link against system libdeflate
export CFLAGS="$(pkgconf --cflags libdeflate) ${CFLAGS-}"
export CXXFLAGS="$(pkgconf --cflags libdeflate) ${CXXFLAGS-}"
export LDFLAGS="$(pkgconf --libs libdeflate) ${LDFLAGS-}"

# Link against system zopfli
export LDFLAGS="-lzopfli ${LDFLAGS-}"

%configure


%build
%make_build


%install
%make_install


# We don’t run upstream tests (%%make_build check) because they are too
# brittle, expecting recompressed outputs to be identical. Across platforms,
# compilers, and unbundled library versions, this doesn’t hold up.


%files
%license COPYING
%doc AUTHORS
%doc HISTORY
%doc README
%doc doc/adv{def,mng,png,zip}.txt

%{_bindir}/adv{def,mng,png,zip}
%{_mandir}/man1/adv{def,mng,png,zip}.1*


%changelog
%autochangelog
