Name:           python-decopatch
Version:        1.4.10
Release:        %autorelease
Summary:        Helper to write python decorators

License:        BSD-3-Clause
URL:            https://pypi.org/project/decopatch
Source:	        %{pypi_source decopatch}
Patch:          0001-Adjust-for-whitespace-changes-with-python-3.12.patch
# Drop the pytest-runner dependency
# https://github.com/smarie/python-decopatch/pull/38
Patch:          decopatch-1.4.10-no-pytest-runner.patch

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros

# There is a build dependency loop when built with tests.
# It involves pytest-cases, pytest-harvest, pytest-steps.
# This bcons allows to bootstrap it.
%bcond tests 1

%global _description %{expand:
Because of a tiny oddity in the python language, writing decorators without help
can be a pain because you have to handle the no-parenthesis usage explicitly.
Decopatch provides a simple way to solve this issue so that writing decorators
is simple and straightforward.}

%description %_description

%package -n python3-decopatch
Summary: %{summary}

%description -n python3-decopatch %_description

%prep
%autosetup -p 1 -n decopatch-%{version}
cat >pyproject.toml <<EOF
[build-system]
requires = ["setuptools_scm"%{?with_tests:, "pypandoc", "pytest", "pytest-cases"}]
build-backend = "setuptools.build_meta"
EOF

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files decopatch

%check
%if %{with tests}
TEST_ARGS=(
  # Test fails with whitespace differences in Python 3.13
  --deselect=tests/test_doc.py::test_doc_add_tag_function
)
PYTHONPATH=build/lib %python3 -m pytest -v "${TEST_ARGS[@]}"
%else
%pyproject_check_import
%endif

%files -n python3-decopatch
%license LICENSE
%doc README.md
%{python3_sitelib}/decopatch/
%{python3_sitelib}/decopatch-%{version}.dist-info/

%changelog
%autochangelog
