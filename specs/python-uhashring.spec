%global module uhashring

Name:           python-%{module}
Version:        2.3
Release:        8%{?dist}
Summary:        Python module uhashring

License:        BSD-3-Clause
URL:            https://github.com/ultrabug/uhashring/
Source:         https://github.com/ultrabug/%{module}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Required to run unit tests
BuildRequires:  python3-pytest
BuildRequires:  python3-memcached

%global _description %{expand:
uhashring implements consistent hashing in pure Python.}

%description %_description

%package -n python3-%{module}
Summary:        %{summary}

%description -n python3-%{module}
%_description

%prep
%autosetup -p1 -n %{module}-%{version}

sed -i 's/ *"black",//g' pyproject.toml
sed -i 's/ *"flake8",//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{module}

%check
%pytest

%files -n python3-%{module} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Alfredo Moralejo <amoralej@redhat.com> - 2.3-2
- Update to 2.3

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Alfredo Moralejo <amoralej@redhat.com> - 2.1-1
- Initial build with version 2.1 

