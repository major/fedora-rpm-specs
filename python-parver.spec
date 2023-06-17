%global pypi_name parver
Name:           python-%{pypi_name}
Version:        0.3.1
Release:        9%{?dist}
Summary:        Parse and manipulate version numbers

License:        MIT
URL:            https://github.com/RazerM/parver
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Parver allows parsing and manipulation of PEP 440 version numbers.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Parver allows parsing and manipulation of PEP 440 version numbers.


%prep
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test -x doctest


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files parver

%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.3.1-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0.3.1-1
- Update to 0.3.1 (#1883344)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.9

* Wed Mar 11 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-1
- Initial package
