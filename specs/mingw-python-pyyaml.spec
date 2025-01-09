%{?mingw_package_header}

%global mod_name pyyaml

Name:          mingw-python-%{mod_name}
Version:       6.0.2
Release:       1%{?dist}
Summary:       MinGW Windows Python %{mod_name} library
BuildArch:     noarch

License:       MIT
URL:           https://github.com/yaml/pyyaml
Source0:       %{pypi_source pyyaml}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-Cython

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-Cython


%description
MinGW Windows Python %{mod_name} library.


%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python2 %{mod_name} library

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python2 %{mod_name} library.


%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python2 %{mod_name}

%description -n mingw64-python3-%{mod_name}
MinGW Windows Python2 %{mod_name} library.


%prep
%autosetup -p1 -n %{mod_name}-%{version}
chmod a-x examples/yaml-highlight/yaml_hl.py
# remove pre-generated file
rm -rf ext/_yaml.c
# we have a patch for Cython 3
sed -i 's/Cython<3.0/Cython/' pyproject.toml


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{mod_name}
%license LICENSE
%{mingw32_python3_sitearch}/yaml/
%{mingw32_python3_sitearch}/_yaml/
%{mingw32_python3_sitearch}/PyYAML-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE
%{mingw64_python3_sitearch}/yaml/
%{mingw64_python3_sitearch}/_yaml/
%{mingw64_python3_sitearch}/PyYAML-%{version}.dist-info/


%changelog
* Tue Jan 07 2025 Sandro Mani <manisandro@gmail.com> - 6.0.2-1
- Update to 6.0.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 6.0.1-1
- Update to 6.0.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 13 2022 Sandro Mani <manisandro@gmail.com> - 6.0-7
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.0-5
- Rebuild with mingw-gcc-12

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 6.0-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 6.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Sandro Mani <manisandro@gmail.com> - 6.0.0-1
- Update to 6.0.0

* Tue Aug 10 2021 Sandro Mani <manisandro@gmail.com> - 5.4.1-1
- Update to 5.4.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 5.3.1-3
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 5.3.1-2
- Update to 5.3.1

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 5.1.2-2
- Rebuild (python-3.9)

* Sun Nov 03 2019 Sandro Mani <manisandro@gmail.com> - 5.1.2-1
- Update to 5.1.2

* Mon Apr 29 2019 Sandro Mani <manisandro@gmail.com> - 5.1-1
- Initial package
