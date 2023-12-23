%global appname io.elementary.wingpanel

%global commit      0fb4a14b3134b07fd4510f3bfec46b4f0193f20a
%global shortcommit %(c=%{commit}; echo ${c:0:7}) 
%global commitdate  20231206

%global _description %{expand:
Stylish top panel that holds indicators and spawns an application
launcher.}

Name:           wingpanel
Version:        3.0.5
Release:        3.%{commitdate}.git%{shortcommit}%{?dist}
Summary:        Stylish top panel
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later

URL:            https://github.com/elementary/wingpanel
Source0:        %{url}/archive/%{commit}/wingpanel-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

%if 0%{?fedora} >= 39
BuildRequires:  pkgconfig(libmutter-13)
BuildRequires:  pkgconfig(mutter-clutter-13)
BuildRequires:  pkgconfig(mutter-cogl-13)
BuildRequires:  pkgconfig(mutter-cogl-pango-13)
%endif
%if 0%{?fedora} == 38
BuildRequires:  pkgconfig(libmutter-12)
BuildRequires:  pkgconfig(mutter-clutter-12)
BuildRequires:  pkgconfig(mutter-cogl-12)
BuildRequires:  pkgconfig(mutter-cogl-pango-12)
%endif

BuildRequires:  pkgconfig(gala)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10

Requires:       hicolor-icon-theme

%description %{_description}


%package        devel
Summary:        Stylish top panel (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel %{_description}

This package contains the files required for developing for wingpanel.


%prep
%autosetup -n wingpanel-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# create plugin directory
mkdir -p %{buildroot}/%{_libdir}/wingpanel

# create settings directory
mkdir -p %{buildroot}/%{_sysconfdir}/wingpanel.d


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%dir %{_sysconfdir}/wingpanel.d
%dir %{_libdir}/wingpanel

%{_bindir}/%{appname}

%{_libdir}/libwingpanel.so.3*
%{_libdir}/gala/plugins/libwingpanel-interface.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%files devel
%{_includedir}/wingpanel/

%{_libdir}/libwingpanel.so
%{_libdir}/pkgconfig/wingpanel.pc

%{_datadir}/vala/vapi/wingpanel.deps
%{_datadir}/vala/vapi/wingpanel.vapi


%changelog
* Thu Dec 14 2023 Fabio Valentini <decathorpe@gmail.com> - 3.0.5-3.20231206.git0fb4a14
- Bump to commit 0fb4a14.

* Sun Nov 12 2023 Fabio Valentini <decathorpe@gmail.com> - 3.0.5-2.20230915.gitd6009d9
- Bump to commit d6009d9.

* Tue May 23 2023 Fabio Valentini <decathorpe@gmail.com> - 3.0.3-1.20230423.git0cbf289
- Packaging refresh for package unretirement.

* Wed Jul 13 2022 Fabio Valentini <decathorpe@gmail.com> 3.0.2-4
- Include upstream PR to support latest mutter / gala changes

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Fabio Valentini <decathorpe@gmail.com> 3.0.2-2
- Include upstream PR for mutter 42 / libmutter-10 support

* Wed Dec 22 2021 Fabio Valentini <decathorpe@gmail.com> 3.0.2-1
- Update to version 3.0.2; Fixes RHBZ#2034028

* Tue Sep 28 2021 Fabio Valentini <decathorpe@gmail.com> 3.0.1-1
- Update to version 3.0.1; Fixes RHBZ#2008349

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Fabio Valentini <decathorpe@gmail.com> - 3.0.0-1
- Update to version 3.0.0.

* Fri Feb 12 2021 Fabio Valentini <decathorpe@gmail.com> - 3.0.0-0.1.20210217.gitdb24c73
- Update to a wingpanel 3.0.0 pre-release snapshot at commit db24c73.
- Rebuilt for granite 6 soname bump.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.2-4
- Add patch for initial mutter 3.38 support.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.2-1
- Update to version 2.3.2.

* Fri May 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-3
- Obsolete the retired wingpanel-indicator-ayatana package.

* Mon Apr 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-2
- Rebuild for gala 3.3.0 and mutter 3.36.

* Mon Apr 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-1
- Update to version 2.3.1.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-2.20200313.git88305e0
- Bump to commit 88305e0.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Update to version 2.3.0.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6-1
- Update to version 2.2.6.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5-1
- Update to version 2.2.5.

* Wed Apr 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4-1
- Update to version 2.2.4.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.2.3-2
- Rebuild with Meson fix for #1699099

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3-1
- Update to version 2.2.3.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-1
- Update to version 2.2.2.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Update to version 2.2.1.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Sun Sep 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-4
- Rebuild for gala mutter328 support.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-2
- Add missing BR: gcc, gcc-c++.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-1
- Update to version 2.1.1.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Rebuild for granite5 soname bump.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-6
- Add patch to support and bump release for mutter 3.28.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-4
- Include upstream patch to fix undefined symbols.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-3
- Remove icon cache scriptlets, replaced by file triggers.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-2
- Rebuild for granite soname bump.

* Wed Sep 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-1
- Update to version 2.0.4.

* Mon Sep 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-5.20170902.git434f674
- Bump to commit 434f674, which includes fixes for the latest mutter.

* Sat Sep 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-4.20170901.git7a1a583
- Bump to commit 7a1a583, which includes support for the latest mutter.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Update to version 2.0.3.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-2
- Create and own missing settings directory.

* Fri Mar 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.
- Remove upstreamed patches.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-12
- Rebuild for new gala snapshot.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-10
- Add patch to fix pkgconfig file.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-9
- Create and own plugin directory.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-8
- Split off -libs subpackage.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-7
- Don't let COPYING be executable.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-6
- Clean up spec file.

* Thu Nov 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-5
- Add rpath workaround for f25.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-4
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Spec file cosmetics.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Update to version 0.4.

