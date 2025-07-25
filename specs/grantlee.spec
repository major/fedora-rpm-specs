
#global apidocs 1

# set this until when/if we port to new cmake macros
%global __cmake_in_source_build 1

Name:    grantlee
Summary: Qt string template engine based on the Django template system
Version: 0.5.1
Release: 30%{?dist}

License: LGPL-2.0-or-later
URL:     http://www.gitorious.org/grantlee/pages/Home
Source0: http://downloads.grantlee.org/grantlee-%{version}%{?pre:-%{pre}}.tar.gz

## upstream patches

BuildRequires: cmake >= 2.8.11
BuildRequires: gcc-c++
BuildRequires: kde4-macros(api)
BuildRequires: pkgconfig(QtGui) pkgconfig(QtScript) 
%if 0%{?apidocs}
BuildRequires: doxygen
BuildRequires: graphviz
%endif
## for %%check
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: make

Requires: kde-filesystem

%description
Grantlee is a plug-in based String Template system written 
using the Qt framework. The goals of the project are to make it easier for
application developers to separate the structure of documents from the 
data they contain, opening the door for theming.

The syntax is intended to follow the syntax of the Django template system, 
and the design of Django is reused in Grantlee. 
Django is covered by a BSD style license.

Part of the design of both is that application developers can extend 
the syntax by implementing their own tags and filters. For details of 
how to do that, see the API documentation.

For template authors, different applications using Grantlee will present 
the same interface and core syntax for creating new themes. For details of 
how to write templates, see the documentation.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package apidocs
Summary: Grantlee API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the Grantlee API documentation in HTML
format for easy browsing.


%prep
%autosetup -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} \
  -DCMAKE_BUILD_TYPE=release \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%if 0%{?apidocs}
make docs -C %{_target_platform}
%endif


%install
make install/fast -C %{_target_platform} DESTDIR=%{buildroot}

# create/own kde4-related dirs
mkdir -p %{buildroot}%{_kde4_libdir}/kde4/plugins/grantlee/0.5/

%if 0%{?apidocs}
mkdir -p %{buildroot}%{_docdir}/HTML/en/grantlee-apidocs
cp -prf %{_target_platform}/apidox/* %{buildroot}%{_docdir}/HTML/en/grantlee-apidocs
%endif


%check
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a make test -C %{_target_platform} ||:


%{ldconfig_scriptlets}

%files
%doc AUTHORS CHANGELOG README
%license COPYING.LIB
%{_libdir}/libgrantlee_core.so.0*
%{_libdir}/libgrantlee_gui.so.0*
%dir %{_libdir}/grantlee/
%{_libdir}/grantlee/0.5/
%{_kde4_libdir}/kde4/plugins/grantlee/0.5/

%files devel
%{_includedir}/grantlee/
%{_includedir}/grantlee_core.h
%{_includedir}/grantlee_templates.h
%{_includedir}/grantlee_textdocument.h
%{_libdir}/libgrantlee_core.so
%{_libdir}/libgrantlee_gui.so
%{_libdir}/cmake/grantlee/

%if 0%{?apidocs}
%files apidocs
%{_docdir}/HTML/en/grantlee-apidocs/
%endif


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Alessandro Astone <ales.astone@gmail.com> - 0.5.1-28
- Fix build dependency on %_kde4_libdir macro

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Than Ngo <than@redhat.com> - 0.5.1-23
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.5.1-17
- FTBFS: set __cmake_in_source_build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.5.1-10
- BR: gcc-c++
- drop -apidocs
- %%check: skip tests
- use %%ldconfig_scriptlets, %%license

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 0.5.1-8
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Rex Dieter <rdieter@fedoraproject.org> 0.5.1-2
- own libdir/kde4/plugins/grantlee/0.5/

* Sun Apr 12 2015 Rex Dieter <rdieter@fedoraproject.org> 0.5.1-1
- grantlee-0.5.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun  8 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.0-6
- make %%check fatal (aarch64 has had some love)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.4.0-4 
- pull in some upstream fixes (and use %%autosetup)
- make %%check non-fatal (aarm64 needs some love)

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-3
- %%check: use xvfb-run

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-2
- %%check: make test

* Fri Nov 29 2013 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-1
- 0.4.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org>  0.3.0-1
- 0.3.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 04 2011 Rex Dieter <rdieter@fedoraproject.org>  0.2.0 -1
- 2.0.0
- pkgconfig-style deps

* Tue Oct 18 2011 Rex Dieter <rdieter@fedoraproject.org>  0.2.0 -0.2.rc2
- 2.0.0-rc2

* Tue Aug 09 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-0.1.rc1
- 2.0.0-rc1

* Tue Jul 12 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.9-1
- 0.1.9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 27 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.1.6-1
- grantlee 0.1.6

* Fri Aug 27 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.1.5-1
- grantlee 0.1.5

* Sun Jul 04 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.1.2-1
- grantlee 0.1.2

* Tue May 18 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.1.1-3
- disabled apidocs until we find a standard path

* Tue May 11 2010 Jaroslav Reznik <jreznik@redhat.com> 0.1.1-2
- added -apidocs subpackage

* Sun May 09 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.1.1-1
- grantlee 0.1.1
- fixed Group

* Thu Apr 15 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.1.0-1
- initial fedora release
