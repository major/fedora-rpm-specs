Name:           compiz-manager
Version:        0.7.0
Release:        23%{?dist}
Summary:        A wrapper script to start compiz with proper options

License:        GPL-2.0-or-later
URL:            https://github.com/raveit65/%{name}/
Source0:        https://github.com/raveit65/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch

Requires:       compiz
Requires:       xdpyinfo
Requires:       pciutils
Requires:       glx-utils
Requires:       libcompizconfig

# Already fixed in upstream git
Patch0:         compiz-manager-0.7.0-xfwm4-fix.patch


%description
This script will detect what options we need to pass to compiz to get it
started, and start a default plugin and possibly window decorator.

%prep
%autosetup -p1

%build
#no build needed

%install
mkdir -p %{buildroot}/%{_bindir}/
cp -p %{name} %{buildroot}/%{_bindir}/


%files
%doc COPYING README.md
%{_bindir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 19 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.7.0-21
- Fixed xfwm4 command name
  Related: rhbz#2269943
- Converted license tag to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 0.7.0-12
- Require xdpyinfo not xorg-x11-utils

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.0-2
- bump version because of stupid bodhi-2

* Sat Dec 19 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.0-1
- update to 0.7.0 releases
- Use different libdirs on different architectures
- Better desktop environments detection
- Cover a possible multiple resolution definition
- Avoid software rasteriser
- Drop PCI-ID blacklisting
- fix changelog

* Sat Sep 06 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.6.0-21
- add compiz-manager_improve-glx-call.patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.6.0-18
- enable fglrx in script
- fix https://bugzilla.redhat.com/show_bug.cgi?id=922123

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.6.0-16
- build for fedora

* Thu Sep 20 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.6.0-15
- improve spec file

* Tue May 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.6.0-14
- build for mate

