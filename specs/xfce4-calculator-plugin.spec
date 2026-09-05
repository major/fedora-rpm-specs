%global majorver 0.8
%global gen_name calculator

Name:		xfce4-calculator-plugin
Version:	0.8.0
Release:	%autorelease
Summary:	A calculator plugin for the Xfce4 panel

License:	GPL-2.0-or-later
URL:		https://docs.xfce.org/panel-plugins/%{name}
Source0:	https://archive.xfce.org/src/panel-plugins/%{name}/%{majorver}/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	gtk3-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	xfce4-panel-devel
Requires:	xfce4-panel

%description
xfce4-calculator-plugin is a calculator plugin for the Xfce4 panel.

Place the plugin in your panel, enter your calculation into the text field 
and press Enter to calculate the result.

The plugin supports common mathematical operators (+, -, *, /, ^) with usual 
precedence rules and some basic functions (e.g., trigonometric functions) 
and constants.


%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

# Remove invalid locale
rm -rf %{buildroot}%{_datadir}/locale/hye

%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/xfce4/panel/plugins/libcalculator.so
%{_datadir}/xfce4/panel/plugins/%{gen_name}.desktop
%{_datadir}/icons/hicolor/*/*/*calculator*

%changelog
%autochangelog
