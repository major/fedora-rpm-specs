Name:           python-tomli
Version:        2.0.1
Release:        5%{?dist}
Summary:        A little TOML parser for Python

License:        MIT
URL:            https://pypi.org/project/tomli/
Source0:        https://github.com/hukkin/tomli/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# The test suite uses the stdlib's unittest framework, but we use %%pytest
# as the test runner.
BuildRequires:  python3-pytest

%global _description %{expand:
Tomli is a Python library for parsing TOML.
Tomli is fully compatible with TOML v1.0.0.}


%description %_description

%package -n python3-tomli
Summary:        %{summary}

%description -n python3-tomli %_description


%prep
%autosetup -p1 -n tomli-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tomli


%check
%py3_check_import tomli
%pytest


%files -n python3-tomli -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%license LICENSE


%changelog
* Fri Oct 07 2022 Maxwell G <gotmax@e.email> - 2.0.1-5
- Remove incorrect python3-dateutil test BuildRequires

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.1-2
- Bootstrap for Python 3.11

* Thu Mar 03 2022 Petr Viktorin <pviktori@redhat.com> - 2.0.1-1
- Version 2.0.1
  - Removed support for text file objects as load input
  - First argument of load and loads can no longer be passed by keyword
  - Raise an error when dotted keys define values outside the "current table"
  - Prepare for inclusion in stdlib

* Wed Feb 02 2022 Petr Viktorin <pviktori@redhat.com> - 1.2.3-1
- Update to 1.2.3
  - Allow lower case "t" and "z" in datetimes

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 29 2021 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Allow a bootstrap build without flit_core

* Wed Oct 27 2021 Petr Viktorin <pviktori@redhat.com> - 1.2.2-1
- Update to version 1.2.2

* Wed Aug 18 2021 Petr Viktorin <pviktori@redhat.com> - 1.2.1-1
- Update to version 1.2.1
  - loading text (as opposed to binary) files is deprecated

* Thu Jul 29 2021 Petr Viktorin <pviktori@redhat.com> - 1.1.0-1
- Update to version 1.1.0
  - `load` can now take a binary file object

* Thu Jul 22 2021 Petr Viktorin <pviktori@redhat.com> - 1.0.4-1
- Initial package
