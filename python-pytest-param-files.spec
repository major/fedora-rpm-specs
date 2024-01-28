Name:           python-pytest-param-files
Version:        0.3.4
Release:        7%{?dist}
Summary:        Create pytest parametrize decorators from external files

# SPDX
License:        MIT
URL:            https://pypi.org/project/pytest_param_files/
Source:         %{pypi_source pytest_param_files}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
A package to generate parametrized pytests from external files.
Create a text file with the dot format, then use the `param_file` pytest marker
to create a parametrized test.}


%description %_description

%package -n     python3-pytest-param-files
Summary:        %{summary}

%description -n python3-pytest-param-files %_description


%prep
%autosetup -p1 -n pytest_param_files-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_param_files


%check
%pytest


%files -n python3-pytest-param-files -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.4-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Karolina Surma <ksurma@redhat.com> - 0.3.4-1
- Initial package
