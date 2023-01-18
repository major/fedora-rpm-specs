%{?mingw_package_header}

%global pypi_name lxml

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       4.9.2
Release:       1%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://lxml.de/
Source0:       %{pypi_source}
# Don't attempt to link against librt
Patch0:        lxml-rt.patch

BuildRequires: libxslt-devel

BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-libxslt
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-Cython

BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-libxslt
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-Cython


%description
MinGW Windows Python %{pypi_name} library.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%{?mingw_debug_package}


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
* Mon Jan 16 2023 Sandro Mani <manisandro@gmail.com> - 4.9.2-1
- Update to 4.9.2

* Tue Oct 11 2022 Sandro Mani <manisandro@gmail.com> - 4.9.1-2
- Switch to python3-build

* Thu Sep 15 2022 Sandro Mani <manisandro@gmail.com> - 4.9.1-1
- Update to 4.9.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 4.7.1-6
- Rebuild with mingw-gcc-12

* Thu Mar 17 2022 Sandro Mani <manisandro@gmail.com> - 4.7.1-5
- Rebuild

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 4.7.1-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 4.7.1-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 18 2021 Sandro Mani <manisandro@gmail.com> - 4.7.1-1
- Update to 4.7.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 4.6.3-2
- Rebuild (python-3.10)

* Wed May 26 2021 Sandro Mani <manisandro@gmail.com> - 4.6.3-1
- Update to 4.6.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Sandro Mani <manisandro@gmail.com> - 4.6.2-1
- Update to 4.6.2

* Tue Sep 22 2020 Sandro Mani <manisandro@gmail.com> - 4.5.1-1
- Update to 4.5.1
- Exclude debug files in main package

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 4.4.1-2
- Rebuild (python-3.9)

* Wed Nov 20 2019 Sandro Mani <manisandro@gmail.com> - 4.4.1-1
- Update to 4.4.1
