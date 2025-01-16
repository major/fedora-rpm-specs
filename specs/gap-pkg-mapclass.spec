%global pkgname mapclass
%global upname  MapClass
%global giturl  https://github.com/gap-packages/MapClass

Name:           gap-pkg-%{pkgname}
Version:        1.4.6
Release:        %autorelease
Summary:        Calculate mapping class group orbits for a finite group

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/MapClass/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex

Requires:       gap-core

%description
The MapClass package calculates the mapping class group orbits for a
given finite group.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        MapClass documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%build
# Build the documentation
mkdir -p ../pkg
ln -s ../%{upname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{upname}/
%{gap_libdir}/pkg/%{upname}/*.g
%{gap_libdir}/pkg/%{upname}/lib/
%{gap_libdir}/pkg/%{upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
