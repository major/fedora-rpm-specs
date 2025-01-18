%global theme_name     Bluebird

Name:           bluebird
Version:        1.3
Release:        16%{?dist}
Summary:        A clean minimalistic theme for Xfce, GTK+ 2 and 3

# Automatically converted from old format: GPLv2+ or CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later OR LicenseRef-Callaway-CC-BY-SA
URL:            http://shimmerproject.org/project/%{name}/
Source0:        https://github.com/shimmerproject/%{theme_name}/archive/v%{version}.tar.gz

BuildArch:      noarch

%description
Bluebird is a GTK2/3/xfwm4/metacity theme based on Zuki Blues.
The xfwm theme is based on axiom.


%package gtk2-theme
Summary:        Bluebird GTK+2 themes
Requires:       gtk-murrine-engine >= 0.98.1.1 gtk2-engines

%description gtk2-theme
Themes for GTK+2 as part of the Bluebird theme.


%package gtk3-theme
Summary:        Bluebird GTK+3 themes

%description gtk3-theme
Themes for GTK+3 as part of the Bluebird theme.


%package metacity-theme
Summary:        Bluebird Metacity themes
Requires:       metacity

%description metacity-theme
Themes for Metacity as part of the Bluebird theme.


%package xfwm4-theme
Summary:        Bluebird Xfwm4 themes
Requires:       xfwm4

%description xfwm4-theme
Themes for Xfwm4 as part of the Bluebird theme.


%package xfce4-notifyd-theme
Summary:        Bluebird Xfce4 notifyd theme
Requires:       xfce4-notifyd

%description xfce4-notifyd-theme
Themes for Xfce4 notifyd as part of the Bluebird theme.


%prep
%autosetup -p1 -n %{theme_name}-%{version}


%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}
cp -pr gtk-2.0/ gtk-3.0/ metacity-1/ xfwm4/ %{buildroot}%{_datadir}/themes/%{theme_name}


%files gtk2-theme
%license LICENSE.GPL LICENSE.CC
%doc README.md
%dir %{_datadir}/themes/%{theme_name}/
%{_datadir}/themes/%{theme_name}/gtk-2.0/


%files gtk3-theme
%license LICENSE.GPL LICENSE.CC
%doc README.md
%dir %{_datadir}/themes/%{theme_name}/
%{_datadir}/themes/%{theme_name}/gtk-3.0/


%files metacity-theme
%license LICENSE.GPL LICENSE.CC
%doc README.md
%dir %{_datadir}/themes/%{theme_name}/
%{_datadir}/themes/%{theme_name}/metacity-1/


%files xfwm4-theme
%license LICENSE.GPL LICENSE.CC
%doc README.md
%dir %{_datadir}/themes/%{theme_name}/
%{_datadir}/themes/%{theme_name}/xfwm4/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 24 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-1
- Update to 1.3, should work with recent GTK3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 08 2014 poma <poma@gmail.com> 1.2-2
- Upstream fix for checkboxes and radios in gtk3.14
- The "shadow" is re-enabled, the full size of the app menu in the system tray
  is resolved upstream - gtkmenu: fix unnecessary scroll buttons gtk-3-14
  https://git.gnome.org/browse/gtk+/commit/?h=gtk-3-14&id=695ff38
- The same applies to the Shimmer Project Desktop Suites for Xfce as a whole, 
  i.e. Greybird, Bluebird and Albatross.
- With these two corrections bugs #1114161, #1139190 and #1139187 
  are solved completely.

* Fri Oct 03 2014 Kevin Fenzi <kevin@scrye.com> 1.2-1
- Update to 1.2
- Add patch for issues with latest gtk3. Thanks poma
- Fixes bug #1139190

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 01 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9-1
- New upstream release

* Wed Aug 28 2013 Miro Hrončok <mhroncok@redhat.com> - 0.8-1
- Update to 0.8
- Split description to 2 lines (it was too long)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Kevin Fenzi <kevin@scrye.com> 0.7.1-1
- Update to 0.7.1

* Sat Mar 09 2013 Athmane Madjoudj <athmane@fedoraproject.org> 0.6.2-1
- Update to 0.6.2
- Cleanup the specfile.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild


* Sun Jul 15 2012 Jayson Rowe <jaysonr@fedoraproject.org> 0.6-4
- Fixed Unico Requirement

* Sat Jul 14 2012 Jayson Rowe <jaysonr@fedoraproject.org> 0.6-3
- Shortened Description

* Thu Jul 12 2012 Jayson Rowe <jaysonr@fedoraproject.org> 0.6-2
- Fixed Release
- Shortened Description

* Tue Jul 10 2012 Jayson Rowe <jaysonr@fedoraproject.org> 0.6-1
- Initial spec (based on Greybird theme)

