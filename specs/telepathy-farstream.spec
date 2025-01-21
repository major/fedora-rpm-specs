Name:           telepathy-farstream
Version:        0.6.1
Release:        29%{?dist}
Summary:        Telepathy client library to handle Call channels

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Telepathy-Farsight
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  telepathy-glib-devel >= 0.19.0
BuildRequires:  farstream02-devel >= 0.2.7
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  gobject-introspection-devel

## Obsolete telepathy-farsight(-python) with Fedora 17.
Provides:       telepathy-farsight = %{version}
Obsoletes:      telepathy-farsight < 0.0.20
Provides:       telepathy-farsight-python = %{version}
Obsoletes:      telepathy-farsight-python < 0.0.20
# Obsolete telepathy-farstream-python with Fedora 18 since gobject-introspection is
# provided now
Provides:       %{name}-python = %{version}
Obsoletes:      %{name}-python < 0.6.0


%description
%{name} is a Telepathy client library that uses Farstream to handle
Call channels.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       telepathy-glib-devel >= 0.19.0
Requires:       farstream02-devel >= 0.2.7
Requires:       dbus-devel
Requires:       dbus-glib-devel
Requires:       pkgconfig

## Obsolete telepathy-farsight with Fedora 17
Provides:       telepathy-farsight-devel = %{version}
Obsoletes:      telepathy-farsight-devel < 0.0.20


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
%configure --enable-static=no
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%check
make check


%ldconfig_scriptlets


%files
%doc NEWS README COPYING
%{_libdir}/libtelepathy-farstream*.so.*
%{_libdir}/girepository-1.0/TelepathyFarstream-0.6.typelib


%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libtelepathy-farstream.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/telepathy-1.0/%{name}/
%{_datadir}/gir-1.0/TelepathyFarstream-0.6.gir


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.1-28
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 9 2020 Petr Viktorin <pviktori@redhat.com> - 0.6.1-19
- Remove BuildRequires on python2-devel

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.1-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 David Woodhouse <dwmw2@infradead.org> - 0.6.1-5
- Rebuilt against farstream 0.2.7

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.1-3
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar  7 2014 Brian Pepple <bpepple@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1.

* Fri Feb 14 2014 Debarshi Ray <rishi@fedoraproject.org> - 0.6.0-4
- Add %%check to run the upstream test suite on each build

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct  3 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0
- Drop python subpackage. gobject-introspection is used now.
- Drop unnecessary buildroot cleaning in install section.
- Update BR for farstream02-devel.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-2
- Rebuild against farstream

* Thu Apr  5 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0.

* Tue Apr 03 2012 Brian Pepple <bpepple@fedoraproject.org. - 0.2.3-2
- Rebuild against new tp-glib.

* Tue Mar 20 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3.

* Tue Mar 13 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.2-2
- Add obsolete/provides on python subpackage.

* Fri Mar  9 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.2-1
- Update 0.2.2.

* Wed Mar  7 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-3
- Enable python bindings.

* Mon Mar  5 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-2
- Use macro for version in provides.
- Change reference Farsight in description to Farstream.

* Sun Mar  4 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1.
- Add BR on farstream-devel.
- Bump minimum version of tp-glib.
- Add obsolete/provide on telepathy-farsight.

* Mon Nov 21 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-1
- Initial Fedora spec file.
- Disable the python bindings for now.

