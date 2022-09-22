%bcond_without tests

%global _description %{expand:
In computer science, a topological sort (sometimes abbreviated topsort or
toposort) or topological ordering of a directed graph is a linear ordering of
its vertices such that for every directed edge uv from vertex u to vertex v, u
comes before v in the ordering.}

Name:           python-toposort
Version:        1.7
Release:        4%{?dist}
Summary:        Implements a topological sort algorithm

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/toposort
Source0:        %{pypi_source toposort}
BuildArch:      noarch

%description %_description

%package -n python3-toposort
Summary:        Implements a topological sort algorithm
BuildRequires:  python3-devel

%description -n python3-toposort %_description

%prep
%autosetup -n toposort-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files toposort

%check
%if %{with tests}
PYTHONPATH="${PWD}:%{buildroot}%{python3_sitelib}" \
    '%{python3}' -m test.test_toposort
%endif

%files -n python3-toposort -f %{pyproject_files}
# pyproject_files handles LICENSE.txt and NOTICE; verify with “rpm -qL -p …”
%doc CHANGES.txt
%doc README.txt

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.7-1
- Update to 1.7 (close RHBZ#2032681)
- Port to pyproject-rpm-macros (a necessity; upstream drops setup.py)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 1.6-1
- Updated to v1.6

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 1.5.0-1
- Initial build
