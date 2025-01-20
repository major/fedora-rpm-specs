Name: radeon-profile-daemon
Version: 20190603
Release: 12%{?dist}
Summary: Daemon for radeon-profile GUI

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/marazmista/radeon-profile-daemon
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(Qt5) >= 5.6
BuildRequires: systemd-rpm-macros

Requires: radeon-profile%{?_isa}

%description
System daemon for reading info about Radeon GPU clocks and volts as well as
control card power profiles so the GUI radeon-profile application can be run
as normal user.

Supports opensource xf86-video-ati and xf86-video-amdgpu drivers.


%prep
%autosetup -p1


%build
pushd %{name}
%qmake_qt5 %{name}.pro
%make_build
popd


%install
%make_install \
    INSTALL_ROOT=%{buildroot} \
    -C %{name}


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_pstun_with_restart %{name}.service


%files
%{_bindir}/%{name}
%{_unitdir}/*.service


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 20190603-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190603-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 20190603-1
- Initial package
