%bcond_without tests

%global forgeurl https://github.com/pychess/scoutfish
%global commit b619262405d19ae8831fd91b2b29bd85c5b23d84
%forgemeta

Name:           scoutfish
Version:        1.1
Release:        10%{?dist}
Summary:        Chess Query Engine 

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
# PR#7 Added handling of Chess 960 PGNs, fixed offsets for extra newlines
Patch0:         %{url}/pull/7.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  sed
%if %{with tests}
BuildRequires:  python3dist(pexpect)
%endif

%description
Scoutfish lets you run powerful and flexible queries on very big chess
databases and with very high speed.

%prep
%autosetup -n %{name}-%{commit} -p1
# Fix python shebang
sed -e 's:/usr/bin/env python:/usr/bin/python3:' -i src/*.py
# Drop arch bitness flags as they break the build on ARM
sed -e 's:-m$(bits)::g' -i src/Makefile

%build
pushd src
%make_build build \
  ARCH="general-%{__isa_bits}" \
  EXTRACXXFLAGS="%{optflags}" \
  EXTRALDFLAGS="${build_ldflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 src/scoutfish %{buildroot}%{_bindir}/

%if %{with tests}
%check
pushd src
%python3 test.py
%endif

%files
%license Copying.txt
%doc README.md src/scoutfish.py
%{_bindir}/scoutfish

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-9
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May  9 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.1-1.20210509gitb619262
- Initial package
