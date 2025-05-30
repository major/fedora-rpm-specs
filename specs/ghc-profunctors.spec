# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name profunctors
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

Name:           ghc-%{pkg_name}
Version:        5.6.2
Release:        %autorelease
Summary:        Profunctors

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/profunctors
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-transformers-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-distributive-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-transformers-prof
%endif
# End cabal-rpm deps

%description
Profunctor represents a profunctor from Hask -> Hask. Intuitively it is a
bifunctor where the first argument is contravariant and the second argument is
covariant.


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


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
