%global branch 1.28

Name:          mate-applets
Version:       %{branch}.1
Release:       %autorelease
Summary:       MATE Desktop panel applets
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: gucharmap-devel
BuildRequires: libgtop2-devel
BuildRequires: libmateweather-devel
BuildRequires: libnl3-devel
BuildRequires: libnotify-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libwnck3-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-settings-daemon-devel
BuildRequires: mate-notification-daemon
BuildRequires: mate-panel-devel
BuildRequires: polkit-devel
BuildRequires: startup-notification-devel
Buildrequires: upower-devel
Buildrequires: gtksourceview4-devel
%ifnarch s390 s390x sparc64
BuildRequires: kernel-tools-libs-devel
%endif

# not kernel-tools for this arch any more
ExcludeArch: i386 i686

Provides:   mate-netspeed%{?_isa} = %{version}-%{release}
Provides:   mate-netspeed = %{version}-%{release}
Obsoletes:  mate-netspeed < %{version}-%{release}

%description
MATE Desktop panel applets

%prep
%autosetup -p1

%build
#NOCONFIGURE=1 ./autogen.sh

%configure   \
    --disable-schemas-compile                \
    --disable-static                         \
    --with-x                                 \
    --enable-polkit                          \
    --enable-ipv6                            \
    --enable-stickynotes                     \
    --libexecdir=%{_libexecdir}/mate-applets \
    --with-dbus-sys=%{_datadir}/dbus-1/system.d \
    --enable-in-process

# https://bugzilla.redhat.com/show_bug.cgi?id=2241946
# fix linking gtksourceview
sed -i /LDFLAGS/s/--as-needed/--no-as-needed/g stickynotes/Makefile

make %{?_smp_mflags} V=1

%install
%{make_install}

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-cpufreq-selector
%{_libdir}/mate-applets
#%%{_libexecdir}/mate-applets
%config(noreplace) %{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_datadir}/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%{_datadir}/mate-applets
%{_datadir}/mate-panel/applets
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.CommandAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.TimerAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.drivemount.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.cpufreq.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.command.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.timer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/devices/*.png
%{_datadir}/icons/hicolor/*/status/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/*
%{_datadir}/pixmaps/mate-cpufreq-applet


%changelog
%autochangelog
