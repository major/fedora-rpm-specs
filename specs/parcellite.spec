# Review: https://bugzilla.redhat.com/show_bug.cgi?id=442473

Name:           parcellite
Version:        1.2.6
Release:        6%{?dist}
Summary:        A lightweight GTK+ clipboard manager

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://%{name}.sf.net/
Source0:        https://github.com/ZaWertun/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# migrate autostart from previous upstream rickyrockrat
Source1:        %{name}-startup.desktop

BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-g++
BuildRequires:  gtk2-devel >= 2.10.0 
BuildRequires:  desktop-file-utils
BuildRequires:  intltool >= 0.23

Requires:       xdotool
Requires:       hicolor-icon-theme

%description
Parcellite is a stripped down, basic-features-only clipboard manager with a 
small memory footprint for those who like simplicity.

In GNOME and Xfce the clipboard manager will be started automatically. For 
other desktops or window managers you should also install a panel with a 
system tray or notification area if you want to use this package.


%prep
%autosetup -n%{name}-%{version}

%build
%cmake
%make_build -C %{_vpath_builddir}

%install
%make_install -C %{_vpath_builddir}
%find_lang %{name}
desktop-file-edit \
    --remove-category=Application \
    --remove-only-show-in=Old \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install \
    --add-category=TrayIcon \
    --add-only-show-in="GNOME;KDE;LXDE;MATE;Razor;ROX;TDE;Unity;XFCE;" \
    --dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
    %{SOURCE1}
install -D data/%{name}.appdata.xml %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.6-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 Raphael Groner <raphgro@fedoraproject.org> - 1.2.6-1
- new version

* Tue Aug 01 2023 Raphael Groner <raphgro@fedoraproject.org> - 1.2.5-2
- install appdata 

* Tue Aug 01 2023 Raphael Groner <raphgro@fedoraproject.org> - 1.2.5-1
- new version, switch upstream

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 Raphael Groner <raphgro@fedoraproject.org> - 1.2.2-2
- enable debuginfo

* Tue Apr 11 2023 Raphael Groner <raphgro@fedoraproject.org> - 1.2.2-1
- bump version, fix security issue#79

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- Update to 1.2.1 (#1116593)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.7-2
- Add 6 upstream patches to fix three segfaults (#1038899 is one of them),
  case-sensitive search, search-as-you-type and updates Russian translations

* Wed Oct 16 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7 (#1019649)

* Sun Aug 04 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6 (#991766, fixes and #989098)
- Remove upstreamed patch for German translation

* Thu Jul 25 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.5-2
- Fix typo in German translation

* Wed Jul 24 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5 (#987384, fixes #919693 and #919696)
- Remove upstreamed or unnecessary patches

* Tue May 14 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.4-3
- Fix desktop vendor conditionals
- Add aarch64 support (#926310)

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 1.1.4-2
- Drop desktop vendor tag.

* Sun Jan 27 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4
- Update de-po.patch

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.3.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.2-0.2.rc5
- Don't ship prebuilt binaries (#800644)
- Fix build error with glib2 >= 2.30

* Sat Mar 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.2-0.1.rc5
- Update to 1.0.2 RC5 (#730240)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.2-2
- Add patch to fix DSO linking (#565054)

* Fri Jan 01 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1
- Remove both patches as all fixes got upstreamed

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.9-1
- Update to 0.9
- Fix Control+Click behaviour
- Small corrections to German translation

* Sat Apr 19 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.8-1
- Update to 0.8

* Sat Apr 19 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.7-2
- No longer require lxpanel
- Preserve timestamps during install
- Include NEWS in doc

* Sat Apr 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.7-1
- Initial Fedora RPM
