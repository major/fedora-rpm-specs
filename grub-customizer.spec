Name:           grub-customizer
Version:        5.2.4
Release:        1%{?dist}
Summary:        Graphical GRUB2 settings manager

License:        GPL-3.0-or-later
URL:            https://launchpad.net/grub-customizer
Source0:        https://launchpad.net/grub-customizer/5.2/%{version}/+download/%{name}_%{version}.tar.gz
Source1:        grub.cfg

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtkmm30-devel
BuildRequires:  gettext
BuildRequires:  openssl-devel
BuildRequires:  libarchive-devel
BuildRequires:  desktop-file-utils

%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif
Requires:       hicolor-icon-theme

ExcludeArch:    s390 s390x %{arm}

%description
Grub Customizer is a graphical interface to configure the grub2/burg settings
with focus on the individual list order - without losing the dynamical behavior
of grub.

The goal of this project is to create a complete and intuitive graphical
grub2/burg configuration interface. The main feature is the boot entry list
configuration - but not simply by modified the grub.cfg: to keep the dynamical
configuration, this application will only edit the script order and generate
proxies (script output filter), if required.

%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/grub.cfg

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc README changelog
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/grubcfg-proxy
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_datadir}/polkit-1/actions/net.launchpad.danielrichter2007.pkexec.grub-customizer.policy


%changelog
* Thu Nov 02 2023 Vasiliy N. Glazov <vascom2@gmail.com> 5.2.4-1
- Update to 5.2.4

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 18 2023 josef radinger <cheese@nosuchhost.net> - 5.2.3-1
- bump version

* Fri Mar 03 2023 Vasiliy N. Glazov <vascom2@gmail.com> 5.2.2-3
- Fix #2174582

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Vasiliy N. Glazov <vascom2@gmail.com> 5.2.2-1
- Update to 5.2.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 5.1.0-9
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 josef radinger <cheese@nosuchhost.net> - 5.1.0-1
- bump version
- update Source-url
- switch to svg for icons

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Vasiliy N. Glazov <vascom2@gmail.com> 5.0.8-1
- Update to 5.0.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> 5.0.6-6
- Revert ExcludeArch change

* Mon Aug 21 2017 Vasiliy N. Glazov <vascom2@gmail.com> 5.0.6-5
- Correct ExcludeArch due to grub2 builded not for all arches

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 22 2016 Vasiliy N. Glazov <vascom2@gmail.com> 5.0.6-1
- Update to 5.0.6

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 5.0.5-4
- aarch64 has grub2 but only the EFI variant

* Fri Apr 08 2016 Vasiliy N. Glazov <vascom2@gmail.com> 5.0.5-3
- Remove POSTIN scriptlet warning (rhbz 1324979)

* Wed Mar 30 2016 Vasiliy N. Glazov <vascom2@gmail.com> 5.0.5-2
- Update to 5.0.5
- Correct EFI support

* Mon Mar 28 2016 Vasiliy N. Glazov <vascom2@gmail.com> 5.0.4-1
- Update to 5.0.4
- Add EFI systems support

* Fri Mar 25 2016 Vasiliy N. Glazov <vascom2@gmail.com> 5.0.3-1
- Update to 5.0.3

* Mon Mar 14 2016 Vasiliy N. Glazov <vascom2@gmail.com> 4.0.6-7
- Disable build for aarch64

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Vasiliy N. Glazov <vascom2@gmail.com> 4.0.6-1
- Update to 4.0.6

* Thu Mar 27 2014 Vasiliy N. Glazov <vascom2@gmail.com> 4.0.4-2
- Exclude arm arch

* Mon Feb 10 2014 Vasiliy N. Glazov <vascom2@gmail.com> 4.0.4-1
- Update to 4.0.4

* Thu Dec 26 2013 Vasiliy N. Glazov <vascom2@gmail.com> 4.0.2-1
- Update to 4.0.2

* Wed Mar 20 2013 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.4-1
- Update to 3.0.4

* Thu Sep 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.2-1
- Update to 3.0.2

* Mon Jul 16 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.5.7-2
- add gtk-update-icon-cache scriptlet
- add desktop-file-validate and BR for it
- add patch for correct FSF address in sources
- clean spec

* Thu Jun 14 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.5.7-1
- Update to 2.5.7

* Sat May 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.5.6-1
- Drop patch
- Update to 2.5.6

* Fri May 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> 2.5.5-1
- Initial release
