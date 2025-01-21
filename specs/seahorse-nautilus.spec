%global gitdate 20220906
%global commit0 2cc2a06148604b2f118ef460527b03d27530f6d4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           seahorse-nautilus
Version:        3.11.92
%global         release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Release:        28%{?gitdate:.%{gitdate}git%{shortcommit0}}%{?dist}
Summary:        PGP encryption and signing for nautilus
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Seahorse
%if 0%{?gitdate}
Source0:        https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.bz2
%else
Source0:        https://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz
%endif
Patch0:         seahorse-nautilus-fix_gnupg2_ver.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  gpgme-devel >= 1.0
BuildRequires:  meson
BuildRequires:  pkgconfig(cryptui-0.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:  pkgconfig(libnotify)

%description
Seahorse nautilus is an extension for nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.


%prep
%autosetup -p0 -n %{?gitdate:%{name}-%{commit0}}%{!?gitdate:%{name}-%{tarball_version}}


%build
%meson
%meson_build


%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/seahorse-pgp-encrypted.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/seahorse-pgp-keys.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/seahorse-pgp-signature.desktop

%find_lang %{name} --with-gnome


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/seahorse-tool
%{_libdir}/nautilus/extensions-4/libnautilus-seahorse.so
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.*gschema.xml
%{_mandir}/man1/seahorse-tool.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-28.20220906git2cc2a06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-27.20220906git2cc2a06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-26.20220906git2cc2a06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-25.20220906git2cc2a06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 23 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 3.11.92-24.20220906git2cc2a06
- Allow building with gnupg2 2.4.x

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-23.20220906git2cc2a06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Kalev Lember <klember@redhat.com> - 3.11.92-22.20220906git2cc2a06
- Update to git snapshot for nautilus 43 support
- Drop old seahorse-plugins obsoletes

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 David King <amigadave@amigadave.com> - 3.11.92-14
- Remove libgnome-keyring dependency

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.11.92-7
- Rebuild for gpgme 1.18

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 29 2015 Kalev Lember <klember@redhat.com> - 3.11.92-5
- Fix the build with gnupg2 2.1.x
- Use license macro for COPYING
- Use make_install macro

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Aug 28 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Mar 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.92-1
- Update to 3.7.92

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Wed Sep 26 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-1
- Update to 3.5.92
- Install the gsettings schema files

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-2
- Use rpm macros to define the version number
- Do verbose builds
- Fix %%files entries to comply with ownership rules

* Tue Mar 27 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-1
- initial packaging for Fedora
