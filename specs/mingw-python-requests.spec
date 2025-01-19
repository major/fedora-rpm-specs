%{?mingw_package_header}

%global pypi_name requests

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2.32.3
Release:       3%{?dist}
BuildArch:     noarch

License:       Apache-2.0
URL:           https://requests.readthedocs.io/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{pypi_name}.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}
Requires:      mingw32-python3-certifi

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}
Requires:      mingw64-python3-certifi

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Strip env shebang in nonexecutable file
sed -i '/#!\/usr\/.*python/d' src/requests/certs.py


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Sandro Mani <manisandro@gmail.com> - 2.32.3-1
- Update to 2.32.3

* Tue May 21 2024 Sandro Mani <manisandro@gmail.com> - 2.32.0-1
- Update to 2.32.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 25 2023 Sandro Mani <manisandro@gmail.com> - 2.31.0-1
- Update to 2.31.0

* Thu Feb 02 2023 Sandro Mani <manisandro@gmail.com> - 2.28.2-1
- Update to 2.28.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 13 2022 Sandro Mani <manisandro@gmail.com> - 2.28.1-3
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Sandro Mani <manisandro@gmail.com> - 2.28.1-1
- Update to 2.28.1

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 2.27.1-5
- Allow charset normalizer >=2 and <3

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.27.1-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.27.1-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Sandro Mani <manisandro@gmail.com> - 2.27.1-1
- Update to 2.27.1

* Fri Jul 30 2021 Sandro Mani <manisandro@gmail.com> - 2.26.0-1
- Update to 2.26.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2.25.1-2
- Rebuild (python-3.10)

* Wed Feb 03 2021 Sandro Mani <manisandro@gmail.com> - 2.25.1-1
- Update to 2.25.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Sandro Mani <manisandro@gmail.com> - 2.25.0-1
- Update to 2.25.0

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 2.24.0-3
- Switch to py3_build/py3_install macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Sandro Mani <manisandro@gmail.com> - 2.24.0-1
- Update to 2.24.0

* Thu Jun 25 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-3
- Be more specific in %%files
- Fix license
- Strip env shebang in nonexecutable file

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-1
- Update to 2.23.0

* Fri Dec 06 2019 Sandro Mani <manisandro@gmail.com> - 2.22.0-1
- Initial package
