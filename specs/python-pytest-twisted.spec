%global pypi_name pytest-twisted
%global srcname pytest_twisted

Name:           python-%{pypi_name}
Version:        1.14.3
Release:        3%{?dist}
Summary:        Twisted plugin for pytest

License:        BSD-3-Clause
URL:            https://github.com/pytest-dev/pytest-twisted
Source0:        %{pypi_source %{srcname}}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
pytest-twisted is a plugin for pytest, which allows to test code, which uses
the twisted framework.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t -e %{toxenv}-defaultreactor


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
%tox -e %{toxenv}-defaultreactor,%{toxenv}-asyncioreactor


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.14.3-2
- Rebuilt for Python 3.14

* Tue Apr 08 2025 Aurelien Bompard <abompard@fedoraproject.org> - 1.14.3-1
- Initial package.
