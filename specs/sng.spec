Name:           sng
Version:        1.1.2
Release:        %autorelease
Summary:        Lossless editing of PNGs via a textual representation

License:        Zlib
URL:            https://sng.sourceforge.net/
# Release tarball is missing many files
Source0:        https://sourceforge.net/code-snapshots/git/s/sn/sng/code.git/sng-code-d0ebae1e7131df4e1f104a2c526dddb3fc965ab4.zip
Patch:          patch-1.diff

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
%autosetup -p1 -C
# Do not ignore specified linker flags
sed -r -i 's/LDFLAGS=/LDFLAGS+=/' Makefile

%build
%make_build VERSION=%{version}

%install
%make_install PREFIX=%{_prefix}
# WTF?
mv %{buildroot}%{_bindir}/bin/sng %{buildroot}%{_bindir}/

%check
# Upstream has a test suite, but the test files are not packaged.
# Let's just check on the files that are in the tarball.
./sng_regress *.png *.sng

%files
%license COPYING
%doc NEWS.adoc README.adoc TODO
%doc %_mandir/man1/sng.1*
%_bindir/sng

%changelog
%autochangelog
