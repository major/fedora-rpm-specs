%global branch 1.28

# Needed to break circular dependencies between mate-settings-daemon(-devel)
# and mate-control-center(-filesystem), especially for new RHEL releases.
%global bootstrap 0

Name:          mate-settings-daemon
Version:       %{branch}.0
Release:       %autorelease
Summary:       MATE Desktop settings daemon
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

# fix rhbz (#1140329)
%if 0%{?rhel}
Patch0:        mate-settings-daemon_fix-xrdb-plugin-for-rhel.patch
%endif

# upstream commits
Patch1:        mate-settings-daemon_0001-build-escape-newline.patch
Patch2:        mate-settings-daemon_0002-plugins-add-missing-x11-linker-flags.patch
Patch3:        mate-settings-daemon_0003-configure.ac-don-t-link-plugins-with-no-undefined.patch
Patch4:        mate-settings-daemon_0004-Add-a-keyboard-shortcut-to-start-a-screen-reader-416.patch
Patch5:        mate-settings-daemon_0005-Remove-remaining-unused-references-to-dbus-glib.patch

BuildRequires: dconf-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: libmatemixer-devel
BuildRequires: libcanberra-devel
BuildRequires: libmatekbd-devel
BuildRequires: libnotify-devel
BuildRequires: libSM-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: nss-devel
BuildRequires: polkit-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: systemd-devel

Requires:       libmatekbd%{?_isa} >= 0:1.6.1-1
%if !0%{?bootstrap}
# needed for xrandr capplet
Requires:       mate-control-center-filesystem
%endif
# since f34
%if 0%{?fedora} && 0%{?fedora} >= 34
Requires:       xmodmap
Requires:       xrdb
%endif

%description
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%package devel
Summary:        Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%prep
%autosetup -p1

NOCONFIGURE=1 ./autogen.sh

%build
%configure                             \
   --enable-pulse                      \
   --disable-static                    \
   --disable-schemas-compile           \
   --enable-polkit                     \
   --with-x                            \
   --with-nssdb

make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%dir %{_sysconfdir}/mate-settings-daemon
%dir %{_sysconfdir}/mate-settings-daemon/xrandr
%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_sysconfdir}/xrdb/
%{_libdir}/mate-settings-daemon
%{_libexecdir}/mate-settings-daemon
%{_libexecdir}/msd-datetime-mechanism
%{_libexecdir}/msd-locate-pointer
%{_udevrulesdir}/61-mate-settings-daemon-rfkill.rules
%{_datadir}/mate-control-center/keybindings/50-accessibility.xml
%{_datadir}/dbus-1/services/org.mate.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.mate.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mate-settings-daemon
%{_datadir}/glib-2.0/schemas/org.mate.*.xml
%{_datadir}/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy
%{_mandir}/man1/*

%files devel
%{_includedir}/mate-settings-daemon
%{_libdir}/pkgconfig/mate-settings-daemon.pc


%changelog
%autochangelog
