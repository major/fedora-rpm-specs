Name:           headsetcontrol
Version:        2.4
Release:        5%{?dist}
Summary:        A tool to control certain aspects of USB-connected headsets on Linux
# The entire source code is GPLv3+ except cmake_modules/Findhidapi.cmake which is Boost
License:        GPLv3+ and Boost 
URL:            https://github.com/Sapd/HeadsetControl
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/Sapd/HeadsetControl/issues/159
Source1:        https://www.boost.org/LICENSE_1_0.txt

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  hidapi-devel

%description
A tool to control certain aspects of USB-connected headsets on Linux

%prep
%setup -q -n HeadsetControl-%{version}
cp %{SOURCE1} license.boost

%build
%cmake
%cmake_build


%install
%cmake_install

%check
%ctest

%files
%{_bindir}/headsetcontrol
%license license license.boost
%doc README.md



%changelog
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
