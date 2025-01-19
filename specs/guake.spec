Name:           guake
Version:        3.7.0
Release:        21%{?dist}
Summary:        Drop-down terminal for GNOME

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://guake-project.org/
Source0:        https://github.com/guake/guake/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  %{py3_dist pbr}
BuildRequires:  gettext
BuildRequires:  gnome-common
BuildRequires:  make
BuildRequires:  glib2
BuildRequires:  desktop-file-utils

Requires:       python3 >= 3.5
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       %{py3_dist pbr}
Requires:       keybinder3
Requires:       libwnck3
Requires:       libnotify
Requires:       vte291 >= 0.42

Recommends:     libutempter

%description
Guake is a dropdown terminal made for the GNOME desktop environment. Guake's
style of window is based on an FPS game, and one of its goals is to be easy to
reach.

%prep
%setup -q

sed -i -e 's|PREFIX?=/usr/local|PREFIX?=/usr|' Makefile
sed -i -e 's|update-desktop-database|true|' Makefile

%build
%make_build

%install
PBR_VERSION=%{version} %make_install prefix=%{_prefix}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-prefs.desktop

rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%find_lang %{name}

%files -f %{name}.lang
%doc README.rst NEWS.rst
%license COPYING
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}*egg-info/
%{_bindir}/%{name}
%{_bindir}/%{name}-toggle
%{_datadir}/applications/%{name}-prefs.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.guake.gschema.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.7.0-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.7.0-18
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.7.0-14
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.7.0-11
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.7.0-8
- Rebuilt for Python 3.10

* Tue Feb 02 2021 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.7.0-1
- Update to 3.7.0 upstream

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-2
- Rebuilt for Python 3.8

* Sat Aug 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.6.3-1
- Update to 3.6.3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.8-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.8.8-1
- Update to 0.8.8

* Mon Aug 29 2016 Oliver Haessler <oliver@redhat.com> - 0.8.7-1
- Update to 0.8.7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Oliver Haessler <oliver@redhat.com> - 0.8.5-1
- Update to 0.8.5

* Thu Apr 14 2016 Oliver Haessler <oliver@redhat.com> - 0.8.4-1
- Update to 0.8.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.8.3-1
- Update to 0.8.3
- Drop the two patches we had added, they are now merged

* Wed Oct 21 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.8.1-1
- Update to 0.8.1
- Backport upstream patch to fix the size of the tab bar
- Backport upstream patch fixing recovering from full-screen mode

* Fri Aug 14 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.8.0-1
- Update to 0.8.0
- Drop merged patch
- Add R and BR to python-keybinder
- Convert the package to noarch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Oliver Haessler <oliver@redhat.com> - 0.7.2-2
- added fix for missing default value in /schemas/apps/guake/general/debug_mode
rhbz#1227382

* Wed May 20 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.2-1
- Update to 0.7.2

* Sun Apr 19 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6.0-1
- Update to upstream's 0.6.0

* Tue Jan 20 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.5.2-1
- Update to upstream's 0.5.2
- Backport patch from upstream to fix resizing the window with the mouse

* Tue Sep 09 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.5.0-3
- Update to the official 0.5.0 as upstream re-tagged it...

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.5.0-1
- Update to 0.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-11
- Remove the Fix-focus-issue-on-gnome-shell patch which seems no longer needed

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 21 2013 Ralph Bean <rbean@redhat.com> - 0.4.4-9
- Patch to include bpython and ipython as interpreters.

* Mon Feb 25 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-8
- Replace the Requires on notification-daemon by a Requires on desktop-notification-daemon

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-6
- Let's be a little more brutal in our killall since we know the guilty guy

* Fri Nov 02 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-5
- Add patch to handle the selection of url/link correctly

* Thu Aug 02 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-4
- Fix indentation in the patch 3

* Wed Aug 01 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-3
- Add patch to allow os.kill(pid, signal.SIGTERM) to fails

* Fri Jul 27 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-2
- Re-add the fix notification patch

* Fri Jul 27 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-1
- Update to 0.4.4
- Clean a little bit the spec according to new guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.3-3
- Add patch to fix the focus issue: RHBZ#828243 - Guake Trac #436

* Tue Jun 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.3-2
- Temporary fix for the globalhotkeys

* Fri Jun 08 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.3-1
- Update to 0.4.3
- Add Requires: notification-daemon
- Drops patches

* Mon Feb 27 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.2-7
- Fix notifications for non-GNOME DE not having the right library RHBZ#710586

* Sat Jan 14 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.2-6
- Fix FTBFS by remove some includes in the file keybinder.c

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.2-4
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 pingou <pingou@pingoured.fr> - 0.4.2-2
- Fix 626303 (import of port from proxy as int and not as string)

* Tue Aug 03 2010 pingou <pingou@pingoured.fr> - 0.4.2-1
- Update to 0.4.2

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat May 08 2010 pingou <pingou@pingoured.fr> - 0.4.1-4
- Change the name.schema to name for the gconf macro

* Sat May 08 2010 pingou <pingou@pingoured.fr> - 0.4.1-3
- Use the gconf_schema macro instead of the former code
- Add the posttrans part

* Thu Feb 04 2010 pingou <pingou@pingoured.fr> - 0.4.1-2
- Rebuild to include French translations

* Tue Feb 02 2010 pingou <pingou@pingoured.fr> - 0.4.1-1
- Update to 0.4.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 pingou <pingou@pingoured.fr> - 0.4.0-1
- Update to version 0.4.0

* Sat Mar 21 2009 pingou <pingou@pingoured.fr> - 0.3.1-10.20090321git
- New version from git

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-9.20090210git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 pingou <pingou@pingoured.fr> - 0.3.1-8.20090210git
- Correct setup -n

* Tue Feb 10 2009 pingou <pingou@pingoured.fr> - 0.3.1-7.20090210git
- Correct typo in the release number

* Tue Feb 10 2009 pingou <pingou@pingoured.fr> - 0.3.1-6.20090210git
- Add a .desktop file for the preferences (see: http://trac.guake-terminal.org/ticket/86 )
- New version from git
- Correct the tab

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.1-5
- Rebuild for Python 2.6

* Wed Nov 26 2008 pingou <pingou@pingoured.fr> - 0.3.1-4
- Quick and dirty trick before upstream patch

* Thu Nov 20 2008 pingou <pingou@pingoured.fr> - 0.3.1-3
- Correct the Source0

* Mon Aug 25 2008 pingou <pingou@pingoured.fr> - 0.3.1-2
- Add pygtk2 >= 2.10 in the BR

* Mon Aug 25 2008 pingou <pingou@pingoured.fr> - 0.3.1-1
- New owner
- New upstream release 0.3.1

* Thu Jul 10 2008  <lokthare@gmail.com> - 0.2.2-5
- Remove NEWS from the doc
- Add dbus-python in Requires

* Tue Jul  1 2008  <lokthare@gmail.com> - 0.2.2-4
- Add BR for GConf
- Fix schemas file

* Sun Jun  8 2008 Jean-François Martin <lokthare@gmail.com> 0.2.2-3
- Don't own /etc/gconf/schemas/
- Don't replace /etc/gconf/schemas/guake.schemas config file
- Remove globalhotkeys.la

* Fri Jun  6 2008 Jean-François Martin <lokthare@gmail.com> 0.2.2-2
- Fix gconf schema install
- Disable static library

* Wed Jun  4 2008 Jean-François Martin <lokthare@gmail.com> 0.2.2-1
- Initial release
