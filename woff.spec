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
# upstream to which this could be reported.
Patch:          possible-double-free.patch

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


%install
# The Makefile has no install target.
install -d '%{buildroot}%{_bindir}'
install -t '%{buildroot}%{_bindir}' -p sfnt2woff woff2sfnt
install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 '%{SOURCE1}' '%{SOURCE2}'


%files
%doc woff-2009-10-03.html
%{_bindir}/sfnt2woff
%{_bindir}/woff2sfnt
%{_mandir}/man1/sfnt2woff.1*
%{_mandir}/man1/woff2sfnt.1*


%changelog
%autochangelog
