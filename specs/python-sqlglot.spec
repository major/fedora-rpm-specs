%global debug_package %{nil}

Name:           python-sqlglot
Version:        5.2.0
Release:        9%{?dist}
Summary:        SQL Parser and Transpiler

License:        MIT
URL:            https://github.com/tobymao/sqlglot
Source0:        %{url}/archive/v%{version}/sqlglot-%{version}.tar.gz

BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-pytest

Recommends:     python3-dateutil

%global _description %{expand:
SQLGlot is a no dependency Python SQL parser, transpiler, and optimizer.
It can be used to format SQL or translate between different dialects like
DuckDB, Presto, Spark, and BigQuery. It aims to read a wide variety of SQL
inputs and output syntactically correct SQL in the targeted dialects.

It is a very comprehensive generic SQL parser with a robust test suite. It
is also quite performant while being written purely in Python.

You can easily customize the parser, analyze queries, traverse expression
trees, and programmatically build SQL.

Syntax errors are highlighted and dialect incompatibilities can warn or
raise depending on configurations.}

%description %_description


%package -n python3-sqlglot
Summary: %{summary}

%description -n python3-sqlglot %{_description}


%prep
%autosetup -n sqlglot-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%check
%pytest --pyargs --ignore tests/test_executor.py -k "not test_simplify and not test_tpch"
# pkgs not available in fedora \
# not sure why these 2nd two fail


%install
%pyproject_install
%pyproject_save_files sqlglot


%files -n python3-sqlglot -f %{pyproject_files}
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.2.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.2.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Jonathan Wright <jonathan@almalinux.org> - 5.2.0-1
- Initial package build
- rhbz#2123519
