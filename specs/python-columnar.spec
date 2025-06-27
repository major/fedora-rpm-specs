%global pypi_name columnar
%global pypi_version 1.4.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        3%{?dist}
Summary:        A tool for printing data in a columnar format

License:        MIT
URL:            https://pypi.org/project/columnar/
Source0:        %{pypi_source Columnar}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A library for creating columnar output strings using data as input.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A library for creating columnar output strings using data as input.

%prep
%autosetup -n Columnar-%{pypi_version}

cat <<EOF> testfile.py
from columnar import columnar

headers = ['name', 'id', 'host', 'notes']

data = [
    ['busybox', 'c3c37d5d-38d2-409f-8d02-600fd9d51239', 'linuxnode-1-292735', 'Test server.'],
    ['alpine-python', '6bb77855-0fda-45a9-b553-e19e1a795f1e', 'linuxnode-2-249253', 'The one that runs python.'],
    ['redis', 'afb648ba-ac97-4fb2-8953-9a5b5f39663e', 'linuxnode-3-3416918', 'For queues and stuff.'],
    ['app-server', 'b866cd0f-bf80-40c7-84e3-c40891ec68f9', 'linuxnode-4-295918', 'A popular destination.'],
    ['nginx', '76fea0f0-aa53-4911-b7e4-fae28c2e469b', 'linuxnode-5-292735', 'Traffic Cop'],
]

table = columnar(data, headers, no_borders=True)
print(table)
EOF

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%py3_test_envvars %python3 testfile.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Wed Jun 25 2025 Python Maint <python-maint@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.14

* Mon May 19 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-2
- Review fixes.

* Wed May 08 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- Initial package.
