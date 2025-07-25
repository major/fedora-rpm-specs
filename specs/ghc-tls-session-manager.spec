# generated by cabal-rpm-2.3.0 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name tls-session-manager
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%global cryptotoken crypto-token-0.1.2

%global subpkgs %{cryptotoken}

Name:           ghc-%{pkg_name}
Version:        0.0.7
# can only be reset when subpkg bumped
Release:        2%{?dist}
Summary:        In-memory TLS session DB and session ticket

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/tls-session-manager
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{cryptotoken}/%{cryptotoken}.tar.gz
Source2:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-auto-update-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-basement-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-clock-devel
#BuildRequires:  ghc-crypto-token-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-psqueues-devel
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-tls-devel
%if %{with ghc_prof}
BuildRequires:  ghc-auto-update-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-basement-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-clock-prof
#BuildRequires:  ghc-crypto-token-prof
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-psqueues-prof
BuildRequires:  ghc-serialise-prof
BuildRequires:  ghc-tls-prof
%endif
# for missing dep 'crypto-token':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-network-byte-order-devel
%if %{with ghc_prof}
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-network-byte-order-prof
%endif
# End cabal-rpm deps

%description
TLS session manager with limitation, automatic pruning, energy saving and
replay resistance and session ticket manager.


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
This package provides the Haskell %{pkg_name} library
documentation.
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
%ghc_lib_subpackage -l BSD-3-Clause %{cryptotoken}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
dos2unix -k -n %{SOURCE2} %{pkg_name}.cabal
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
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Mar 25 2025 Jens Petersen <petersen@redhat.com> - 0.0.7-1
- https://hackage.haskell.org/package/tls-session-manager-0.0.7/changelog
- add crypto-token

* Sun Feb 23 2025 Jens Petersen <petersen@redhat.com> - 0.0.4-24
- cabal-rpm-2.3.0

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Jens Petersen <petersen@redhat.com> - 0.0.4-22
- revise .cabal file

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Jens Petersen <petersen@redhat.com> - 0.0.4-20
- refresh to cabal-rpm-2.2.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 29 2023 Jens Petersen <petersen@redhat.com> - 0.0.4-17
- bump release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 Jens Petersen <petersen@redhat.com> - 0.0.4-11
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Jens Petersen <petersen@redhat.com> - 0.0.4-9
- rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jens Petersen <petersen@redhat.com> - 0.0.4-7
- rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.0.4-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.0.4-1
- update to 0.0.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.0.2.1-1
- update to 0.0.2.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.0.0.2-6
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.0.0.2-4
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.0.0.2-1
- update to 0.0.0.2

* Wed Nov 15 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.0.1-1
- Update to latest version.

* Sat Jul 22 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.0.0.0-1
- spec file generated by cabal-rpm-0.11
