%bcond tests 1

# For scidash
%global scidash_commit 5d47042d3eb40abcb062ba15f90f64d4d208d433
%global scidash_shortcommit     %(c=%{scidash_commit}; echo ${c:0:7})

%global _description %{expand:
A framework for validating scientific models by creating
experimental-data-driven unit tests.}

Name:           python-sciunit
Version:        0.2.8
Release:        %autorelease
Summary:        Framework for test-driven validation of scientific models

License:        MIT
URL:            http://sciunit.io/

# For tagged releases on Github: pypi does not include docs etc.
Source0:        https://github.com/scidash/sciunit/archive/v%{version}/sciunit-%{version}.tar.gz

# Required for tests
# https://github.com/scidash/sciunit/blob/0.2.2/test.sh#L3
Source1:        https://github.com/scidash/scidash/archive/%{scidash_commit}/scidash-%{scidash_shortcommit}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-sciunit
Summary:        %{summary}
BuildRequires:  git-core
BuildRequires:  python3-devel

# Part of sciunit/utils.py (marked by a comment) was copied from cypy in
# https://github.com/scidash/sciunit/commit/28612172bf23c25a9f81ffe5578265aa8849f813.
# The version is assumed; there was only a single release on PyPI at the time.
#
# Upstream was asked to comment per packaging guidelines:
# “Statement on bundling cypy?”
# https://github.com/scidash/sciunit/issues/215
Provides:       bundled(python3dist(cypy)) = 0.2

%description -n python3-sciunit %_description

%prep
%autosetup -n sciunit-%{version} -S git

# Update requirements, our package does not provide bs4
# Remove version pins
# Remove backports.tempfile, we use what's in py3
sed -i -e 's/bs4/beautifulsoup4/' -e '/backports/ d' -e 's/importlib-metadata.*/importlib-metadata/' setup.cfg
sed -i -e 's/backports.tempfile/tempfile/' sciunit/utils.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sciunit

%check
%if %{with tests}
# https://github.com/scidash/sciunit/blob/master/test.sh
tar -xf %{SOURCE1}
mv scidash-%{scidash_commit} ../scidash
# Disable test that requires it to be a git repo by adding the necessary decorator
sed -i '/def test_Versioned/i  \ \ \ \ @unittest.skip' sciunit/unit_test/base_tests.py
sed -i '/def test_versioned/i  \ \ \ \ @unittest.skip' sciunit/unit_test/utils_tests.py
# https://github.com/scidash/sciunit/issues/211
sed -i '/def test_source_check/i  \ \ \ \ @unittest.skip' sciunit/unit_test/model_tests.py
# Disable tests failing in Python3.12
# https://github.com/scidash/sciunit/issues/218
sed -i '/def test_testsuite/i  \ \ \ \ @unittest.skip' sciunit/unit_test/test_tests.py
sed -i '/def test_testsuite_set_verbose/i  \ \ \ \ @unittest.skip' sciunit/unit_test/test_tests.py
%{py3_test_envvars} %{python3} -m sciunit.unit_test buffer
%endif

%files -n python3-sciunit -f %{pyproject_files}
%doc README.md
%{_bindir}/sciunit

%changelog
%autochangelog
