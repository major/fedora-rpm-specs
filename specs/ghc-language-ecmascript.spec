# generated by cabal-rpm-2.3.0 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name language-ecmascript
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# testsuite missing deps: test-framework test-framework-hunit test-framework-quickcheck2 testing-feat

Name:           ghc-%{pkg_name}
Version:        0.19.1.0
Release:        %autorelease -b 8
Summary:        JavaScript parser and pretty-printer library

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/language-ecmascript
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
# generated from a1e47e6
Patch0:         language-ecmascript-ghc9.6.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-charset-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-uniplate-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-ansi-wl-pprint-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-charset-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-uniplate-prof
%endif
# End cabal-rpm deps

%description
Tools for working with ECMAScript 3 (popularly known as JavaScript).
Includes a parser, pretty-printer, tools for working with source tree
annotations and an arbitrary instance.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library
documentation.
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
%autopatch -p1
# End cabal-rpm setup
cabal-tweak-dep-ver ansi-wl-pprint '< 1' '< 2'
cabal-tweak-dep-ver base '< 4.19' '< 4.20'
cabal-tweak-dep-ver Diff '0.4.*' '0.5.*'


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
%doc CHANGELOG


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
