%global gap_pkgname fplsa
%global gap_upname  FPLSA
%global giturl      https://github.com/gap-packages/FPLSA

Name:           gap-pkg-%{gap_pkgname}
Version:        1.2.7
Release:        %autorelease
Summary:        Finitely presented Lie algebras

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/FPLSA/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
# Fedora-only patch: look for the ini file in multiple places, in this order:
# - $HOME/.config/gap
# - /etc
# - $PWD/src
Patch:          %{name}-ini.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc

Requires:       gap-core%{?_isa}

%description
When K is a finitely-presented Lie algebra, the GAP operation
IsomorphismSCTableAlgebra can be used to make the structure of K explicit, in
the form of an isomorphic algebra given by structure constants, which is much
more amenable to further computations.

This GAP package installs an alternative method for this operation, which
calls an external C program (fplsa version 4.0) to do the hard part of the
computation.  This speeds up the calculation and permits larger problems to be
attempted.  The external program has much additional functionality which is
not used by the present version of the package.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only
Summary:        FPLSA documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%build -p
# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure --with-gaproot=%{gap_archdir}
%make_build

%install -a
# Install the .ini file
mkdir -p %{buildroot}%{_sysconfdir}
cp -p src/fplsa4.ini %{buildroot}%{_sysconfdir}

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/lib/
%{gap_archdir}/pkg/%{gap_upname}/tst/
%config(noreplace) %{_sysconfdir}/fplsa4.ini

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
