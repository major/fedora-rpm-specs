Name:           minipro
Version:        0.7
Release:        4%{?dist}
Summary:        Utility for MiniPro TL866A/TL866/CS programmer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gitlab.com/DavidGriffith/minipro
Source0:        https://gitlab.com/DavidGriffith/minipro/-/archive/%{version}/minipro-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  systemd-udev
Requires:       systemd-udev

%description
Programming utility compatible with Minipro TL866CS and Minipro TL866A
programmers.

Supports programming more than 16000 kinds of devices (including AVRs,
PICs, GALs and EPROMs) as well as testing logic devices.


%prep
%autosetup


%build
%{make_build} PREFIX=%{_prefix} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"


%install
%{make_install} PREFIX=%{_prefix} COMPLETIONS_DIR=%{_datadir}/bash-completion/completions
# This is obsolete; we just keep the uaccess rule
rm %{buildroot}%{_udevrulesdir}/61-minipro-plugdev.rules


%files
%license LICENSE
%{_datadir}/bash-completion/completions
%{_bindir}/minipro
%{_udevrulesdir}/60-minipro.rules
%{_udevrulesdir}/61-minipro-uaccess.rules
%{_datadir}/%{name}/infoic.xml
%{_datadir}/%{name}/logicic.xml
%{_mandir}/man1/minipro.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 13 2024 Lubomir Rintel <lkundrak@v3.sk> - 0.7-1
- Update to version 0.7

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Lubomir Rintel <lkundrak@v3.sk> - 0.6
- Update to version 0.6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4.20220607git83b3775
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 07 2022 Lubomir Rintel <lkundrak@v3.sk> - 0.5-3.20220607git83b3775
- Update to a newer Git snapshot

* Sun May 22 2022 Lubomir Rintel <lkundrak@v3.sk> - 0.5-3.20220522gitfefd160
- Update to a newer Git snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3.20210810git0774b07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 10 2021 Lubomir Rintel <lkundrak@v3.sk> - 0.5-2.20210810git0774b07
- Update to a Git snapshot with support for logic IC testing

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Dan Horák <dan[at]danny.cz> - 0.5-1
- update to 0.5
- fix license tag

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Lubomir Rintel <lkundrak@v3.sk> - 0.4-3
- Drop obsolete udev rules file

* Thu Jan 23 2020 Lubomir Rintel <lkundrak@v3.sk> - 0.4-2
- Fix Arm support

* Thu Nov 07 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.4-1
- Update to version 0.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.3-1
- Update to version 0.3

* Sat Feb 09 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.2-1.20181017git57b293d
- Update to a newer version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.1-3.20161103git484abde
- Fix the udev rule

* Thu Nov 03 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.1-2.20161103git484abde
- Upstreamed the patches

* Sat Oct 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.1-2.20161029git484abde
- Fix access for unprivileged users

* Sat Oct 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.1-1.20161029git484abde
- Update to a later snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.0.1-1
- Update to a tagged release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.20141215gitd6dee16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141215gitd6dee16
- Rebase to a later upstream snapshot

* Fri Dec 05 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141205git0107a7a
- Fix ATMEGA32 support
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Sat Oct 11 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141011git6a561be
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Tue Oct 07 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20140902git1b451ae
- Actually apply the patches...

* Tue Oct 07 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-5.20140902git1b451ae
- Fix insecure temporary file
- Fix PIC12 support

* Wed Oct 01 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-4.20140902git1b451ae
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Tue Sep 30 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-3.20140902git6f36b9e
- Patch away the shebang from completion file (Mihkel Vain, #1128356)

* Thu Sep 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-2.20140902git6f36b9e
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Sat Aug 09 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-2.20140624gite521a63
- Add a link to upstream pull request
- Don't mark bash completion nonsense as %%config (Christopher Meng, #1128356)

* Sat Aug 09 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-1.20140624gite521a63
- Initial packaging
