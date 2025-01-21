Name:    sugar
Version: 0.121
Release: 5%{?dist}
Summary: Constructionist learning platform
URL:     http://sugarlabs.org/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later

Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Source1: activities.defaults

BuildRequires: make
BuildRequires: gcc
BuildRequires: dconf-devel
BuildRequires: gettext
BuildRequires: GConf2-devel
BuildRequires: gobject-introspection
BuildRequires: gtk3-devel
BuildRequires: gtksourceview3-devel
BuildRequires: intltool
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: python3-empy
# py-compile needs updating
BuildRequires: automake

Requires: avahi-tools
Requires: dbus-x11
Requires: dconf
Requires: ethtool
Requires: gnome-keyring-pam
Requires: gstreamer-plugins-espeak
Requires: gtksourceview3
Requires: gvfs
Requires: libwnck3
Requires: libxklavier
Requires: metacity
Requires: NetworkManager
Requires: openssh
Requires: polkit
Requires: python3-gwebsockets
Requires: sugar-artwork
Requires: sugar-toolkit-gtk3
Requires: telepathy-glib
Requires: telepathy-mission-control
Requires: telepathy-gabble
Requires: telepathy-salut
Requires: upower
Requires: webkit2gtk4.1
Requires: libsoup3
Requires: xdg-user-dirs

Obsoletes: sugar-base < 0.9.8-18
Provides: sugar-base

BuildArch: noarch

%description
Sugar provides simple yet powerful means of engaging young children in the 
world of learning that is opened up by computers and the Internet. With Sugar,
even the youngest learner will quickly become proficient in using the 
computer as a tool to engage in authentic problem-solving.  Sugar promotes 
sharing, collaborative learning, and reflection, developing skills that help 
them in all aspects of life. 

Sugar is also the learning environment for the One Laptop Per Child project. 
See http://www.laptop.org for more information on this project.

%package cp-all
Summary: All control panel modules 
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cp-background %{name}-cp-backup %{name}-cp-datetime 
Requires: %{name}-cp-frame %{name}-cp-language %{name}-cp-modemconfiguration
Requires: %{name}-cp-network %{name}-cp-keyboard %{name}-cp-webaccount 
Requires: %{name}-cp-updater

%description cp-all
This is a meta package to install all Sugar Control Panel modules

%package cp-background
Summary: Sugar Background control panel
Requires: %{name} = %{version}-%{release}

%description cp-background
This is the Sugar control panel to change the background

%package cp-backup
Summary: Sugar Backup control panel
Requires: %{name} = %{version}-%{release}

%description cp-backup
This is the Sugar control panel to backup and restore the Journal

%package cp-datetime
Summary: Sugar Date and Time control panel
Requires: %{name} = %{version}-%{release}

%description cp-datetime
This is the Sugar Date and Time settings control panel

%package cp-frame
Summary: Sugar Frame control panel
Requires: %{name} = %{version}-%{release}

%description cp-frame
This is the Sugar Frame settings control panel

%package cp-keyboard
Summary: Sugar Keyboard control panel
Requires: %{name} = %{version}-%{release}

%description cp-keyboard
This is the Sugar Keyboard settings control panel

%package cp-language
Summary: Sugar Language control panel
Requires: %{name} = %{version}-%{release}

%description cp-language
This is the Sugar Language settings control panel

%package cp-modemconfiguration
Summary: Sugar Modem configuration control panel
Requires: %{name} = %{version}-%{release}
Requires: mobile-broadband-provider-info

%description cp-modemconfiguration
This is the Sugar Modem configuration control panel

%package cp-network
Summary: Sugar Network control panel
Requires: %{name} = %{version}-%{release}

%description cp-network
This is the Sugar Network settings control panel

%package cp-power
Summary: Sugar Power control panel
Requires: %{name} = %{version}-%{release}

%description cp-power
This is the Sugar Power settings control panel

%package cp-updater
Summary: Sugar Activity Update control panel
Requires: %{name} = %{version}-%{release}

%description cp-updater
This is the Sugar Activity Updates control panel

%package cp-webaccount
Summary: Sugar Web Account control panel
Requires: %{name} = %{version}-%{release}

%description cp-webaccount
This is the Sugar Web Account control panel


%prep
%autosetup -p1

%build
autoreconf
ls -1 %{_datadir}/automake-*/py-compile | sort | \
	tail -n 1 | while read f
do
	cp -p $f .
done
%configure
%make_build

%install
%make_install
mkdir %{buildroot}/%{_datadir}/sugar/activities
rm -rf %{buildroot}/%{_datadir}/sugar/extensions/cpsection/__pycache__/
install -p %{SOURCE1} %{buildroot}%{_datadir}/sugar/data/activities.defaults

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/sugar/
%py_byte_compile %{python3} %{buildroot}%{python3_sitelib}/jarabe/

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%config %{_sysconfdir}/dbus-1/system.d/nm-user-settings.conf
%{_bindir}/sugar*
%{_datadir}/glib-2.0/schemas/org.sugarlabs.gschema.xml
%{_datadir}/mime/packages/sugar.xml
%{_datadir}/xsessions/sugar.desktop

%{python3_sitelib}/jarabe/

%dir %{_datadir}/sugar
%dir %{_datadir}/sugar/activities
%dir %{_datadir}/sugar/extensions
%dir %{_datadir}/sugar/extensions/cpsection

%{_datadir}/sugar/data
%{_datadir}/sugar/data/activities.defaults
%{_datadir}/sugar/extensions/deviceicon
%{_datadir}/sugar/extensions/globalkey
%{_datadir}/sugar/extensions/webservice
%{_datadir}/sugar/extensions/cpsection/*.py*
%{_datadir}/sugar/extensions/cpsection/aboutcomputer
%{_datadir}/sugar/extensions/cpsection/aboutme
%exclude %{_datadir}/sugar/extensions/cpsection/[b-z]*
%{_datadir}/polkit-1/actions/org.sugar.*.policy
%{_datadir}/sugar/extensions/cpsection/__pycache__/

%files cp-all

%files cp-background
%{_datadir}/sugar/extensions/cpsection/background

%files cp-backup
%{_datadir}/sugar/extensions/cpsection/backup

%files cp-datetime
%{_datadir}/sugar/extensions/cpsection/datetime

%files cp-frame
%{_datadir}/sugar/extensions/cpsection/frame

%files cp-keyboard
%{_datadir}/sugar/extensions/cpsection/keyboard

%files cp-language
%{_datadir}/sugar/extensions/cpsection/language

%files cp-modemconfiguration
%{_datadir}/sugar/extensions/cpsection/modemconfiguration

%files cp-network
%{_datadir}/sugar/extensions/cpsection/network

%files cp-power
%{_datadir}/sugar/extensions/cpsection/power

%files cp-updater
%{_datadir}/sugar/extensions/cpsection/updater

%files cp-webaccount
%{_datadir}/sugar/extensions/cpsection/webaccount

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.121-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.121-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.121-2
- Rebuilt for Python 3.13

* Tue Feb 06 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.121-1
- New Release 0.121

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.120-5
- Update py-compile for python 3.12, imp module removed

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.120-3
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 21 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.120-1
- New Release 0.120

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.119-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.119-2
- Rebuilt for Python 3.11

* Fri May 27 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.119-1
- Change release

* Fri May 27 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.119-1
- New Release 0.119

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.118-4
- Rebuilt for Python 3.10

* Wed Feb 10 2021 Alexander Perez <aperez@sugarlabs.org> - 0.118-3
- Fix broken Language control panel

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 0.118-1
- Update to 0.118 release

* Thu Jan 21 2021 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 0.116-10
- Add patches that fix collaboration failure, patches will be removed when
  package is updated to 0.118.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.116-7
- Rebuilt for Python 3.9

* Wed Mar 18 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 0.116-6
- Update sugar-0.116-config-empy-fix.patch
- Add sugar-fix-hang-on-make.patch

* Tue Mar 03 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 0.116-5
- Add patch for SSID handling

* Tue Feb 18 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.116-4
- Ship the activities.defaults in the sugar package

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Adam Williamson <awilliam@redhat.com> - 0.116-2
- Replace python3-telepathy dep with telepathy-glib per upstream

* Sat Nov 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-1
- Update to 0.116 release

* Wed Aug 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.114-1
- Update to 0.114 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.113-3
- Drop unnessary python-unversioned-command

* Mon Apr 22 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.113-2
- Further fix for collaboration

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.113-1
- Update to sugar 0.113 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.112-5
- Fix Network Control panel

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.112-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.112-1
- Upgrade to sugar 0.112 stable release

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.110.0-6
- Run autoreconf so new files are installed (fixes rhbz 1490668)

* Fri Aug 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.110.0-5
- Add a build-time dependency on python2-devel

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.110.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.110.0-3
- Add patch to drop WebKitGtk3 requirements

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.110.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.110.0-1
- Upgrade to sugar 0.110.0 stable release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Mar  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.1-1
- Sugar 0.108.1 stable release

* Sat Feb 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.0-1
- Sugar 0.108.0 stable release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.2-1
- Sugar 0.107.2 devel release

* Mon Jan 4  2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.1-1
- Sugar 0.107.1 devel release

* Fri Nov 27 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.0-1
- Sugar 0.107.0 devel release

* Tue Jul  7 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.106.0-1
- Sugar 0.106.0 stable release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.105.2-1
- Sugar 0.105.2 development release

* Tue May 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.105.1-1
- Sugar 0.105.1 development release

* Tue Mar 10 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.1-1
- Sugar 0.104.1 stable release

* Mon Mar  9 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.0-2
- Explicitly require telepathy-gabble and telepathy-salut

* Sat Feb 14 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.0-1
- Sugar 0.104.0 stable release

* Sat Jan 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.2-1
- New upstream 0.103.2 development release

* Thu Dec 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.1-1
- New upstream 0.103.1 development release

* Thu Nov 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.0-1
- New upstream 0.103.0 development release

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 0.102.0-4
- update/optimize mime scriptlet

* Thu Sep 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-3
- Add mobile provider dep to the modem control panel

* Tue Aug 12 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-2
- Add new backup control panel
- Add dependency on dconf

* Wed Jul  2 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-1
- Sugar 0.102.0 stable release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.7-1
- 0.101.7 devel release

* Sun Apr 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.6-1
- 0.101.6 devel release

* Thu Mar 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.5-1
- 0.101.5 devel release

* Sun Mar  9 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.4-1
- 0.101.4 devel release

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.3-1
- 0.101.3 devel release

* Tue Feb  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.1-2
- Compile GSettings schemas

* Mon Jan 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.1-1
- 0.101.1 devel release

* Sun Dec  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.0-1
- 0.101.0 devel release

* Fri Nov 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.2-1
- Sugar 0.100.2 stable release

* Fri Nov  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.1-1
- Sugar 0.100.1 stable release

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.4-1
- 0.99.4 devel release

* Sat Aug 10 2013 Daniel Drake <dsd@laptop.org> 0.99.1-3
- Add dependency on libxklavier, used via gobject-introspection

* Mon Aug  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-2
- Add dependency on gwebsockets for webservices

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Thu Jul 11 2013 Daniel Drake <dsd@laptop.org> 0.99.0-2
- Remove dependencies not required by Sugar shell

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release
- Trim changelog

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.8-2
- Update default control panels

* Fri May 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.8-1
- Sugar 0.98.8 stable release

* Fri Apr 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.7-1
- Sugar 0.98.7 stable release

* Fri Mar 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.6-1
- Sugar 0.98.6 stable release

* Fri Mar  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.5-1
- Sugar 0.98.5 stable release

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.4-1
- Sugar 0.98.4 stable release

* Fri Dec 21 2012 Simon Schampijer <simon@laptop.org> - 0.98.3-1
- Sugar 0.98.3 stable release

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.2-1
- Sugar 0.98.2 stable release

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.0 stable release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.13-1
- 0.97.13 devel release

* Sat Nov 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.12-1
- 0.97.12 devel release 

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.11-1
- 0.97.11 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.10-1
- 0.97.10 devel release

* Thu Oct 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.9-1
- 0.97.9 devel release

* Tue Oct 16 2012 Daniel Drake <dsd@laptop.org> 0.97.8-1
- 0.97.8 devel release

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.7-1
- 0.97.7 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.6-1
- 0.97.6 devel release

* Thu Oct  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.5-2
- Split out Control Panels to sub packages
- Update gnome-keyring patch. RHBZ 862581
- Add patch to update build dependencies

* Thu Sep 27 2012 Daniel Drake <dsd@laptop.org> - 0.97.5-1
- New development release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.4-1
- New development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.2-1
- 0.97.2 devel release

* Tue Aug 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.1 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Tue Jun  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-2
- Add patch to create gnome keyring if it doesn't exist

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.7-1
- devel release 0.95.7

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.6-1
- devel release 0.95.6

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.5-1
- devel release 0.95.5

* Tue Mar  6 2012 Daniel Drake <dsd@laptop.org> - 0.95.4-2
- Add dependency on sugar-toolkit-gtk3 (needed to launch activities)

* Thu Feb  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.4-1
- devel release 0.95.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-3
- Drop premature sugar-base obsoletion

* Thu Dec 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-2
- Obsolete sugar-base

* Wed Dec 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Wed Nov 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-1
- devel release 0.95.2

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1
