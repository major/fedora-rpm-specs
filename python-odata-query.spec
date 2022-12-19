Name:           python-odata-query
Version:        0.7.1
Release:        1%{?dist}
Summary:        An OData v4 query parser and transpiler for Python

License:        MIT
URL:            https://odata-query.readthedocs.io
Source0:        https://github.com/gorilla-co/odata-query/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
odata-query is a library that parses OData v4 filter strings, and can convert
them to other forms such as Django Queries, SQLAlchemy Queries, or just plain
SQL.}

%description %_description

%package -n python3-odata-query
Summary:        %{summary}

%description -n python3-odata-query %_description

%pyproject_extras_subpkg -n python3-odata-query django sqlalchemy

%prep
%autosetup -p1 -n odata-query-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files odata_query


%check
%tox


%files -n python3-odata-query -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Sat Dec 17 2022 Roman Inflianskas <rominf@aiven.io> - 0.7.1-1
- Update to 0.7.1 (resolves rhbz#2093198)

* Tue Nov 08 2022 Roman Inflianskas <rominf@aiven.io> - 0.7.0-1
- Update to 0.7.0 (#2093198)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.11

* Tue Mar 15 2022 Roman Inflianskas <rominf@aiven.io> - 0.5.2-1
- Update to 0.5.2 (#2063780)

* Thu Mar 03 2022 Roman Inflianskas <rominf@aiven.io> - 0.5.1-1
- Update to 0.5.1
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Roman Inflianskas <rominf@aiven.io> - 0.4.2-2
- Enable sqlalchemy extra and tests where possible
* Mon Dec 20 2021 Roman Inflianskas <rominf@aiven.io> - 0.4.2-1
- Update to 0.4.2 (documentation improvements)
* Fri Dec 10 2021 Roman Inflianskas <rominf@aiven.io> - 0.4.1-1
- Initial package
