# Review at https://bugzilla.redhat.com/show_bug.cgi?id=173552
# VCS   https://gitlab.xfce.org/panel-plugins/xfce4-sensors-plugin

%global minor_version 1.5
%global xfceversion 4.20

Name:           xfce4-sensors-plugin
Version:        1.5.0
Release:        %autorelease
Summary:        Sensors plugin for the Xfce panel

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/panel-plugins/xfce4-sensors-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  hddtemp
BuildRequires:  libnotify-devel >= 0.7
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel
BuildRequires:  lm_sensors-devel >= 2.8
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel >= %{xfceversion}

Requires:       hddtemp
Requires:       lm_sensors >= 2.8
Requires:       xfce4-panel >= %{xfceversion}

Obsoletes:      %{name}-devel < 1.5.0
Provides:       %{name}-devel = %{version}-%{release}

%description
This plugin displays various hardware sensor values in the Xfce panel.


%prep
%autosetup -p1


%build
%meson \
    -Dhddtemp=enabled \
    -Dhddtemp-path=%{_bindir}/hddtemp \
    -Dsysfsacpi=enabled \
    -Dxnvctrl=disabled
%meson_build


%install
%meson_install

# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}

desktop-file-install --vendor "" \
        --add-category "System" \
        --remove-category "Utility" \
        --dir %{buildroot}%{_datadir}/applications \
        --delete-original \
        %{buildroot}%{_datadir}/applications/xfce4-sensors.desktop


%check
%meson_test


%files -f %{name}.lang
%license COPYING LICENSE
%doc AUTHORS ChangeLog NEWS TODO
%{_bindir}/xfce4-sensors
%{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.so
%{_datadir}/applications/xfce4-sensors.desktop
%{_datadir}/icons/hicolor/*/apps/xfce-sensors.png
%{_datadir}/icons/hicolor/scalable/apps/xfce-sensors.svg
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.*
%{_mandir}/man1/xfce4-sensors.1.gz


%changelog
%autochangelog
