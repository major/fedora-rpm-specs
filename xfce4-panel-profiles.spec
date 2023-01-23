%global majorver 1.0
%global app_org_name org.xfce.PanelProfiles

Name:		xfce4-panel-profiles
Version:	1.0.13
Release:	5%{?dist}
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
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.13-1
- Update to 1.0.13

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12

* Mon Dec 28 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.10-2
- Add man pages

* Tue Jan 14 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10

* Tue Jul 30 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.8-3
- Fix provides and remove INSTALL file from package

* Fri Oct 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.8-2
- Fix packaging issues

* Fri Oct 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.8-1
- Rename to xfce4-panel-profiles

* Tue Apr 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.6-3
- Truly fix files and appdata issues

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.6-2
- Fix build problems

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6
- Change appdata filename
- Drop upstreamed patches
- Stop removing xubuntu layout

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.4-2
- Added fedora and el conditionals

* Thu Apr 14 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.4-1
- Updated to v1.0.4

* Mon Mar 07 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.3-3
- Added italian translation

* Sun Mar 06 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.3-2
- Add desktop-file-validate for .desktop files
- Fix buildrequires
- Add appdata file and corresponding BR

* Sat Mar 05 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.3-1
- Inital package 
