Name:           sng
Version:        1.1.1
Release:        %autorelease
Summary:        Lossless editing of PNGs via a textual representation

License:        Zlib
URL:            https://sng.sourceforge.net/
Source0:        https://sourceforge.net/projects/sng/files/sng-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  rgb
BuildRequires:  rubygem-asciidoctor

Requires:       rgb

%description
SNG (Scriptable Network Graphics) is a minilanguage designed specifically to
represent the entire contents of a PNG (Portable Network Graphics) file in an
editable form. Thus, SNGs representing elaborate graphics images and ancillary
chunk data can be readily generated or modified using only text tools.

SNG is implemented by a compiler/decompiler called sng that losslessly
translates between SNG and PNG.

%prep
%autosetup

%build
%make_build

%install
%make_install prefix=%{_prefix}

%check
# Upstream has a test suite, but the test files are not packaged.
# Let's just check on the files that are in the tarball.
./sng_regress *.png *.sng

%files
%license COPYING
%doc NEWS.adoc README TODO
%doc %_mandir/man1/sng.1*
%_bindir/sng

%changelog
%autochangelog
