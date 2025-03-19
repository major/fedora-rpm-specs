Name:          mate-sensors-applet
Version:       1.28.0
Release:       %autorelease
Summary:       MATE panel applet for hardware sensors
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz

Patch1:        mate-sensors-applet_0001-Fix-an-invalid-pointer-crash-with-glib-2.83.2.patch

BuildRequires: gtk3-devel
BuildRequires: libnotify-devel
BuildRequires: libXNVCtrl-devel
BuildRequires: lm_sensors-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-panel-devel

Requires:      hddtemp

%description
MATE Sensors Applet is an applet for the MATE Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds
and voltage readings under Linux.
Can interface via the Linux kernel i2c modules, or the i8k kernel modules
Includes a simple, yet highly customization display and intuitive 
user-interface.
Alarms can be set for each sensor to notify the user once a certain value
has been reached, and can be configured to execute a given command at given
repeated intervals.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The mate-sensors-applet-devel package contains libraries and header files for
developing applications that use mate-sensors-applet.

%prep
%autosetup -p1

%build
%configure \
    --disable-static \
    --disable-schemas-compile \
    --enable-in-process \
    --enable-libnotify \
    --with-nvidia

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
%{make_install}

find $RPM_BUILD_ROOT -name "*.la" -exec rm -rf {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
#%%{_libexecdir}/mate-sensors-applet
%{_libdir}/libmate-sensors-applet-plugin.so.*
%{_libdir}/mate-sensors-applet/
%{_datadir}/mate-sensors-applet/ui/
%{_datadir}/pixmaps/mate-sensors-applet/
%{_datadir}/icons/hicolor/*/*/*.png
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.SensorsAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.sensor.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.SensorsApplet.mate-panel-applet

%files devel
%{_libdir}/libmate-sensors-applet-plugin.so
%{_includedir}/mate-sensors-applet/


%changelog
%autochangelog

