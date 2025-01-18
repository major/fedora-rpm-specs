
%global majorver 1
%global minorver 28
%global patchver 1

%global commit 27b915d95d625cafe77efc56f8e4a854ffdb3ff5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20231119

%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif

Name:    genders
Version: %{majorver}.%{minorver}.%{patchver}~^%{commitdate}git%{shortcommit}
Release: 3%{?dist}
Summary: Static cluster configuration database
License: GPL-2.0-only

URL: https://github.com/chaos/genders
Source: https://github.com/chaos/genders/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: autoconf
%if ! %{JAVA}
Obsoletes: genders-java < %{version}-%{release}
Obsoletes: genders-javadoc < %{version}-%{release}
Obsoletes: genders-java-devel < %{version}-%{release}
%endif

%description
Genders is a static cluster configuration database used for cluster
configuration management.  It is used by a variety of tools and
scripts for management of large clusters.  The genders database is
typically replicated on every node of the cluster. It describes the
layout and configuration of the cluster so that tools and scripts can
sense the variations of cluster nodes. By abstracting this information
into a plain text file, it becomes possible to change the
configuration of a cluster by modifying only one file.

%package compat
Summary: Compatibility library 
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
%if 0%{?rhel} >= 6 || 0%{?fedora} > 0
BuildArch: noarch
%endif
%description compat
Genders API that is compatible with earlier releases of genders.

%package perl
Summary: Perl libraries
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Config)
%description perl
Genders API bindings for perl.

%if %{JAVA}
%package javadoc
Summary: Java Documentation
BuildRequires: java-devel
%description javadoc
Genders API Documentation for java.

%package java-devel
Summary: Java Development libraries
Requires: %{name}-java%{?_isa} = %{version}-%{release}
%description java-devel
Genders API bindings for java.

%package java
Summary: Java libraries
BuildRequires: java-devel
BuildRequires: make
%description java
%endif
Genders API bindings for java.

%global __provides_exclude_from ^(.%{perl_vendorarch}/*\\.so)$

%package -n libgenders
Summary: Genders libraries
%description -n libgenders
Genders API for C.

%package -n libgenders-devel
Summary: Genders development libraries
Requires: libgenders%{?_isa} = %{version}-%{release}
%description -n libgenders-devel
Genders development headers and libraries for C.

%package -n libgendersplusplus
Summary: Genders libraries for C++
Requires: libgenders%{?_isa} = %{version}-%{release}
%description -n libgendersplusplus
Genders API for C++.

%package -n libgendersplusplus-devel
Summary: Genders development libraries
Requires: libgenders-devel%{?_isa} = %{version}-%{release}
Requires: libgendersplusplus%{?_isa} = %{version}-%{release}
%description -n libgendersplusplus-devel
Genders development headers and libraries for C++.

%prep
%setup  -q -n %{name}-%{commit}

%if 0%{?rhel} <= 6
%global __provides_exclude ^Lib%{name}.so.*$
%endif

%build
%if %{JAVA}
export CPPFLAGS='-I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -I../../../src/libgenders'
%else
export CPPFLAGS='-I../../../src/libgenders'
%endif
%configure \
    --with-perl-extensions \
    --with-perl-vendor-arch \
%if %{JAVA}
    --with-java-extensions \
%else
    --without-java-extensions \
%endif
    --without-python-extensions \
    --with-cplusplus-extensions \
    --with-extension-destdir="%{buildroot}"
%{__make}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} make install
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.a
chmod +w %{buildroot}/%{perl_vendorarch}/auto/Lib%{name}/Lib%{name}.so
rm -f %{buildroot}/%{perl_vendorarch}/auto/Lib%{name}/Lib%{name}.bs
rm -f %{buildroot}/%{perl_vendorarch}/auto/Lib%{name}/.packlist
mkdir -p %{buildroot}/%{_libexecdir}

mkdir -p %{buildroot}/%{_jnidir}
%if 0%{?rhel} == 5
%define _datarootdir %{_prefix}/share
%endif
%if %{JAVA}
mv %{buildroot}/%{_datarootdir}/java/Genders.jar %{buildroot}/%{_jnidir}/
%endif

%ldconfig_scriptlets -n libgenders
%ldconfig_scriptlets -n libgendersplusplus
%if %{JAVA}
%ldconfig_scriptlets -n genders-java
%endif

%files
%doc README NEWS ChangeLog DISCLAIMER DISCLAIMER.UC COPYING TUTORIAL genders.sample
%{_mandir}/man1/*
%{_mandir}/man3/genders.3*
%{_bindir}/*

%files -n libgenders
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libgenders.so.0*
%{_mandir}/man3/libgenders.3*

%files -n libgenders-devel
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_mandir}/man3/genders_*
%{_includedir}/genders.h
%{_libdir}/libgenders.so

%files -n libgendersplusplus
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libgendersplusplus.so.2*

%files -n libgendersplusplus-devel
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libgendersplusplus.so
%{_includedir}/gendersplusplus*

%files perl
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_mandir}/man3/Libgenders*
%{_mandir}/man3/Genders*
%{perl_vendorarch}/*

%if %{JAVA}
%files java-devel
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libGendersjni.so

%files java
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_libdir}/libGendersjni.so.*
%{_jnidir}/Genders.jar

%files javadoc
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_docdir}/%{name}-%{majorver}.%{minorver}.%{patchver}-javadoc
%endif

%files compat
%doc DISCLAIMER DISCLAIMER.UC COPYING 
%{_mandir}/man3/gendlib*
%{_usr}/lib/genders/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1~^20231119git27b915d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1~^20231119git27b915d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Neil Hanlon <neil@shrug.pw> - 1.28.1^20231119git27b915d9-1
- update to latest commit of upstream (#2259159 #2292216) (prerelease 1.28.1)

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.27.2-19
- Perl 5.40 rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.27.2-15
- Perl 5.38 rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 03 2022 Trey Dockendorf <treydock@gmail.com> 1.27.3-13
- Fix java build issues for Fedora 37 (Fixes bz #2104043)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.27.2-11
- Perl 5.36 rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.27.2-10
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.27.2-7
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.27.2-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.27.2-3
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Tom Callaway <spot@fedoraproject.org> - 1.27.2-1
- update to 1.27-2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-22
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.22-20
- Subpackage python2-genders has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-18
- Perl 5.28 rebuild

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.22-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.22-16
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.22-14
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.22-13
- Python 2 binary package renamed to python2-genders
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.22-10
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-9
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-6
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-3
- Perl 5.22 rebuild

* Tue May 19 2015 David Brown <david.brown@pnnl.gov> - 1.22-2
- Bugfix make libgenders man page part of libgenders (#1220093)

* Sat May 2 2015 David Brown <david.brown@pnnl.gov> - 1.22-1
- new upstream build
- fix bugzilla #1217007

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-3
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 07 2014 David Brown <david.brown@pnnl.gov> - 1.21-1
- New updated version
- Wow, they have java bindings now

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.20-5
- Perl 5.18 rebuild

* Tue Mar 26 2013 David Brown <david.brown@pnnl.gov> - 1.20-4
* added autoconf to build depends just to be safe

* Mon Mar 25 2013 David Brown <david.brown@pnnl.gov> - 1.20-3
- autoreconf so aarch64 will work on f19
- add perl(Config) for build depends

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 David Brown <david.brown@pnnl.gov> - 1.20-1
- New Upstream Version

* Fri Aug 10 2012 David Brown <david.brown@pnnl.gov> - 1.18-9
- got a better patch from upstream

* Fri Aug 10 2012 David Brown <david.brown@pnnl.gov> - 1.18-8
- Patched an import bug not finding SystemError class

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 David Brown <david.brown@pnnl.gov> - 1.18-6
- python egginfo files don't exist on el5

* Fri Jul 06 2012 David Brown <david.brown@pnnl.gov> - 1.18-5
- change mode on python shared objects

* Thu Jul 05 2012 David Brown <david.brown@pnnl.gov> - 1.18-4
- move compat stuff back to hard coded lib directory
- remove parallel build doesn't work with yacc deps

* Thu Apr 12 2012 David Brown <david.brown@pnnl.gov> - 1.18-3
- Add some Groups for EPEL 5/6 repos
- Fix up Changelogs to add spaces

* Wed Apr 11 2012 David Brown <david.brown@pnnl.gov> - 1.18-2
- Followed advice from bugzilla
- Used proper BuildRoot tag
- Removed superfluous '.' from end of descriptions
- Fixed Requires by adding release and _isa
- Changed out RPM_BUILD_ROOT for %%{buildroot}
- Added four argument defattr lines in files sections

* Mon Apr 9 2012 David Brown <david.brown@pnnl.gov> - 1.18-1
- initial packaging

