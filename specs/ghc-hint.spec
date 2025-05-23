# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hint
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# uses cabal
%bcond tests 0

Name:           ghc-%{pkg_name}
Version:        0.9.0.8
Release:        %autorelease
Summary:        A Haskell interpreter built on top of the GHC API

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/hint
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-boot-devel
BuildRequires:  ghc-ghc-paths-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-ghc-prof
BuildRequires:  ghc-ghc-boot-prof
BuildRequires:  ghc-ghc-paths-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-typed-process-devel
%endif
# End cabal-rpm deps

%description
This library defines an Interpreter monad. It allows to load Haskell modules,
browse them, type-check and evaluate strings with Haskell expressions and even
coerce them into values. The library is thread-safe and type-safe (even the
coercion of expressions to values). It is, essentially, a huge subset of the
GHC API wrapped in a simpler API.


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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
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
%doc AUTHORS CHANGELOG.md README.md examples


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
