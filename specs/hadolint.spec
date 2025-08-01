# generated by cabal-rpm-2.3.0 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name hadolint
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%global commutativesemigroups commutative-semigroups-0.1.1.0
%global monoidsubclasses monoid-subclasses-1.2.5.1
%global primes primes-0.2.1.0
%global timerep timerep-2.1.0.0

%global subpkgs %{commutativesemigroups} %{primes} %{monoidsubclasses} %{timerep}

# monoid-subclasses needs quickcheck-instances
%bcond tests 0

Name:           %{pkg_name}
Version:        2.12.0
# can only be reset when all subpkgs bumped
Release:        20%{?dist}
Summary:        Dockerfile linter, validate inline bash

License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/hadolint
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{commutativesemigroups}/%{commutativesemigroups}.tar.gz
Source2:        https://hackage.haskell.org/package/%{monoidsubclasses}/%{monoidsubclasses}.tar.gz
Source3:        https://hackage.haskell.org/package/%{primes}/%{primes}.tar.gz
Source4:        https://hackage.haskell.org/package/%{timerep}/%{timerep}.tar.gz
# End cabal-rpm sources
# https://github.com/hadolint/hadolint/pull/902
Patch0:         902.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HsYAML-devel
BuildRequires:  ghc-ShellCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-colourista-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-email-validate-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-gitrev-devel
BuildRequires:  ghc-ilist-devel
BuildRequires:  ghc-language-docker-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-semver-devel
BuildRequires:  ghc-spdx-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
#BuildRequires:  ghc-timerep-devel
BuildRequires:  ghc-void-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-HsYAML-prof
BuildRequires:  ghc-ShellCheck-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-colourista-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptonite-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-email-validate-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-foldl-prof
BuildRequires:  ghc-gitrev-prof
BuildRequires:  ghc-ilist-prof
BuildRequires:  ghc-language-docker-prof
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-parallel-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-semver-prof
BuildRequires:  ghc-spdx-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
#BuildRequires:  ghc-timerep-prof
BuildRequires:  ghc-void-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-silently-devel
%endif
BuildRequires:  help2man
# for missing dep 'monoid-subclasses':
BuildRequires:  ghc-vector-devel
%if %{with ghc_prof}
BuildRequires:  ghc-vector-prof
%endif
# for missing dep 'timerep':
BuildRequires:  ghc-attoparsec-devel
%if %{with ghc_prof}
BuildRequires:  ghc-attoparsec-prof
%endif
# End cabal-rpm deps

%description
A smarter Dockerfile linter that helps you build best practice Docker images.

The linter parses the Dockerfile into an AST and performs check rules
on the AST. It uses ShellCheck to lint the Bash code inside
RUN instructions.


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif


%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)

%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{commutativesemigroups}
%ghc_lib_subpackage -l BSD-3-Clause %{monoidsubclasses}
%ghc_lib_subpackage -l BSD-3-Clause %{primes}
%ghc_lib_subpackage -l BSD-3-Clause %{timerep}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -a1 -a2 -a3 -a4
# End cabal-rpm setup
%autopatch -p1
cabal-tweak-flag static False
cabal-tweak-dep-ver deepseq '<1.5' '<1.6'
cabal-tweak-dep-ver language-docker '<13' '<14'


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_lib_install

set noclobber
mkdir -p %{buildroot}%{bash_completions_dir}
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{bash_completions_dir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1/
help2man --no-info %{buildroot}%{_bindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1
# End cabal-rpm install


%check
%if %{with tests}
PATH=%{buildroot}%{_bindir}:$PATH
%cabal_test
%endif


%files
# Begin cabal-rpm files:
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{bash_completions_dir}/%{name}
%{_mandir}/man1/%{name}.1*
# End cabal-rpm files


%files -n ghc-%{name} -f ghc-%{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc README.md


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Mar 30 2025 Jens Petersen <petersen@redhat.com> - 2.12.0-19
- Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 31 2024 Jens Petersen <petersen@redhat.com> - 2.12.0-17
- commutative-semigroups-0.1.1.0
- monoid-subclasses-1.2.5.1
- patch for language-docker 0.12

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 17 2024 Jens Petersen <petersen@redhat.com> - 2.12.0-15
- rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug  6 2023 Jens Petersen <petersen@redhat.com> - 2.12.0-12
- monoid-subclasses-1.2.3 needs commutative-semigroups

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 22 2023 Jens Petersen <petersen@redhat.com> - 2.12.0-10
- https://hackage.haskell.org/package/hadolint-2.12.0/changelog
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Dec 29 2022 Jens Petersen <petersen@redhat.com> - 2.8.0-9
- rebuild

* Mon Dec 12 2022 Jens Petersen <petersen@redhat.com> - 2.8.0-8
- rebuild

* Mon Jul 25 2022 Jens Petersen <petersen@redhat.com> - 2.8.0-7
- spdx is packaged in Fedora

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Jens Petersen <petersen@redhat.com> - 2.8.0-1
- https://github.com/hadolint/hadolint/releases/tag/v2.8.0

* Mon Jun 13 2022 Jens Petersen <petersen@redhat.com> - 2.7.0-4
- monoid-subclasses-1.1.3
- spdx-1.0.0.3
- colourista and ilist were packaged

* Mon Feb  7 2022 Jens Petersen <petersen@redhat.com> - 2.7.0-3
- restore the bundled deps to fix FTI (#2031307, #2031315)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Thu Aug 05 2021 Jens Petersen <petersen@redhat.com> - 2.6.1-2
- update to 2.6.1
- monoid-subclasses-1.1.1

* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 2.6.0-1
- update to 2.6.0
- subpackage new deps: colourista, ilist, monoid-subclasses, primes, spdx, timerep

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 28 2021 Jens Petersen <petersen@redhat.com> - 1.18.2-3
- rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.18.2-1
- Update to 1.18.2

* Thu Sep 03 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.18.0-1
- Initial RPM release, from spec file generated by cabal-rpm-2.0.6
