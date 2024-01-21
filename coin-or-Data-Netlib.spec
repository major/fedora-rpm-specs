%global		module		Data-Netlib

Name:		coin-or-%{module}
Summary:	COIN-OR Netlib models
Version:	1.2.9
Release:	9%{?dist}
License:	EPL-1.0
URL:		https://www.coin-or.org/download/pkgsource/Data
Source0:	%{url}/%{module}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(zlib)

%description
This package contains the COmputational INfrastructure for Operations
Research (COIN-OR) models from netlib for testing.

%prep
%autosetup -n %{module}-%{version}

# We cannot regenerate the configure script due to missing macro definitions.
# However, the existing configure script will soon stop working due to
# https://fedoraproject.org/wiki/Changes/PortingToModernC
# Munge the script for now until we can get upstream to fix the issue.
sed -i '/ctype\.h/i#include <stdlib.h>' configure

%build
%configure
%make_build

%install
%make_install pkgconfiglibdir=%{_datadir}/pkgconfig

%files
%{_datadir}/coin/
%{_datadir}/pkgconfig/coindatanetlib.pc

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Jerry James <loganjerry@gmail.com> - 1.2.9-1
- Version 1.2.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Jerry James <loganjerry@gmail.com> - 1.2.8-1
- Initial RPM
