# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173670
# VCS   https://gitlab.xfce.org/panel-plugins/xfce4-wavelan-plugin
%global minorversion 0.7
%global xfceversion 4.20

Name:           xfce4-wavelan-plugin
Version:        0.7.0
Release:        %autorelease
Summary:        WaveLAN plugin for the Xfce panel

License:        BSD-2-Clause
URL:            https://docs.xfce.org/panel-plugins/xfce4-wavelan-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfceversion}

Requires:       xfce4-panel >= %{xfceversion}

%description
A plugin for the Xfce panel that monitors a wireless LAN interface. It 
displays stats for signal state, signal quality and network name (SSID).

%prep
%setup -q


%build
%meson
%meson_build

%install
%meson_install

# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

# FIXME: make sure debuginfo is generated properly (#795107)
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%check
%meson_test


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_libdir}/xfce4/panel/plugins/libwavelan.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
