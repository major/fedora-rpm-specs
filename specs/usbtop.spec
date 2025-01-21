Name:           usbtop
Version:        1.0
Release:        14%{?dist}
Summary:        Utility to show USB bandwidth
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/aguinet/usbtop
Source0:        %{url}/archive/release-%{version}/usbtop-%{version}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  boost-devel >= 1.48.0


%description
usbtop is a top-like utility that shows an estimated instantaneous bandwidth on
USB buses and devices.


%prep
%autosetup -n usbtop-release-%{version}
rm -rf third-party


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install
install -d %{buildroot}%{_modulesloaddir}
echo usbmon > %{buildroot}%{_modulesloaddir}/usbtop.conf


%post
modprobe usbmon &> /dev/null || :


%files
%license LICENSE
%doc README.md CHANGELOG
%{_sbindir}/usbtop
%{_modulesloaddir}/usbtop.conf


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Carl George <carl@george.computer> - 1.0-2
- BuildRequires systemd-rpm-macros and use %%_modulesloaddir
- Use %%autosetup

* Tue Sep 03 2019 Carl George <carl@george.computer> - 1.0-1
- Initial package rhbz#1748678
