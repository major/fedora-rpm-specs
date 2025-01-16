%global pkgname polenta
%global giturl  https://github.com/gap-packages/polenta

Name:           gap-pkg-%{pkgname}
Version:        1.3.10
Release:        %autorelease
Summary:        Polycyclic presentations for matrix groups

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/polenta/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-alnuth-doc
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-radiroot

Requires:       gap-pkg-alnuth
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-radiroot

Recommends:     gap-pkg-aclib

%description
The Polenta package provides methods to compute polycyclic presentations
of matrix groups (finite or infinite).  As a by-product, this package
gives some functionality to compute certain module series for modules of
solvable groups.  For example, if G is a rational polycyclic matrix
group, then we can compute the radical series of the natural Q[G]-module
Q^d.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polenta documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-alnuth-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g exam lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
# POLENTA.tst and POLENTA2.tst require more memory than some koji builders have
# available, so we disable them.  The maintainer should run them on a machine
# with a minimum of 16 GB of RAM prior to updating to a new version.
sed -i 's/"POLENTA\.tst"/#&/;/POLENTA2/s/Add/;#&/' tst/testall.g

gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc CHANGES README.md TODO
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/exam/
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
