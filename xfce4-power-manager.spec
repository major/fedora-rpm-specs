%global xfceversion 4.16

Name:		xfce4-power-manager
Version:	4.16.0
Release:	6%{?dist}
Summary:	Power management for the Xfce desktop environment

License:	GPLv2+
URL:		http://goodies.xfce.org/projects/applications/%{name}
#VCS: git:git://git.xfce.org/xfce/xfce4-power-manager
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Source1:	%{name}.xml
# https://gitlab.xfce.org/xfce/xfce4-power-manager/-/commit/fcc9bbe3d58265360a47348f42703a359839cda7
Patch0:		xfce4-power-manager-4.16.0-inhibit-dpms.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfceversion}
BuildRequires:  pkgconfig(dbus-1) >= 0.60
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.70
BuildRequires:  pkgconfig(libnotify) >= 0.4.1
BuildRequires:  pkgconfig(xrandr) >= 1.2.0
BuildRequires:  xorg-x11-proto-devel >= 1.0.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  upower-devel
BuildRequires:  libappstream-glib

Requires:       xfce4-panel >= %{xfceversion}
Requires:       polkit
Requires:       upower >= 0.99

%description
Xfce Power Manager uses the information and facilities provided by HAL to 
display icons and handle user callbacks in an interactive Xfce session.
Xfce Power Preferences allows authorised users to set policy and change 
preferences.


%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# install xfpm default config
mkdir -p %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
cp -p %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/

%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-settings.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/%{name}.xml
%{_bindir}/%{name}
%{_bindir}/%{name}-settings
%{_sbindir}/xfce4-pm-helper
%{_metainfodir}/%{name}.appdata.xml
%{_libdir}/xfce4/panel/plugins/libxfce4powermanager.so
%{_datadir}/xfce4/panel/plugins/power-manager-plugin.desktop
%{_sbindir}/xfpm-power-backlight-helper
%config %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%doc
%{_mandir}/man1/%{name}-settings.1.*
%{_mandir}/man1/%{name}.1.*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 07 2022 Dan Horák <dan[at]danny.cz> - 4.16.0-5
- inhibit DPMS when getting power inhibit request

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.6-1
- Update to 1.6.6

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.5-1
- Update to 1.6.5

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.4-1
- Update to 1.6.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.3-1
- Update to 1.6.3

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2
- Fix appdata installation

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.1-20
- Rebuild for xfce version 4.13

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1
- Drop upstreamed patches

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 01 2016 poma <poma@gmail.com> - 1.6.0-4
- Fix startup delay and systray menu lag - rhbz #1339335

* Thu May 26 2016 Kevin Fenzi <kevin@scrye.com> - 1.6.0-3
- Do not show in MATE. Fixes bug #1318642

* Sun Mar 20 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.0-2
- Spec file cleanup

* Sat Mar 19 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.0-1
- Update to v1.6.0
- drop all upstreamed patches
- Minor spec file clean up

* Tue Mar 08 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.5.2-6
- Fix slow shutdown, Fixes #1310871

* Thu Feb 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.2-5
- Add default config for xfpm

* Mon Feb 08 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.2-4
- Fix broken brightness indicator
- Fix slider adjust crash

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Kevin Fenzi <kevin@scrye.com> 1.5.2-1
- Update to 1.5.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0
- Dependencies bumped: upower >=0.99, libxfce4ui-2

* Sun Mar 22 2015 Kevin Fenzi <kevin@scrye.com> 1.4.4-1
- Update to 1.4.4

* Mon Mar 02 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.3-2
- Added patch to fix xfpm panel plugin crashes in non-UTF8 locale

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.4.2-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Dec 01 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2 - bugfix release
- removed patches from src rpm
- removed clean section in the spec

* Wed Oct 01 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.1-3
- Fix spec file errors and missing dependencies

* Tue Sep 30 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.1-2
- disable patch not needed

* Tue Sep 30 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.1-1
- Updated to latest upstream version
- changes made to files to accomodate changes in new version

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 13 2013 Kevin Fenzi <kevin@scrye.com> 1.2.0-8
- Add patch to use systemd methods for suspend/hibernate instead of upower. 
- Upsteam bug: https://bugzilla.xfce.org/show_bug.cgi?id=9963

* Thu Mar 21 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-7
- Make inhibit patch conditional >= F18 only

* Thu Mar 21 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-6
- Fix crash through buggy locales (#754585, #921966)

* Fri Feb 22 2013 Kevin Fenzi <kevin@scrye.com> 1.2.0-5
- Add patch to inhibit systemd from doing power management when we are running. 

* Sun Feb 17 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-4
- Require upower and udisks (#890680)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (Xfce 4.10 final)

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 1.1.0-1
- Update to 1.1.0 (Xfce 4.10pre2)

* Tue Apr 03 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.11-1
- Update to 1.0.11

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 10 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.10-2
- Fix crash in brightness management (#736727 and #736964)
- Fix expanding of battery icon after resume (#765726)
- No longer depend on xfce4-doc (#721291)
- Include various patches from GIT
- Update translations from transifex

* Sun Feb 20 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 04 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- No longer require hal because the brightness backend was removed
- Require polkit

* Sun Dec 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Thu Dec 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1-0.1-1
- Update to 1.0.1 on Xfce 4.8 pre2

* Sat Nov 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5
- Fix for libnotify 0.7.0
- Make build verbose

* Sat Nov 21 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.4.2-1
- Update to 0.8.4.2

* Mon Nov 02 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.4.1-1
- Update to 0.8.4.1

* Tue Sep 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4
- Drop xfpm_session_set_client_id patch, fixed upstream

* Wed Sep 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.3.1-2
- Fix segfault in xfpm_session_set_client_id

* Sun Aug 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.3.1-1
- Update to 0.8.3.1

* Sat Aug 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3

* Thu Jul 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-3
- Patch to include dpmsconst.h instead of dpms.h

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Mon Jul 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1.1-1
- Update to 0.8.1.1

* Fri Jul 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
- Drop libglade2 requirement

* Wed Jun 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0 final
- Update gtk-icon-cache scriptlets

* Wed May 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-0.3.RC2
- Update to 0.8.0RC2

* Tue Apr 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-0.3.RC1
- Update to 0.8.0RC1

* Mon Apr 13 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-0.2.beta2
- Update to 0.8.0beta2
- Drop xfpm-button-hal.patch, no longer necessary

* Mon Apr 13 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-0.2.beta1
- Add xfpm-button-hal.patch by Mike Massonnet

* Sun Apr 12 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-0.1.beta1
- Update to 0.8.0beta1

* Thu Apr 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-0.1.alpha2
- Update to 0.8.0alpha2

* Thu Apr 02 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-0.1.alpha
- Update to 0.8.0alpha 

* Tue Mar 24 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5
- Remove custom autostart file

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Sat Feb  7 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1
- Include additional desktop file for autostarting the app

* Mon Nov 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-0.1.RC1
- Update to 0.6.0 RC1

* Fri Oct 31 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-0.1.0.beta1
- Initial Fedora package
