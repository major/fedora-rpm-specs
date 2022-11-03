%{?mingw_package_header}

%global pypi_name toml

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python %{pypi_name}
Version:        0.10.2
Release:        6%{?dist}
BuildArch:      noarch

License:        MIT
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}


BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build


%description
MinGW Python %{pypi_name}


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name}

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 %{pypi_name}.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name}

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 %{pypi_name}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


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
* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 0.10.2-6
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 0.10.2-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 0.10.2-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sandro Mani <manisandro@gmail.com> - 0.10.2-1
- Initial package
