%global pkgname float

Name:           gap-pkg-%{pkgname}
Version:        1.0.4
Release:        %autorelease
Summary:        GAP access to mpfr, mpfi, mpc, fplll and cxsc

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/float/
VCS:            https://github.com/gap-packages/float
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Remove atexit hack, not needed for non-coverage builds
Patch0:         %{name}-atexit.patch
# Remove use of deprecated set_unexpected
Patch1:         %{name}-unexpected.patch

BuildRequires:  cxsc-devel
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gcc-c++
BuildRequires:  libmpc-devel
BuildRequires:  make
BuildRequires:  mpfi-devel
BuildRequires:  pkgconfig(fplll)
BuildRequires:  pkgconfig(mpfr)

Requires:       gap-core%{?_isa}

%description
This package implements floating-point numbers within GAP, with
arbitrary precision, based on the C libraries FPLLL, MPFR, MPFI, MPC
and CXSC.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        FLOAT documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p0

# Do not override Fedora build flags
sed -i 's/-O3 -fomit-frame-pointer//;s/-O3/-O2/' configure

%build
export LC_ALL=C.UTF-8
export CPPFLAGS="-I %{_includedir}/cxsc"
%configure --with-gaproot=%{gap_archdir}
%make_build

# Build the documentation
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

%install
%make_install

# Install the GAP files; we install test files for use by GAP's internal test
# suite runner.
cp -a *.g lib tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
rm -f %{buildroot}%{gap_archdir}/pkg/%{pkgname}/{lib,tst}/Makefile*

# Install the documentation
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc README.md THANKS
%license COPYING
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
