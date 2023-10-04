# cabal2spec-0.25.2
# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name GLUT

%global common_summary Haskell %{pkg_name} library

%global common_description The Haskell %{pkg_name} library.\
This is a set of bindings to the C %{pkg_name} library.

# ghc-7.4.1 haddock breaks on GLUT
%global without_haddock 1

Name:           ghc-%{pkg_name}
# part of haskell-platform-2011.4.0.0
Version:        2.1.2.1
Release:        14%{?dist}
Summary:        %{common_summary}

Group:          System Environment/Libraries
License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
ExclusiveArch:  %{ghc_arches}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros %{!?without_hscolour:hscolour}
# END cabal2spec
BuildRequires:  ghc-OpenGL-prof
BuildRequires:  freeglut-devel%{?_isa}
Patch1:         ghc-GLUT-extralibs.patch

%description
%{common_description}


%prep
%setup -q -n %{pkg_name}-%{version}
%patch1 -p1 -b .orig


%build
%ghc_lib_build


%install
%ghc_lib_install


%ghc_devel_package
Requires:  freeglut-devel%{?_isa}

%ghc_devel_description


%ghc_devel_post_postun


%ghc_files LICENSE


%changelog
* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 2.1.2.1-14
- disable haddock for now for ghc-7.4.1

* Fri Jan  6 2012 Jens Petersen <petersen@redhat.com> - 2.1.2.1-13
- update to cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.1.2.1-12.3
- rebuild with new gmp without compat lib

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.1.2.1-12.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 2.1.2.1-12.1
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 2.1.2.1-12
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 2.1.2.1-11
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Fri May 27 2011 Jens Petersen <petersen@redhat.com> - 2.1.2.1-10
- update to cabal2spec-0.23: add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.1.2.1-9
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Jens Petersen <petersen@redhat.com> - 2.1.2.1-7
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 2.1.2.1-6
- drop -o obsolete

* Sat Jul 31 2010 Jens Petersen <petersen@redhat.com> - 2.1.2.1-5
- part of haskell-platform-2010.2.0.0
- ghc-rpm-macros-0.8.1 for doc obsoletes
- add hscolour

* Sun Jun 27 2010 Jens Petersen <petersen@redhat.com> - 2.1.2.1-4
- sync cabal2spec-0.22.1

* Thu Jun 10 2010 Jens Petersen <petersen@redhat.com> - 2.1.2.1-3
- add extralibs glut in .cabal file to fix ghci linking
  (reported by Ian Collier, #601640)

* Tue Apr 27 2010 Jens Petersen <petersen@redhat.com> - 2.1.2.1-2
- part of haskell-platform-2010.1.0.0
- rebuild against ghc-6.12.2
- condition ghc_lib_package

* Mon Jan 11 2010 Jens Petersen <petersen@redhat.com> - 2.1.2.1-1
- update to 2.1.2.1 (haskell-platform-2009.3.1)
- update to ghc-rpm-macros-0.5.1 and cabal2spec-0.21.1:
- drop doc and prof bcond
- use ghc_lib_package, ghc_pkg_deps, and ghc_pkg_c_deps

* Sat Dec 26 2009 Jens Petersen <petersen@redhat.com> - 2.1.1.2-3
- update for ghc-6.12.1: add shared library support
- use new ghc*_requires macros: needs ghc-rpm-macros 0.4.0
- add common_summary and common_description

* Mon Aug 31 2009 Jens Petersen <petersen@redhat.com> - 2.1.1.2-2
- move BRs to source (base) package

* Wed Aug 12 2009 Bryan O'Sullivan <bos@serpentine.com> - 2.1.1.2-1
- initial packaging for Fedora created by cabal2spec
