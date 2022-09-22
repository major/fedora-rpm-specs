Name: libmbim
Version: 1.26.4
Release: 2%{?dist}
Summary: Support library for the Mobile Broadband Interface Model protocol
License: LGPLv2+
URL: http://freedesktop.org/software/libmbim
Source: http://freedesktop.org/software/libmbim/%{name}-%{version}.tar.xz

BuildRequires: automake autoconf libtool
BuildRequires: gcc
BuildRequires: glib2-devel >= 2.48.0
BuildRequires: gtk-doc
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: python3


%description
This package contains the libraries that make it easier to use MBIM
functionality from applications that use glib.


%package devel
Summary: Header files for adding MBIM support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa}

%description devel
This package contains the header and pkg-config files for developing
applications using MBIM functionality from applications that use glib.

%package utils
Summary: Utilities to use the MBIM protocol from the command line
Requires: %{name}%{?_isa} = %{version}-%{release}
License: GPLv2+

%description utils
This package contains the utilities that make it easier to use MBIM
functionality from the command line.


%prep
%autosetup -p1


%build
%configure --disable-static --enable-gtk-doc
%{make_build}

%install
%{make_install}
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference configure.ac
find %{buildroot} -type f -name "*.la" -delete


%check
make check


%ldconfig_scriptlets


%files
%license COPYING.LIB
%doc NEWS AUTHORS README
%{_libdir}/libmbim-glib.so.4*

%files devel
%{_includedir}/libmbim-glib/
%{_libdir}/pkgconfig/mbim-glib.pc
%{_libdir}/libmbim-glib.so
%{_datadir}/gtk-doc/html/libmbim-glib/

%files utils
%license COPYING
%{_bindir}/mbimcli
%{_bindir}/mbim-network
%{_datadir}/bash-completion
%{_libexecdir}/mbim-proxy
%{_mandir}/man1/mbim*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 14 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.26.4-1
- Update to 1.26.4

* Sat Feb 12 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.26.2-1
- Update to 1.26.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.24.8-1
- Update to 1.24.8

* Tue Feb 23 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.24.6-1
- Update tp 1.24.6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.24.4-1
- Update to 1.24.4

* Mon Jul 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.24.2-1
- Update to 1.24.2

* Thu Mar  5 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.22.0-1
- Update to 1.22.0 release
- Fix shipped license, use %%license
- Spec cleanups

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.20.2
- Update to 1.20.2 release

* Mon Sep 23 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.20.0
- Update to 1.20.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.18.2-2
- Regenerate manuals that are broken in dist

* Mon May 06 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.18.2-1
- Update to 1.18.2 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.18.0-1
- Update to 1.18.0 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.16.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.16.0-1
- Update to 1.16.0 release

* Tue Aug 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.14.2-1
- Update to 1.14.2 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 08 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.14.0-1
- Update to 1.14.0 release

* Mon Mar 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.12.4-1
- Update to 1.12.2 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.12.2-1
- Update to 1.12.2 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Dan Williams <dcbw@redhat.com> - 1.12.0-1
- Update to 1.12.0 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Dan Williams <dcbw@redhat.com> - 1.10.0-1
- Update to 1.10.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar  8 2014 Dan Williams <dcbw@redhat.com> - 1.8.0-1
- Update to 1.8.0 release

* Sat Feb  1 2014 poma <poma@gmail.com> - 1.6.0-1
- Update to 1.6.0 release

* Thu Aug 15 2013 Dan Williams <dcbw@redhat.com> - 1.5.0-1.20130815git
- Initial Fedora release

