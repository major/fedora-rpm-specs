# Review at https://bugzilla.redhat.com/show_bug.cgi?id=173552
%global minor_version 1.4
%global xfceversion 4.18

Name:           xfce4-sensors-plugin
Version:        1.4.5
Release:        %autorelease
Summary:        Sensors plugin for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  lm_sensors-devel >= 2.8
BuildRequires:  hddtemp
BuildRequires:  libnotify-devel >= 0.4
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libtool

Requires:       xfce4-panel >= %{xfceversion}
Requires:       lm_sensors >= 2.8
Requires:       hddtemp
# lm_sensors is not available on s390 and s390x
ExcludeArch:    s390 s390x

%description
This plugin displays various hardware sensor values in the Xfce panel.

%package devel
Summary:        Development files for xfce4-sensors-plugin
Requires:       %{name} = %{version}-%{release}
Requires:       libxfce4util-devel

%description devel
Static libraries and header files for the xfce4-sensors-plugin.


%prep
%autosetup -p1
sed -i 's/libxfce4ui-1/libxfce4ui-2/g' lib/libxfce4sensors-1.0.pc.in


%build
%configure --disable-static \
        --enable-sysfsacpi=yes \
        --with-pathhddtemp=%{_bindir}/hddtemp
%make_build


%install
%make_install

%find_lang %{name}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

desktop-file-install --vendor "" \
        --add-category "System" \
        --remove-category "Utility" \
        --dir %{buildroot}%{_datadir}/applications \
        --delete-original \
        %{buildroot}%{_datadir}/applications/xfce4-sensors.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO
%{_bindir}/xfce4-sensors
%dir %{_libdir}/xfce4/modules/
%{_libdir}/xfce4/modules/libxfce4sensors.so.*
%{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.so
%{_datadir}/applications/xfce4-sensors.desktop
%{_datadir}/icons/hicolor/*/apps/xfce-sensors.png
%{_datadir}/icons/hicolor/scalable/apps/xfce-sensors.svg
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.*
%{_mandir}/man1/xfce4-sensors.1.gz

%files devel
%{_libdir}/pkgconfig/libxfce4sensors-1.0.pc
%{_libdir}/xfce4/modules/libxfce4sensors.so


%changelog
%autochangelog
