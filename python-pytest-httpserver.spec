%global srcname pytest-httpserver

%global desc %{expand: \
This library is designed to help to test http clients without contacting 
the real http server. In other words, it is a fake http server which is 
accessible via localhost can be started with the pre-defined expected 
http requests and their responses.}

Name:		python-%{srcname}
Version:	1.0.4
Release:	4%{?dist}
Summary:	HTTP server for pytest

License:	MIT
URL:		https://github.com/csernazs/pytest-httpserver
Source0:	%{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

Patch0:		pyproject.patch

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	pyproject-rpm-macros

%description
%{desc}

%package -n python3-%{srcname}
Summary:	%{summary}

%description -n python3-%{srcname} %desc

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove unnecessary dependencies
sed -i '/flake8/d' pyproject.toml
sed -i '/pytest-cov/d' pyproject.toml
sed -i '/coverage/d' pyproject.toml
sed -i '/mypy/d' pyproject.toml
sed -i '/types-requests/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_httpserver

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES.rst CONTRIBUTION.md

%changelog
* Thu Jun 22 2023 Python Maint <python-maint@redhat.com> - 1.0.4-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Ali Erdinc Koroglu <aekoroglu@fedorapackage.org> - 1.0.4-1
- Initial package
