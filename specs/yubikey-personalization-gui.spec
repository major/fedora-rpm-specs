Name:           yubikey-personalization-gui
Version:        3.1.25
Release:        17%{?dist}
Summary:        GUI for Yubikey personalization

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://opensource.yubico.com/yubikey-personalization-gui/
Source0:        http://opensource.yubico.com/yubikey-personalization-gui/releases/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  libyubikey-devel >= 1.11
BuildRequires:  ykpers-devel >= 1.14.1
BuildRequires:  desktop-file-utils
BuildRequires:  qt-devel

%description
Yubico's YubiKey can be re-programmed with a new AES key. This is a graphical
tool that makes this an easy task.


%prep
%setup -q


%build
%{qmake_qt4} "CONFIG+=fedora"
make %{?_smp_mflags}


%install
install -D -p -m 0755 build/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 resources/lin/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1

mkdir -p %{buildroot}/%{_datadir}/pixmaps
install -p -m 0644 resources/lin/%{name}.xpm %{buildroot}/%{_datadir}/pixmaps/
install -p -m 0644 resources/lin/%{name}.png %{buildroot}/%{_datadir}/pixmaps/

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    resources/lin/%{name}.desktop


%files
%doc NEWS README COPYING ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.25-16
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Kevin Fenzi <kevin@scrye.com> - 3.1.25-1
- Updated to 3.1.25. Fixes bug #1534997

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> 3.1.24-2
- use %%qmake_qt4 macro

* Tue Jan 05 2016 Oliver Haessler <oliver@redhat.com> - 3.1.24-1
- Update to 3.1.24

* Mon Nov 16 2015 Oliver Haessler <oliver@redhat.com> - 3.1.23-1
- Update to 3.1.23

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kevin Fenzi <kevin@scrye.com> 3.1.20-1
- Update to 3.1.20

* Wed Nov 26 2014 Nick Bebout <nb@fedoraproject.org> - 3.1.17-1
- Update to 3.1.17

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 1 2013 Maxim Burgerhout <maxim@wzzrd.com> - 3.1.11-2
- Add BR on ykpers >= 1.14.1, for clarity

* Thu Nov 28 2013 Maxim Burgerhout <maxim@wzzrd.com> - 3.1.11-1
- New upstream release 3.1.11; with support for Qt5

* Fri Aug 16 2013 Maxim Burgerhout <maxim@wzzrd.com> - 3.1.10-1
- Compared to previously built version a lot changes, like:
- Crash fixes
- Import and export capabilities
- Easier uploading of programmed keys to Yubico
- Improved NEO support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Maxim Burgerhout <maxim@wzzrd.com> - 3.1.2-1
- Update to new upstream release, supporting deleting configurations, testing
  of write operations, fixes to NDEF programming and other bugfixes.

* Wed Oct 17 2012 Maxim Burgerhout <maxim@wzzrd.com> - 3.1.1-2
- Updated for comments on RR

* Wed Oct 17 2012 Maxim Burgerhout <maxim@wzzrd.com> - 3.1.1-1
- Initial packaging
