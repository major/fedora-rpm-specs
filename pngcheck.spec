Name:           pngcheck
Version:        3.0.3
Release:        %autorelease
Summary:        Verifies the integrity of PNG, JNG and MNG files

# Note that the main package contains only pngcheck, compiled from a single
# source file, pngcheck.c, under a minimal MIT-style license that matches SPDX
# HPND:
#   https://gitlab.com/fedora/legal/fedora-license-data/-/issues/85
#   https://tools.spdx.org/app/license_requests/187/
#   https://github.com/spdx/license-list-XML/issues/1725
# The new utilities licensed under GPL-2.0-or-later are compiled from the gpl/
# subdirectory and packaged in the extras subpackage.
License:        HPND
URL:            http://www.libpng.org/pub/png/apps/pngcheck.html
Source:         http://www.libpng.org/pub/png/src/pngcheck-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  make

%description
pngcheck verifies the integrity of PNG, JNG and MNG files (by checking the
internal 32-bit CRCs [checksums] and decompressing the image data); it can
optionally dump almost all of the chunk-level information in the image in
human-readable form. For example, it can be used to print the basic statistics
about an image (dimensions, bit depth, etc.); to list the color and
transparency info in its palette (assuming it has one); or to extract the
embedded text annotations. This is a command-line program with batch
capabilities.

The current release supports all PNG, MNG and JNG chunks, including the newly
approved sTER stereo-layout chunk. It correctly reports errors in all but two
of the images in Chris Nokleberg's brokensuite-20061204.


%package extras
Summary:        Helper utilities distributed with pngcheck
License:        GPL-2.0-or-later

%description extras
Included with pngcheck (since version 2.1.0) are two helper utilities:

  - pngsplit - break a PNG, MNG or JNG image into constituent chunks (numbered
    for easy reassembly)
  - png-fix-IDAT-windowsize - fix minor zlib-header breakage caused by libpng
    1.2.6


%prep
%autosetup


%build
%make_build -f Makefile.unx \
    CFLAGS="${CFLAGS-} -DUSE_ZLIB $(pkg-config --cflags zlib)" \
    LIBS="${LDFLAGS-} $(pkg-config --libs zlib)"


%install
install -t '%{buildroot}%{_bindir}' -D -p \
    pngcheck pngsplit png-fix-IDAT-windowsize
install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p *.1 gpl/*.1


%files
%license LICENSE
%doc CHANGELOG
%doc README
%{_bindir}/pngcheck
%{_mandir}/man1/pngcheck.1*


%files extras
%license gpl/COPYING
%doc CHANGELOG
%doc README
%{_bindir}/pngsplit
%{_bindir}/png-fix-IDAT-windowsize
%{_mandir}/man1/pngsplit.1*
%{_mandir}/man1/png-fix-IDAT-windowsize.1*


%changelog
%autochangelog
