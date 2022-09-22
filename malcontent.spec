Name:           malcontent
Version:        0.11.0
Release:        1%{?dist}
Summary:        Parental controls implementation

License:        LGPLv2+
URL:            https://gitlab.freedesktop.org/pwithnall/malcontent/
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-testing-0)
BuildRequires:  pam-devel

Requires: polkit

# Descriptions mostly gathered from:
# https://github.com/endlessm/malcontent/blob/debian-master/debian/control

%description
libmalcontent implements parental controls support which can be used by
applications to filter or limit the access of child accounts to inappropriate
content.

%package control
Summary:        Parental Controls UI
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description control
This package contains a user interface for querying and setting parental
controls for users.

%package pam
Summary:        Parental Controls PAM Module

%description pam
This package contains a PAM module which prevents logins for users who have
exceeded their allowed computer time.

%package tools
Summary:        Parental Controls Tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains tools for querying and updating the parental controls
settings for users.

%package ui-devel
Summary:        Development files for libmalcontent-ui
Requires:       %{name}-ui-libs%{?_isa} = %{version}-%{release}

%description ui-devel
This package contains the pkg-config file and development headers
for libmalcontent-ui.

%package ui-libs
Summary:        Libraries for %{name}

%description ui-libs
This package contains libmalcontent-ui.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the pkg-config file and development headers
for %{name}.

%package libs
Summary:        Libraries for %{name}

%description libs
This package contains libmalcontent.

%prep
%autosetup -p1 -S git

%build
%meson -Dui=enabled
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.freedesktop.MalcontentControl.appdata.xml

%files -f %{name}.lang
%license COPYING COPYING-DOCS
%doc README.md
%{_datadir}/accountsservice/interfaces/
%{_datadir}/dbus-1/interfaces/
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/polkit-1/rules.d/com.endlessm.ParentalControls.rules

%files control
%license COPYING
%doc README.md
%{_bindir}/malcontent-control
%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.MalcontentControl.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.freedesktop.MalcontentControl-symbolic.svg
%{_datadir}/metainfo/org.freedesktop.MalcontentControl.appdata.xml

%files pam
%license COPYING
%{_libdir}/security/pam_malcontent.so

%files tools
%license COPYING
%{_bindir}/malcontent-client
%{_mandir}/man8/malcontent-client.8.*

%files ui-devel
%license COPYING
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/MalcontentUi-1.gir
%{_libdir}/libmalcontent-ui-1.so
%{_includedir}/malcontent-ui-1/
%{_libdir}/pkgconfig/malcontent-ui-1.pc

%files ui-libs
%license COPYING
%doc README.md
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/MalcontentUi-1.typelib
%{_libdir}/libmalcontent-ui-1.so.*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Malcontent-0.gir
%{_includedir}/malcontent-0/
%{_libdir}/libmalcontent-0.so
%{_libdir}/pkgconfig/malcontent-0.pc

%files libs
%license COPYING
%doc README.md
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/Malcontent-0.typelib
%{_libdir}/libmalcontent-0.so.*

%changelog
* Mon Sep 12 2022 Bastien Nocera <bnocera@redhat.com> - 0.11.0-1
+ malcontent-0.11.0-1
- Update to 0.11.0

* Tue Aug 02 2022 Bastien Nocera <bnocera@redhat.com> - 0.10.5-1
+ malcontent-0.10.5-1
- Update to 0.10.5 (#2113504)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.3-1
- Update to 0.10.3 (#2020858)

* Mon Oct 04 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.2-2
+ malcontent-0.10.2-2
- Make parental controls app unremovable (#2009852)

* Mon Oct 04 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.2-1
+ malcontent-0.10.2-1
- Update to 0.10.2

* Thu Sep 09 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.1-2
+ malcontent-0.10.1-2
- Make Parental controls app require the malcontent base package
- Fixes: rhbz#2001555

* Thu Aug 26 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.1-1
+ malcontent-0.10.1-1
- Update to 0.10.1
- Hide management application in GNOME, it's accessible through the User accounts panel

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Bastien Nocera <bnocera@redhat.com> - 0.10.0-1
+ malcontent-0.10.0-1
- Update to 0.10.0

* Tue Sep 08 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-5
+ malcontent-0.8.0-5
- More review comments

* Mon Sep 07 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-4
+ malcontent-0.8.0-4
- Fix more review comments again

* Fri Sep 04 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-3
+ malcontent-0.8.0-3
- Fix more review comments

* Fri Aug 28 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-2
+ malcontent-0.8.0-2
- Fix review comments

* Thu Jul 23 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-1
+ malcontent-0.8.0-1
- First package
