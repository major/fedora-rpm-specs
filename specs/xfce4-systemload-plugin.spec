# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173668
# VCS   https://gitlab.xfce.org/panel-plugins/xfce4-systemload-plugin

%global minorversion 1.4
%global xfceversion 4.20

Name:           xfce4-systemload-plugin
Version:        1.4.0
Release:        %autorelease
Summary:        Systemload monitor for the Xfce panel

License:        BSD-2-Clause
URL:            https://docs.xfce.org/panel-plugins/xfce4-systemload-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

%if 0%{?fedora} >= 39
ExcludeArch:    %{ix86}
%endif

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libgtop2-devel
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel
BuildRequires:  meson
BuildRequires:  upower-devel
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  xfconf-devel

Requires:       xfce4-panel >= %{xfceversion}

%description
A system-load monitor plugin for the Xfce panel. It displays the current CPU 
load, the memory in use, the swap space and the system uptime.


%prep
%autosetup


%build
%meson
%meson_build


%check
%meson_test


%install
%meson_install

# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.systemload.*

%changelog
%autochangelog
