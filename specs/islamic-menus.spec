%global owner ojuba-org
%global commit 276a1aa30d3740539c4a8a3340245711fe9f7284

Name:			islamic-menus
Version:		1.0.6
Release:		25%{?dist}
Summary:		Islamic menus for desktops conforming with XDG standards
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:		GPL-3.0-or-later
URL:			https://github.com/ojuba-org/islamic-menus
Source0:		https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:		noarch
Requires:		redhat-menus hicolor-icon-theme
BuildRequires:	intltool
BuildRequires: make

%description
Categorize islamic apps in a menu for the GNOME, KDE and other
XDG-conforming desktops.

%prep
%setup -q -n %{name}-%{commit}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_sysconfdir}/xdg/menus/applications-gnome-merged/islamic.menu

%files
%doc COPYING
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/islamic.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/hicolor/scalable/categories/*.svg

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.6-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 26 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.6-3
- Another tweak of make line.

* Tue Nov 26 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.6-2
- Repair make install line.

* Thu Nov 21 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.6-1
- Remove line about applications-gnome-merged due to GNOME_BZ #688972

* Sun Nov 17 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-6
- Remove un-necessary lines about buildroot.
- Use Fedora icon cache rules.
- Update source line to github directly.

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-5
- To zero warnings by rpmlint.

* Sat Oct 12 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-4
- Fix spec name.

* Tue Oct 8 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-3
- Hosted at Ojuba project.

* Mon Oct 7 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-2
- Update sources and URL.

* Wed Jun 2 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 1.0.3-1
- Initial release.

