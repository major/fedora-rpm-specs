Name: netrate
Version: 0.1
Release: 9%{?dist}
Summary: Network interface traffic meter
License: GPL-2.0-only
URL: https://github.com/mindbit/netrate
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: make

%description
netrate is a simple program that displays real-time byte and packet
count rate of network interfaces in Linux systems.

%prep
%autosetup

%build
%make_build -C src

%install
%make_install -C src

%files
%{_bindir}/netrate
%license LICENSE.md
%doc README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 02 2023 Radu Rendec <radu@rendec.net> - 0.1-4
- Update license tag to use SPDX identifiers
- Use the newer autosetup macro
- Do not call the %set_build_flags macro explicitly

* Tue Jan 04 2022 Radu Rendec <radu@rendec.net> - 0.1-3
- Use URL macro to define source URL
- Split build deps into separate BuildRequires lines

* Mon Jan 03 2022 Radu Rendec <radu@rendec.net> - 0.1-2
- Use distribution provided CFLAGS

* Thu Dec 30 2021 Radu Rendec <radu@rendec.net> - 0.1-1
- First release
