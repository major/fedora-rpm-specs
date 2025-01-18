Name:           ahven
Version:        2.8
Release:        13%{?dist}
Summary:        A unit testing framework for Ada 95
Summary(sv):    Ett enhetstestramverk för ada 95

License:        ISC
URL:            https://www.ahven-framework.com/
Source:         https://www.ahven-framework.com/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc-gnat make fedora-gnat-project-common
BuildRequires:  gprbuild
BuildRequires:  python3-sphinx
# Build only on architectures where gcc-gnat is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Ahven is a simple unit testing library (or a framework) for the Ada \
programming language. It is loosely modeled after Junit and some ideas are \
taken from Aunit.

%global common_description_sv \
Ahven är ett enkelt bibliotek (eller ramverk) för enhetstestning i \
programmeringsspråket ada. Det efterliknar Junit i stora drag, och några idéer \
är hämtade från Aunit.

%description %{common_description_en}

Features:
· Simple API
· Small size
· Junit-compatible test results in XML format, which allows integration with
  tools like Jenkins or Teamcity
· Strict coding style (enforced by Adacontrol)
· Plain Ada 95 code, no Ada 2005 features used, but can be compiled as Ada 2005
  or Ada 2012 code if needed
· Portable across different compilers and operating systems
· Permissive Open Source license (ISC)

%description -l sv %{common_description_sv}

Fördelar:
· Enkelt programmeringsgränssnitt
· Liten kodstorlek
· Junit-kompatibla testresultat i XML-form, vilket möjliggör samverkan med
  sådana verktyg som Jenkins eller Teamcity
· Stränga kodformateringsregler (upprätthållna av Adacontrol)
· Renodlad ada 95-kod som inte använder några ada 2005-finesser men kan
  kompileras som ada 2005 eller ada 2012 vid behov
· Portabelt mellan olika kompilatorer och operativsystem
· Medgörlig, fri licens (ISC)


%package devel
Summary:        Development files for Ahven
Summary(sv):    Filer för programmering med Ahven
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use Ahven.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder Ahven.


%prep
%setup -q


%build
%{Comfignat_make} all GNAT_BUILDER=gprbuild OS_VERSION=unix


%install
%{make_install}

# These files aren't needed in the package.
rm %{buildroot}%{_pkgdocdir}/html/{.buildinfo,objects.inv}

# Include these documentation files.
cp --preserve=timestamps README.md ROADMAP NEWS.txt %{buildroot}%{_pkgdocdir}


%check
%global GNAT_add_rpath x
# Disable the hardening hack only for the testsuite.
# https://bugzilla.redhat.com/show_bug.cgi?id=1197501
%undefine _hardened_build

# Append -shared to override ahven_tests.gpr's -static.
# https://bugzilla.redhat.com/show_bug.cgi?id=2225696
export GNATBINDFLAGS=-shared

%{Comfignat_make} check GNAT_BUILDER=gprbuild OS_VERSION=unix


%files
%{_libdir}/*.so.*
%license LICENSE.txt

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{name}
%{_GNAT_project_dir}/*
%{_pkgdocdir}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2.8-12
- Rebuilt with GCC 15 prerelease.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2.8-8
- Rebuilt with GCC 14 prerelease.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2.8-5
- Rebuilt with GCC 13.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2.8-1
- Upgraded to 2.8.

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2.7-10
- rebuilt with gcc-11.0.1-0.3

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Björn Persson <Bjorn@Rombobjörn.se> - 2.7-8
- Rebuilt with GCC 11.

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2.7-3
- Built for x86.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Björn Persson <Bjorn@Rombobjörn.se> - 2.7-1
- Upgraded to 2.7.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Björn Persson <Bjorn@Rombobjörn.se> - 2.6-10
- Switched to building with GPRbuild as project file support was removed from
  Gnatmake in GCC 8.

* Tue Nov 14 2017 Björn Persson <Bjorn@Rombobjörn.se> - 2.6-9
- Switched to running Sphinx in Python 3.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Björn Persson <Bjorn@Rombobjörn.se> - 2.6-7
- Changed unversioned "python-" prefixes to "python2-".

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Björn Persson <Bjorn@Rombobjörn.se> - 2.6-4
- Rebuilt with GCC 7 prerelease.

* Fri Aug 12 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2.6-3
- Rebuilt to let it be built on new architectures.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2.6-2
- Rebuilt with GCC 6 prerelease.

* Sat Dec 26 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2.6-1
- Upgraded to 2.6.
- Updated the URLs to point to Ahven's new website.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 02 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2.4-4
- Don't build on ppc64le.

* Wed Apr 01 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2.4-3
- Removed two files that Sphinx generates, that aren't needed in the package.

* Sun Mar 29 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2.4-2
- Tagged the license file as such.
- Fixed to build in current Rawhide.

* Wed Feb 12 2014 Björn Persson <Bjorn@Rombobjörn.se> - 2.4-1
- Ready to be submitted for review.
