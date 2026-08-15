# Review at https://bugzilla.redhat.com/show_bug.cgi?id=398111
# VCS https://gitlab.xfce.org/panel-plugins/xfce4-time-out-plugin

%global minor_version 1.2
%global xfceversion 4.20

Name:           xfce4-time-out-plugin
Version:        1.2.0
Release:        %autorelease
Summary:        Xfce panel plugin for taking breaks from the computer

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/panel-plugins/xfce4-time-out-plugin/start
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libICE-devel
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel >= %{xfceversion}

Requires:       xfce4-panel >= %{xfceversion}

%description
This plugin makes it possible to take periodical breaks from the computer every
X minutes. During breaks it locks your screen. It optionally allows you to 
postpone breaks for a certain time.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/libtime-out.so

# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/xfce4/panel/plugins/libtime-out.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*


%changelog
%autochangelog

