Name:           pytest
Version:        8.3.5
Release:        %autorelease
Summary:        Simple powerful testing with Python
# SPDX
License:        MIT
URL:            https://pytest.org
Source:         %{pypi_source pytest %{version}}

# Compatibility fix for attrs 25.2+
Patch:          https://github.com/pytest-dev/pytest/pull/13291.patch

# Officially support Python 3.14
# This fixes/xfails Python 3.14 test failures
# Rebased from https://github.com/pytest-dev/pytest/pull/13440
Patch:          13440.patch

# Fix compatibility with Twisted 25
# Rebased from https://github.com/pytest-dev/pytest/pull/13502
Patch:          13502.patch

# Fix test_doctest_unexpected_exception on Python 3.14
Patch:          https://github.com/pytest-dev/pytest/pull/13548.patch

# testing: skip pkg_resources tests if modern setuptools
Patch:          https://github.com/pytest-dev/pytest/pull/13446.patch

# Remove -s from Python shebang,
# ensure that packages installed with pip to user locations are testable
# https://bugzilla.redhat.com/2152171
%undefine _py3_shebang_s

# When building pytest for the first time with new Python version
# we might not yet have all the BRs, those conditionals allow us to do that.

# This can be used to disable all tests for faster bootstrapping.
# The tests are enabled by default except when building on RHEL/ELN
# (to avoid pulling in extra dependencies into next RHEL).
%bcond tests %{undefined rhel}

# Only disabling the optional tests is a more complex but careful approach
# Pytest will skip the related tests, so we only conditionalize the BRs
%bcond optional_tests %{with tests}

# To run the tests in %%check we use pytest-timeout
# When building pytest for the first time with new Python version
# that is not possible as it depends on pytest
%bcond timeout %{with tests}

# When building pytest for the first time with new Python version
# we also don't have sphinx yet and cannot build docs.
# The docs are enabled by default except when building on RHEL/ELN
# (to avoid pulling in extra dependencies into next RHEL).
%bcond docs %{undefined rhel}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-51

%if %{with tests}
# we avoid using %%pyproject_buildrequires -x testing as it mixes optional and non-optional deps
BuildRequires:  python3-attrs >= 19.2
BuildRequires:  python3-hypothesis >= 3.56
BuildRequires:  python3-pygments >= 2.7.2
BuildRequires:  python3-xmlschema
%if %{with optional_tests}
BuildRequires:  python3-argcomplete
#BuildRequires:  python3-asynctest -- not packaged in Fedora
BuildRequires:  python3-decorator
BuildRequires:  python3-jinja2
BuildRequires:  python3-mock
BuildRequires:  python3-numpy
BuildRequires:  python3-pexpect
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-twisted
BuildRequires:  /usr/bin/lsof
%endif
%if %{with timeout}
BuildRequires:  python3-pytest-timeout
%endif
%endif

%if %{with docs}
BuildRequires:  %{_bindir}/rst2html
# pluggy >= 1 is needed to build the docs, older versions are allowed on runtime:
BuildRequires:  python3-pluggy >= 1
BuildRequires:  python3-pygments-pytest
BuildRequires:  python3-furo
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-removed-in
BuildRequires:  python3-sphinxcontrib-trio
# See doc/en/conf.py -- sphinxcontrib.inkscapeconverter is only used when inkscape is available
# we don't BR inkscape so we generally don't need it, but in case inkscape is installed accidentally:
BuildRequires:  (python3-sphinxcontrib-inkscapeconverter if inkscape)
BuildRequires:  make
%endif

BuildArch:      noarch

%description
The pytest framework makes it easy to write small tests, yet scales to support
complex functional testing for applications and libraries.


%package -n python3-%{name}
Summary:        Simple powerful testing with Python
Provides:       pytest = %{version}-%{release}

%description -n python3-%{name}
The pytest framework makes it easy to write small tests, yet scales to support
complex functional testing for applications and libraries.


%prep
%autosetup -p1 -n %{name}-%{version}

# documentation dependencies missing in Fedora
sed -i '/sphinxcontrib-towncrier/d' doc/en/requirements.txt
sed -i '/sphinxcontrib\.towncrier/d' doc/en/conf.py
sed -i '/sphinx_issues/d' doc/en/conf.py
sed -i '/sphinx-issues/d' doc/en/requirements.txt


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%if %{with docs}
for l in doc/* ; do
  %make_build -C $l html PYTHONPATH="$(pwd)/src"
done
for f in README CHANGELOG CONTRIBUTING ; do
  rst2html ${f}.rst > ${f}.html
done
%endif


%install
%pyproject_install
%pyproject_save_files _pytest pytest py

mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest-%{python3_version}
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest-3
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test-%{python3_version}
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test-3

# We use 3.X per default
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test

%if %{with docs}
mkdir -p _htmldocs/html
for l in doc/* ; do
  # remove hidden file
  rm ${l}/_build/html/.buildinfo
  mv ${l}/_build/html _htmldocs/html/${l##doc/}
done
%endif

# remove shebangs from all scripts
find %{buildroot}%{python3_sitelib} \
     -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;


%check
%if %{with tests}
%global __pytest %{buildroot}%{_bindir}/pytest
# optional_tests deps contain pytest-xdist, so we can use it to run tests faster
%pytest testing %{?with_timeout:--timeout=30} %{?with_optional_tests:-n auto} -rs
%else
%pyproject_check_import
%endif


%files -n python3-%{name} -f %{pyproject_files}
%if %{with docs}
%doc CHANGELOG.html
%doc README.html
%doc CONTRIBUTING.html
%doc _htmldocs/html
%endif
%{_bindir}/pytest
%{_bindir}/pytest-3
%{_bindir}/pytest-%{python3_version}
%{_bindir}/py.test
%{_bindir}/py.test-3
%{_bindir}/py.test-%{python3_version}


%changelog
%autochangelog
