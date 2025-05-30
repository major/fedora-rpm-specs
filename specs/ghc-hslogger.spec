# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hslogger
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        1.3.1.2
Release:        %autorelease
Summary:        Versatile logging framework

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/hslogger
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-bsd-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-bsd-prof
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unix-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
%endif
# End cabal-rpm deps

%description
'hslogger' is a logging framework for Haskell, roughly similar to [Python's
logging module](https://docs.python.org/2/library/logging.html).

'hslogger' lets each log message have a priority and source be associated with
it. The programmer can then define global handlers that route or filter
messages based on the priority and source. 'hslogger' also has a
[Syslog](https://tools.ietf.org/html/rfc5424) handler built in.


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
%doc CHANGELOG.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
