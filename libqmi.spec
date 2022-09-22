Name: libqmi
Version: 1.30.6
Release: 2%{?dist}
Summary: Support library to use the Qualcomm MSM Interface (QMI) protocol
License: LGPLv2+
URL: http://freedesktop.org/software/libqmi
Source: http://freedesktop.org/software/libqmi/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: glib2-devel >= 2.48.0
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gudev-1.0) >= 147
BuildRequires: libmbim-devel >= 1.18.0
BuildRequires: libqrtr-glib-devel
BuildRequires: make
BuildRequires: python3

%description
This package contains the libraries that make it easier to use QMI functionality
from applications that use glib.


%package devel
Summary: Header files for adding QMI support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel
Requires: pkgconfig

%description devel
This package contains the header and pkg-config files for development
applications using QMI functionality from applications that use glib.


%package utils
Summary: Utilities to use the QMI protocol from the command line
Requires: %{name}%{?_isa} = %{version}-%{release}
License: GPLv2+

%description utils
This package contains the utilities that make it easier to use QMI functionality
from the command line.


%prep
%autosetup -p1


%build
%configure --disable-static --enable-gtk-doc --enable-mbim-qmux
%{make_build} V=1


%install
%make_install
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference configure.ac
find %{buildroot} -type f -name "*.la" -delete


%ldconfig_scriptlets


%files
%license COPYING.LIB
%doc NEWS AUTHORS README
%{_libdir}/libqmi-glib.so.*
%{_libdir}/girepository-1.0/Qmi-1.0.typelib


%files devel
%{_includedir}/libqmi-glib/
%{_libdir}/pkgconfig/qmi-glib.pc
%{_libdir}/libqmi-glib.so
%{_datadir}/gtk-doc/html/libqmi-glib/
%{_datadir}/gir-1.0/Qmi-1.0.gir


%files utils
%license COPYING
%{_bindir}/qmicli
%{_bindir}/qmi-network
%{_bindir}/qmi-firmware-update
%{_datadir}/bash-completion
%{_libexecdir}/qmi-proxy
%{_mandir}/man1/*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 14 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.30.6-1
- Update to 1.30.6

* Sat Feb 12 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.30.4-1
- Update to 1.30.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.30.2-1
- Update to 1.30.2

* Sat Aug 14 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.30.0-1
- Update to 1.30.0

* Wed Aug 04 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.28.8-1
- Update to 1.28.8

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.28.6-1
- Update to 1.28.6

* Tue Apr 13 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.28.2-1
- Update to 1.28.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.26.8-1
- Update to 1.26.8

* Tue Nov  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.26.6-1
- Update to 1.26.6

* Fri Aug 28 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.26.4-1
- Update to 1.26.4

* Mon Jul 27 2020 Peter Robinson <pbrobinson@fedoraproject.org>
- Update to 1.26.2

* Tue Mar 24 2020 Lubomir Rintel <lkundrak@v3.sk> - 1.24.8
- Update to 1.24.8

* Thu Mar  5 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.24.6-1
- Update to 1.24.6
- Spec cleanups, fix shipped licenses

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.24.0
- Update to 1.24.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.22.4-1
- Update to 1.22.4

* Thu Apr 11 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.22.2-1
- Update to 1.22.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.20.0-1
- Update to 1.22.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.20.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.20.0-1
- Update to 1.20.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.18.0-1
- Update to 1.18.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.16.2-1
- Update to 1.16.2

* Tue Oct 04 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.16.0-2
- Enable hardening

* Fri Jul 08 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.16.0-1
- Update to 1.16.0

* Tue May 03 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.14.2-1
- Update to 1.14.2

* Mon Mar 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.14.0-1
- Update to 1.14.0 release

* Tue Mar 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.12.6-3
- Fix FTBFS with GCC 6 (#1307733)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.12.6-1
- Update to 1.12.6 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.12.4-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Feb 11 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.12.4-1
- Update to 1.12.4 release

* Tue Feb 10 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.12.2-1
- Clean up the spec file a bit
- Update to 1.12.2 release

* Thu Jan 15 2015 Dan Williams <dcbw@redhat.com> - 1.12.0-1
- Update to 1.12.0 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Dan Williams <dcbw@redhat.com> - 1.10.2
- Update to 1.10.2 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb  1 2014 poma <poma@gmail.com> - 1.8.0-1
- Update to 1.8.0 release

* Fri Sep  6 2013 Dan Williams <dcbw@redhat.com> - 1.6.0-1
- Update to 1.6.0 release

* Fri Jun  7 2013 Dan Williams <dcbw@redhat.com> - 1.4.0-1
- Update to 1.4.0 release

* Fri May 10 2013 Dan Williams <dcbw@redhat.com> - 1.3.0-1.git20130510
- Initial Fedora release

