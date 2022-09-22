%global theme_name gnome-shell-selene
%global src_name gnome-shell-theme-selene_3.4.1-0ubuntu1~tista1
%global src_pkg gnome-shell-theme-selene_3.4.1-0ubuntu1~tista1.tar.gz
%global theme_dir gnome-shell-theme-selene-3.4.0
Name: gnome-shell-theme-selene
Version: 3.4.0
Release: 23%{?dist}
Summary: The Selene gnome-shell theme
License: GPLv3 and LGPLv2.1
URL: https://launchpad.net/~tista/+archive/selene
Source0: https://launchpad.net/~tista/+archive/selene/+files/%{src_name}.tar.gz
Requires: gnome-shell-extension-user-theme
Requires: gnome-shell >= 3.2
BuildArch: noarch

%description
Selene is an "almost dark" theme based on elementary GTK theme,
inspired by the old Atolm GTK2 theme.

%prep
%setup -q %{theme_dir}

%build

%install
mkdir -p -m755 $RPM_BUILD_ROOT/%{_datadir}/themes/%{theme_name}/gnome-shell
cp -r %{_builddir}/%{theme_dir}/%{_datadir}/themes/%{theme_name}/gnome-shell/* $RPM_BUILD_ROOT/%{_datadir}/themes/%{theme_name}/gnome-shell/.

%files
%doc %{_datadir}/themes/%{theme_name}/gnome-shell/LICENSE
%dir %{_datadir}/themes/%{theme_name}
%dir %{_datadir}/themes/%{theme_name}/gnome-shell
%{_datadir}/themes/%{theme_name}/gnome-shell/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Jens Petersen <petersen@redhat.com> - 3.4.0-6
- F18 gnome-shell-extension-user-theme no longer provides
  gnome-shell-extensions-user-theme
- cleanup spec file horizontal space

* Wed Sep 19 2012 Adrian Alves <alvesadrian@fedoraproject.org> 3.4.0-5
- License fixed

* Tue Sep 18 2012 Adrian Alves <alvesadrian@fedoraproject.org> 3.4.0-4
- License fixed

* Sun Sep 16 2012 Adrian Alves <alvesadrian@fedoraproject.org> 3.4.0-3
- Fixed %%build section and white spaces for rpmlint

* Sat Sep 15 2012 Adrian Alves <alvesadrian@fedoraproject.org> 3.4.0-2
- Fixed %%files section

* Wed May 23 2012 Tim Lauridsen <timlau@fedoraproject.org> 3.4.0-1
- initial rpm build
