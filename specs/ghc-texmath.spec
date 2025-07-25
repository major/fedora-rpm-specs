# generated by cabal-rpm-2.3.0 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name texmath
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%global typstsymbols typst-symbols-0.1.7

%global subpkgs %{typstsymbols}

# testsuite missing deps: tasty-golden

Name:           ghc-%{pkg_name}
Version:        0.12.9
# can only be reset when subpkg bumped
Release:        4%{?dist}
Summary:        Conversion between math formats

License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/texmath
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{typstsymbols}/%{typstsymbols}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-text-devel
#BuildRequires:  ghc-typst-symbols-devel
BuildRequires:  ghc-xml-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-text-prof
#BuildRequires:  ghc-typst-symbols-prof
BuildRequires:  ghc-xml-prof
%endif
# End cabal-rpm deps

%description
The texmath library provides functions to read and write TeX math, presentation
MathML, and OMML (Office Math Markup Language, used in Microsoft Office).
Support is also included for converting math formats to Gnu eqn, typst, and
pandoc's native format (allowing conversion, via pandoc, to a variety of
different markup formats). The TeX reader supports basic LaTeX and AMS
extensions, and it can parse and apply LaTeX macros. (See
<https://johnmacfarlane.net/texmath here> for a live demo of bidirectional
conversion between LaTeX and MathML.)


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
%ghc_lib_subpackage -l MIT %{typstsymbols}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
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
%doc README.md changelog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Mar 25 2025 Jens Petersen <petersen@redhat.com> - 0.12.9-3
- https://hackage.haskell.org/package/texmath-0.12.9/changelog

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jul 28 2024 Jens Petersen <petersen@redhat.com> - 0.12.8.7-1
- https://hackage.haskell.org/package/texmath-0.12.8.7/changelog
- typst-symbols-0.1.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 27 2023 Jens Petersen <petersen@redhat.com> - 0.12.8.3-3
- https://hackage.haskell.org/package/texmath-0.12.8.3/changelog
- https://hackage.haskell.org/package/typst-symbols-0.1.4/changelog

* Wed Jul 26 2023 Jens Petersen <petersen@redhat.com> - 0.12.8-1
- https://hackage.haskell.org/package/texmath-0.12.8/changelog
- subpackage typst-symbols

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 22 2023 Jens Petersen <petersen@redhat.com> - 0.12.5.5-1
- https://hackage.haskell.org/package/texmath-0.12.5.5/changelog
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 07 2022 Jens Petersen <petersen@redhat.com> - 0.12.3.3-1
- https://hackage.haskell.org/package/texmath-0.12.3.3/changelog

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 0.12.3-1
- update to 0.12.3

* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 0.12.1-1
- update to 0.12.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 0.12.0.2-1
- update to 0.12.0.2

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 0.11.3-1
- update to 0.11.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 0.11.2.2-1
- update to 0.11.2.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.11.1.2-1
- update to 0.11.1.2

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.10.1.2-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 0.10.1.2-1
- update to 0.10.1.2

* Tue Jul 24 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-5
- Enable annotated build again

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-4
- Rebuilt for #1607054

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.10.1-1
- update to 0.10.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jens Petersen <petersen@redhat.com> - 0.9.1-1
- update to 0.9.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 27 2016 Jens Petersen <petersen@redhat.com> - 0.8.6.4-1
- update to 0.8.6.4

* Thu Jun 16 2016 Jens Petersen <petersen@redhat.com> - 0.8.4.2-2
- build with network-uri

* Sat Mar 05 2016 Jens Petersen <petersen@redhat.com> - 0.8.4.2-1
- update to 0.8.4.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0.1-4
- Rebuild (aarch64 vector hashes)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Jens Petersen <petersen@redhat.com> - 0.8.0.1-2
- run tests in utf8 on aarch64

* Sun Feb  1 2015 Jens Petersen <petersen@redhat.com> - 0.8.0.1-1
- update to 0.8.0.1
- disable tests on armv7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Jens Petersen <petersen@redhat.com> - 0.6.6.1-1
- update to 0.6.6.1

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 0.6.6-1
- update to 0.6.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.5-2
- update to new simplified Haskell Packaging Guidelines

* Wed Jun 05 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.5-1
- update to 0.6.1.5

* Sun Mar 10 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.3-1
- update to 0.6.1.3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Jens Petersen <petersen@redhat.com> - 0.6.1.1-1
- update to 0.6.1.1
- update summary and description

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.6-2
- change prof BRs to devel

* Wed Jun 13 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.6-1
- update to 0.6.0.6

* Fri Mar 23 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.3-2
- add license to ghc_files

* Sun Feb 12 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.3-1
- update to 0.6.0.3

* Tue Feb  7 2012 Jens Petersen <petersen@redhat.com> - 0.5.0.4-2
- rebuild

* Thu Jan  5 2012 Jens Petersen <petersen@redhat.com> - 0.5.0.4-1
- update to 0.5.0.4 and cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5.0.1-3.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5.0.1-3.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.5.0.1-3.1
- rebuild with new gmp

* Wed Jul 27 2011 Jens Petersen <petersen@redhat.com> - 0.5.0.1-3
- rebuild for xml-1.3.9

* Wed Jun 22 2011 Jens Petersen <petersen@redhat.com> - 0.5.0.1-2
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Sat May 28 2011 Jens Petersen <petersen@redhat.com> - 0.5.0.1-1
- update to 0.5.0.1
- update to cabal2spec-0.23: add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4-6
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 0.4-5
- rebuild for haskell-platform-2011.1 updates

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Jens Petersen <petersen@redhat.com> - 0.4-3
- update to cabal2spec-0.22.4

* Tue Dec 21 2010 Jens Petersen <petersen@redhat.com> - 0.4-2
- need depends on syb for ghc-7.0

* Fri Nov 12 2010 Jens Petersen <petersen@redhat.com> - 0.4-1
- GPLv2+
- add deps and description
- remove unused tests and cgi data files

* Fri Nov 12 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.4-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
