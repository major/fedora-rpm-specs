Name:           woff
Version:        0.20091126
Release:        %autorelease
Summary:        Encoding and decoding for Web Open Font Format (WOFF)

License:        MPL-1.0 OR GPL-2.0-or-later OR LGPL-2.0-or-later
# Note that the URL http://people.mozilla.org/~jkew/woff/, where the original
# WOFF reference implementation sources were published, is no longer available.
# A copy of that page can be found at
# https://web.archive.org/web/20170630235618/https://people-mozilla.org/~jkew/woff/,
# and the sources are mirrored at https://github.com/TheJessieKirk/sfnt2woff.
%global original_url https://people-mozilla.org/~jkew/woff/
# The URL is no longer active, so we reference an archived copy:
URL:            https://web.archive.org/web/20170630235618/%{original_url}
# There is no longer a working URL for this archive.
Source0:        %{original_url}/woff-code-latest.zip
# Hand-written for Fedora in groff_man(7) format based on --help output
Source1:        sfnt2woff.1
Source2:        woff2sfnt.1

# It’s possible that tableOrder could be freed twice if a failure occurs. Set
# the pointer null after freeing it to prevent this. There is no current
# upstream to which this could be reported; however, this was reported to the
# sfnt2woff-zopfli fork:
#
# Fix a possible double free in woffEncode()
# https://github.com/bramstein/sfnt2woff-zopfli/pull/18
Patch:          possible-double-free.patch

# Add full text of the three WOFF licenses:
#   - LICENSE-WOFF-MPL, from
#     https://www.mozilla.org/media/MPL/1.1/index.0c5913925d40.txt
#   - LICENSE-WOFF-GPL, from
#     https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#   - LICENSE-WOFF-LGPL, from
#     https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
# https://github.com/bramstein/sfnt2woff-zopfli/commit/7e08f1c944142c8e37050d9e02d91ec326d60ba5
Patch:          https://github.com/bramstein/sfnt2woff-zopfli/commit/7e08f1c944142c8e37050d9e02d91ec326d60ba5.patch
# Update GPL/LGPL license texts for remote-only FS
# https://github.com/bramstein/sfnt2woff-zopfli/pull/21
Patch:          https://github.com/bramstein/sfnt2woff-zopfli/pull/21.patch

# Fix segfault due to https://bugs.debian.org/785795.
#   Remaining Debian patch rollup
# https://github.com/bramstein/sfnt2woff-zopfli/pull/20
# Since the patches from the sfnt2woff-zopfli do not apply directly, we link
# the patches Debian uses for woff (which they call woff-tools) where possible;
# see https://sources.debian.org/patches/woff-tools/0:2009.10.04-2.
# - Fix segfault due to https://bugs.debian.org/785795
#   https://github.com/bramstein/sfnt2woff-zopfli/pull/20/commits/51d74ebc4ab782f9e272fa4f135ee2375c991a5b
#   Rebased from the sfnt2woff-zopfli fork onto the original woff release
Patch:          segfault-debian-bug-785795.patch
# - Add arithmetic overflow checks in woff encoding routines
Patch:          https://sources.debian.org/data/main/w/woff-tools/0%3A2009.10.04-2/debian/patches/add-overflow-checks.patch
# - Fix CVE-2010-1028: WOFF heap corruption due to integer overflow
Patch:          https://sources.debian.org/data/main/w/woff-tools/0%3A2009.10.04-2/debian/patches/CVE-2010-1028.patch
# - fix some compiler and cppcheck warnings
Patch:          https://sources.debian.org/data/main/w/woff-tools/0%3A2009.10.04-2/debian/patches/fix-compiler-and-cppcheck-warnings.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc

BuildRequires:  zlib-devel

%description
Provides the sfnt2woff and woff2sfnt command-line tools for encoding and
decoding Web Open Font Format (WOFF) files.

%prep
%autosetup -c -p1


%build
%make_build CFLAGS="${CFLAGS}"
awk '
    /BEGIN LICENSE BLOCK/ { b = 1 }
    b
    /END LICENSE BLOCK/ { b = 0 }' woff.c |
  tee LICENSE-WOFF


%install
# The Makefile has no install target.
install -d '%{buildroot}%{_bindir}'
install -t '%{buildroot}%{_bindir}' -p sfnt2woff woff2sfnt
install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 '%{SOURCE1}' '%{SOURCE2}'


# Upstream provides no tests


%files
%license LICENSE-WOFF
%license LICENSE-WOFF-MPL
%license LICENSE-WOFF-GPL
%license LICENSE-WOFF-LGPL

%doc woff-2009-10-03.html

%{_bindir}/sfnt2woff
%{_bindir}/woff2sfnt
%{_mandir}/man1/sfnt2woff.1*
%{_mandir}/man1/woff2sfnt.1*


%changelog
%autochangelog
