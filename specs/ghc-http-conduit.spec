# generated by cabal-rpm-2.2.1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name http-conduit
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# testsuite missing deps: wai-conduit

Name:           ghc-%{pkg_name}
Version:        2.3.8.3
Release:        %autorelease
Summary:        HTTP client package with conduit interface and HTTPS support

License:        BSD-3-Clause
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unliftio-core-devel
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-prof
%endif
# End cabal-rpm deps

%description
This package uses conduit for parsing the actual contents of the HTTP
connection. It also provides higher-level functions which allow you to avoid
directly dealing with streaming data. See
<http://www.yesodweb.com/book/http-conduit> for more information.

The 'Network.HTTP.Conduit.Browser' module has been moved to
<http://hackage.haskell.org/package/http-conduit-browser/>.


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
cabal-tweak-drop-dep attoparsec-aeson


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