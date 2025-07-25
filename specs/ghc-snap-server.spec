# generated by cabal-rpm-2.3.0 --stream hackage --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name snap-server
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%global iostreamshaproxy io-streams-haproxy-1.0.1.0

%global subpkgs %{iostreamshaproxy}

# testsuite missing deps: test-framework test-framework-hunit test-framework-quickcheck2

Name:           ghc-%{pkg_name}
Version:        1.1.2.1
# can only be reset when subpkg bumped
Release:        30%{?dist}
Summary:        A web server for the Snap Framework

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/snap-server
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{iostreamshaproxy}/%{iostreamshaproxy}.tar.gz
Source2:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-io-streams-devel
#BuildRequires:  ghc-io-streams-haproxy-devel
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-snap-core-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-vector-devel
%if %{with ghc_prof}
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-clock-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-io-streams-prof
#BuildRequires:  ghc-io-streams-haproxy-prof
BuildRequires:  ghc-lifted-base-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-snap-core-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-vector-prof
%endif
# End cabal-rpm deps

%description
Snap is a simple and fast web development framework and server written in
Haskell. For more information or to download the latest version, you can visit
the Snap project website at <http://snapframework.com/>.

The Snap HTTP server is a high performance web server library written in
Haskell. Together with the 'snap-core' library upon which it depends, it
provides a clean and efficient Haskell programming interface to the HTTP
protocol.


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
%ghc_lib_subpackage -l BSD-3-Clause %{iostreamshaproxy}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
dos2unix -k -n %{SOURCE2} %{pkg_name}.cabal
# End cabal-rpm setup
cabal-tweak-drop-dep bytestring-builder,

(
cd %{iostreamshaproxy}
cabal-tweak-dep-ver attoparsec '< 0.14' '< 0.15'
cabal-tweak-dep-ver base '< 4.13' '< 4.20'
cabal-tweak-dep-ver bytestring '< 0.11' '< 0.13'
cabal-tweak-dep-ver network '< 3.1' '< 3.3'
cabal-tweak-dep-ver transformers '< 0.6' '< 0.7'
)


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
%doc CONTRIBUTORS README.SNAP.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Mar 30 2025 Jens Petersen <petersen@redhat.com> - 1.1.2.1-29
- Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug  5 2024 Jens Petersen <petersen@redhat.com> - 1.1.2.1-27
- revise bounds

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Jens Petersen <petersen@redhat.com> - 1.1.2.1-23
- https://hackage.haskell.org/package/snap-server-1.1.2.1/changelog

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 17 2023 Jens Petersen <petersen@redhat.com> - 1.1.2.0-21
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Jens Petersen <petersen@redhat.com> - 1.1.2.0-19
- rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug  8 2021 Jens Petersen <petersen@redhat.com> - 1.1.2.0-17
- update to 1.1.2.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.2-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 1.1.1.2-12
- update to 1.1.1.2

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 1.1.1.1-11
- update to 1.1.1.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Jens Petersen <petersen@redhat.com> - 1.1.0.0-9
- update for ghc-8.6.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 1.1.0.0-7
- update to 1.1.0.0

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.0.3.3-6
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 1.0.3.3-4
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Jens Petersen <petersen@redhat.com> - 1.0.3.3-1
- update to 1.0.3.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Jens Petersen <petersen@redhat.com> - 1.0.1.1-1
- update to 1.0.1.1
- subpackage io-streams-haproxy

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Jens Petersen <petersen@redhat.com> - 0.9.5.1-1
- update to 0.9.5.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jens Petersen <petersen@redhat.com> - 0.9.4.6-1
- update to 0.9.4.6

* Mon Sep 01 2014 Jens Petersen <petersen@redhat.com> - 0.9.4.5-1
- update to 0.9.4.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Jens Petersen <petersen@redhat.com> - 0.9.3.4-3
- update to cblrpm-0.8.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Jens Petersen <petersen@redhat.com> - 0.9.3.4-1
- 0.9.3.4
- add static provides to devel

* Thu Jun 27 2013 Jens Petersen <petersen@redhat.com> - 0.9.3.3-1
- minor description tweaks and add CONTRIBUTORS

* Thu Jun 27 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.9.3.3-0
- spec file generated by cabal-rpm-0.8.2
