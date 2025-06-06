# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name pretty-show
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond system_jquery 0

Name:           ghc-%{pkg_name}
Version:        1.10
Release:        %autorelease
Summary:        Tools for working with derived Show instances and generic inspection of values

License:        MIT
URL:            https://hackage.haskell.org/package/pretty-show
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-haskell-lexer-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-text-devel
%if %{with ghc_prof}
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-haskell-lexer-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-text-prof
%endif
BuildRequires:  happy
# End cabal-rpm deps
%if %{with system_jquery}
Requires:       js-jquery
# Make symlinks valid.
BuildRequires:  web-assets-devel
%else
Provides:       bundled(jquery) = 3.3.1
%endif

%description
We provide a library and an executable for working with derived 'Show'
instances. By using the library, we can parse derived 'Show' instances into a
generic data structure. The 'ppsh' tool uses the library to produce
human-readable versions of 'Show' instances, which can be quite handy for
debugging Haskell programs. We can also render complex generic values into an
interactive Html page, for easier examination.


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

%if %{with system_jquery}
%global _style_dir %{buildroot}%{_datadir}/%{pkgver}/style
# Replace shipped jQuery with system version.
rm -v %{_style_dir}/jquery.js
ln -s %{_webassetdir}/jquery/1/jquery.min.js %{_style_dir}/jquery.js
%endif


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
%{_datadir}/%{pkgver}
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG
%{_bindir}/ppsh


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
