# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hspec-core
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# testsuite missing deps: hspec-meta

Name:           ghc-%{pkg_name}
Version:        2.11.12
Release:        %autorelease
Summary:        A Testing Framework for Haskell

License:        MIT
URL:            https://hackage.haskell.org/package/hspec-core
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-haskell-lexer-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-quickcheck-io-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tf-random-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
%if %{with ghc_prof}
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-call-stack-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-haskell-lexer-prof
BuildRequires:  ghc-hspec-expectations-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-quickcheck-io-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tf-random-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
%endif
# End cabal-rpm deps

%description
This package exposes internal types and functions that can be used to extend
Hspec's functionality.


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
Obsoletes:      %{name}-devel-doc < %{version}-%{release}

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
