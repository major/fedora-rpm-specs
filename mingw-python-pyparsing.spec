%{?mingw_package_header}

%global pypi_name pyparsing

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python %{pypi_name}
Version:        2.4.7
Release:        5%{?dist}
BuildArch:      noarch

License:        MIT
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}


BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools


%description
MinGW Python %{pypi_name}.


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
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}.py
%{mingw32_python3_sitearch}/__pycache__/%{pypi_name}.*
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}.py
%{mingw64_python3_sitearch}/__pycache__/%{pypi_name}.*
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw64_python3_version}.egg-info/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.4.7-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.4.7-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sandro Mani <manisandro@gmail.com> - 2.4.7-1
- Initial package
