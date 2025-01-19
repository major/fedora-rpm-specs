%define inchi_so_ver 1.06.00
%define url_ver 106

Summary: The IUPAC International Chemical Identifier library
Name: inchi
Version: 1.0.6
Release: 12%{?dist}
URL: https://www.inchi-trust.org/about-the-inchi-standard/
Source0: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-SRC.zip
Source1: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-DOC.zip
Source2: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-TEST.zip
Patch0: %{name}-rpm.patch
# reported upstream:
# https://sourceforge.net/p/inchi/bugs/77/
Patch1: %{name}-1.0.6-0001-MolfileReadCountsLine-fix-storing-n_atoms-n_bonds-me.patch
License: LicenseRef-IUPAC-InChI-Trust
BuildRequires: dos2unix
BuildRequires: gcc
BuildRequires: make

%description
The IUPAC International Chemical Identifier (InChITM) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

This package contains the command line conversion utility.

%package libs
Summary: The IUPAC International Chemical Identifier library

%description libs
The IUPAC International Chemical Identifier (InChITM) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

%package devel
Summary: Development headers for the InChI library
Requires: %{name}-libs%{_isa} = %{version}-%{release}

%description devel
The inchi-devel package includes the header files and libraries
necessary for developing programs using the InChI library.

If you are going to develop programs which will use this library
you should install inchi-devel.  You'll also need to have the
inchi package installed.

%package doc
Summary: Documentation for the InChI library
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The inchi-doc package contains user documentation for the InChI software
and InChI library API reference for developers.

%prep
%setup -q -n INCHI-1-SRC -a 1 -a 2
%patch -P0 -p1 -b .r
%patch -P1 -p1 -b .big_endian
for file in readme.txt ; do
  dos2unix -k $file
done
pushd INCHI-1-TEST/test
unzip -d reference -qq -a test-results.zip
unzip -qq -a test-datasets.zip
dos2unix -k reference/*.inc *.sdf
for f in inchify_{InChI_TestSet,zzp} ; do
    sed -e 's,REM,#,g' -e 's,/,-,g' -e 's,NUL,/dev/null,g' -e 's,inchi-1.exe,../../INCHI_EXE/bin/Linux/inchi-1,g' ${f}.cmd >${f}.sh
    dos2unix ${f}.sh
done
popd

%build
pushd INCHI_API/demos/inchi_main/gcc
%make_build SHARED_LINK_PARM="%{optflags}" OPTFLAGS="%{optflags} -Wno-comment -Wno-parentheses -Wno-unused -Wno-unused-but-set-variable"
popd
pushd INCHI_EXE/inchi-1/gcc
%make_build LINKER_OPTIONS="%{optflags}" OPTFLAGS="%{optflags} -Wno-comment -Wno-parentheses -Wno-unused -Wno-unused-but-set-variable"
popd

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/inchi}
install -pm 755 INCHI_EXE/bin/Linux/inchi-1 %{buildroot}%{_bindir}/
install -p INCHI_API/bin/Linux/libinchi.so.%{inchi_so_ver} $RPM_BUILD_ROOT%{_libdir}
ln -s libinchi.so.%{inchi_so_ver} $RPM_BUILD_ROOT%{_libdir}/libinchi.so.1
ln -s libinchi.so.1               $RPM_BUILD_ROOT%{_libdir}/libinchi.so
install -pm644 INCHI_BASE/src/{ichisize,inchi_api,ixa}.h $RPM_BUILD_ROOT%{_includedir}/inchi

%check
export LD_LIBRARY_PATH=$(pwd)/INCHI_API/bin/Linux/
pushd INCHI-1-TEST/test
for f in inchify_{InChI_TestSet,zzp} ; do
    sh ./${f}.sh
done
for t in its-*.inc zzp-*.inc ; do diff -u reference/$t $t ; done
popd

%files
%{_bindir}/inchi-1

%files libs
%license LICENCE.pdf
%doc readme.txt
%{_libdir}/libinchi.so.1*

%files devel
%{_includedir}/inchi
%{_libdir}/libinchi.so

%files doc
%doc INCHI-1-DOC/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.6-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-3
- Fix member read size mistake, especially on big endian (#1930943)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Dominik Mierzejewski <rpm@greysector.net> 1.0.6-1
- update to 1.0.6 (#1910095)
- allow tests to fail on s390x (#1930943)

* Thu Feb  4 2021 Jerry James <loganjerry@gmail.com> - 1.0.5-12
- Install ichisize.h (bz 1911393)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Dominik Mierzejewski <rpm@greysector.net> 1.0.5-6
- Add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Drop unnecessary scriptlets
- Drop ancient Obsoletes:
- Switch to HTTPS in URLs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Dominik Mierzejewski <rpm@greysector.net> 1.0.5-1
- update to 1.05 (final)
- drop obsolete patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 11 2016 Dominik Mierzejewski <rpm@greysector.net> 1.0.5-0.2
- fix some misc issues (patch by Burt Leland and Noel O'Boyle)
- silence some harmless warnings to reduce gcc warning spam

* Fri Oct 07 2016 Dominik Mierzejewski <rpm@greysector.net> 1.0.5-0.1
- update to 1.05 (pre-release)
- update URLs
- include new IXA API header
- use license macro
- drop obsolete defattr

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Dominik Mierzejewski <rpm@greysector.net> 1.0.4-6
- update source URLs
- drop obsolete specfile parts
- enable testsuite
- build CLI tool and move libinchi to -libs subpackage
- fix undefined weak symbol warnings for libinchi

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Dominik Mierzejewski <rpm@greysector.net> 1.0.4-1
- update to 1.04
- update homepage and source URLs
- use dos2unix for EOL conversion

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 07 2010 Dominik Mierzejewski <rpm@greysector.net> 1.0.3-1
- updated to 1.03 (ABI break)
- rebased patch

* Thu Oct 08 2009 Dominik Mierzejewski <rpm@greysector.net> 1.0.2-2
- added doc subpackage (based on a patch by Takanori MATSUURA)

* Wed Aug 26 2009 Dominik Mierzejewski <rpm@greysector.net> 1.0.2-1
- updated to final 1.02 release (unfortunately, it breaks ABI)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2-0.3
- Autorebuild for GCC 4.3

* Mon Oct 01 2007 Dominik Mierzejewski <rpm@greysector.net> 1.0.2-0.2
- updated license tag
- fixed non-Unix EOLs in docs
- fixed dangling symlinks

* Thu Sep 06 2007 Dominik Mierzejewski <rpm@greysector.net> 1.0.2-0.1
- updated to 1.02b
- dropped WDI patch (upstream'd)
- updated license tag

* Sun Jul 01 2007 Dominik Mierzejewski <rpm@greysector.net> 1.0.1-8
- initial build
