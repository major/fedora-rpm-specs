%global pkgname ace
%global giturl  https://github.com/gap-packages/ace

Name:           gap-pkg-%{pkgname}
Version:        5.6.2
Release:        %autorelease
Summary:        Advanced Coset Enumerator

License:        MIT
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/ace/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  tth

Requires:       gap-core%{?_isa}

%description
The ACE package provides a mechanism to replace GAP's usual Todd-Coxeter
coset enumerator by ACE, so that functions that behind the scenes use
coset enumeration will use the ACE enumerator.  The ACE enumerator may
also be used explicitly; both non-interactively and interactively.
However the package is used, a plethora of options and strategies are
available to assist the user in avoiding incomplete coset enumerations.

%package doc
# The content is MIT.  The remaining licenses cover the various fonts embedded
# in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        MIT AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        Advanced Coset Enumerator documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure %{gap_archdir}
%make_build

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/etc ../../etc
make doc
rm -f ../../{doc,etc}

# Package PDF instead of PostScript
pushd standalone-doc
ps2pdf ace3001.ps ace3001.pdf
popd

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin examples gap htm res-examples tst VERSION \
   %{buildroot}%{gap_archdir}/pkg/%{pkgname}
rm %{buildroot}%{gap_archdir}/pkg/%{pkgname}/gap/CHANGES
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/gap/
%{gap_archdir}/pkg/%{pkgname}/tst/
%{gap_archdir}/pkg/%{pkgname}/VERSION

%files doc
%doc standalone-doc/ace3001.pdf
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/examples/
%docdir %{gap_archdir}/pkg/%{pkgname}/htm/
%docdir %{gap_archdir}/pkg/%{pkgname}/res-examples/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/examples/
%{gap_archdir}/pkg/%{pkgname}/htm/
%{gap_archdir}/pkg/%{pkgname}/res-examples/

%changelog
%autochangelog
