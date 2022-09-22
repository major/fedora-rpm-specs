%global xfceversion 4.16

Name:           xfce4-session
Version:        4.16.0
Release:        6%{?dist}
Summary:        Xfce session manager

License:        GPLv2+
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfce4-session
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
# Add a xfce-mimeapps.list to allow setting mime handlers for Xfce apps

Source2:        xfce-mimeapps.list
# Patch startxfce4 to keep it on the same vty for logind
# https://bugzilla.redhat.com/show_bug.cgi?id=1117682
Patch1:         xfce-session-4.10-startxfce4.patch

BuildRequires: make
BuildRequires:  dbus-devel >= 1.1.0
BuildRequires:  dbus-glib-devel >= 0.84
BuildRequires:  glib2-devel >= 2.24.0
BuildRequires:  libSM-devel
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  startup-notification-devel
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  iceauth xrdb xset
# Build tools
BuildRequires:  desktop-file-utils
BuildRequires:  gettext 
BuildRequires:  intltool
BuildRequires:  libxslt
#BuildRequires:  libxml2
BuildRequires:  systemd-devel >= 195
BuildRequires:  polkit-devel
BuildRequires:  libtool
Requires:       iceauth xrdb xset
Requires:       xfce-polkit >= 0.2-2
Requires:       systemd >= 195
# Needed for exo desktop preferred applications
Requires:       exo
# Need this to pull in the right imsettings in groupinstalls
# See https://bugzilla.redhat.com/show_bug.cgi?id=1349743
Suggests:       imsettings-xfce

Obsoletes:      xfce-utils < 4.8.3-7.fc18

# splash screens no longer exists
Obsoletes:      xfce4-session-engines <= 4.13.1
Obsoletes:      xfce4-session-devel <= 4.13.3

%description
xfce4-session is the session manager for the Xfce desktop environment.

%prep
%autosetup -p1

%build
%configure --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install

# remove xscreensaver autostart file
rm -fr %{buildroot}%{_sysconfdir}/xdg/autostart/xscreensaver.desktop

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

# install our xfce-mimeapps.list file to set mime handlers
mkdir -p %{buildroot}%{_datadir}/applications
cp -a %{SOURCE2} %{buildroot}%{_datadir}/applications/xfce-mimeapps.list

%files -f %{name}.lang
%license COPYING
%doc AUTHORS BUGS ChangeLog NEWS TODO
%doc doc/FAQ doc/NEWS.pre-4.3 doc/README.Kiosk
%{_sysconfdir}/xdg/xfce4
%{_bindir}/*
%dir %{_libdir}/xfce4/session/
%{_libdir}/xfce4/session/xfsm-shutdown-helper
%{_datadir}/applications/*.desktop
%{_datadir}/applications/xfce-mimeapps.list
%{_datadir}/xsessions/xfce.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/polkit-1/actions/org.xfce.session.policy
%{_mandir}/man1/*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-3
- Drop xscreensaver autostart since we are using xfce4-screensaver (Fixes #1957658)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 4.14.2-2
- {Build,}Require iceauth xrdb xset, not xorg-x11-server-utils

* Sun Mar 29 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.14.2-1
- Update to 4.14.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.14.1-1
- Update to 4.14.1

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.14.0-1
- Update to 4.14.0
- Update startxfce4 patch

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.4-2
- Drop -devel subpackage

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.4-1
- Update to 4.13.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.3-1
- Update to 4.13.3

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.2-2
- Drop -engines subpackages (splash screens are gone)

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.2-1
- Update to 4.13.2
- Drop patch no longer needed

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Dan Horák <dan[at]danny.cz> - 4.13.1-22
- Add support for xfce4-screensaver

* Thu Jan 17 2019 Dan Horák <dan[at]danny.cz> - 4.13.1-21
- Drop unused BR

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.1-20
- Update to 4.13.1
- drop upstreamed xflock4 patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.1-14
- Change BR:gnome-keyring-devel to libgnome-keyring-devel

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 25 2016 Kevin Fenzi <kevin@scrye.com> - 4.12.1-9
- Add a Suggests imsettings-xfce to workaround dnf issue. Bug #1349743

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 08 2015 Kevin Fenzi <kevin@scrye.com> - 4.12.1-7
- Drop patch for gnome-polkit so we can switch to xfce-polkit

* Sat Sep 12 2015 Kevin Fenzi <kevin@scrye.com> 4.12.1-6
- Adjust xfce-mimeapps.list to use exo for preferred applications. Fixes bug #1256442

* Sat Aug 08 2015 Kevin Fenzi <kevin@scrye.com> 4.12.1-5
- Add xfce-mimeapps.list file to handle mapping mime types to Xfce apps when running Xfce.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Kevin Fenzi <kevin@scrye.com> 4.12.1-3
- Actually apply the patch. :( 

* Sun Mar 29 2015 Kevin Fenzi <kevin@scrye.com> 4.12.1-2
- Add patch for xflock4 to look for an use a user defined screen locker in xfconf
- Fixes bug #1166227

* Mon Mar 16 2015 Kevin Fenzi <kevin@scrye.com> 4.12.1-1
- Update to 4.12.1

* Sun Mar 15 2015 Kevin Fenzi <kevin@scrye.com> 4.12.0-2
- Rebuild with fixed libxfce4ui for glade path issue

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.0-1
- Update to stable release 4.12.0

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 4.10.1-8
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Oct 08 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.10.1-7
- Add patch for fixing bashisms. Fixes bug 1150207

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Kevin Fenzi <kevin@scrye.com> 4.10.1-5
- Add patch to handle running startxfce4 from console. Fixes bug #1117682
- Thanks poma for patch.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 05 2013 Kevin Fenzi <kevin@scrye.com> 4.10.1-3
- Add patch for better systemd support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 05 2013 Kevin Fenzi <kevin@scrye.com> 4.10.1-1
- Update to 4.10.1, drop upstreamed patches. 

* Sat Apr 27 2013 Kevin Fenzi <kevin@scrye.com> 4.10.0-8
- Add upstream patches to hopefully fix crashes with glib2. 
- Fixes bug #891113 #865539

* Fri Mar 29 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-7
- more systemd-login1 love (+suspend/hibernate)

* Fri Feb 22 2013 Kevin Fenzi <kevin@scrye.com> 4.10.0-6
- Add patch for systemd-logind support. 

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 30 2012 Kevin Fenzi <kevin@scrye.com> 4.10.0-4
- Add upstream commit to fix session saves with 2 or more apps that ask to save. 
- https://bugzilla.xfce.org/show_bug.cgi?id=5379

* Fri Sep 14 2012 Kevin Fenzi <kevin@scrye.com> 4.10.0-3
- Drop fortune-mod. No longer used in 4.10. Fixes bug #857404

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-1
- Update to 4.10.0 final
- Make build verbose
- Add VCS key

* Fri Apr 20 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.2-1
- Update to 4.9.2 

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.1-1
- Update to 4.9.1 (Xfce 4.10pre2)

* Tue Apr 03 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.0-1
- Update to 4.9.0

* Sun Feb 12 2012 Kevin Fenzi <kevin@scrye.com> - 4.8.3-1
- Update to 4.8.3 and drop upstreamed gobject link patch.

* Wed Feb 01 2012 Kevin Fenzi <kevin@scrye.com> - 4.8.2-3
- Add patch to link with gobject. 

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.2-1
- Update to 4.8.2
- Remove gdmlang.patch and hostname.patch, both upstream

* Wed Jul 27 2011 Kevin Fenzi <kevin@scrye.com> - 4.8.1-5
- Add patch for hostname issue. Fixes bug #706563

* Sat Apr 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.1-4
- Autostart polkit-gnome-authentication-agent-1 (#693152)
- Remove --enable-gen-doc configure option as it requires network access

* Thu Mar 10 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.1-3
- Add patch to fix LANG handling with new gdm. Fixes #683941

* Tue Feb 15 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.1-2
- Fix versioning of the devel package's requirements
 
* Mon Feb 14 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.1-1
- Update to 4.8.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.0-1
- Update to 4.8.0

* Sun Jan 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3

* Fri Dec 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Mon Nov 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.1-1
- Update to 4.7.1

* Sun Sep 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0

* Fri May 21 2010 Kevin Fenzi <kevin@tummy.com> - 4.6.2-1
- Update to 4.6.2

* Thu Dec 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-5
- Remove libtool archives of splash engines

* Wed Nov 11 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.1-4
- Don't own /usr/share/themes (fixes #534107)

* Wed Sep 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-3
- Fix German text in logout dialog
- Fix shadows in 'simple' splash engine
- Don't ship static lib in -devel package
- configure with --disable-static instead of removing *.a files
- Fix directory ownership issue

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 19 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.1-1
- Update to 4.6.1

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.0-1
- Update to 4.6.0
- Remove some unneeded BuildRequires

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.99.1-1
- Update to 4.5.99.1

* Tue Jan 13 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.93-1
- Update to 4.5.93

* Fri Dec 26 2008 Kevin Fenzi <kevin@tummy.com> - 4.5.92-1
- Update 4.5.92

* Mon Aug 11 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-4
- Fix icon for autostarted applications (fixes #442804)

* Tue Apr 22 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-3
- Disable tips by default for now. 

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-2
- Rebuild for gcc43

* Sun Nov 18 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.2-1
- Update to 4.4.2

* Mon Aug 27 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-2
- Update License tag

* Wed Apr 11 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-1
- Update to 4.4.1
- Own the themes and themes/Default directories. 

* Tue Apr  3 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.0-2
- Own some unowned directories
- Add Requires: redhat-menus for directory ownership

* Sun Jan 21 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.0-1
- Update to 4.4.0

* Mon Nov 27 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.2-2
- Add dbus-devel and GConf2-devel to BuildRequires, fixes bug #217082

* Fri Nov 10 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.2-1
- Update to 4.3.99.2

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-6
- Fix defattr
- Add gtk-update-icon-cache

* Wed Oct  4 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-5
- Bump release for devel checkin

* Sun Sep 24 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-4
- Don't own doc directories that xfdesktop owns. 

* Sun Sep 17 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-3
- Only own icons, not any of the icon dirs. 

* Tue Sep 12 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-2
- Add Requires for fortune-mod, needed for xfce4-tips

* Sun Sep  3 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-1
- Upgrade to 4.3.99.1
- Fix macros in changelog
- Add post/postun ldconfig

* Wed Jul 12 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.2-1
- Upgrade to 4.3.90.2

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 4.2.3-3.fc5
- Rebuild for fc5

* Tue Jan 31 2006 Kevin Fenzi <kevin@tummy.com> - 4.2.3-2.fc5
- Added xorg-x11-server-utils, imake, libXt-devel BuildRequires
- Added xorg-x11-server-utils to Requires

* Mon Nov  7 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.3-1.fc5
- Update to 4.2.3
- Added dist tag

* Tue May 17 2005 Kevin Fenzi <kevin@tummy.com> 4.2.2-1.fc4
- Update to 4.2.2

* Sun May  8 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-5.fc4
- Add xorg-x11 buildrequires for iceauth check in configure

* Fri Mar 25 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-4.fc4
- lowercase Release

* Wed Mar 23 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-3.FC4
- Removed unneeded la/a files
- Added version to requires in devel and engine subpackages

* Sun Mar 20 2005 Warren Togami <wtogami@redhat.com> - 4.2.1-2
- fix BuildReqs

* Tue Mar 15 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-1
- Updated to 4.2.1 version

* Tue Mar  8 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.0-2
- Fixed to use %%find_lang
- Removed generic INSTALL from %%doc

* Sun Mar  6 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.0-1
- Inital Fedora Extras version

