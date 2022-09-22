%global uuid org.gabmus.%{name}

Name:           hydrapaper
Version:        3.2.0
Release:        5%{?dist}
Epoch:          1
Summary:        Set two different backgrounds for each monitor on GNOME

License:        GPLv3+
URL:            https://gitlab.com/gabmus/HydraPaper
Source0:        %{url}/-/archive/%{version}/HydraPaper-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libhandy-devel >= 0.90.0
BuildRequires:  meson >= 0.58.0
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.3.1
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0.0-0.5.alpha.3

Requires:       dbus-common
Requires:       glib2
Requires:       hicolor-icon-theme
Requires:       libadwaita >= 1.0.0-0.5.alpha.3
Requires:       libhandy >= 0.90.0
Requires:       python3-dbus
Requires:       python3-pillow

Patch0:         hydrapaper-fix-dbus-path.patch

%description
GTK utility to set two different backgrounds for each monitor on GNOME (which
lacks this feature).


%prep
%autosetup -n HydraPaper-%{version} -p1


%build
%meson \
%if 0%{?flatpak}
  -Denabledaemon=false
%endif

%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%if !0%{?flatpak}
%post
%systemd_user_post %{uuid}d.service

%preun
%systemd_user_preun %{uuid}d.service

%postun
%systemd_user_postun_with_restart %{uuid}d.service
%endif


%files -f %{name}.lang
%license COPYING LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%if !0%{?flatpak}
%{_libexecdir}/%{name}d
%endif
%{_mandir}/man1/*.1*
%{_metainfodir}/*.xml
%if !0%{?flatpak}
%{_userunitdir}/*.service
%endif
%{python3_sitelib}/%{name}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:3.2.0-4
- Rebuilt for Python 3.11

* Thu Apr 07 2022 Tomas Popela <tpopela@redhat.com> - 1:3.2.0-3
- Fix the dbus path for Flatpak builds

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1:3.2.0-1
- chore(update): 3.2.0

* Fri Oct 15 2021 Kalev Lember <klember@redhat.com> - 1:3.1.0-2
- Add missing python3-dbus requires
- Require libhandy instead of libhandy1

* Mon Sep 20 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1:3.1.0-1
- build(update): 3.1.0

* Sun Aug 15 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1:3.0.0-2
- fix: Bump for rebuild 3.0.0

* Sun Aug 15 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1:3.0.0-1
- build(update): 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1:2.0.3-4
- build(downgrade): 2.0.3 | rh#1975639

* Fri Jun 11 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.0-1
- build(update): 3.0.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.3-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.3-1
- build(update): 2.0.3

* Thu Oct 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.2-1
- build(update): 2.0.2

* Wed Sep 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Tue Sep  1 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0-1
- Update to 2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.12-1
- Update to 1.12
- Migrate to 'libhandy1'

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11-2
- Rebuilt for Python 3.9

* Wed May 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11-1
- Update to 1.11

* Sat Apr 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.10-1
- Update to 1.10

* Sat Mar 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.9-2
- Remove 'libwnck3'

* Sat Mar 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.9-1
- Update to 1.9.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Kalev Lember <klember@redhat.com> - 1.9.8-2
- Add missing libhandy requires

* Tue Dec 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.8-1
- Update to 1.9.8
- Minor spec file fixes

* Mon Sep 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.4-1
- Update to 1.9.4

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9-1
- Update to 1.9

* Wed Jul 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.3-1
- Initial package
