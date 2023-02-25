Name:           micropipenv
Version:        1.4.6
Release:        %autorelease
Summary:        A simple wrapper around pip to support Pipenv and Poetry files

License:        LGPLv3+
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
%pyproject_buildrequires -r -t -x toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
# skipped tests requires internet or checks pip version
%pytest -m "not online" -k "not test_check_pip_version and not test_install_invalid_toml_file"

%files -f %pyproject_files
%doc README.rst
%{_bindir}/micropipenv

%changelog
%autochangelog
