%global build_type_safety_c 0

Summary:	A slick-looking LightDM greeter
Name:			slick-greeter
Version:	2.2.7
Release:	%autorelease
License:	GPL-3.0-or-later
URL:			https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	10_%{name}-cinnamon.gschema.override.in
Source2:	%{name}.conf

ExcludeArch:    %{ix86}

BuildSystem:		meson
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(liblightdm-gobject-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:  pkgconfig(xapp)
BuildRequires:	vala

Provides:	lightdm-greeter = 1.2
Provides:	lightdm-%{name} = %{version}

Requires:	lightdm%{?_isa}

# Themeing require
Requires:	google-noto-sans-fonts
Requires:	system-logos
Requires:	desktop-backgrounds-compat

Recommends:	lightdm-settings
Recommends:	onboard

Obsoletes:  %{name}-mate < %{version}-%{release}

# Make sure cinnamon override is installed
Requires:	(%{name}-cinnamon = %{version}-%{release} if cinnamon)

%description
A cross-distro LightDM greeter based on unity-greeter.

%package -n %{name}-cinnamon
Summary: Slick-greeter customisation for the CINNAMON desktop
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
# Themeing require
Requires:	desktop-backgrounds-basic
Requires:	mint-y-icons
Requires:	mint-y-theme
Recommends: paper-icon-theme

%description -n %{name}-cinnamon
Slick-greeter customisation for the CINNAMON desktop.

%prep
%autosetup -p1

install -pm 0644 %{SOURCE2} %{name}.conf.example

%install -a
mkdir -p %{buildroot}%{_datadir}/lightdm/lightdm.conf.d	\
	%{buildroot}%{_datadir}/glib-2.0/schemas	\
	%{buildroot}%{_sysconfdir}/lightdm

install --target-directory=%{buildroot}%{_datadir}/lightdm/lightdm.conf.d	\
	-Dpm 0644 debian/90-%{name}.conf

sed -e 's!@color@!#202020!g'	\
	-e 's!@wallpaper@!%{_datadir}/backgrounds/tiles/default_blue.jpg!'	\
	< %{SOURCE1}								\
	> %{buildroot}%{_datadir}/glib-2.0/schemas/10_%{name}-cinnamon.gschema.override

install --target-directory=%{buildroot}%{_sysconfdir}/lightdm	\
	-Dpm 0644 %{SOURCE2}

chmod -c a+x %{buildroot}%{_bindir}/*

%find_lang %{name}

%check
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/xgreeters/*.desktop

%pre
%{_sbindir}/update-alternatives --remove lightdm-greeter	\
	%{_datadir}/xgreeters/%{name}.desktop 2> /dev/null ||:

%files -f %{name}.lang
%doc debian/changelog README.md %{name}.conf.example
%license debian/copyright COPYING
%{_bindir}/%{name}-check-hidpi
%{_bindir}/%{name}-set-keyboard-layout
%{_bindir}/%{name}-enable-tap-to-click
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/lightdm/%{name}.conf
%{_datadir}/%{name}/
%{_datadir}/xgreeters/
%{_datadir}/glib-2.0/schemas/x.dm.%{name}.gschema.xml
%{_datadir}/lightdm/lightdm.conf.d/90-%{name}.conf
%{_mandir}/man?/%{name}*

%files -n %{name}-cinnamon
%{_datadir}/glib-2.0/schemas/10_%{name}-cinnamon.gschema.override

%changelog
%autochangelog