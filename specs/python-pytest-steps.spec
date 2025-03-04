Name:		python-pytest-steps
Version:	1.7.2
Release:	%autorelease
Summary:	Create step-wise / incremental tests in pytest

License:	BSD-3-Clause
URL:		https://pypi.org/project/pytest-steps/
Source0:	%{pypi_source pytest-steps}

# Downstream-only: remove setup_requires on pytest-runner
#
# A full migration away from pytest-runner, tests_require, and "setup.py
# test" would require a more significant change, so this patch is
# inadequate for offering as a PR to upstream.
#
# The pytest-runner dependency and "setup.py test" are obsolete
# https://github.com/smarie/python-pytest-steps/issues/55
#
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch:          pytest-steps-1.7.2-no-pytest-runner.patch

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros
BuildRequires:	python3dist(pytest)

%description
%{summary}.

%package -n python3-pytest-steps
Summary: %{summary}
%{?python_provide:%python_provide python3-pytest-steps}

%description -n python3-pytest-steps
%{summary}.

%prep
%autosetup -n pytest-steps-%{version} -p1

# upstream has a pyproject.toml file, but it does not have enough stuff.
cat >pyproject.toml <<EOF
[build-system]
requires = ["pytest-harvest",
	    "setuptools_scm",
	    "pypandoc",
	    "six",
	    "wheel",
	    "wrapt",
	    "pandas",
	    "tabulate"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py
sed -r -i "s/(TESTS_REQUIRE = \[.*)\]/\1, 'wrapt'\]/" setup.py

mv -i -v pytest_steps/tests/conftest.py .

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
args=(
  --ignore=pytest_steps/tests/test_with_cases.py # avoid circular dep

  # Those fail with python-pandas-2.2.1-4.fc41~bootstrap
  --deselect=pytest_steps/tests/test_steps_harvest.py::test_synthesis
  --deselect=pytest_steps/tests/test_docs_example_with_harvest.py::test_synthesis_df
)
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest -v "${args[@]}"

%files -n python3-pytest-steps
%license LICENSE
%doc README.md
%{python3_sitelib}/pytest_steps/
%{python3_sitelib}/pytest_steps-%{version}.dist-info/

%changelog
%autochangelog
