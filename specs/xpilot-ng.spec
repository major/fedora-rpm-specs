%global logwatch_root %{_datadir}/logwatch
%global logwatch_conf %{logwatch_root}/dist.conf
%global logwatch_scripts %{logwatch_root}/scripts

Name:           xpilot-ng
Version:        4.7.3
Release:        34%{?dist}
Summary:        Space arcade game for multiple players

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://xpilot.sourceforge.net
Source0:        http://downloads.sourceforge.net/sourceforge/xpilot/xpilot-ng-%{version}.tar.gz
Source1:        xpilot-ng.png
Source2:        xpilot-ng-sdl.desktop
Source3:        xpilot-ng-sdl.appdata.xml
Source4:        xpilot-ng-server.service
Source5:        xpilot-ng.sysconfig
Source6:        xpilot-ng.logrotate
Source10:       logwatch.logconf.xpilot
Source11:       logwatch.script.xpilot
Source12:       logwatch.serviceconf.xpilot
Source13:       logwatch.shared.applyxpilotdate
Source14:       xpilot-ng-server.metainfo.xml
Patch0:         xpilot-ng-4.7.2-scoreassert.patch
Patch1:         xpilot-ng-4.7.2-rhbz830640.patch
Patch2:         xpilot-ng-4.7.3-fix-alut-detect.patch
Patch3:         xpilot-ng-c99.patch
Patch4:         xpilot-ng-SDL_window.patch
Patch5:         xpilot-ng-c99-return-mismatch.patch
Patch6:         xpilot-ng-c99-incompatible-pointer-types.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  expat-devel SDL_ttf-devel SDL_image-devel zlib-devel
BuildRequires:  libXt-devel libGLU-devel
BuildRequires:  openal-soft-devel freealut-devel automake
Requires:       %{name}-data = %{version}-%{release} hicolor-icon-theme
Provides:       %{name}-engine = %{version}-%{release}

%description
A highly addictive, infinitely configurable multi-player space
arcade game.  You pilot a spaceship around space, dodging
obstacles, shooting players and bots, collecting power-ups, and
causing general mayhem.


%package x11
Summary:        Xpilot-ng X11 version
Requires:       %{name}-data = %{version}-%{release}
Provides:       %{name}-engine = %{version}-%{release}

%description x11
Version of %{name} which uses libX11 rather then SDL.


%package data
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release} dejavu-sans-fonts

%description data
Data files for %{name}.


%package server
Summary:        Server for hosting xpilot games
Requires:       %{name}-data = %{version}-%{release}
Requires:       logrotate
Requires(pre):  shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires:  systemd
Provides:       %{name}-engine = %{version}-%{release}
# Make sure the old no longer supported selinux policy from 4.7.2 gets removed
Obsoletes:      %{name}-selinux < %{version}-%{release}
Provides:       %{name}-selinux = %{version}-%{release}

%description server
The xpilot server.  This allows you to host xpilot games on your
computer and develop new xpilot maps.  This is required if you
are playing alone, but not required if you are joining one of the
public xpilot games hosted on the internet.


%package logwatch
Summary:        Logwatch scripts for the xpilot game server
Requires:       %{name}-server = %{version}-%{release} logwatch

%description logwatch
logwatch scripts for the Xpilot game server


%prep
%autosetup -p1
# regenerate autofoo files for patch2
autoreconf -ivf
# fixup textfile encodings
pushd doc/man
iconv --from=ISO-8859-1 --to=UTF-8 xpilot-ng-server.man > xpilot-ng-server.man.new
touch -r xpilot-ng-server.man xpilot-ng-server.man.new
mv xpilot-ng-server.man.new xpilot-ng-server.man

iconv --from=ISO-8859-1 --to=UTF-8 xpilot-ng-x11.man > xpilot-ng-x11.man.new
touch -r xpilot-ng-x11.man xpilot-ng-x11.man.new
mv xpilot-ng-x11.man.new xpilot-ng-x11.man
popd

iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new
touch -r AUTHORS AUTHORS.new
mv AUTHORS.new AUTHORS


%build
%configure --enable-sound
iconv --from=ISO-8859-1 --to=UTF-8 README -o README
touch -r README.in README
make %{?_smp_mflags}


%install
%make_install INSTALL="install -p"

# Drop old Python 2 only map conversion script
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/mapconvert.py

desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.xml

install -p -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT/lib/systemd/system/%{name}-server.service

# Copy certain configuration files to /etc so that they can be properly managed
# as config files.
install -p -D -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}-server-cmdline-opts
install -p -D -m 644 lib/defaults.txt $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/defaults.txt
install -p -D -m 600 lib/password.txt $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/password.txt

install -p -D -m 644 %{SOURCE6} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}-server

# Replace bundled fonts with system fonts

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/FreeSansBoldOblique.ttf
ln -s %{_datadir}/fonts/dejavu/DejaVuSans-BoldOblique.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/FreeSansBoldOblique.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/VeraMoBd.ttf
ln -s %{_datadir}/fonts/dejavu/DejaVuSansMono-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/VeraMoBd.ttf


# Install logwatch files
install -pD -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{logwatch_conf}/logfiles/%{name}.conf
install -pD -m 0644 %{SOURCE11} $RPM_BUILD_ROOT%{logwatch_scripts}/services/%{name}
install -pD -m 0644 %{SOURCE12} $RPM_BUILD_ROOT%{logwatch_conf}/services/%{name}.conf
install -pD -m 0644 %{SOURCE13} $RPM_BUILD_ROOT%{logwatch_scripts}/shared/applyxpilotdate

%pre server
getent group xpilot >/dev/null || groupadd -r xpilot
getent passwd xpilot >/dev/null || \
useradd -r -g xpilot -d %{_datadir}/%{name} -s /sbin/nologin \
    -c "xpilot game server" xpilot
exit 0

%post server
%systemd_post xpilot-ng-server.service

%preun server
%systemd_preun xpilot-ng-server.service

%postun server
%systemd_postun_with_restart xpilot-ng-server.service 


%files
%{_bindir}/xpilot-ng-replay
%{_bindir}/xpilot-ng-sdl
%{_datadir}/appdata/xpilot-ng-sdl.appdata.xml
%{_datadir}/applications/xpilot-ng-sdl.desktop
%{_datadir}/icons/hicolor/48x48/apps/xpilot-ng.png
%{_mandir}/man6/xpilot-ng-replay.6.gz
%{_mandir}/man6/xpilot-ng-sdl.6.gz

%files data
%doc AUTHORS BUGS ChangeLog FEATURES README TODO
%license COPYING
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/textures
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/sound

%files x11
%{_bindir}/xpilot-ng-x11
%{_mandir}/man6/xpilot-ng-x11.6.gz

%files server
%{_bindir}/xpilot-ng-xp-mapedit
%{_bindir}/xpilot-ng-server
/lib/systemd/system/xpilot-ng-server.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/textures
%exclude %{_datadir}/%{name}/fonts
%exclude %{_datadir}/%{name}/sound
%{_datadir}/appdata/xpilot-ng-server.metainfo.xml
%dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(0600,xpilot,root) %{_sysconfdir}/%{name}/password.txt
%config(noreplace) %{_sysconfdir}/%{name}/defaults.txt
%config(noreplace) %{_sysconfdir}/%{name}/xpilot-ng-server-cmdline-opts
%{_mandir}/man6/xpilot-ng-server.6.gz
%{_mandir}/man6/xpilot-ng-xp-mapedit.6.gz

%files logwatch
%{logwatch_conf}/logfiles/%{name}.conf
%{logwatch_conf}/services/%{name}.conf
%{logwatch_scripts}/services/%{name}
%{logwatch_scripts}/shared/applyxpilotdate


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.7.3-33
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Florian Weimer <fweimer@redhat.com> - 4.7.3-30
- Additional C compatibility fixes (#2155781)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Florian Weimer <fweimer@redhat.com> - 4.7.3-27
- C99 port (#2155781)
- Fix build issue due to SDL_Window identifier conflict with newer SDL

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Hans de Goede <hdegoede@redhat.com> - 4.7.3-19
- Drop libXxf86misc-devel BuildRequires, all #if HAVE_XF86MISC code was
  commented out already, so this does not influence xpilot-ng behavior
- Fix FTBFS (rhbz#1736985)
- Drop script for converting old format maps, because it is Python 2 only
- Fix a bunch of rpmlint warnings, ignore others

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Hans de Goede <hdegoede@redhat.com> - 4.7.3-17
- Fix FTBFS (rhbz#1676250)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.7.3-13
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Hans de Goede <hdegoede@redhat.com> - 4.7.3-8
- Enable sound support
- Use systemd-rpm macros (rhbz#850373)
- Split out client data in a -data package, share it between client and server
- Split out libX11 client version into a -x11 package, drop .desktop for it
- Add appdata

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 4.7.3-3
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Sun Jul 29 2012 Hans de Goede <hdegoede@redhat.com> - 4.7.3-2
- Move server cmdline config file to /etc/xpilot-ng, where all the other
  config-files are. You can now find it here:
  /etc/xpilot/xpilot-ng-server-cmdline-opts

* Sun Jul 29 2012 Hans de Goede <hdegoede@redhat.com> - 4.7.3-1
- Fix a crash in the welcome screen (rhbz#830640)
- Upgrade to latest upstream 4.7.3
- Drop selinux module, it no longer compiles and selinux support belongs
  in selinux-policy*, not in the apps themselves
- Replace sysv init script by a systemd unit file

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 25 2010 Wart <wart@kobold.org> - 4.7.2-19
- Replace bundled fonts with system fonts (BZ #477487)

* Fri Jan 15 2010 Hans de Goede <hdegoede@redhat.com> - 4.7.2-18
- Fix FTBFS (#511717)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 4.7.2-15
- Rebuild for Python 2.6

* Mon Feb 18 2008 Wart <wart at kobold.org>
- Better Sourceforge download URL

* Mon Feb 18 2008 Wart <wart at kobold.org> 4.7.2-14
- Rebuild for gcc 4.3

* Thu Aug 23 2007 Wart <wart at kobold.org> 4.7.2-13
- Minor selinux modifications for rawhide
- License tag clarification
- Fix version and category fields in .desktop files
- Use new user creation guidelines

* Fri Feb 23 2007 Wart <wart at kobold.org> 4.7.2-12
- Update logwatch script with a previously unknown log field

* Thu Feb 22 2007 Wart <wart at kobold.org> 4.7.2-11
- Add patch to prevent crash when running with robots not in idle mode
- Added logwatch files
- Switch from fedora-usermgmt to vanilla useradd

* Tue Aug 29 2006 Wart <wart at kobold.org> 4.7.2-10
- Added SELinux policies for the game server
- Don't attempt to create the xpilot user if it already exists
- Don't ghost the compiled python files anymore

* Mon Jul 17 2006 Wart <wart at kobold.org> 4.7.2-9
- Use the new xpilot user in the init.d script
- Add info on firewall configuration in the sysconfig script
- Explicitly disable reporting to the meta server (BZ #199164)
- Don't restart the server in %%postun unless it was already running.

* Tue Jul 11 2006 Wart <wart at kobold.org> 4.7.2-8
- Fix Requires: for the -server subpackage

* Wed Mar 1 2006 Wart <wart at kobold.org> 4.7.2-7
- Create an xpilot user for running the server daemon
- Fix typo in logrotate configuration file.

* Tue Feb 28 2006 Wart <wart at kobold.org> 4.7.2-6
- Added sysconfig and initrd files for starting xpilot server at boot time
- Add copies of customizable configuration files to /etc/xpilot
- More readable spacing in changelog
- Add missing ; in desktop file
- Added RPM_OPT_FLAGS to compile line

* Thu Feb 16 2006 Wart <wart at kobold.org> 4.7.2-5
- Rebuild for FC-5

* Mon Feb 6 2006 Wart <wart at kobold.org> 4.7.2-4
- Don't make duplicates of the doc files for the subpackage.
- Use version macro is source path
- Preserve timestamps when installing icons.

* Fri Feb 3 2006 Wart <wart at kobold.org> 4.7.2-3
- Add readme and license files to the server subpackage
- Set default file attributes for the server subpackage

* Fri Feb 3 2006 Wart <wart at kobold.org> 4.7.2-2
- Allow both packages to 0wn datadir/xpilot-ng
- Clean up non-utf8 man pages 

* Thu Feb 2 2006 Wart <wart at kobold.org> 4.7.2-1
- Initial submission to Fedora Extras
