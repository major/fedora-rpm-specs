Name:           libgnome-games-support
Version:        2.0.0
Release:        7%{?dist}
Summary:        Support library for GNOME games

# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libgnome-games-support/
Source0:        https://download.gnome.org/sources/libgnome-games-support/2.0/libgnome-games-support-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)

%description
libgnome-games-support is a small library intended for internal use
by GNOME Games, but it may be used by others.
The API will only break with the major version number.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install

%find_lang libgnome-games-support2


%files -f libgnome-games-support2.lang
%doc README
%license COPYING.LESSER
%{_libdir}/libgnome-games-support-2.so.4*

%files devel
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Kalev Lember <klember@redhat.com> - 2.0.0-1
- Update to 2.0.0
- Drop old, unused libgames-support provides

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Kalev Lember <klember@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 1.7.1-1
- Update to 1.7.1

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 1.6.0.1-1
- Update to 1.6.0.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan  4 2020 Yanko Kaneti <yaneti@declera.com> - 1.5.90-1
- Update to 1.5.90. Switch to meson

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 1.4.4-1
- Update to 1.4.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Yanko Kaneti <yaneti@declera.com> - 1.4.3-1
- Update to 1.4.3

* Wed Aug 22 2018 Yanko Kaneti <yaneti@declera.com> - 1.4.2-1
- Update to 1.4.2
- Change url to gitlab.gnome.org

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Kalev Lember <klember@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Sat Mar 10 2018 Yanko Kaneti <yaneti@declera.com> - 1.4.0-1
- Update to 1.4.0

* Mon Feb 19 2018 Yanko Kaneti <yaneti@declera.com> - 1.3.90-1
- Update to 1.3.90
- Soname change
- New ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep  9 2017 Yanko Kaneti <yaneti@declera.com> - 1.2.3-1
- Update to 1.2.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Yanko Kaneti <yaneti@declera.com> - 1.2.2-1
- Update to 1.2.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Yanko Kaneti <yaneti@declera.com> - 1.2.1-1
- Update to 1.2.1

* Mon Sep 19 2016 Yanko Kaneti <yaneti@declera.com> - 1.2.0-1
- Update to 1.2.0

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 1.1.91-1
- Update to 1.1.91

* Thu Aug 18 2016 Yanko Kaneti <yaneti@declera.com> - 1.1.90-3
- Move  libgames-support-devel obsoletes to -devel

* Thu Aug 18 2016 Yanko Kaneti <yaneti@declera.com> - 1.1.90-2
- Add libgames-support obsoltes

* Thu Aug 18 2016 Yanko Kaneti <yaneti@declera.com> - 1.1.90-1
- Renamed libgames-support for review.
