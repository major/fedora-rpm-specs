%global gap_pkgname resclasses
%global giturl      https://github.com/gap-packages/resclasses

Name:           gap-pkg-%{gap_pkgname}
Version:        4.7.4
Release:        %autorelease
Summary:        Set-theoretic computations with Residue Classes

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/resclasses/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-utils

Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-utils

Recommends:     gap-pkg-io

%description
ResClasses is a GAP package for set-theoretic computations with residue
classes of the integers and a couple of other rings.  The class of sets which
ResClasses can deal with includes the open and the closed sets in the topology
on the respective ring which is induced by taking the set of all residue
classes as a basis, as far as the usual restrictions imposed by the finiteness
of computing resources permit this.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        ResClasses documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc CHANGES README
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
