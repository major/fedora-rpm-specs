Name:           python-parameterized
Version:        0.9.0
Release:        %autorelease
Summary:        Parameterized testing with any Python test framework

License:        BSD-2-Clause-Views
URL:            https://github.com/wolever/parameterized
# CHANGELOG.txt is no longer included in the PyPI sdist
# https://github.com/wolever/parameterized/issues/168
# Source:         %%{pypi_source parameterized}
Source:         %{url}/archive/v%{version}/parameterized-%{version}.tar.gz

# Remove the usage of assertRaisesRegexp unit test alias removed in Python 3.12
Patch:          https://github.com/wolever/parameterized/pull/169.patch

# Fix tests to handle Python 3.13 stripping indents from docstrings
Patch:          https://github.com/wolever/parameterized/pull/176.patch

# Remove test dependency on PyPI mock
#
# Use `unittest.mock` from the Python standard library instead.
#
# https://fedoraproject.org/wiki/Changes/DeprecatePythonMock
Patch:          https://github.com/wolever/parameterized/pull/186.patch

BuildSystem:            pyproject
BuildOption(install):   -l parameterized
# - parameterized.test is only importable when running the tests
BuildOption(check):     -e parameterized.test

BuildArch:      noarch

# Upstream supports tox, and in theory we could generate these by something like:
#   %%pyproject_buildrequires -t -e %%{toxenv}-nose2,%%{toxenv}-pytest4,%%{toxenv}-unit
# but upstream is not keeping up, and we would also have to patch in support
# for environments after py311. It’s not worth it; we can more easily run the
# tests manually and specify the BR’s manually. See %%check.
BuildRequires:  %{py3_dist nose2}
BuildRequires:  %{py3_dist pytest}

%description
%{summary}.


%package -n python3-parameterized
Summary:        %{summary}

%description -n python3-parameterized
%{summary}.


%prep -a
# Workaround for:
#   Support pytest7
#   https://github.com/wolever/parameterized/issues/167
sed -r -i 's/assert_equal\(missing/# &/' parameterized/test.py


%check -a
%{py3_test_envvars} %{python3} -m nose2 -v
%pytest parameterized/test.py
%{py3_test_envvars} %{python3} -m unittest -v parameterized.test


%files -n python3-parameterized -f %{pyproject_files}
%doc CHANGELOG.txt README.rst


%changelog
%autochangelog
