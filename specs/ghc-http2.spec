# generated by cabal-rpm-2.2.1 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name http2
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%global networkcontrol network-control-0.0.2

%global subpkgs %{networkcontrol}

# testsuite missing deps: network-run

Name:           ghc-%{pkg_name}
Version:        5.0.1
Release:        1%{?dist}
Summary:        HTTP/2 library

License:        BSD-3-Clause
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{networkcontrol}/%{networkcontrol}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-byte-order-devel
#BuildRequires:  ghc-network-control-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-time-manager-devel
BuildRequires:  ghc-unix-time-devel
BuildRequires:  ghc-unliftio-devel
%if %{with ghc_prof}
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-byte-order-prof
#BuildRequires:  ghc-network-control-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-time-manager-prof
BuildRequires:  ghc-unix-time-prof
BuildRequires:  ghc-unliftio-prof
%endif
# for missing dep 'network-control':
BuildRequires:  ghc-psqueues-devel
%if %{with ghc_prof}
BuildRequires:  ghc-psqueues-prof
%endif
# End cabal-rpm deps

%description
HTTP/2 library including frames, priority queues, HPACK, client and server.


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


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{networkcontrol}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog