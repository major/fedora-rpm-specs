
%undefine __cmake_in_source_build

%{?!mono_arches: %global mono_arches %{ix86} x86_64 sparc sparcv9 ia64 %{arm} alpha s390x ppc ppc64}

%ifarch %{mono_arches}
# No linux system is actually using the csharp bindings
%global with_csharp 0
%endif
%global with_java 1
%if 0%{?fedora} >= 41
%ifarch %{ix86}
%global with_php 0
%else
%global with_php 1
%endif
%else
%global with_php 1
%endif
%global with_python 1

%if 0%{?with_php} > 0
%global ini_name     40-kolabformat.ini
%endif

# Filter out private python and php libs. Does not work on EPEL5,
# therefor we use it conditionally
%if 0%{?with_php} > 0
%if 0%{?with_python} > 0
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_provides_in %{php_extdir}/.*\.so$
%filter_setup
}
%else
%{?filter_setup:
%filter_provides_in %{php_extdir}/.*\.so$
%filter_setup
}
%endif
%else
%if 0%{?with_python} > 0
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}
%endif
%endif

Name:           libkolabxml
Version:        1.2.0
Release:        30%{?dist}
Summary:        Kolab XML format collection parser library

License:        LGPL-3.0-or-later
URL:            http://www.kolab.org

Source0:        https://cgit.kolab.org/libkolabxml/snapshot/libkolabxml-%{version}.tar.gz
Patch0:         libkolabxml-1.2.0-fix-for-swig4.patch

BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.6
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  swig
BuildRequires:  uuid-devel
BuildRequires:  xerces-c-devel
BuildRequires:  xsd

# libkolab FTBFS, so ...
# https://bugzilla.redhat.com/show_bug.cgi?id=1518800
%global libkolab_obsoletes 1.0.2-20
%if 0%{?libkolab_obsoletes:1}
Obsoletes: libkolab < %{libkolab_obsoletes}
Obsoletes: libkolab-devel < %{libkolab_obsoletes}
Obsoletes: python2-libkolab < %{libkolab_obsoletes}
%endif

%if 0%{?with_csharp} < 1
Obsoletes:      csharp-kolabformat < %{version}-%{release}
#Provides:       csharp-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_java} < 1
Obsoletes:      java-kolabformat < %{version}-%{release}
#Provides:       java-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_php} < 1
Obsoletes:      php-kolabformat < %{version}-%{release}
#Provides:       php-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_python} < 1
Obsoletes:      python-kolabformat < %{version}-%{release}
Obsoletes:      python2-kolabformat < %{version}-%{release}
%endif

%description
The libkolabxml parsing library interprets Kolab XML formats (xCal, xCard)
with bindings for Python, PHP and other languages. The language bindings
are available through sub-packages.

%package devel
Summary:        Kolab XML library development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       libcurl-devel
Requires:       xerces-c-devel
Requires:       cmake
%description devel
Development headers for the Kolab XML libraries.

%if 0%{?with_csharp} > 0
%package -n csharp-kolabformat
Summary:        C# Bindings for libkolabxml
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  mono-core
%description -n csharp-kolabformat
C# bindings for libkolabxml
%endif

%if 0%{?with_java} > 0
%package -n java-kolabformat
Summary:        Java Bindings for libkolabxml
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n java-kolabformat
Java bindings for libkolabxml
%endif

%if 0%{?with_php} > 0
%package -n php-kolabformat
Summary:        PHP bindings for libkolabxml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
BuildRequires:  php >= 5.3
BuildRequires:  php-devel >= 5.3
%description -n php-kolabformat
The PHP kolabformat package offers a comprehensible PHP library using the
bindings provided through libkolabxml.
%endif

%if 0%{?with_python} > 0
%package -n python3-kolabformat
Summary:        Python bindings for libkolabxml
Obsoletes:      python-kolabformat < 1.1.4
Provides:       python-kolabformat = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
%description -n python3-kolabformat
The PyKolab format package offers a comprehensive Python library using the
bindings provided through libkolabxml.
%endif


%prep
%autosetup -p1

sed -i "s/-php/-php7/g" src/php/CMakeLists.txt


%build
%cmake \
    -DBUILD_TESTS:BOOL=OFF \
%if 0%{?with_csharp} > 0
    -DCSHARP_BINDINGS=ON \
    -DCSHARP_INSTALL_DIR=%{_datadir}/%{name}/csharp/ \
%endif
%if 0%{?with_java} > 0
    -DJAVA_BINDINGS=ON \
    -DJAVA_INSTALL_DIR=%{_datadir}/%{name}/java/ \
%endif
%if 0%{?with_php} > 0
    -DPHP_BINDINGS=ON \
    -DPHP_INSTALL_DIR=%{php_extdir} \
%endif
%if 0%{?with_python} > 0
    -DPYTHON_BINDINGS=ON \
    -DPYTHON_INSTALL_DIR=%{python3_sitearch}
%endif

%cmake_build


%install
%cmake_install

%if 0%{?with_php} > 0
mkdir -p \
    %{buildroot}/%{_datadir}/php \
    %{buildroot}/%{php_inidir}/
cat > %{buildroot}/%{php_inidir}/%{ini_name} << EOF
extension=kolabformat.so
EOF
%endif


%check
pushd %{_vpath_builddir}
export LD_LIBRARY_PATH=$( pwd )/src/
%if 0%{?with_php} > 0
php -d enable_dl=On -dextension=src/php/kolabformat.so src/php/test.php ||:
%endif
%if 0%{?with_python} > 0
python3 src/python/test.py ||:
%endif
popd


%ldconfig_scriptlets

%files
%doc DEVELOPMENT NEWS README
%license COPYING*
%{_libdir}/libkolabxml.so.1*

%files devel
%{_includedir}/kolabxml/
%{_libdir}/libkolabxml.so
%{_libdir}/cmake/Libkolabxml/

%if 0%{?with_csharp} > 0
%files -n csharp-kolabformat
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/csharp
%endif

%if 0%{?with_java} > 0
%files -n java-kolabformat
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/java
%endif

%if 0%{?with_php} > 0
%files -n php-kolabformat
%{php_extdir}/kolabformat.so
%config(noreplace) %{php_inidir}/%{ini_name}
%endif

%if 0%{?with_python} > 0
%files -n python3-kolabformat
%{python3_sitearch}/kolabformat.py
%{python3_sitearch}/_kolabformat.so
%{python3_sitearch}/__pycache__/*
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Pete Walter <pwalter@fedoraproject.org> - 1.2.0-29
- Rebuild for xerces-c 3.3

* Fri Oct 18 2024 Pete Walter <pwalter@fedoraproject.org> - 1.2.0-28
- Rebuild for xerces-c 3.3

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.2.0-27
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-25
- convert license to SPDX

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.2.0-24
- Rebuilt for Python 3.13

* Tue Apr  9 2024 Remi Collet <remi@fedoraproject.org> - 8.0.1-14
- disable PHP extension on 32-bit
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-20
- Rebuilt for Boost 1.83

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.2.0-19
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.0-17
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-16
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.2.0-14
- add a patch for Swig 4.1 (bug 2137815)

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.2.0-13
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.0-11
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.2.0-10
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.2.0-8
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-7
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-5
- drop depredated qt4 dep
- -DBUILD_TESTS=OFF (tests require qt4)
- use %%autosetup

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-2
- Rebuilt for Boost 1.75

* Mon Sep 28 2020 Jeff Law <law@redhat.com> - 1.2.0-1
- Re-enable LTO

* Sat Aug 15 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.2.0-0
- Upgrade to libkolabxml 1.2.0

* Mon Aug 10 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.1.6-19
- Adjusted for new cmake macros (out of source builds)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 1.1.6-16
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-15
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-12
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 1.1.6-10
- Rebuilt for Boost 1.69

* Mon Jan 21 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.1.6-9
- enable PHP again, supporting PHP 7

* Mon Jan 21 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.1.6-8
- enable Python again, supporting Python 3

* Mon Jan 21 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.1.6-7
- Drop python2-kolabformat for mass Python 2 package removal

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.1.6-6
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1.6-4
- Obsoletes: libkolab < 1.0.2-20
- use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1.6-2
- rebuild (boost)

* Wed Nov 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.1.6-1
- 1.1.6

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 1.1.4-6
- Rebuilt for Boost 1.64

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.1.4-5
- Rebuild due to bug in RPM (RHBZ #1468476)

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 1.1.4-4
- Rebuilt for Boost 1.63

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.4-2
- -devel: Requires: libcurl-devel xerces-c-devel

* Tue Jun 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.4-1
- 1.1.4, disable php bindings (FTBFS)

* Wed May 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.3-8
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0.3-6
- Rebuilt for boost-1.60.

* Sun Sep 13 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-5
- Rebuild (boost)

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.3-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-1
- 1.0.3

* Wed Feb 25 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-9
- rebuild (gcc5)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.0.1-8
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Remi Collet <rcollet@redhat.com> - 1.0.1-6
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-4
- rebuild once more with feeling (boost)

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.0.1-3
- Rebuild for boost 1.55.0

* Mon Jan 13 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.1-2
- Require php-kolab for php-kolabformat, and void
  /etc/php.d/kolabformat.ini (#2667)

* Wed Oct 30 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.1-1
- New upstream release

* Mon Oct 14 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.0-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.8.4-2
- Rebuild for boost 1.54.0

* Fri Apr 12 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 0.8.3-2
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Tue Feb 26 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.8.3-1
- New upstream release with file format handling

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.8.1-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.8.1-3
- Rebuild for Boost-1.53.0

* Wed Aug 22 2012 Dan Horák <dan[at]danny.cz> - 0.8.1-2
- build csharp subpackage only when Mono exists

* Wed Aug 15 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.8.1-1
- New upstream version 0.8.1
- Revert s/qt-devel/qt4-devel/ - just require the latest qt-devel
- Revert s/kdelibs-devel/kdelibs4-devel/ - also require the latest
  kdelibs (frameworks FTW!)

* Sun Aug 12 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.7.0-3
- drop BR: gcc-c++
- s/qt-devel/qt4-devel/ s/kdelibs-devel/kdelibs4-devel/
- fix build against boost-1.50

* Wed Jul 25 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7.0-2
- Fix build on ppc64
- New upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6.0-3
- Correct dependency on php

* Tue Jun 26 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6.0-2
- Also remove xsd-utils requirement for -devel sub-package

* Mon Jun 25 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6.0-1
- Actual 0.6.0 release

* Sat Jun 23 2012 Christoph Wickert <wickert@kolabsys.com> - 0.6-1
- Update to 0.6 final
- Run ldconfig in %%post and %%postun
- Mark kolabformat.ini as config file
- Export LD_LIBRARY_PATH so tests can be run in %%check
- Add php dependencies to php-kolabformat package
- Make base package requirements are arch-specific
- Filter unwanted provides of php-kolabformat and python-kolabformat

* Wed Jun 20 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-0.4
- Some other cleanups to prevent review scrutiny from blocking
  inclusion
- Drop build requirement for xsd-utils

* Sat Jun  9 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-0.2
- Git snapshot release

* Wed May 23 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5-5
- Correct use of Python keyword None
- Snapshot version with attendee cutype support

* Tue May 22 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5-3
- Snapshot version with attendee delegation support

* Sat May 12 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5-2
- Snapshot version with build system changes

* Wed May  9 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.4.0-3
- Fix PHP kolabformat module packaging

* Wed May  2 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.4.0-2
- New version

* Fri Apr 20 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.0-1
- New version

* Mon Apr  9 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3-0.1
- First package

