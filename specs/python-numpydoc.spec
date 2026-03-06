# No matplot yet in EPEL10
%if 0%{?rhel} >= 10
%bcond_with matplotlib
%else
%bcond_without matplotlib
%endif

Name:           python-numpydoc
Version:        1.9.0
Release:        %autorelease
Summary:        Sphinx extension to support docstrings in NumPy format

License:        BSD-2-Clause
URL:            https://pypi.python.org/pypi/numpydoc
Source:         %pypi_source numpydoc

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package provides the numpydoc Sphinx extension for handling docstrings
formatted according to the NumPy documentation format. The extension also adds
the code description directives np:function, np-c:function, etc.}

%description %{_description}


%package -n     python3-numpydoc
Summary:        %{summary}

%description -n python3-numpydoc %{_description}


%prep
%autosetup -p1 -n numpydoc-%{version}
# let's not measure coverage:
sed -i '/pytest-cov/d' pyproject.toml
sed -Ei 's/\s+--cov\S+//g' pyproject.toml
%if %{without matplotlib}
sed -i '/matplotlib/d' pyproject.toml
%endif

# Remove a useless shebang
sed -i '\,#!/usr/bin/env python,d' numpydoc/validate.py

%generate_buildrequires
%pyproject_buildrequires -g test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l numpydoc

%check
# Deselected tests need to download an inventory from docs.python.org
%pytest -k "not test_MyClass and not test_my_function"


%files -n python3-numpydoc -f %pyproject_files
%doc README.rst
%{_bindir}/numpydoc

%changelog
%autochangelog
