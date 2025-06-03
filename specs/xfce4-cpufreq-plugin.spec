%global _hardened_build 1
%global minorversion 1.3

Name:           xfce4-cpufreq-plugin
Version:        1.3.0
Release:        %autorelease
Summary:        CPU frequency scaling plugin for the Xfce4 panel 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  xfce4-panel-devel
BuildRequires:  meson 

Requires:       xfce4-panel

%description
The CpuFreq Plugin shows in the Xfce Panel the following information:
    current CPU frequency
    current used governor

In a separate dialog it provides you following information:
    all available CPU frequencies
    all available governors
    used driver for the CPU

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

find %{buildroot} -name \*.la -exec rm {} \;


%files -f %{name}.lang
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/xfce4/panel/plugins/libcpufreq.so
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/xfce4/panel/plugins/cpufreq.desktop

%changelog
%autochangelog
