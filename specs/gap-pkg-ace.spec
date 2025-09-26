%global gap_pkgname ace
%global giturl      https://github.com/gap-packages/ace

Name:           gap-pkg-%{gap_pkgname}
Version:        5.7.0
Release:        %autorelease
Summary:        Advanced Coset Enumerator

License:        MIT
URL:            https://gap-packages.github.io/ace/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin examples gap htm res-examples tst VERSION
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  tth

Requires:       gap-core%{?_isa}

%description
The ACE package provides a mechanism to replace GAP's usual Todd-Coxeter coset
enumerator by ACE, so that functions that behind the scenes use coset
enumeration will use the ACE enumerator.  The ACE enumerator may also be used
explicitly; both non-interactively and interactively.  However the package is
used, a plethora of options and strategies are available to assist the user in
avoiding incomplete coset enumerations.

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -p1 -n %{gap_upname}-%{version}

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

%install -a
rm %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/gap/CHANGES

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/tst/
%{gap_archdir}/pkg/%{gap_upname}/VERSION

%files doc
%doc standalone-doc/ace3001.pdf
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_archdir}/pkg/%{gap_upname}/examples/
%docdir %{gap_archdir}/pkg/%{gap_upname}/htm/
%docdir %{gap_archdir}/pkg/%{gap_upname}/res-examples/
%{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/examples/
%{gap_archdir}/pkg/%{gap_upname}/htm/
%{gap_archdir}/pkg/%{gap_upname}/res-examples/

%changelog
%autochangelog
