# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name skein
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        1.0.9.4
Release:        %autorelease
Summary:        Skein, a family of cryptographic hash functions.  Includes Skein-MAC as well

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/skein
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-tagged-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-crypto-api-prof
BuildRequires:  ghc-tagged-prof
%endif
%if %{with tests}
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
Skein (<http://www.skein-hash.info/>) is a family of fast secure cryptographic
hash functions designed by Niels Ferguson, Stefan Lucks, Bruce Schneier, Doug
Whiting, Mihir Bellare, Tadayoshi Kohno, Jon Callas and Jesse Walker.

This package uses bindings to the optimized C implementation of Skein.
We provide a high-level interface (see module "Crypto.Skein") to some of the
Skein use cases. We also provide a low-level interface (see module
"Crypto.Skein.Internal") should you need to use Skein in a different way.

Currently we have support for Skein as cryptographic hash function as Skein as
a message authentication code (Skein-MAC). For examples of how to use this
package, see "Crypto.Skein" module documentation.

This package includes Skein v1.3. Versions of this package before 1.0.0
implemented Skein v1.1.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%if %{with tests}
%cabal_test
%endif


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
