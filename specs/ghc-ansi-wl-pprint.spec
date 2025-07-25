# generated by cabal-rpm-2.3.0 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name ansi-wl-pprint
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%global prettyprintercompatansiwlpprint prettyprinter-compat-ansi-wl-pprint-1.0.2

%global subpkgs %{prettyprintercompatansiwlpprint}

Name:           ghc-%{pkg_name}
Version:        1.0.2
Release:        5%{?dist}
Summary:        The Wadler/Leijen Pretty Printer for colored ANSI terminal output

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/ansi-wl-pprint
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{prettyprintercompatansiwlpprint}/%{prettyprintercompatansiwlpprint}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-base-devel
#BuildRequires:  ghc-prettyprinter-compat-ansi-wl-pprint-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
#BuildRequires:  ghc-prettyprinter-compat-ansi-wl-pprint-prof
%endif
# for missing dep 'prettyprinter-compat-ansi-wl-pprint':
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-text-devel
%if %{with ghc_prof}
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-prettyprinter-ansi-terminal-prof
BuildRequires:  ghc-text-prof
%endif
# End cabal-rpm deps

%description
This is a pretty printing library based on Wadler's paper ["A Prettier
Printer"](https://homepages.inf.ed.ac.uk/wadler/papers/prettier/prettier.pdf).
It has been enhanced with support for ANSI terminal colored output using the
[ansi-terminal](https://hackage.haskell.org/package/ansi-terminal) package.


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
%ghc_lib_subpackage -l BSD-2-Clause %{prettyprintercompatansiwlpprint}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup
sed -i 's/\r$//' README.md


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
%doc Changelog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Apr 07 2025 Jens Petersen <petersen@redhat.com> - 1.0.2-4
- Rebuild

* Sun Mar 30 2025 Jens Petersen <petersen@redhat.com> - 1.0.2-3
- Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jul 28 2024 Jens Petersen <petersen@redhat.com> - 1.0.2-1
- https://hackage.haskell.org/package/ansi-wl-pprint-1.0.2/changelog

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Jens Petersen <petersen@redhat.com> - 0.6.9-21
- refresh to cabal-rpm-2.2.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Jens Petersen <petersen@redhat.com> - 0.6.9-18
- revised .cabal file

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 Jens Petersen <petersen@redhat.com> - 0.6.9-10
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Jens Petersen <petersen@redhat.com> - 0.6.9-8
- rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jens Petersen <petersen@redhat.com> - 0.6.9-6
- rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 0.6.9-2
- refresh to cabal-rpm-2.0.6

* Sun Feb 09 2020 Jens Petersen <petersen@redhat.com> - 0.6.9-1
- update to 0.6.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Jens Petersen <petersen@redhat.com> - 0.6.8.2-5
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.6.8.2-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.6.8.2-1
- update to 0.6.8.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.6.8.1-1
- update to 0.6.8.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.6.7.3-3
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Jens Petersen <petersen@redhat.com> - 0.6.7.3-1
- update to 0.6.7.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Jens Petersen <petersen@redhat.com> - 0.6.7.1-5
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Jens Petersen <petersen@redhat.com> - 0.6.7.1-2
- drop the readme file also because it is in dos encoding (#1075569)

* Wed Mar 12 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.6.7.1
- spec file generated by cabal-rpm-0.8.10
