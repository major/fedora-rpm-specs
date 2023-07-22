Name:           herqq
Version:        1.0.0
Release:        29%{?dist}
Summary:        A software library for building UPnP devices and control points
# test application is GPLv3 but we do not ship it
License:        LGPLv3+
URL:            http://herqq.org/
Source0:        http://downloads.sourceforge.net/project/hupnp/hupnp/%{name}-%{version}.zip
Patch2:         herqq-1.0.0-qtsoap-library.patch
Patch3:         herqq-1.0.0-c++11.patch


BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel
BuildRequires:  qtsoap-devel
BuildRequires: make


%description
Herqq UPnP (HUPnP) is a software library for building UPnP 
devices and control points conforming to the UPnP Device 
Architecture version 1.1. 

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}
Provides: hupnp-devel = %{version}-%{release}
%description devel
Header files for developing applications using %{name}.

%prep
%setup -q

# lQtSolutions to lqtsoap
%patch2 -p1 -b .qtsoap-library
%patch3 -p1 -b .c++11

%build
# we have to disable bundled QtSOAP library
%{qmake_qt4} PREFIX=%{_prefix} -config DISABLE_QTSOAP \
  -config DISABLE_TESTAPP -config USE_QT_INSTALL_LOC
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install


%ldconfig_scriptlets


%files
%doc hupnp/ChangeLog hupnp/LICENSE_LGPLv3.txt
%{_qt4_libdir}/libHUpnp.so.1*

%files devel
%{_qt4_libdir}/libHUpnp.so
%{_qt4_headerdir}/HUpnpCore/

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-18
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 29 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.0-13
- Fix FTBFS with C++11 (#1307615)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-11
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 06 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.0-2
- Provides: hupnp(-devel)

* Wed Jul 20 2011 Jaroslav Reznik <jreznik@redhat.com> - 1.0.0-1
- post-review update to 1.0.0

* Wed Jul 20 2011 Jaroslav Reznik <jreznik@redhat.com> - 0.9.1-3
- fix license to LGPLv3+
- qt4 header dir for consistency
- shlib soname tracked in %%files
- -devel should not duplicate COPYING

* Tue Jul 19 2011 Jaroslav Reznik <jreznik@redhat.com> - 0.9.1-2
- qtsoap library
- cleanup SPEC file

* Tue Feb 22 2011 Jaroslav Reznik <jreznik@redhat.com> - 0.9.1-1
- Initial spec file 
