Name:           sfnt2woff-zopfli
Version:        1.3.1
Release:        %autorelease
Summary:        Create WOFF files with Zopfli compression

# From COPYING:
#
#   Sources in the top-level directory belong to, or are based on, the WOFF
#   reference implementation originally published at
#   http://people.mozilla.org/~jkew/woff/, and are distributed under the terms
#   specified in the file LICENSE-WOFF (MPL 1.1/GPL 2.0/LGPL 2.1).
#   
#   Additionally, the zopfli/ directory contains a bundled copy of Zopfli
#   (https://github.com/google/zopfli), distributed under the terms in the file
#   LICENSE-ZOPFLI (Apache License 2.0). When this bundled library is used,
#   these terms also apply to the compiled software.
#
# Note that all bundled Zopfli code is removed in %%prep, so only the
# MPL/GPL/LGPL portions remain.
License:        MPL-1.0 OR GPL-2.0-or-later OR LGPL-2.0-or-later
URL:            https://github.com/bramstein/sfnt2woff-zopfli
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Fix a possible double free in woffEncode()
# https://github.com/bramstein/sfnt2woff-zopfli/pull/18
Patch:          %{url}/pull/18.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Note that the URL http://people.mozilla.org/~jkew/woff/, where the original
# WOFF reference implementation sources were published, is no longer available.
# A copy of that page can be found at
# https://web.archive.org/web/20170630235618/https://people-mozilla.org/~jkew/woff/,
# and the sources are mirrored at https://github.com/TheJessieKirk/sfnt2woff.
# See also https://src.fedoraproject.org/rpms/woff.

BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  zopfli-devel

%description
This is a modified version of the sfnt2woff utility that uses Zopfli as a
compression algorithm instead of zlib. This results in compression gains of —
on average — 5-8% compared to regular WOFF files. Zopfli generates compressed
output that is compatible with regular zlib compression so the resulting WOFF
files can be used everywhere.

A corresponding version of the woff2sfnt utility is also provided.


%prep
%autosetup -p1
# Strip out bundled Zopfli sources
rm -rvf zopfli


%build
%make_build \
    ZLIB_CFLAGS="$(pkg-config --cflags zlib)" \
    ZLIB_LIBS="$(pkg-config --libs zlib)" \
    ZOPFLI_CFLAGS='' \
    ZOPFLI_LIBS='-lzopfli'


%install
install -d '%{buildroot}%{_bindir}'
install -t '%{buildroot}%{_bindir}' -p sfnt2woff-zopfli woff2sfnt-zopfli
install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 \
    sfnt2woff-zopfli.1 woff2sfnt-zopfli.1


%files
%doc README.md
%license COPYING
%license LICENSE-WOFF
%license LICENSE-WOFF-MPL
%license LICENSE-WOFF-GPL
%license LICENSE-WOFF-LGPL

%{_bindir}/sfnt2woff-zopfli
%{_bindir}/woff2sfnt-zopfli

%{_mandir}/man1/sfnt2woff-zopfli.1*
%{_mandir}/man1/woff2sfnt-zopfli.1*


%changelog
%autochangelog
