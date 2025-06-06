# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name cborg-json
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        0.2.6.0
Release:        %autorelease
Summary:        A library for encoding JSON as CBOR

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/cborg-json
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-cborg-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
%endif
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif
# End cabal-rpm deps

%description
This package implements the bijection between JSON and CBOR defined in the CBOR
specification, RFC 7049.


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
%license LICENSE.txt
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE.txt
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
