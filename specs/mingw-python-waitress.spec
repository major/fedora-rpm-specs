%{?mingw_package_header}

%global mod_name waitress
%global pypi_name waitress

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       3.0.2
Release:       1%{?dist}
BuildArch:     noarch

License:       ZPL-2.1
URL:           https://github.com/Pylons/waitress
# Remove docs folder it is released under the non-free
# Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License
# See CONTRIBUTORS.txt
# Generate with ./waitress-tarball-nodocs.sh $version
Source0:       waitress-%{version}-nodocs.tar.xz
Source1:       waitress-tarball-nodocs.sh

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


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
%autosetup -p1 -n %{pypi_name}-%{version}-nodocs


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{mod_name}
%license LICENSE.txt
%{mingw32_bindir}/waitress-serve
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE.txt
%{mingw64_bindir}/waitress-serve
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Feb 07 2025 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 31 2024 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Sandro Mani <manisandro@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Sandro Mani <manisandro@gmail.com> - 2.1.2-2
- Use cleaned source tarball without docs

* Tue Nov 01 2022 Sandro Mani <manisandro@gmail.com> - 2.1.2-1
- Initial package
