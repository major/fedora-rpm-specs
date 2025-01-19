Name:           libnitrokey
Version:        3.7
Release:        8%{?dist}
Summary:        Communicate with Nitrokey stick devices in a clean and easy manner

License:        LGPL-3.0-or-later
URL:            https://github.com/Nitrokey/libnitrokey
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)

%description
Libnitrokey is a project to communicate with Nitrokey Pro and Storage devices
in a clean and easy manner.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains development libraries and header files are needed
to develop using libnitrokey.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%post	
%udev_rules_update

%postun
%udev_rules_update

%files
%license LICENSE
%doc README.md
%{_libdir}/libnitrokey.so.*
%{_udevrulesdir}/*-nitrokey.rules

%files devel
%{_libdir}/libnitrokey.so
%{_libdir}/pkgconfig/libnitrokey-1.pc
%{_includedir}/libnitrokey/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 3.7-6
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.7-1
- Update to 3.7 (RHBZ #1870893)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5-1
- Update to 3.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Hughes <tom@compton.nu> - 3.4.1-2
- Patch for changes in catch2 pkg-config module name

* Wed Jul 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1

* Tue Jul 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4-1
- Update to 3.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Ed Marshall <esm@logic.net> - 3.3-1
- Update to 3.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1-2
- Switch to %%ldconfig_scriptlets

* Tue Oct 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1-1
- Update to 3.1

* Sat Oct 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0-0.2.20171007git.fa871ec
- Update to latest snapshot

* Sat Oct 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0-0.1.20171007git.544f69c
- Initial package
