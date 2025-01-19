%{?mingw_package_header}

%global mod_name shapely
%global pypi_name shapely

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2.0.6
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD-3-Clause
URL:           https://github.com/Toblerity/Shapely
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-gcc
BuildRequires: mingw32-geos
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-Cython
BuildRequires: mingw32-python3-numpy

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-gcc
BuildRequires: mingw64-geos
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-Cython
BuildRequires: mingw64-python3-numpy


%description
MinGW Windows Python %{pypi_name} library.


%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
# See Patch0
Requires:      mingw32(libgeos_c-1.dll)

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{mod_name} library
# See Patch0
Requires:      mingw64(libgeos_c-1.dll)

%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.

%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# We don’t need the “oldest supported numpy” in the RPM build, and the
# metapackage in question (https://pypi.org/project/oldest-supported-numpy/) is
# not packaged. Just depend on numpy.
sed -r -i \
    -e 's/oldest-supported-(numpy)/\1/' \
    pyproject.toml


%build
export GEOS_INCLUDE_PATH=%{mingw32_includedir}/geos
export GEOS_LIBRARY_PATH=%{mingw32_libdir}
%mingw32_py3_build_wheel
export GEOS_INCLUDE_PATH=%{mingw64_includedir}/geos
export GEOS_LIBRARY_PATH=%{mingw64_libdir}
%mingw64_py3_build_wheel


%install
export NO_GEOS_CONFIG=1
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 21 2024 Sandro Mani <manisandro@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Sandro Mani <manisandro@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Thu Apr 18 2024 Sandro Mani <manisandro@gmail.com> - 2.0.4-1
- Update to 2.0.4

* Fri Feb 16 2024 Sandro Mani <manisandro@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Sandro Mani <manisandro@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 1.8.5-1
- Update to 1.8.5
- Switch to python3-build

* Tue Aug 30 2022 Sandro Mani <manisandro@gmail.com> - 1.8.4-1
- Update to 1.8.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Sandro Mani <manisandro@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.8.1-2
- Rebuild with mingw-gcc-12

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.8.0-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.8.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Sandro Mani <manisandro@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 1.7.1-6
- Rebuild (geos)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 1.7.1-4
- Rebuild (python-3.10)

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 1.7.1-3
- Rebuild (geos)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.7a2-2
- Rebuild (python-3.9)

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 1.7a2-1
- Initial package
