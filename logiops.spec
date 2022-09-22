%global commitshakey dbe2b28
%global commitshakeylong dbe2b28a5307dfc25e7b4858b94bded9acc5ea5c

Name:    logiops
Version: 0.2.3^1.git%{commitshakey}
Release: 11%{?dist}
Summary: Unofficial driver for Logitech mice and keyboard

License: GPLv3
URL:     https://github.com/PixlOne/logiops

Source0: https://github.com/PixlOne/logiops/archive/%{name}-%{commitshakeylong}.tar.gz

BuildRequires:  cmake
BuildRequires:  systemd-devel
BuildRequires:  systemd-udev
BuildRequires:  systemd-rpm-macros
BuildRequires:  libconfig-devel
BuildRequires:  libevdev-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
This is an unofficial driver for Logitech mice and keyboard.

This is currently only compatible with HID++ >2.0 devices.

%prep
%setup -q -n %{name}-%{commitshakeylong}

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%post
%systemd_post logid.service

%preun
%systemd_preun logid.service

%postun
%systemd_postun_with_restart logid.service

%files
%{_bindir}/logid
%{_unitdir}/logid.service
%license LICENSE
%doc README.md
%doc TESTED.md
%doc logid.example.cfg

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^1.gitdbe2b28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 08 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.3^1.gitdbe2b28-10
- Updated to latest commit dbe2b28 from upstream

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^1.git6bb4700-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 06 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.3^1.git6bb4700-8
- Updated to latest commit 6bb4700 from upstream

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 13 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.3-6
- New version 0.2.3

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.2-5
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 15 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.2-3
- Fix build error (thread import) see bug 1923298

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.2-1
- Initial packaging
