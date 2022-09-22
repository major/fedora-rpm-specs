%{?mingw_package_header}

%global pypi_name packaging

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python packaging core utils
Version:        21.3
Release:        5%{?dist}
BuildArch:      noarch

License:        BSD or ASL 2.0
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}


BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools


%description
MinGW Python packaging core utils.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 packaging core utils
Requires:      mingw32-python3-pyparsing

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 packaging core utils.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 packaging core utils
Requires:      mingw64-python3-pyparsing

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 packaging core utils.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pypi_name}
%license LICENSE.BSD LICENSE.APACHE LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.BSD LICENSE.APACHE LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw64_python3_version}.egg-info/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 21.3-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 21.3-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Sandro Mani <manisandro@gmail.com> - 21.3-1
- Update to 21.3

* Tue Nov 02 2021 Sandro Mani <manisandro@gmail.com> - 21.2-1
- Update to 21.2

* Mon Sep 20 2021 Sandro Mani <manisandro@gmail.com> - 21.0-2
- Also include LICENSE in %%license
- Require: mingw-python-pyparsing

* Tue Sep 14 2021 Sandro Mani <manisandro@gmail.com> - 21.0-1
- Initial package
