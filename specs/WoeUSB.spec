%global debug_package   %{nil}

Name:           WoeUSB
Version:        5.2.4
Release:        10%{?dist}
Summary:        Windows USB installation media creator
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/WoeUSB/WoeUSB
Source0:        https://github.com/WoeUSB/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    s390x

Requires:       bash
Requires:       dosfstools
Requires:       gawk
Requires:       grep
Requires:       grub2-pc-modules
Requires:       ntfs-3g
Requires:       parted
Requires:       wget
Requires:       wimlib
Requires:       wimlib-utils
BuildRequires:  make

%description
A utility that enables you to create your own bootable Windows installation
USB storage device from an existing Windows Installation disc or disk image.

%prep
%autosetup

%build
# Replace the version placeholders
find . -type f -print0 | xargs -0 sed -i "s/@@WOEUSB_VERSION@@/%{version}/"
sed -i '1!b;s/env bash/bash/' sbin/woeusb

%install
install -d -m 777 %{buildroot}%{_bindir}
install -m 755 sbin/woeusb %{buildroot}%{_bindir}/woeusb
install -d -m 777 %{buildroot}%{_mandir}/man1
install -m 444 share/man/man1/woeusb.1 %{buildroot}%{_mandir}/man1/woeusb.1
ls -l %{buildroot}%{_mandir}/man1

%files
%license LICENSES/GPL-3.0-or-later.txt
%{_bindir}/woeusb
%{_mandir}/man1/woeusb.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 5.2.4-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 mprahl <mprahl@redhat.com> - 5.2.4-1
- Update to v5.2.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 mprahl <mprahl@redhat.com> - 5.1.2-2
- Fix a build failure

* Tue Jun 15 2021 mprahl <mprahl@redhat.com> - 5.1.2-1
- Update to v5.1.2
- Remove the unmaintained GUI
- Add missing requirements

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 16 2020 mprahl <mprahl@redhat.com> - 3.3.1-2
- Stop building for s390x due to RHBZ#1813540

* Tue Mar 10 2020 mprahl <mprahl@redhat.com> - 3.3.1-1
- new version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 mprahl <mprahl@redhat.com> - 3.3.0-2
- Apply a workaround for RHBZ#1783669

* Wed Oct 16 2019 mprahl <mprahl@redhat.com> - 3.3.0-1
- new version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 mprahl <mprahl@redhat.com> - 3.2.12-1
- new version

* Sat Sep 08 2018 mprahl <mprahl@redhat.com> - 3.2.2-1
- New version
- Add grub2-pc-modules as a requirement

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 mprahl <mprahl@redhat.com> - 3.2.1-1
- new version

* Mon Apr 2 2018 Matt Prahl <mprahl@redhat.com> - 3.1.5-2
* Address rpmgrill failures

* Mon Apr 2 2018 Matt Prahl <mprahl@redhat.com> - 3.1.5-1
- Update to v3.1.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 9 2017 Matt Prahl <mprahl@redhat.com> - 2.2.2-1
- Update to v2.2.2

* Wed Sep 20 2017 Matt Prahl <mprahl@redhat.com> - 2.1.3-1
- Initial release
