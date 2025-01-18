Name:           gmime30
Version:        3.2.15
Release:        2%{?dist}
Summary:        Library for creating and parsing MIME messages

# The library is LGPL-2.1-or-later; various files (which we don't package)
# in examples/ and tests/ are GPL-2.0-or-later.
License:        LGPL-2.1-or-later
URL:            https://github.com/jstedfast/gmime
Source0:        https://github.com/jstedfast/gmime/releases/download/%{version}/gmime-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  vala

%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n gmime-%{version}

%build
%configure --disable-static
%make_build V=1

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/libgmime-3.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GMime-3.0.typelib

%files devel
%{_libdir}/libgmime-3.0.so
%{_libdir}/pkgconfig/gmime-3.0.pc
%{_includedir}/gmime-3.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GMime-3.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gmime-3.*/
%{_datadir}/vala/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 David King <amigadave@amigadave.com> - 3.2.15-1
- Update to 3.2.15 (#2293536)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Kalev Lember <klember@redhat.com> - 3.2.14-1
- Update to 3.2.14 (rhbz#2065645)
- Use SPDX license identifiers

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 3.2.7-1
- Update to 3.2.7

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.2.6-1
- Update to 3.2.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Kalev Lember <klember@redhat.com> - 3.2.5-1
- Update to 3.2.5

* Fri Oct 04 2019 Kalev Lember <klember@redhat.com> - 3.2.4-1
- Update to 3.2.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Kalev Lember <klember@redhat.com> - 3.2.3-1
- Update to 3.2.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.2.0-1
- Update to 3.2.0
- Remove ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Kalev Lember <klember@redhat.com> - 3.0.5-1
- Update to 3.0.5

* Tue Nov 21 2017 Kalev Lember <klember@redhat.com> - 3.0.4-1
- Update to 3.0.4

* Thu Nov 02 2017 Kalev Lember <klember@redhat.com> - 3.0.3-1
- Update to 3.0.3

* Fri Sep 08 2017 Kalev Lember <klember@redhat.com> - 3.0.2-1
- Initial Fedora packaging
