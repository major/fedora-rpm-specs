Name: radeon-profile-daemon
Version: 20190603
Release: 5%{?dist}
Summary: Daemon for radeon-profile GUI

License: GPLv2+
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
