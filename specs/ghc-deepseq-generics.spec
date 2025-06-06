# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name deepseq-generics
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# testsuite missing deps: test-framework test-framework-hunit

Name:           ghc-%{pkg_name}
Version:        0.2.0.0
Release:        %autorelease
Summary:        Generics-based normal form reduction for deepseq

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/deepseq-generics
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-deepseq-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-prof
%endif
# End cabal-rpm deps

%description
This package provides a "GHC.Generics"-based
'Control.DeepSeq.Generics.genericRnf' function which can be used for providing
a 'rnf' implementation. See the documentation for the 'genericRnf' function in
the "Control.DeepSeq.Generics" module to get started.

The original idea was pioneered in the 'generic-deepseq' package (see
<http://www.haskell.org/pipermail/haskell-cafe/2012-February/099551.html> for
more information).

This package differs from the 'generic-deepseq' package by working in
combination with the existing 'deepseq' package as opposed to defining a
conflicting drop-in replacement for 'deepseq's 'Control.Deepseq' module.

Note: The ability to auto-derive via "GHC.Generics" has been merged into
'deepseq-1.4.0.0'. This package is now still useful for writing code that's
also compatible with older 'deepseq' versions not yet providing
"GHC.Generics"-support.


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
cp -bp %{SOURCE1} %{pkg_name}.cabal
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
%doc changelog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
