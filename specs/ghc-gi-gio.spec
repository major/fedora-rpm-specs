# generated by cabal-rpm-2.2.1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name gi-gio
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

Name:           ghc-%{pkg_name}
Version:        2.0.34
Release:        %autorelease
Summary:        Gio bindings

License:        LGPL-2.1-or-later
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-gi-glib-devel
BuildRequires:  ghc-gi-gobject-devel
BuildRequires:  ghc-haskell-gi-devel
BuildRequires:  ghc-haskell-gi-base-devel
BuildRequires:  ghc-haskell-gi-overloading-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-gi-glib-prof
BuildRequires:  ghc-gi-gobject-prof
BuildRequires:  ghc-haskell-gi-prof
BuildRequires:  ghc-haskell-gi-base-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
%endif
BuildRequires:  pkgconfig(gio-2.0)
# End cabal-rpm deps

%description
Bindings for Gio, autogenerated by haskell-gi.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gio-2.0)
# End cabal-rpm deps

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
# Linking Setup ...
# /usr/lib64/libHSgi-gobject-2.0.23-HoBseCvMOu36DMtXiJmMXL-ghc8.8.4.so: error: undefined reference to 'g_param_spec_uref'
# /usr/lib64/libHSgi-gobject-2.0.23-HoBseCvMOu36DMtXiJmMXL-ghc8.8.4.so: error: undefined reference to 'intern'
%define ghc_static_setup 1
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