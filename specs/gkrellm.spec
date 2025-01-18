%global _hardened_build 1

Name:           gkrellm
Version:        2.3.11
Release:        19%{?dist}
Summary:        Multiple stacked system monitors in one process
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.gkrellm.net/
Source0:        http://gkrellm.srcbox.net/releases/%{name}-%{version}.tar.bz2
Source1:        gkrellmd.service
Source2:        gkrellm.desktop
Source3:        gkrellm.png
Source4:        gnome-gkrellm.appdata.xml
Source5:        make-git-snapshot.sh
Patch1:         gkrellm-2.3.5-config.patch
Patch2:         gkrellm-2.2.4-sansfont.patch
Patch3:         gkrellm-2.2.7-width.patch
# Debian patches from https://sources.debian.org/patches/gkrellm/2.3.10-2/
Patch10:        04_fix_manpage_hyphen.patch
Patch11:        05_bts437033_fix_strip.patch
Patch12:        10_fix_glib_underlinkage.patch
BuildRequires:  gcc
BuildRequires:  gtk2-devel openssl-devel libSM-devel desktop-file-utils gettext
BuildRequires:  lm_sensors-devel libntlm-devel libappstream-glib
%if 0%{?fedora} >= 41
Requires:       gdk-pixbuf2-modules-extra%{?_isa}
%endif

%description
GKrellM charts CPU, load, Disk, and all active net interfaces
automatically.  An on/off button and online timer for the PPP
interface is provided, as well as monitors for memory and swap usage,
file system, internet connections, APM laptop battery, mbox style
mailboxes, and temperature sensors on supported systems.  Also
included is an uptime monitor, a hostname label, and a clock/calendar.
Additional features are:

  * Autoscaling grid lines with configurable grid line resolution.
  * LED indicators for the net interfaces.
  * A gui popup for configuration of chart sizes and resolutions.


%package daemon
Summary:        The GNU Krell Monitors Server
# systemd >= 186 for scriptlet macros
BuildRequires:  systemd >= 186
BuildRequires: make
Requires(pre):  shadow-utils systemd
Requires(post,preun,postun): systemd


%description daemon
gkrellmd listens for connections from gkrellm clients. When a gkrellm
client connects to a gkrellmd server all builtin monitors collect their
data from the server.


%package        devel
Summary:        Development files for the GNU Krell Monitors
Requires:       gtk2-devel%{?_isa}

%description devel
Development files for the GNU Krell Monitors.


%prep
%autosetup -p1

for i in gkrellmd.1 gkrellm.1 README Changelog Changelog-plugins.html \
    src/gkrellm.h server/gkrellmd.h; do
   sed -i -e "s@/usr/lib/gkrellm2*/plugins@%{_libdir}/gkrellm2/plugins@" $i
   sed -i -e "s@/usr/local/lib/gkrellm2*/plugins@/usr/local/%{_lib}/gkrellm2/plugins@" $i
done


%build
make %{?_smp_mflags} INSTALLROOT=%{_prefix} PKGCONFIGDIR=%{_libdir}/pkgconfig \
  INCLUDEDIR=%{_includedir} CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" \
  LDFLAGS="$RPM_LD_FLAGS"


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gkrellm2/themes
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

make install \
    LOCALEDIR=$RPM_BUILD_ROOT%{_datadir}/locale \
    INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} \
    SINSTALLDIR=$RPM_BUILD_ROOT%{_sbindir} \
    MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    PKGCONFIGDIR=$RPM_BUILD_ROOT%{_libdir}/pkgconfig \
    INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/gkrellmd.service
install -Dpm 644 server/gkrellmd.conf \
    $RPM_BUILD_ROOT%{_sysconfdir}/gkrellmd.conf
%find_lang %name

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor gnome             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/gnome-%{name}.appdata.xml

%pre daemon
getent group gkrellmd >/dev/null || groupadd -r gkrellmd
getent passwd gkrellmd >/dev/null || \
useradd -r -g gkrellmd -M -d / -s /sbin/nologin -c "GNU Krell daemon" gkrellmd
:

%post daemon
%systemd_post gkrellmd.service

%preun daemon
%systemd_preun gkrellmd.service

%postun daemon
%systemd_postun_with_restart gkrellmd.service


%files -f %{name}.lang
%license COPYRIGHT
%doc Changelog README Themes.html
%{_bindir}/%{name}
%{_libdir}/gkrellm2
%{_datadir}/gkrellm2
%{_mandir}/man1/%{name}.1*
%{_datadir}/appdata/gnome-%{name}.appdata.xml
%{_datadir}/applications/gnome-%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files devel
%license %{_licensedir}/%{name}*
%{_includedir}/gkrellm2
%{_libdir}/pkgconfig/%{name}.pc

%files daemon
%license %{_licensedir}/%{name}*
%{_unitdir}/gkrellmd.service
%{_sbindir}/gkrellmd
%{_mandir}/man1/gkrellmd.*
%config(noreplace) %{_sysconfdir}/gkrellmd.conf


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Kevin Fenzi <kevin@scrye.com> - 2.3.11-18
- Rebuild for new libntlm soname bump.

* Fri Jul 26 2024 Benjamin Gilbert <bgilbert@backtick.net> - 2.3.11-17
- Require gdk-pixbuf2-modules-extra on F41+ to fix crash (rhbz#2276464)

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.11-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.3.11-8
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.11-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 2019 Adam Goode <adam@spicenitz.org> - 2.3.11-1
- Update to 2.3.11 (#1742316)
- Include Debian patches directly instead of via source

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.10-7
- Drop old sys-v mingration bits

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.3.10-1
- Update to 2.3.10

* Wed Oct 12 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.3.9-1
- Update to 2.3.9

* Thu Sep  8 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.3.8-1
- Update to 2.3.8

* Thu Jul 14 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.3.7-2
- Patch to fix gkrellm.pc (#1356479)
- Optimize gkrellm.png with zopflipng

* Sat Jun  4 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.3.7-1
- Update to 2.3.7
- Make gkrellmd.conf noreplace again

* Fri Feb 26 2016 Hans de Goede <hdegoede@redhat.com> - 2.3.6-0.1.rc1.git20160226
- Update to a 2.3.6-rc git snapshot for misc. fixes (inspired by Debian)
- Add a bunch of patches from Debian
- Add appdata

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct  9 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-23
- Mark COPYRIGHT as %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-20
- Start daemon after lm_sensors (#1117750, DaveG)
- Specfile cleanups

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-18
- Patch daemon to allow binding to a listen address that doesn't exist yet.
- Use systemd macros in scriptlets (#850128).

* Tue Dec 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-17
- Run icon through optipng (#1047215).

* Wed Dec 11 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-16
- Use main package's doc dir for -devel and -daemon.

* Fri Dec  6 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-15
- Fix build with -Werror=format-security (#1037086).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Feb  8 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-12
- Systemd unit: add Documentation, remove obsolete After=syslog.target.
- Fix bogus dates in %%changelog.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-10
- Build with hardening flags on.

* Sun Jan 15 2012 Hans de Goede <hdegoede@redhat.com> - 2.3.5-8
- Explicitly link against gmodule-2.0 to fix building with latest glib

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 13 2011 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-7
- Build with $RPM_LD_FLAGS.
- Clean up specfile stuff no longer needed with Fedora or EL6+.

* Mon Jun 20 2011 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-5
- Migrate daemon to systemd (#661656).
- Do icon dir timestamp update in %%post with lua.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Hans de Goede <hdegoede@redhat.com> - 2.3.5-3
- Add COPYRIGHT file to -devel and -daemon sub-packages

* Sun Oct 24 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.3.5-2
- Add StartupNotify and StartupWMClass to gkrellm.desktop.

* Sun Oct 10 2010 Hans de Goede <hdegoede@redhat.com> 2.3.5-1
- New upstream release 2.3.5

* Mon Jun 21 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.3.4-3
- Make -devel gtk2-devel dependency ISA qualified.

* Sun Feb 14 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.3.4-2
- Fix build with --no-add-needed (#564850).
- Fix plugin dir defaults in installed headers.
- Build with NTLM support.

* Tue Jan  5 2010 Hans de Goede <hdegoede@redhat.com> 2.3.4-1
- New upstream release 2.3.4

* Tue Dec 22 2009 Hans de Goede <hdegoede@redhat.com> 2.3.3-1
- New upstream release 2.3.3
- Fixes the gkrellm client crash when the gkrellm server reboots (#545327)
- Drop a number of upstreamed patches

* Sun Dec 20 2009 Hans de Goede <hdegoede@redhat.com> 2.3.2-8
- Don't crash on laptops with dead batteries (#545987)
- Don't crash with transparent themes (#549005)

* Fri Nov 27 2009 Hans de Goede <hdegoede@redhat.com> 2.3.2-7
- Fix crash when using multiple simap/spop mailboxes (#541824)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.3.2-6
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.3.2-4
- Sync icon cache update scriptlets with current Fedora guidelines.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> 2.3.2-2
- rebuild with new openssl

* Thu Oct 23 2008 Hans de Goede <hdegoede@redhat.com> 2.3.2-1
- New upstream release 2.3.2
- Drop upstreamed memleak patch

* Thu Oct  2 2008 Hans de Goede <hdegoede@redhat.com> 2.3.1-6
- Fix a small memory leak (which would accumulate over time) thanks to
  Daniel Colascione for the patch (rh 464040)

* Wed Sep 10 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.1-5
- Build against openssl instead of gnutls-openssl fixing symbol conflicts when
  using pam_ldap (which uses openssl), this fixes rh 446860

* Wed Jun 25 2008 Tomas Mraz <tmraz@redhat.com> 2.3.1-4
- rebuild with new gnutls

* Wed Feb 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.1-3
- Fix building with latest glibc
- Rebuild for gcc 4.3

* Tue Dec  4 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.3.1-2
- Clean up desktop-file-utils 0.14 warnings.

* Mon Dec  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.1-1
- New upstream release 2.3.1
- Drop upstreamed gnutls and lm_sensors-3.0.0 patches

* Wed Oct 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.0-5
- Add support for lm_sensors-3.0.0

* Wed Sep  5 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.3.0-4
- Rewrite gkrellmd init script: better LSB compliance, hddtemp
  interoperability, avoidance of X error messages, general cleanup.

* Tue Sep  4 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.3.0-3
- Fix gnutls detection/build and use it instead of openssl.
- Sync user and group creation with current Fedora guidelines.

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.0-2
- Update License tag for new Licensing Guidelines compliance

* Sun Jul 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.0-1
- New upstream release 2.3.0

* Fri Jul 20 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.10-3
- Rebuild, including libsensors support on ppc and ppc64 as lm_sensors is
  available there now.

* Wed Nov  8 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.10-2
- Add special case for via 686 volt sensors <sigh> (bug 213304)

* Tue Oct 31 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.10-1
- New upstream release 2.2.10
- Drop integrated lmsensors and sysfs sensors patches

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.2.9-10
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.9-9
- Fixup .desktop so that gkrellm actually gets shown in the menu (bz 206775)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.9-8
- FE6 Rebuild

* Sun Jul 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.9-7
- Add -r to groupadd
- Add || : to the gkrellmd service related scripts (deviation from the wiki).
- Don't make -devel package require the main one as it doesn't need it
- Install .desktop file with --vendor gnome to not break existing kde panel
  buttons, etc.
- Drop "StartupNotify=false" from .desktop to not interfere with kde's
  internal startup notification
- use gkrellmd as group in default gkrellmd.conf

* Sat Jul 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.9-6
- Various specfile improvements by Ville Skyttä (ville.skytta@iki.fi)
- Make the daemon package scripts match the ScriptletSnippets wiki page
- Add LSB aliases (try-restart, force-reload) to the -daemon initscript
- Add %%{?dist} to the release for consistency with other packages I maintain

* Sat Jul 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.9-5
- Remove Obsoletes/Provides gkrellm-server
- Don't remove user on uninstall
- Only build with lm_sensors support on x86 / x86_64 since lm_sensors is not
  available on other archs.
- Use %%{_sysconfdir} instead of /etc in %%install

* Fri Jul  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.2.9-4
- Moving to Fedora Extras, initial FE submission
- Various specfile improvements / cleanups
- Remove gkrellm-wireless (will be submitted as a separate package)
- Use libsensors instead of DIY code to read lm_sensors sensors
- Don't strip the binaries when installing so we get a usable -debuginfo rpm

* Mon May 22 2006 Karsten Hopp <karsten@redhat.de> 2.2.9-3
- fix libdir patch

* Mon May 15 2006 Karsten Hopp <karsten@redhat.de> 2.2.9-2
- fix header file conflict between 32bit and 64bit archs

* Mon Apr 03 2006 Karsten Hopp <karsten@redhat.de> 2.2.9-1
- update to 2.2.9
- remove explicit UID/GUIs from useradd/groupadd (#186974)

* Tue Feb 28 2006 Karsten Hopp <karsten@redhat.de> 2.2.7-7
- BuildRequires: libSM-devel

* Wed Feb 15 2006 Karsten Hopp <karsten@redhat.de> 2.2.7-6
- fix chkconfig requires

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2.7-5.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2.7-5.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 18 2005 Bill Nottingham <notting@redhat.com> 2.2.7-5
- Fix references to obsolete /usr/X11R6 path

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> 2.2.7-4
- rebuilt with new openssl

* Tue Sep 06 2005 Karsten Hopp <karsten@redhat.de> 2.2.7-3
- fix path to gkrellm2 plugins on 64bit archs (#164066)

* Thu Aug 18 2005 Florian La Roche <laroche@redhat.com>
- the the kernel dep form a Requires: into a Conflicts:

* Thu Jun 09 2005 Karsten Hopp <karsten@redhat.de> 2.2.7-1
- update to 2.2.7
- add Requires: /sbin/chkconfig for -daemon subpackage
- allow gkrellm width up to 1600 pixel
- change spec file to valid UTF-8 (#159578)

* Tue May 17 2005 Karsten Hopp <karsten@redhat.de> 2.2.4-5
- use Sans fonts (Ville Skytta, #157899)

* Fri Apr 01 2005 Karsten Hopp <karsten@redhat.de> 2.2.4-4
- Include gkrellm2/plugins directories (Michael Schwendt)
  #153073

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 2.2.4-3
- build with gcc-4

* Thu Feb 03 2005 Karsten Hopp <karsten@redhat.de> 2.2.4-2
- BuildRequires openssl-devel (#137548)

* Tue Nov 16 2004 Karsten Hopp <karsten@redhat.de> 2.2.4-1
- update

* Mon Sep 06 2004 Karsten Hopp <karsten@redhat.de> 2.2.2-2
- change group of wireless subpackage (#131699)
- add icon

* Tue Aug 03 2004 Karsten Hopp <karsten@redhat.de> 2.2.2-1
- update to 2.2.2 to fix pixbuf memory leak

* Wed Jun 23 2004 Karsten Hopp <karsten@redhat.de> 2.2.1-1
- update to latest stable release

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 31 2004 Warren Togami <wtogami@redhat.com> 2.2.0-1
- upgrade to 2.2.0
- #123846 bogus dep
- Cleanup deps, build deps, and docs

* Mon Mar 15 2004 Karsten Hopp <karsten@redhat.de> 2.1.28-3
- remove Provides: gkrellm-devel from main package (#117105)

* Thu Mar 11 2004 Karsten Hopp <karsten@redhat.de> 2.1.28-2
- don't run gkrellmd as nobody, use a unique UID (#116314)
- fix chkconfig at package removal

* Wed Mar 10 2004 Karsten Hopp <karsten@redhat.de> 2.1.28-1
- update
- add runlevel links with chkconfig (#107481)
- use slightly patched config file from the tarball for gkrellmd
- add wireless plugin

* Wed Mar 03 2004 Karsten Hopp <karsten@redhat.de> 2.1.26-2
- fix -devel provision (#117105)
- remove stringfreeze hack

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Karsten Hopp <karsten@redhat.de> 2.1.26-1
- update to 2.1.26, which fixes sensor data being 10x to high (#115850)
- requires kernel >= 2.6.2

* Sat Feb 21 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- mv /etc/init.d -> /etc/rc.d/init.d

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 09 2004 Karsten Hopp <karsten@redhat.de> 2.1.24-1
- update to 2.1.24

* Mon Oct 13 2003 Karsten Hopp <karsten@redhat.de> 2.1.21-1
- update:
- fix temperature reads from /proc/acpi
- Use username instead of userid in session management userid property.
  Fixes no session restarts in KDE 3.1.4.
- de.po update

* Thu Oct 09 2003 Karsten Hopp <karsten@redhat.de> 2.1.20-3
- make it compatible with 3d party packages

* Thu Oct 09 2003 Karsten Hopp <karsten@redhat.de> 2.1.20-2
- added patches from Ville Skyttä <ville.skytta@iki.fi>:
  - Add icon for desktop entry
  - Install daemon in %%{_sbindir}
  - Include themes and plugins dirs in main package
  - Make -daemon obsolete -server
  - devel subpackage (disabled because of string freeze)


* Wed Oct 08 2003 Karsten Hopp <karsten@redhat.de> 2.1.20-1
- update to make it work with kernel 2.6

* Wed Oct 01 2003 Karsten Hopp <karsten@redhat.de> 2.1.19-1
- Update to 2.1.19, includes fix for #106073

* Tue Jul 08 2003 Karsten Hopp <karsten@redhat.de> 2.1.14-3
- run as user nobody
- fix file ownership

* Mon Jul 07 2003 Karsten Hopp <karsten@redhat.de> 2.1.14-2
- add init script and config file for gkrellmd
- daemon subpackage
- fix pkgconfig file

* Thu Jun 26 2003 Karsten Hopp <karsten@redhat.de> 2.1.14-1
- update to fix buffer overflow in gkrellmd_client_read

* Wed Jun 18 2003 Karsten Hopp <karsten@redhat.de> 2.1.13-1
- update

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 05 2003 Karsten Hopp <karsten@redhat.de> 2.1.9-2
- rebuild

* Thu Apr 10 2003 Karsten Hopp <karsten@redhat.de> 2.1.9-1
- update to 2.1.9
- daily/weekly/monthly transfer stats

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 14 2003 Karsten Hopp <karsten@redhat.de> 2.1.5-2
- rename menu entry (#81876)

* Sun Jan 12 2003 Karsten Hopp <karsten@redhat.de> 2.1.5-1
- update (#81620)

* Mon Dec 16 2002 Tim Powers <timp@redhat.com> 2.1.3-2
- rebuild

* Wed Dec 11 2002 Karsten Hopp <karsten@redhat.de>
- 2.1.3-1
- Battery monitor can display multiple batteries
- Net timer lost the minutes display with large connect times
- use disk stats from /proc/partitions if available

* Tue Dec 03 2002 Karsten Hopp <karsten@redhat.de> 2.1.2-1
- updated translations
- .desktop file (#78562)
- minor bugfixes

* Mon Nov 11 2002 Karsten Hopp <karsten@redhat.de>
- update to 2.1 (glib2, gtk2)

* Wed Jul 17 2002 Karsten Hopp <karsten@redhat.de>
- update
- own /usr/include/gkrellm directory

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Karsten Hopp <karsten@redhat.de>
- Update to 1.2.11

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Feb 27 2002 Karsten Hopp <karsten@redhat.de>
- Update to 1.2.9

* Wed Jan 23 2002 Karsten Hopp <karsten@redhat.de>
- Update to 1.2.6

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Dec 13 2001 Karsten Hopp <karsten@redhat.de>
- update to 1.2.5-1
- nls patch not required anymore

* Mon Nov 26 2001 Karsten Hopp <karsten@redhat.de>
- enable nls

* Mon Nov 26 2001 Karsten Hopp <karsten@redhat.de>
- update to 1.2.4

* Fri Jul  6 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Add %%defattr
- langify
- Don't define name, ver and rel at the top of the spec file

* Wed Jun 27 2001 Karsten Hopp <karsten@redhat.de>
- fix _mandir
- fix BuildRequires

* Wed Jun 27 2001 SATO Satoru <ssato@redhat.com>
- clean up (use system-defined macros)
- enable NLS

* Wed Mar 14 2001 Rob Lineweaver <rbline@wm.edu>
- fixed new manpage inclusion for newer RPM versions
- source is 1.0.7
- compiled for PPC and i386

* Fri Jan 19 2001 Kevin Ford <klford@uitsg.com>
- general cleanup of spec file

* Thu Jan 18 2001 Kevin Ford <klford@uitsg.com>
- Updated spec file to work with both v3 & v4 rpm
- moved changelog to bottom of spec file
- added defines for common items

* Thu Apr 6 2000 Bill Wilson
- added INCLUDEDIR to the make install

* Fri Oct 29 1999 Gary Thomas <gdt@linuxppc.org>
- .spec file still broken

* Thu Oct 7 1999 David Mihm <davemann@ionet.net>
- fixed spec.
