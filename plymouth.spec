Summary: Graphical Boot Animation and Logger
Name: plymouth
Version: 22.02.122
Release: 3%{?dist}
License: GPLv2+
URL: http://www.freedesktop.org/wiki/Software/Plymouth

Source0: https://gitlab.freedesktop.org/plymouth/plymouth/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source2: charge.plymouth

# Patches cherry-picked from upstream git
Patch1:  0001-drm-Retry-setting-scanout-buffer-on-failure.patch
Patch2:  0002-Add-support-for-CSI-sequences.patch
Patch3:  0003-ply-utils-Reintroduce-ply_string_has_prefix-helper.patch
Patch4:  0004-ply-device-manager-Treat-SimpleDRM-drm-devices-as-fb.patch
Patch5:  0005-ply-device-manager-Move-verify_drm_device-higher-up-.patch
Patch6:  0006-ply-device-manager-Also-ignore-SimpleDRM-devs-in-col.patch

BuildRequires: make
BuildRequires: gcc libtool git
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libudev)
BuildRequires: kernel-headers
BuildRequires: libpng-devel
BuildRequires: libxslt, docbook-style-xsl
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pango-devel >= 1.21.0
BuildRequires: cairo-devel
BuildRequires: gettext-devel
BuildRequires: intltool
# for /usr/bin/systemd-tty-ask-password-agent
BuildRequires: systemd
# for _unitdir macro
BuildRequires: systemd-rpm-macros

Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-scripts = %{version}-%{release}
Suggests: logrotate

%description
Plymouth provides an attractive graphical boot animation in
place of the text messages that normally get shown.  Text
messages are instead redirected to a log file for viewing
after boot.


%package system-theme
Summary: Plymouth default theme
Requires: plymouth(system-theme) = %{version}-%{release}

%description system-theme
This meta-package tracks the current distribution default theme.


%package core-libs
Summary: Plymouth core libraries

%description core-libs
This package contains the core libraries used by Plymouth.


%package graphics-libs
Summary: Plymouth graphics libraries
Requires: %{name}-core-libs = %{version}-%{release}
Requires: system-logos

%description graphics-libs
This package contains the libraries used by graphical Plymouth splashes.


%package devel
Summary: Libraries and headers for writing Plymouth splash plugins
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the libraries and headers needed to develop
3rd party splash plugins for Plymouth.


%package scripts
Summary: Plymouth related scripts
Requires: findutils, coreutils, gzip, cpio, dracut
Requires: %{name} = %{version}-%{release}

%description scripts
This package contains scripts that help integrate Plymouth with
the system.


%package plugin-label
Summary: Plymouth label plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}

%description plugin-label
This package contains the label control plugin for Plymouth.
It provides the ability to render text on graphical boot splashes.


%package plugin-script
Summary: Plymouth "script" plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}

%description plugin-script
This package contains the "script" boot splash plugin for
Plymouth. It features an extensible boot splash language that
allows writing new plugins as scripts, simplifying the process
of designing custom boot splash themes.


%package plugin-fade-throbber
Summary: Plymouth "Fade-Throbber" plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.


%package plugin-space-flares
Summary: Plymouth "space-flares" plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
Requires: plymouth-plugin-label = %{version}-%{release}

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.


%package plugin-two-step
Summary: Plymouth "two-step" plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
Requires: plymouth-plugin-label = %{version}-%{release}
# Spinifinity like themes should now use two-step instead of throbgress
# No provides, the throbgress plugin has been removed upstream
Obsoletes: %{name}-plugin-throbgress < %{version}-%{release}

%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.


%package theme-charge
Summary: Plymouth "Charge" plugin
Requires: %{name}-plugin-two-step = %{version}-%{release}
Requires: fedora-logos-classic
Requires(post): plymouth-scripts

%description theme-charge
This package contains the "charge" boot splash theme for
Plymouth. It features the shadowy hull of a Fedora logo charge up and
and finally burst into full form.


%package theme-fade-in
Summary: Plymouth "Fade-In" theme
Requires: %{name}-plugin-fade-throbber = %{version}-%{release}
Requires(post): plymouth-scripts

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for
Plymouth. It features a centered logo that fades in and out
while stars twinkle around the logo during system boot up.


%package theme-script
Summary: Plymouth "Script" plugin
Requires: %{name}-plugin-script = %{version}-%{release}
Requires(post): plymouth-scripts

%description theme-script
This package contains the "script" boot splash theme for
Plymouth. It it is a simple example theme the uses the "script"
plugin.


%package theme-solar
Summary: Plymouth "Solar" theme
Requires: %{name}-plugin-space-flares = %{version}-%{release}
Requires(post): plymouth-scripts

%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.


%package theme-spinfinity
Summary: Plymouth "Spinfinity" theme
Requires: %{name}-plugin-two-step = %{version}-%{release}
Requires(post): plymouth-scripts

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for
Plymouth. It features a centered logo and animated spinner that
spins in the shape of an infinity sign.


%package theme-spinner
Summary: Plymouth "Spinner" theme
Requires: %{name}-plugin-two-step = %{version}-%{release}
Requires: font(cantarell) font(cantarelllight)
Requires(post): plymouth-scripts
Provides: plymouth(system-theme) = %{version}-%{release}

%description theme-spinner
This package contains the "spinner" boot splash theme for
Plymouth. It features a small spinner on a dark background.


%prep
%autosetup -p1
autoreconf --install --symlink -Wno-portability
# Change the default theme
sed -i -e 's/spinner/bgrt/g' src/plymouthd.defaults


%build
%configure --enable-tracing                                      \
           --with-logo=%{_datadir}/pixmaps/system-logo-white.png \
           --with-background-start-color-stop=0x0073B3           \
           --with-background-end-color-stop=0x00457E             \
           --with-background-color=0x3391cd                      \
           --with-runtimedir=/run                                \
           --disable-gdm-transition                              \
           --enable-systemd-integration                          \
           --without-system-root-install                         \
           --without-rhgb-compat-link
%make_build


%install
%make_install
%find_lang %{name}
find $RPM_BUILD_ROOT -name '*.la' -delete

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth

# Add charge, our old default
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
cp $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow/{box,bullet,entry,lock}.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge

# Drop glow, it's not very Fedora-y
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow


%ldconfig_scriptlets core-libs

%ldconfig_scriptlets graphics-libs

%postun theme-charge
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "charge" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun theme-fade-in
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "fade-in" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun theme-solar
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "solar" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun theme-spinfinity
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "spinfinity" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%post theme-spinner
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
# On upgrades replace charge with the new bgrt default
if [ $1 -eq 2 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "charge" ]; then
        %{_sbindir}/plymouth-set-default-theme bgrt
    fi
fi

%postun theme-spinner
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "bgrt" -o \
         "$(%{_sbindir}/plymouth-set-default-theme)" == "spinner" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi


%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%dir %{_libexecdir}/plymouth
%dir %{_localstatedir}/lib/plymouth
%dir %{_libdir}/plymouth/renderers
%dir %{_sysconfdir}/plymouth
%config(noreplace) %{_sysconfdir}/plymouth/plymouthd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/bootlog
%{_sbindir}/plymouthd
%{_libexecdir}/plymouth/plymouthd-fd-escrow
%{_bindir}/plymouth
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/text.so
%{_libdir}/plymouth/tribar.so
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{_datadir}/plymouth/themes/tribar/tribar.plymouth
%{_datadir}/plymouth/plymouthd.defaults
%{_localstatedir}/spool/plymouth
%{_mandir}/man?/*
%ghost %verify(not mode) %{_localstatedir}/lib/plymouth/boot-duration
%{_unitdir}/

%files devel
%{_libdir}/libply.so
%{_libdir}/libply-splash-core.so
%{_libdir}/libply-boot-client.so
%{_libdir}/libply-splash-graphics.so
%{_libdir}/pkgconfig/ply-splash-core.pc
%{_libdir}/pkgconfig/ply-splash-graphics.pc
%{_libdir}/pkgconfig/ply-boot-client.pc
%{_libdir}/plymouth/renderers/x11*
%{_includedir}/plymouth-1

%files core-libs
%{_libdir}/libply.so.*
%{_libdir}/libply-splash-core.so.*
%{_libdir}/libply-boot-client.so.*
%dir %{_libdir}/plymouth

%files graphics-libs
%{_libdir}/libply-splash-graphics.so.*
%{_libdir}/plymouth/renderers/drm*
%{_libdir}/plymouth/renderers/frame-buffer*

%files scripts
%{_sbindir}/plymouth-set-default-theme
%{_libexecdir}/plymouth/plymouth-update-initrd
%{_libexecdir}/plymouth/plymouth-generate-initrd
%{_libexecdir}/plymouth/plymouth-populate-initrd

%files plugin-label
%{_libdir}/plymouth/label.so

%files plugin-script
%{_libdir}/plymouth/script.so

%files plugin-fade-throbber
%{_libdir}/plymouth/fade-throbber.so

%files plugin-space-flares
%{_libdir}/plymouth/space-flares.so

%files plugin-two-step
%{_libdir}/plymouth/two-step.so

%files theme-charge
%{_datadir}/plymouth/themes/charge

%files theme-fade-in
%{_datadir}/plymouth/themes/fade-in

%files theme-script
%{_datadir}/plymouth/themes/script

%files theme-solar
%{_datadir}/plymouth/themes/solar

%files theme-spinfinity
%{_datadir}/plymouth/themes/spinfinity

%files theme-spinner
# bgrt is a variant of spinner with different settings in its .plymouth file
%{_datadir}/plymouth/themes/bgrt
%{_datadir}/plymouth/themes/spinner

%files system-theme


%changelog
* Wed Sep 28 2022 Hans de Goede <hdegoede@redhat.com> - 22.02.122-3
- Fix SimpleDRM sometimes not being ignored (rhbz#2127663)
- Mark boot-duration file as %%verify(not mode (rhbz#2122896)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02.122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar  7 2022 Hans de Goede <hdegoede@redhat.com> - 22.02.122-1
- New upstream release 22.02.122 (#2039427)
- Add patches from upstream to fix some issues with the kernel switch
  to simpledrm

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5.20210331git1ea1020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec  6 2021 Hans de Goede <hdegoede@redhat.com> - 0.9.5-4.20210331git1ea1020
- Add "Requires: fedora-logos-classic" to the plymouth-theme-charge package

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3.20210331git1ea1020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Hans de Goede <hdegoede@redhat.com> - 0.9.5-2.20210331git1ea1020
- New git snapshot
- Fixes 1933378 - Bootsplash doesn't always fully clear on boot to console
- Fixes 1941329 - Flickering plymouth on shutdown/reboot
- Prune spec-file changelog a bit

* Tue Mar 23 2021 Hans de Goede <hdegoede@redhat.com> - 0.9.5-1.20210323git8a3c9bb
- Update to 0.9.5 + a bunch of extra fixes from git (new upstream git snapshot)
- Fixes 1896929 - systemd complains about Unit configured to use KillMode=none

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-17.20200325gite31c81f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-16.20200325gite31c81f
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-15.20200325gite31c81f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 25 2020 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-14.20200306git58a7289
- New upstream git snapshot
- Add RemainAfterExit=yes to plymouth's systemd service files (rhbz#1807771)
- Fix the spinner / animation missing on shutdown and reboot

* Mon Mar  9 2020 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-13.20200306git58a7289
- Add patches fixing crash on monitor hot(un)plug (rhbz#1809681)
- Add patches fixing delay between gdm telling us to deactivate and
  us telling gdm it is ok to continue
- Drop plymouth-plugin-throbgress sub-package, the spinfinity theme now
  uses the two-step plugin

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-12.20191022git32c097c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-11.20191022git32c097c
- Drop our private plymouth-update-initrd copy, it is identical to upstream
- New upstream git snapshot, with the following fixes:
- Tweaks to the spinner/bgrt themes to match the gdm/gnome-shell lock screen
  password entry style tweaks done in GNOME 3.34
- Move the keyboard layout and capslock indicator closer to the text field
- Fix flickering below spinner on hidpi displays:
  https://gitlab.freedesktop.org/plymouth/plymouth/issues/83
- Add logrotate file for /var/log/boot.log so that it does not grow endlessly:
  https://gitlab.freedesktop.org/plymouth/plymouth/issues/31
- Some bgrt fixes for devices with non-upright mounted LCD panels

* Tue Oct  1 2019 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-10.20191001gita8aad27
- We are carrying so much patches from upstream that we are practically
  following upstream master, switch to a git snapshot
- Add keyboard layout and capslock state indicator support (rhbz#825406)
- Fix "Installing Updates..." text being rendered all garbled on devices
  where the panel is mounted 90 degrees rotated (rhbz#1753418)

* Sat Sep  7 2019 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-9
- Add a patch fixing issues when using cards which default to the radeon
  kms driver with the amdgpu kms driver (rhbz#1490490)
- Extend default DeviceTimeout to 8 seconds (rhbz#1737221)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-7
- One more patch for dealing with some devices with a non-upright mounted
  LCD-panel (rhbz#1730783)

* Wed Jun 12 2019 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-6
- Add patches from upstream for:
  - Fix failing to pick the native monitor mode starting with kernel 5.2
  - Fix firmware bootsplash support for devices which use the new
    (in ACPI 6.2) rotation bits in the BGRT header
  - Add support for firmware-upgrade mode

* Mon Mar 25 2019 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-5
- Update bgrt/spinner background to solid black to make the experience on
  systems where we do not show the firmware boot-splash consistent with
  systems where we do show the firmware boot-splash
- Update translations

* Mon Mar  4 2019 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-4
- Add translations for the new spinner/bgrt offline-updates splash

* Wed Feb 13 2019 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.4-3
- Add patches from upstream for:
  - Monitor hotplug support, this fixes issues with monitors on DP-MST
    docs sometimes not lighting up (rhbz#1652279)
  - Adding support for using the firmware's bootsplash as theme background
  - New bgrt theme which implements the boot-theme design from:
    https://wiki.gnome.org/Design/OS/BootProgress
    Including the new theming for offline-updates shown there
- Make the bgrt theme the new default and upgrade systems which are using the
  charge theme, which is the old default to use the new bgrt theme
- Cleanup the spec-file a bit:
  - Remove unused / unnecessary %%global variables
  - Sort the sections for the various plugins and themes alphabetically
  - Simplify theme filelists

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Ray Strode <rstrode@redhat.com> - 0.9.4-1
- Update to 0.9.4

* Thu Oct 04 2018 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.3-14
- Add patches from upstream to fix the disk unlock screen sometimes having
  a very low resolution on UEFI machines:
  https://gitlab.freedesktop.org/plymouth/plymouth/issues/68

* Mon Aug 06 2018 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.3-13
- Update patches for CONFIG_FRAMEBUFFER_CONSOLE_DEFERRED_TAKEOVER interaction
  to the latest patches from master, this fixes the transition from plymouth
  to gdm being non smooth
- Drop unused default-boot-duration file (rhbz#1456010)

* Thu Aug  2 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.3-12
- Drop groups in spec
- Drop requires on initscripts (rhbz 1592383)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.3-10
- Add patches from upstream fixing details view on kernels build with
  CONFIG_FRAMEBUFFER_CONSOLE_DEFERRED_TAKEOVER

* Wed Jun 06 2018 Adam Williamson <awilliam@redhat.com> - 0.9.3-9
- Backport patch to avoid loading renderers on non-rhgb boot
- Backport patch to handle 'rhgb' but no renderers available
- Move frame-buffer rendererer back to graphics-libs subpackage

* Mon Jun 04 2018 Adam Williamson <awilliam@redhat.com> - 0.9.3-8
- Move frame-buffer and drm renderers back to main package
  Having both in subpackage breaks minimal installs with rhgb

* Fri Jun 01 2018 Adam Williamson <awilliam@redhat.com> - 0.9.3-7
- Move frame-buffer renderer to graphics-libs
- Resolves: #1518464

* Sun Apr 15 2018 Hans de Goede <jwrdegoede@fedoraproject.org> - 0.9.3-6
- Add patches from upstream git for devices with non upright mounted LCD panels
  https://bugs.freedesktop.org/show_bug.cgi?id=104714
