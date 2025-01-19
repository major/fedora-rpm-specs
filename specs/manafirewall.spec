# Force out of source build
%undefine __cmake_in_source_build

Name:		manafirewall
Version:	0.0.3
Release:	13%{?dist}
Summary:	ManaTools FirewallD configuration tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/manatools/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	cmake			>= 3.4.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig
BuildRequires:	python3-devel		>= 3.4.0
BuildRequires:	python3-setuptools
BuildRequires:	python3-yaml
BuildRequires:	python3-yui
BuildRequires:	python3-manatools	>= 0.0.3

Requires:	hicolor-icon-theme
Requires:	python3-yaml
Requires:	python3-yui
Requires:	python3-manatools	>= 0.0.3
Requires:	python3-firewall	>= 0.9.0
Requires:	firewalld
# Ensure base TUI deps are installed
Requires:	libyui-ncurses
Requires:	libyui-mga-ncurses

Provides:	%{name}-gui		= %{version}-%{release}
Recommends:	(libyui-mga-qt if qt5-qtbase-gui)
Recommends:	(libyui-mga-gtk if gtk3)

%description
%{name} is the graphical configuration tool for firewalld based on python
manatools and libYui (Suse widget abstraction library), to be run using
Qt 5, GTK+ 3, or ncurses interfaces.

%prep
%autosetup -p1


%build
%cmake	-DCHECK_RUNTIME_DEPENDENCIES=ON
%cmake_build


%install
%cmake_install

%find_lang %{name}

%check
# Validate desktop-files.
%{_bindir}/desktop-file-validate		\
	%{buildroot}%{_datadir}/applications/*.desktop
# Validate metainfo-files.
appstream-util validate-relax --nonet		\
	%{buildroot}%{_datadir}/metainfo/*.metainfo.xml


%files -f %{name}.lang
%doc README.md TODO.md
%license AUTHORS LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{_datadir}/applications/*%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_metainfodir}/*%{name}.metainfo.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.3-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.0.3-10
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.0.3-7
- Add setuptools as a BR

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.0.3-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.3-2
- Rebuilt for Python 3.11

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.0.3-1
- Version 0.0.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.2-2
- Rebuilt for Python 3.10

* Sat Mar 13 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.2-1
- Update to 0.0.2
- Drop fix included in this release
- Fix license tag

* Sun Mar 07 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1-4
- Adapt to Fedora
- Backport fix to install metainfo file

* Sun Sep 13 2020 Angelo Naselli <anaselli@mageia.org> 0.0.1-3.mga8
+ Revision: 1625884
- Added firewalld dependencies

* Sun Sep 13 2020 Angelo Naselli <anaselli@mageia.org> 0.0.1-2.mga8
+ Revision: 1625766
- manafirewall description

* Sun Sep 13 2020 Angelo Naselli <anaselli@mageia.org> 0.0.1-1.mga8
+ Revision: 1625677
- python manatools dependency
- imported package manafirewall

