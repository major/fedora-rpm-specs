%global tarball_version %%(echo %{version} | tr '~' '.')
%global shell_version 44~beta

Name:           gnome-shell-extension-background-logo
Version:        44~beta
Release:        1%{?dist}
Summary:        Background logo extension for GNOME Shell

License:        GPLv2+
URL:            https://pagure.io/background-logo-extension
Source0:        https://releases.pagure.org/background-logo-extension/background-logo-extension-%{tarball_version}.tar.xz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  glib2-devel
BuildRequires:  git

Requires:       gnome-shell >= %{shell_version}
Requires:       system-logos

%description
Show your pride! Display the Fedora logo (or any other graphic) in the corner of your desktop.

%prep
%autosetup -n background-logo-extension-%{tarball_version} -S git

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_datadir}/glib-2.0/schemas/org.fedorahosted.background-logo-extension.gschema.xml
%{_datadir}/gnome-shell/extensions/background-logo@fedorahosted.org/

%changelog
* Tue Feb 14 2023 Florian Müllner <fmuellner@redhat.com> - 44~beta-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 17 2022 Florian Müllner <fmuellner@redhat.com> - 43.0-1
-  Update to 43.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 04 2022 Florian Müllner <fmuellner@redhat.com> - 42.0-1
- Update to 42.0

* Tue Feb 15 2022 Florian Müllner <fmuellner@redhat.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Florian Müllner <fmuellner@redhat.com> - 41.0-1
- Update to 41.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0~rc-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Michael Catanzaro <mcatanzaro@redhat.com> - 40.0~rc-2
- Fix logo flickering

* Tue Mar 16 2021 Florian Müllner <fmuellner@redhat.com> - 40.0~rc-1
- Update to 40.rc

* Tue Feb 23 2021 Florian Müllner <fmuellner@redhat.com> - 40.0~beta-1
- Update to 40.beta

* Tue Feb 02 2021 Florian Müllner <fmuellner@redhat.com> - 3.37.3-4.20210574ed73
- Build snapshot from current upstream

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Florian Müllner <fmuellner@redhat.com> - 3.37.3-1
- Update to 3.37.3

* Sat Mar 07 2020 Florian Müllner <fmuellner@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Thu Feb 20 2020 Florian Müllner <fmuellner@redhat.com> - 3.34.0-3
- Adjust to gnome-shell changes + shut up some warnings

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Florian Müllner <fmuellner@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Florian Müllner <fmuellner@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Matthew Miller <mattdm@fedoraproject.org> - 3.24.0-4
- make description descriptive

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.24.0-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 Florian Müllner <fmuellner@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 30 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.91-1
- Update to 3.21.91

* Tue Jun 21 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Fri May 27 2016 Florian Müllner <fmuellner@redhat.com> . 3-21-2-1
- Update to 3.21.2

* Tue Mar 22 2016 Florian Müllner <fmuellner@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Mar 16 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Thu Mar 03 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Fri Feb 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Thu Dec 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Wed Nov 25 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Thu Oct 29 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Mon Sep 21 2015 Florian Müllner <fmuellner@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Wed Sep 16 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Thu Sep 03 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Thu Aug 20 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.3-2
- Don't own /usr/share/gnome-shell/extensions directory: now part of
  gnome-shell package

* Thu Jul 02 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.2-1
- Update to 3.17.2

* Thu Apr 30 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.1-1
- Update to 3.17.1

* Thu Apr 16 2015 Florian Müllner <fmuellner@redhat.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Florian Müllner <fmuellner@redhat.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.92-1
- Update to 3.15.92

* Thu Mar 05 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.91-1
- Update to 3.15.91

* Fri Feb 20 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Fri Dec 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.3-1
- Update to 3.15.3

* Thu Nov 27 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.2-1
- Update to 3.15.2

* Thu Nov 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.1-1
- Update to 3.15.1

* Fri Nov 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Initial Fedora packaging
