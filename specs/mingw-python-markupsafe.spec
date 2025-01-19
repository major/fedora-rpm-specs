%{?mingw_package_header}

%global mod_name markupsafe

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{mod_name} library
Version:       3.0.2
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD-3-Clause
URL:           https://pypi.org/project/MarkupSafe/
Source0:       %{pypi_source markupsafe}

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-gcc
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{mod_name} library.


%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{mod_name} library

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{mod_name} library.


%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{mod_name} library

%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{mod_name} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{mod_name}-%{version}
# Allow older setuptools
sed -i '/setuptools/s/>=.*"/"/' pyproject.toml


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{mod_name}
%license LICENSE.txt
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/MarkupSafe-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE.txt
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/MarkupSafe-%{version}.dist-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 30 2024 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 27 2024 Sandro Mani <manisandro@gmail.com> - 2.1.5-1
- Update to 2.1.5

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Mon Jan 30 2023 Sandro Mani <manisandro@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Sandro Mani <manisandro@gmail.com> - 2.1.1-4
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.1.1-2
- Rebuild with mingw-gcc-12

* Mon Mar 21 2022 Sandro Mani <manisandro@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.0.1-5
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.0.1-4
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Sandro Mani <manisandro@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 1.1.1-5
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 1.1.1-3
- Switch to py3_build/py3_install macros

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.1.1-2
- Rebuild (python-3.9)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.1.1-1
- Initial package
