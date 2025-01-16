%global pkgname nq
%global giturl  https://github.com/gap-packages/nq

Name:           gap-pkg-%{pkgname}
Version:        2.5.11
Release:        %autorelease
Summary:        Nilpotent Quotients of finitely presented groups

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/nq/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gmp)

Requires:       gap-core%{?_isa}
Requires:       gap-pkg-polycyclic

%description
This package provides access from within GAP to the ANU nilpotent
quotient program for computing nilpotent factor groups of finitely
presented groups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        NQ documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%conf
./autogen.sh

%build
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules
%make_build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin examples gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/gap/
%{gap_archdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/examples/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/examples/

%changelog
%autochangelog
