%{?mingw_package_header}

%global pypi_name build

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python %{pypi_name} library
Version:        0.9.0
Release:        1%{?dist}
BuildArch:      noarch

License:        MIT
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}
Source1:        macros.mingw32-python3-wheel
Source2:        macros.mingw64-python3-wheel


BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools


%description
MinGW Python %{pypi_name} library.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name} library
Requires:      mingw32-python3-installer
Requires:      mingw32-python3-setuptools
Requires:      mingw32-python3-wheel
# For %%{_rpmconfigdir}/macros.d/
Requires:      rpm

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 %{pypi_name} library.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name} library
Requires:      mingw64-python3-installer
Requires:      mingw64-python3-setuptools
Requires:      mingw64-python3-wheel
# For %%{_rpmconfigdir}/macros.d/
Requires:      rpm

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 %{pypi_name} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build
%mingw64_py3_build
%mingw32_py3_build_host
%mingw64_py3_build_host


%install
%mingw32_py3_install
%mingw64_py3_install
%mingw32_py3_install_host
%mingw64_py3_install_host

# Install macros
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw32-python3-wheel
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw64-python3-wheel


%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_bindir}/pyproject-build
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info
%{_prefix}/%{mingw32_target}/bin/pyproject-build
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info
%{_rpmconfigdir}/macros.d/macros.mingw32-python3-wheel

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_bindir}/pyproject-build
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info
%{_prefix}/%{mingw64_target}/bin/pyproject-build
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info
%{_rpmconfigdir}/macros.d/macros.mingw64-python3-wheel


%changelog
* Tue Nov 01 2022 Sandro Mani <manisandro@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Sun Oct 30 2022 Sandro Mani <manisandro@gmail.com> - 0.8.0-3
- Require rpm for %%{_rpmconfigdir}/macros.d/

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 0.8.0-2
- Switch to setuptools based build and drop bootstrap logic

* Thu Oct 13 2022 Sandro Mani <manisandro@gmail.com> - 0.8.0-1
- Initial package
