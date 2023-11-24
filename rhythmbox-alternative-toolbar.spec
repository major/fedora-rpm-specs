%global debug_package %{nil}
%global mod_name alternative-toolbar

Name:		rhythmbox-alternative-toolbar
Version:	0.20.4
Release:	%autorelease
Summary:	Client-side decorated compact toolbar for Rhythmbox
License:	GPL-3.0-or-later

URL:		https://github.com/fossfreedom/alternative-toolbar
Source0:	%{url}/releases/download/v%{version}/%{mod_name}-%{version}.tar.xz
Source1:	%{url}/releases/download/v%{version}/%{mod_name}-%{version}.tar.xz.asc
Source2:	https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x1e1fb0017c998a8ae2c498a6c2eaa8a26adc59ee#/1E1FB0017C998A8AE2C498A6C2EAA8A26ADC59EE.gpg

BuildRequires:	gcc
BuildRequires:	intltool
BuildRequires:	glib2-devel
BuildRequires:	python3-gobject
BuildRequires:	gtk3
BuildRequires:	gobject-introspection
BuildRequires:	rhythmbox-devel
BuildRequires:	make

BuildRequires:	gnupg2

Requires:	rhythmbox

ExcludeArch:	s390 s390x

%description
Alternative Toolbar replaces the Rhythmbox large toolbar with a Client-Side
Decorated or Compact toolbar which can be hidden.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{mod_name}-%{version}

%build
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/rhythmbox/plugins/%{mod_name}/LICENSE
%find_lang %{mod_name}

%files -f %{mod_name}.lang
%{_libdir}/rhythmbox/plugins/%{mod_name}/
%{_datadir}/rhythmbox/plugins/%{mod_name}
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.plugins.alternative_toolbar.gschema.xml
%{_datadir}/metainfo/org.gnome.rhythmbox.alternative-toolbar.addon.appdata.xml
%license LICENSE
%doc README.md

%changelog
%autochangelog
