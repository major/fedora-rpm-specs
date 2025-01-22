%global pypi_name mbstrdecoder

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        1%{?dist}
Summary:        multi-byte character string decoder

License:        MIT
URL:            https://github.com/thombashi/mbstrdecoder 
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz 
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
multi-byte character string decoder

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:  python3-chardet

%description -n python3-%{pypi_name}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's/chardet>=3.0.4,<.*/chardet>=3.0.4/g' requirements/requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files} 
%license LICENSE
%doc README.rst

%changelog
* Mon Jan 20 2025 Joel Capitao <jcapitao@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.2-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.2-2
- Rebuilt for Python 3.12

* Tue Feb 07 2023 Karolina Kula <kkula@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Karolina Kula <kkula@redhat.com> - 1.1.0-2
- Remove chardet <5 requirement
- Remove %python_provide depracated macros
- Add pytest as BR

* Thu May 19 2022 Karolina Kula <kkula@redhat.com> - 1.1.0-1
- initial package build

