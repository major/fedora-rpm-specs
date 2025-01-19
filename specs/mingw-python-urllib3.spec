%{?mingw_package_header}

%global pypi_name urllib3

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name}
Version:       2.3.0
Release:       2%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://urllib3.readthedocs.io/en/latest/
Source0:       %{pypi_source}
# Switch back to flit as build-system, hatchling is not packaged for mingw
Patch0:        urllib3-no-hatch.patch

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-flit-core

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-flit-core


%description
MinGW Windows Python %{pypi_name}.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 28 2024 Sandro Mani <manisandro@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Fri Sep 13 2024 Sandro Mani <manisandro@gmail.com> - 2.2.3-1
- Update to 2.2.3

* Thu Sep 12 2024 Sandro Mani <manisandro@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Sandro Mani <manisandro@gmail.com> - 1.26.19-1
- Update to 1.26.19

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Sandro Mani <manisandro@gmail.com> - 1.26.18-1
- Update to 1.26.18

* Tue Oct 03 2023 Sandro Mani <manisandro@gmail.com> - 1.26.17-1
- Update to 1.26.17

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 1.26.16-1
- Update to 1.26.16

* Fri Jun 02 2023 Sandro Mani <manisandro@gmail.com> - 1.26.15-1
- Update to 1.26.15

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 1.26.12-2
- Switch to python3-build

* Fri Sep 23 2022 Sandro Mani <manisandro@gmail.com> - 1.26.12-1
- Update to 1.26.12

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Sandro Mani <manisandro@gmail.com> - 1.26.9-1
- Update to 1.26.9

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.26.8-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.26.8-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 Sandro Mani <manisandro@gmail.com> - 1.26.8-1
- Update to 1.26.8

* Tue Sep 28 2021 Sandro Mani <manisandro@gmail.com> - 1.26.7-1
- Update to 1.26.7

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Sandro Mani <manisandro@gmail.com> - 1.26.6-1
- Update to 1.26.6

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 1.26.5-2
- Rebuild (python-3.10)

* Wed May 26 2021 Sandro Mani <manisandro@gmail.com> - 1.26.5-1
- Update to 1.26.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 1.25.10-1
- Update to 1.25.10

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.25.7-2
- Rebuild (python-3.9)

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 1.25.7-1
- Initial package
