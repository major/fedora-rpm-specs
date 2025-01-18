Name:       fedora-jam-kde-theme
Version:    3.0.6
Release:    11%{?dist}
Summary:    Fedora Jam KDE Theme and Configs

License:    MIT

URL:        https://fedoraproject.org/wiki/Fedora_jam
Source0:    https://pagure.io/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    COPYING

BuildArch:  noarch

BuildRequires:  kde4-filesystem
Requires: kde4-filesystem
Requires: xdg-user-dirs
## add breeze deps here? probably, need more too -- rex
Requires: breeze-icon-theme
Requires: breeze-gtk
Requires: kde-settings
Requires: kde-settings-plasma
Requires: fedora-jam-backgrounds-kde

%description
This is the Fedora Jam KDE Theme and settings files.

%prep
%autosetup -p1

%build
# blank

%install
tar cpf - . | tar --directory %{buildroot} -xvpf -
 
if [ %{_prefix} != /usr ] ; then
   pushd %{buildroot}
   mv %{buildroot}/usr %{buildroot}%{_prefix}
   mv %{buildroot}/etc %{buildroot}%{_sysconfdir}
   popd
fi
 
cp -p %{SOURCE1} .
 
%files
%license COPYING
%{_datadir}/kde-jam-settings/
%config %{_sysconfdir}/skel/.gtkrc-2.0
%config %{_sysconfdir}/skel/.config/gtk-3.0/settings.ini
%{_sysconfdir}/xdg/plasma-workspace/env/env-jam.sh
%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora-jam.desktop/
%{_datadir}/sddm/themes/00-breeze-fedora-jam
%config(noreplace) %{_sysconfdir}/sysctl.d/50-fedora-jam.conf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Adam Williamson <awilliam@redhat.com> - 3.0.6-3
- Rebuild for unretirement, for F35 and F36

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 24 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.0.6-1
- Add previews to global theme

* Wed Sep 23 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.0.5-1
- Fix for missing XDG environment variables affecting menu

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.0.4-1
- Change from dark to default Fedora Breeze theme

* Tue May 26 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.0.3-1
- Fix sddm theme showing wrong image
- Force gtk theme selection

* Mon May 25 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.0.2-1
- Fix for no image on SDDM theme

* Mon May 25 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.0.1-1
- Fix for color scheme

* Thu May 21 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 3.0.0-1
- change to not conflict with kde-settings (rehaul package)

* Wed May 20 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.1.0-1
- Add default screen locker wallpaper
- Changes to default look and feel
- Add default sddm theme

* Mon May 11 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.0-1
- Complete package overhaul

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-3
- Correct typo in default splash

* Tue Dec 04 2012 Jørn Lomax <northlomax@gmail.com> 1.0.1-2
- added lines to set defualts for all new users 
* Mon Nov 12 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-1
- New 1.0.1

* Sat Oct 27 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-1
- Initial package

