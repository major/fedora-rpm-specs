%global pkgname factint
%global upname  FactInt
%global giturl  https://github.com/gap-packages/FactInt

Name:           gap-pkg-%{pkgname}
Version:        1.6.3
Release:        %autorelease
Summary:        Advanced methods for factoring integers

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/FactInt/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
FactInt provides implementations of the following methods for factoring
integers:
- Pollard's p-1
- Williams' p+1
- Elliptic Curves Method (ECM)
- Continued Fraction Algorithm (CFRAC)
- Multiple Polynomial Quadratic Sieve (MPQS)
FactInt also makes use of Richard P. Brent's tables of known factors of
integers of the form bk+/-1 for "small" b.

The ECM method is suited best for finding factors which are neither too
small (i.e. have less than about 12 decimal digits) nor too close to the
square root of the number to be factored.  The MPQS method is designed
for factoring products of two primes of comparable orders of magnitude.
CFRAC is the historical predecessor of the MPQS method.  Pollard's p-1
and Williams' p+1 are useful for finding factors p such that all prime
factors of p-1 (respectively p+1) are "small", e.g. smaller than 1000000.
All factoring methods implemented in this package are probabilistic.  In
particular the time needed by the ECM method depends largely on luck.

FactInt provides a general-purpose factorization routine which uses an
appropriate combination of the methods mentioned above, the Pollard Rho
routine which is implemented in the GAP Library and a variety of tricks
for special cases to obtain a good average performance for "arbitrary"
integers.  At the user's option, FactInt provides detailed information
about the progress of the factorization process.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        FactInt documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g lib tables tst %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{upname}/
%{gap_libdir}/pkg/%{upname}/*.g
%{gap_libdir}/pkg/%{upname}/lib/
%{gap_libdir}/pkg/%{upname}/tables/
%{gap_libdir}/pkg/%{upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
