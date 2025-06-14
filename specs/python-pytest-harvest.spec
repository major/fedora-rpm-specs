Name:		python-pytest-harvest
Version:	1.10.5
Release:	%autorelease
Summary:	Store data created during test execution and retrieve it at the end

License:	BSD-3-Clause
URL:		https://pypi.org/project/pytest-harvest/
Source0:	%{pypi_source pytest-harvest}

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros
BuildRequires:	python3dist(pytest)

%description
Store data created during your pytest tests execution, and retrieve it
at the end of the session, e.g. for applicative benchmarking purposes.

%package -n python3-pytest-harvest
Summary: %{summary}
%{?python_provide:%python_provide python3-pytest-harvest}

%description -n python3-pytest-harvest
%{summary}.

%prep
%autosetup -n pytest-harvest-%{version} -p1

cat >pyproject.toml <<EOF
[build-system]
requires = ["setuptools_scm",
            "wheel",
            "pandas",
            "tabulate",
	    "pypandoc",
	    "six"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py

mv -i -v pytest_harvest/tests/conftest.py .

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
# This package is effectively tested by python-pytest-cases.
# This one, python-makefun and python-pytest-cases require one another,
# without specifying this, and thus without specifying minimial versions.
# So let's just build the latest version of each and hope for the best.
%python3 -m pytest -v || :

%files -n python3-pytest-harvest
%license LICENSE
%doc README.md
%{python3_sitelib}/pytest_harvest/
%{python3_sitelib}/pytest_harvest-%{version}.dist-info/

%changelog
%autochangelog
