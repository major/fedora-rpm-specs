# some test dependencies are unwanted in RHEL
%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           micropipenv
Version:        1.9.0
Release:        %autorelease
Summary:        A simple wrapper around pip to support Pipenv and Poetry files

License:        LGPL-3.0-or-later
URL:            https://github.com/thoth-station/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%py_provides    python3-%{name}

Recommends:     micropipenv+toml

%description
A lightweight wrapper for pip to support Pipenv and Poetry lock files or
converting them to pip-tools compatible output.

%pyproject_extras_subpkg -n %{name} toml

%prep
%autosetup
# Remove shebang line from the module
sed -i '1{\@^#!/usr/bin/env python@d}' %{name}.py

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-t} -x toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%if %{with tests}
# skipped tests requires internet or checks pip version
%pytest -m "not online" -k "not test_check_pip_version and not test_install_invalid_toml_file"
%else
%pyproject_check_import
%endif

%files -f %pyproject_files
%doc README.rst
%{_bindir}/micropipenv

%changelog
%autochangelog
