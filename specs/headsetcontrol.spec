Name:           headsetcontrol
Version:        3.0.0
Release:        4%{?dist}
Summary:        A tool to control certain aspects of USB-connected headsets on Linux
# The entire source code is GPLv3+ except cmake_modules/Findhidapi.cmake which is Boost
# Automatically converted from old format: GPLv3+ and Boost - review is highly recommended.
License:        GPL-3.0-or-later AND BSL-1.0 
URL:            https://github.com/Sapd/HeadsetControl
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         3.0.0_build_fix.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  hidapi-devel

%description
A tool to control certain aspects of USB-connected headsets on Linux

%prep
%setup -q -n HeadsetControl-%{version}
%patch -P0 -p1

%build
%cmake
%cmake_build


%install
%cmake_install

%check
%ctest

%files
%{_bindir}/headsetcontrol
%{_prefix}/lib/udev/rules.d/70-headsets.rules
%license license
%doc README.md



%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Mohan Boddu <mboddu@bhujji.com> - 3.0.0-1
- Update to 3.0.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Mohan Boddu <mboddu@bhujji.com> - 2.7.0-1
- Update to 2.7.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 06 2023 Mohan Boddu <mboddu@bhujji.com> - 2.6.1-1
- Update to 2.6.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Mohan Boddu <mboddu@bhujji.com> - 2.4-1
- First import of version 2.4
