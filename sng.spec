Name:           sng
Version:        1.1.0
Release:        %autorelease
Summary:        Lossless editing of PNGs via a textual representation

License:        zlib
URL:            http://sng.sourceforge.net/
Source0:        http://sourceforge.net/projects/sng/files/sng-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  rgb

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
%configure
%make_build

%install
%make_install

%check
# Upstream has a test suite, but the test files are not packaged.
# Let's just check on the files that are in the tarball.
./sng_regress *.png *.sng

%files
%license COPYING
%doc NEWS README TODO
%doc %_mandir/man1/sng.1*
%_bindir/sng

%changelog
%autochangelog
