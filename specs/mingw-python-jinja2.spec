%{?mingw_package_header}

%global mod_name jinja2
%global pypi_name jinja2

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       3.1.5
Release:       1%{?dist}
BuildArch:     noarch

License:       BSD-3-Clause
URL:           https://palletsprojects.com/p/jinja/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-flit-core

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-flit-core


%description
MinGW Windows Python %{pypi_name} library.


%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{mod_name}
%license LICENSE.txt
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE.txt
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Jan 08 2025 Sandro Mani <manisandro@gmail.com> - 3.1.5-1
- Update to 3.1.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 07 2024 Sandro Mani <manisandro@gmail.com> - 3.1.4-1
- Update to 3.1.4

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Sandro Mani <manisandro@gmail.com> - 3.1.3-1
- Update to 3.1.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Sandro Mani <manisandro@gmail.com> - 3.0.3-6
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 3.0.3-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 3.0.3-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2.11.3-2
- Rebuild (python-3.10)

* Mon Feb 08 2021 Sandro Mani <manisandro@gmail.com> - 2.11.3-1
- Update to 2.11.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 2.11.2-4
- Switch to py3_build/py3_install macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 2.11.2-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2.11.2-1
- Update to 2.11.2

* Wed Oct 30 2019 Sandro Mani <manisandro@gmail.com> - 2.10.3-1
- Update to 2.10.3
- Switch to python3

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 2.9.6-1
- Initial package
