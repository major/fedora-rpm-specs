# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name warp-tls
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

Name:           ghc-%{pkg_name}
Version:        3.4.9
Release:        %autorelease
Summary:        HTTP over TLS support for Warp via the TLS package

License:        MIT
URL:            https://hackage.haskell.org/package/warp-tls
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-recv-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-tls-session-manager-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-warp-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-recv-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-tls-session-manager-prof
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-prof
%endif
# End cabal-rpm deps

%description
SSLv1 and SSLv2 are obsoleted by IETF. We should use TLS 1.2 (or TLS 1.1 or TLS
1.0 if necessary). HTTP/2 can be negotiated by ALPN. API docs and the README
are available at <http://www.stackage.org/package/warp-tls>.


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


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
