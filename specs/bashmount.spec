Name:              bashmount
Version:           4.3.2
Release:           12%{?dist}

Summary:           A menu-driven bash script for mounting removable media
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:           GPL-2.0-only
URL:               https://github.com/jamielinux/bashmount
Source0:           https://github.com/jamielinux/bashmount/archive/%{version}.tar.gz

BuildArch:         noarch
Requires:          bash
Requires:          sed
Requires:          udisks2
Requires:          util-linux

%description
bashmount is a menu-driven bash script that uses udisks2 to easily mount,
unmount or eject removable devices without dependencies on any GUI or
desktop environment. An extensive configuration file allows custom commands
to be run on devices.


%prep
%setup -q


%build
#nothing to do


%install
install -p -D -m755 bashmount \
    %{buildroot}%{_bindir}/bashmount
install -p -D -m644 bashmount.conf \
    %{buildroot}%{_sysconfdir}/bashmount.conf
install -p -D -m644 bashmount.1 \
    %{buildroot}%{_mandir}/man1/bashmount.1


%files
%doc COPYING NEWS
%{_bindir}/bashmount
%{_mandir}/man1/bashmount.1*
%config(noreplace) %{_sysconfdir}/bashmount.conf


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.2-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Jamie Nguyen <jamielinux@fedoraproject.org> - 4.3.2-1
- Update to upstream release 4.3.2

* Sun Aug 23 2020 Jamie Nguyen <jamielinux@fedoraproject.org> - 4.3.1-1
- Update to upstream release 4.3.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Jamie Nguyen <jamielinux@fedoraproject.org> - 4.3.0-1
- Update to upstream release 4.3.0

* Fri Jun 12 2020 Jamie Nguyen <jamielinux@fedoraproject.org> - 4.2.5-1
- Update to upstream release 4.2.5

* Thu Jun 11 2020 Jamie Nguyen <jamielinux@fedoraproject.org> - 4.1.0-1
- Update to upstream release 4.1.0
- Update URL
- Add missing dependencies

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.2.0-3
- fix macro for udisks2 dependency

* Sat Apr 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.2.0-2
- do not depend on udisks2 on EL6

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.2.0-1
- update to upstream release 3.2.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 09 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.6.2-3
- preserve timestamps
- remove some unnecessary macros

* Tue Feb 07 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.6.2-2
- remove redundant BuildRoot tag
- remove redundant cleaning of BuildRoot within the install section
- remove redundant clean section

* Mon Feb 06 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.6.2-1
- update to 1.6.2

* Sun Feb 05 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.6.1-1
- initial Fedora package
