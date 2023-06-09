%global majorver 1.0
%global app_org_name org.xfce.PanelProfiles

Name:		xfce4-panel-profiles
Version:	1.0.14
Release:	%autorelease
Summary:	A simple application to manage Xfce panel layouts

License:	GPLv3
URL:		https://git.xfce.org/apps/xfce4-panel-profiles/about/
Source0:	https://archive.xfce.org/src/apps/%{name}/%{majorver}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	python3-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils

BuildArch:	noarch

Requires:	xfce4-panel

Provides:	xfpanel-switch = %{version}-%{release}
Obsoletes:	xfpanel-switch <= 1.0.7

%description
A simple application to manage Xfce panel layouts

With the modular Xfce Panel, a multitude of panel layouts can be created. 
This tool makes it possible to backup, restore, import, and export these 
panel layouts.

%prep
%autosetup
sed -i '4s/$/Configuration;User;/'  org.xfce.PanelProfiles.desktop.in
sed -i '/Keywords/d' org.xfce.PanelProfiles.desktop.in

%build
./configure --prefix=%{_prefix}

%make_build

%install
%make_install


%find_lang %{name}

# fix executable permissions on tarballs
chmod -x %{buildroot}%{_datadir}/%{name}/layouts/*

# get rid of INSTALL and extra license file
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
rm -f %{buildroot}%{_docdir}/%{name}/COPYING

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_org_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{app_org_name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS README.md
%{_mandir}/man1/%{name}*
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{app_org_name}.desktop
%{_datadir}/metainfo/%{app_org_name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{app_org_name}.*

%changelog
%autochangelog
