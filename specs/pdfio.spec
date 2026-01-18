Name: pdfio
Version: 1.6.1
Release: 2%{?dist}
Summary: C library for PDF I/O
# Apache 2.0 with exception - pdfio code
# GPL-2.0-or-later - code128 font from examples
# Zlib - md5 code
# MIT-CMU - rc4 code
# BSD-3-Clause - sha256 code
License: Apache-2.0 WITH LLVM-exception AND Zlib AND GPL-2.0-or-later AND MIT-CMU AND BSD-3-Clause
URL: https://msweet.org/pdfio
Source0: https://github.com/michaelrsweet/pdfio/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/michaelrsweet/pdfio/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# Mike's public key from here https://www.msweet.org/pgp.html
Source2: msweet-pub.gpg


# Patches


# uses autosetup with git
BuildRequires: git-core
# builds with gcc
BuildRequires: gcc
# for verifying the tarball signature
BuildRequires: gpgverify
# use make for Makefile
BuildRequires: make
# uses pkg-config in SPEC and in configure
BuildRequires: pkgconf-pkg-config
# supports compression
BuildRequires: pkgconfig(zlib)
# for enhanced PNG support
BuildRequires: pkgconfig(libpng16)

%description
PDFIO is C library for reading and writing PDF files. It includes support
for reading and writing encrypted PDF files, accessing pages, objects,
and streams withing PDF file, working with PDF metadata etc.

%package devel
Summary: PDFIO development files and examples
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
# uses Roboto fonts in examples - use requires instead of bundling them
Requires: google-roboto-fonts
Requires: google-roboto-mono-fonts

%description devel
The package contains development files for PDFIO library.

%package doc
Summary: PDFIO documentation
BuildArch: noarch

%description doc
The package contains HTML documentation and man page for PDFIO library.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S git


%build
%configure --libdir=%{_libdir} \
  --disable-static \
  --enable-shared \
  --enable-libpng

%make_build


%install
make install

# remove duplicated license
rm %{buildroot}/%{_pkgdocdir}/{LICENSE,NOTICE}
# copy the font licenses into correct license dir and remove the files
# in the old location
cp -p %{buildroot}%{_pkgdocdir}/examples/code128-LICENSE.txt .
rm %{buildroot}%{_pkgdocdir}/examples/*LICENSE*

# copy the examples to -devel
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
cp -pr %{buildroot}%{_pkgdocdir}/examples/ %{buildroot}%{_docdir}/%{name}-devel
rm -rf %{buildroot}%{_pkgdocdir}/examples/

# make symlink for big fonts which are already packaged in Fedora
for font in Roboto-Bold.ttf Roboto-Italic.ttf Roboto-Regular.ttf
do
  ln -sf ../../../fonts/google-roboto/$font %{buildroot}%{_docdir}/%{name}-devel/examples/$font
done

ln -sf ../../../fonts/google-roboto-mono-fonts/RobotoMono-Regular.ttf %{buildroot}%{_docdir}/%{name}-devel/examples/RobotoMono-Regular.ttf


%check
make test


%files
%license LICENSE NOTICE
%{_libdir}/libpdfio.so.1

%files devel
%license code128-LICENSE.txt
# TrueType fonts, C source files, docs
# for examples
%dir %{_docdir}/%{name}-devel
%{_docdir}/%{name}-devel/examples
%{_includedir}/pdfio.h
%{_includedir}/pdfio-content.h
%{_libdir}/libpdfio.so
%{_libdir}/pkgconfig/pdfio.pc

%files doc
%dir %{_pkgdocdir}
%{_docdir}/%{name}/pdfio.html
%{_docdir}/%{name}/pdfio-512.png
%{_mandir}/man3/pdfio.3.gz


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jan 14 2026 Zdenek Dohnal <zdohnal@redhat.com> - 1.6.1-1
- Initial import (fedora#2428693)
