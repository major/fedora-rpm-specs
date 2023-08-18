Name:           ugrep
Version:        3.12.7
Release:        %autorelease
Summary:        Faster, user-friendly, and compatible grep replacement
License:        BSD-3-Clause
URL:            https://github.com/Genivia/ugrep
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pcre2-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  lz4-devel
BuildRequires:  libzstd-devel

# https://github.com/Genivia/ugrep/issues/215
Provides:       bundled(libreflex) = 3.3.0


%description
Ultra fast grep with interactive TUI, fuzzy search, boolean queries, hexdumps
and more: search file systems, source code, text, binary files, archives
(cpio/tar/pax/zip), compressed files (gz/Z/bz2/lzma/xz/lz4/zstd), documents
etc.  A faster, user-friendly and compatible grep replacement.


%prep
%autosetup


%build
%ifarch %{arm}
# https://github.com/Genivia/ugrep/issues/128
%configure --disable-neon
%else
%configure
%endif
%make_build


%install
%make_install


%check
%make_build test


%files
%license LICENSE.txt
%{_bindir}/ug
%{_bindir}/ug+
%{_bindir}/ugrep
%{_bindir}/ugrep+
%{_mandir}/man1/ug.1*
%{_mandir}/man1/ugrep.1*
%{_datadir}/ugrep


%changelog
%autochangelog
