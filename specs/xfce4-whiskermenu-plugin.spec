%undefine __cmake_in_source_build
%global minorversion	2.8

Name:		xfce4-whiskermenu-plugin
Version:	2.8.4
Release:	2%{?dist}
Summary:	An alternate application launcher for Xfce

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://gottcode.org/xfce4-whiskermenu-plugin/
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	exo-devel
BuildRequires:	garcon-devel
BuildRequires:	xfce4-panel-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	accountsservice-devel
BuildRequires:	gtk-layer-shell-devel
BuildRequires:	gettext

Requires:	xfce4-panel
Requires:	hicolor-icon-theme


%description
Alternate application launcher for Xfce. When you open it you are shown 
a list of applications you have marked as favorites. You can browse through
all of your installed applications by clicking on the category buttons on the
side. Top level categories make browsing fast, and simple to switch between. 
Additionally, Whisker Menu keeps a list of the last ten applications 
that you’ve launched from it

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc README NEWS
%{_bindir}/xfce4-popup-whiskermenu
%{_libdir}/xfce4/panel/plugins/libwhiskermenu.so
# Type=X-XFCE-PanelPlugin is a valid extension of freedesktop.org specs, but 
# desktop-file-utils refuse to install or verify these files
%{_datadir}/xfce4/panel/plugins/whiskermenu.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.whiskermenu.*g
%{_mandir}/man1/xfce4-popup-whiskermenu.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 7 2025 Eduardo Echeverria  <echevemaster@gmail.com> - 2.8.4-1
- Update to 2.8.4

* Sun Dec 22 2024 Mukundan Ragavan <nonamedotc@gmail.com> - 2.8.3-5
- rebuild for xfce-4.20

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.8.3-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.8.3-1
- Update to v2.8.3

* Wed Aug 30 2023 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.8.0-1
- Update to v2.8.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Filipe Rosset <rosset.filipe@gmail.com> - 2.7.3-1
- Update to 2.7.3 fixes rhbz#2189912

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.7.2-1
- Update to v2.7.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 12 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1

* Sun Nov 21 2021 Filipe Rosset <rosset.filipe@gmail.com> - 2.7.0-1
- Update to 2.7.0 fixes rhbz#2025197

* Sat Nov 13 2021 Filipe Rosset <rosset.filipe@gmail.com> - 2.6.2-1
- Update to 2.6.2 fixes rhbz#2022971

* Wed Oct 13 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Sun Sep 19 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.3-1
- Update to 2.5.3

* Fri Jan 15 2021 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.2-1
- Update to 2.5.2

* Sun Jan  3 2021 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.1-1
- Update to 2.5.1 fixes rhbz#1910803

* Thu Dec 24 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.6-1
- Update to 2.4.6

* Wed Jul 22 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.4.5-1
- Update to 2.4.5

* Wed Apr 22 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.4-1
- Update to 2.4.4

* Sun Mar 15 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.3-1
- Update to 2.4.3

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Thu Feb 13 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Mon Feb 10 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.0-1
- Update to 2.4.0 fixes rhbz#1801462

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.5-1
- Update to 2.3.5

* Fri Nov 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Fri Aug 09 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.3-1
- Update to 2.3.3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 31 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.1-2
- Add explicit build directory

* Sat Jan 19 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Mon Oct 01 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.1-20
- Rebuild for xfce version 4.13

* Tue Jul 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Sun Apr 22 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.7-1
- Update to 2.1.7 (bugfixes)

* Sun Apr 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6
- Modernize spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7.5-1
- Update to 1.7.5

* Tue Nov 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4

* Sun Aug 06 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.7.3-1
- Update 1.7.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.7.2-1
- Update to 1.7.2

* Thu Mar 02 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Sat Dec 10 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.6.2-1
- Rebuilt for new upstream release 1.6.2

* Sat Nov 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.6.1-1
- Rebuilt for new upstream release 1.6.1

* Sun Oct 02 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Mon Apr 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3 (bugfix release)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.5.1-1
- Rebuilt for new upstream release 1.5.1, fixes rhbz #1266049

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.5.0-2
- Rebuild for Xfce 4.12

* Sun Feb 22 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.5.0-1
- Rebuilt for new upstream release 1.5.0, fixes rhbz #1194183

* Sun Dec 28 2014 Eduardo Echeverria <echevemaster@gmail.com> - 1.4.2-1
- Updated to the 1.4.2 version

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 19 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.4.0-1
- Rebuilt for new upstream release 1.4.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Eduardo Echeverria <echevemaster@gmail.com> - 1.3.2-1
- Bumped to new upstream release 1.3.2

* Wed Jan 15 2014 Eduardo Echeverria <echevemaster@gmail.com> - 1.3.1-1
- Bumped to new upstream release 1.3.1

* Thu Dec 5 2013 Eduardo Echeverria <echevemaster@gmail.com> - 1.2.2-1
- Bumped to new upstream release 1.2.2

* Fri Sep 13 2013 Eduardo Echeverria <echevemaster@gmail.com> - 1.1.1-1
- Initial Packaging

