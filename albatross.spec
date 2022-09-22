%global theme_name     Albatross

Name:           albatross
Version:        1.7.4
Release:        13%{?dist}
Summary:        Desktop Suite for Xfce, GTK+ 2 and 3

License:        GPLv2+ or CC-BY-SA
URL:            http://shimmerproject.org/project/%{name}/

Source0:        https://github.com/shimmerproject/%{theme_name}/archive/v%{version}.tar.gz

BuildArch:      noarch

%description
Albatross is a theme for GTK2/3 and xfwm4/metacity designed to be smooth: no rough borders, no contrasted edges, no violent contrasts, a soft blue colour.


%package gtk2-theme
Summary:        Albatross GTK+2 themes
Requires:       gtk-murrine-engine >= 0.98.1.1 gtk2-engines

%description gtk2-theme
Themes for GTK+2 as part of the Albatross theme.


%package gtk3-theme
Summary:        Albatross GTK+3 themes
Requires:       gtk-unico-engine >= 1.0.1

%description gtk3-theme
Themes for GTK+3 as part of the Albatross theme.


%package metacity-theme
Summary:        Albatross Metacity themes
Requires:       metacity

%description metacity-theme
Themes for Metacity as part of the Albatross theme.


%package xfwm4-theme
Summary:        Albatross Xfwm4 themes
Requires:       xfwm4

%description xfwm4-theme
Themes for Xfwm4 as part of the Albatross theme.

%package xfce4-notifyd-theme
Summary:        Albatross Xfce4 notifyd theme
Requires:       xfce4-notifyd

%description xfce4-notifyd-theme
Themes for Xfce4 notifyd as part of the Albatross theme.

%prep
%setup -q -n %{theme_name}-%{version}

%build
# Nothing to build


%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}
cp -pr gtk-2.0/ gtk-3.0/ metacity-1/ xfwm4/ %{buildroot}%{_datadir}/themes/%{theme_name}


%files gtk2-theme
%doc LICENSE.GPL LICENSE.CC README
%dir %{_datadir}/themes/Albatross/
%{_datadir}/themes/%{theme_name}/gtk-2.0/


%files gtk3-theme
%doc LICENSE.GPL LICENSE.CC README
%dir %{_datadir}/themes/Albatross/
%{_datadir}/themes/%{theme_name}/gtk-3.0/


%files metacity-theme
%doc LICENSE.GPL LICENSE.CC README
%dir %{_datadir}/themes/Albatross/
%{_datadir}/themes/%{theme_name}/metacity-1/


%files xfwm4-theme
%doc LICENSE.GPL LICENSE.CC README
%dir %{_datadir}/themes/Albatross/
%{_datadir}/themes/%{theme_name}/xfwm4/


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Kevin Fenzi <kevin@scrye.com> - 1.7.4-1
- Update to 1.7.4. 

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 poma <poma@gmail.com> 1.7.3-2
- Upstream fix for checkboxes and radios in gtk3.14
- The "shadow" is re-enabled, the full size of the app menu in the system tray
  is resolved upstream - gtkmenu: fix unnecessary scroll buttons gtk-3-14
  https://git.gnome.org/browse/gtk+/commit/?h=gtk-3-14&id=695ff38
- The same applies to the Shimmer Project Desktop Suites for Xfce as a whole, 
  i.e. Greybird, Bluebird and Albatross.
- With these two corrections bugs #1114161, #1139190 and #1139187 
  are solved completely.

* Fri Oct 03 2014 Kevin Fenzi <kevin@scrye.com> 1.7.3-1
- Update to 1.7.3
- Apply patch for recent gtk3 changes. Thanks poma
- Fixes bug #1139187

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 15 2013 Kevin Fenzi <kevin@scrye.com> 1.5-1
- Update to 1.5 release, switch to tar.gz download. 

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild


* Sun Jul 15 2012 Jayson Rowe <jaysonr@fedoraproject.org> 1.2-3
- Fixed Unico requirement.

* Thu Jul 12 2012 Jayson Rowe <jaysonr@fedoraproject.org> 1.2-2
- Fixed release number
- Shortened description

* Tue Jul 10 2012 Jayson Rowe <jaysonr@fedoraproject.org> 1.2-1
- Initial spec (based on Greybird theme)

