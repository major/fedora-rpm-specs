%global srcname setuptools

# used when bootstrapping new Python versions
%bcond bootstrap 0

# The original RHEL N+1 content set is defined by (build)dependencies
# of the packages in Fedora ELN. Hence we disable tests and documentation here
# to prevent pulling many unwanted packages in.
%bcond tests %[%{without bootstrap} && %{defined fedora}]

%global python_wheel_name %{srcname}-%{version}-py3-none-any.whl

Name:           python-setuptools
# When updating, update the bundled libraries versions bellow!
Version:        80.9.0
Release:        %autorelease
Summary:        Easily build and distribute Python packages
# setuptools is MIT
# autocommand is LGPL-3.0-only
# backports-tarfile is MIT
# importlib-metadata is Apache-2.0
# inflect is MIT
# jaraco-context is MIT
# jaraco-collections is MIT
# jaraco-functools is MIT
# jaraco-text is MIT
# more-itertools is MIT
# packaging is BSD-2-Clause OR Apache-2.0
# platformdirs is MIT
# tomli is MIT
# typeguard is MIT
# typing-extensions is Python-2.0.1
# wheel is MIT
# zipp is MIT
# the setuptools logo is MIT
License:        MIT AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0) AND Python-2.0.1 AND LGPL-3.0-only
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source %{srcname} %{version}}

# Some test deps are optional and either not desired or not available in Fedora, thus this patch removes them.
Patch:          Remove-optional-or-unpackaged-test-deps.patch

# The `setup.py install` deprecation notice might be confusing for RPM packagers
# adjust it, but only when $RPM_BUILD_ROOT is set
Patch:          Adjust-the-setup.py-install-deprecation-message.patch

# setuptools rewrites all shebangs to "#!python" which breaks workflows
# where no external installers (usually rewriting this) are involved.
# https://github.com/pypa/setuptools/issues/4883
# - Resolution: deprecated functionality won't be fixed.
# brp-mangle-shebang script cannot mangle this and fails for many pkgs.
Patch:          Revert-Always-rewrite-a-Python-shebang-to-python.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with bootstrap}
BuildRequires:  unzip
%endif

%if %{with tests}
BuildRequires:  gcc
%endif

# python3 bootstrap: this is built before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
# The minimal version is for bundled provides verification script to accept multiple files as input
BuildRequires:  python3-rpm-generators >= 12-8
# we also use %%{_pyproject_wheeldir}, so an explicit requirement on the pyproject-macros is needed
BuildRequires:  pyproject-rpm-macros

%if %{without bootstrap}
# Not to use the pre-generated egg-info, we use setuptools from previous build to generate it
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.

# Virtual provides for the packages bundled by setuptools.
# Bundled packages are defined in multiple files. Generate the list with:
# pip freeze --path setuptools/_vendor > vendored.txt
# %%{_rpmconfigdir}/pythonbundles.py --namespace 'python%%{python3_pkgversion}dist' vendored.txt
%global bundled %{expand:
Provides: bundled(python%{python3_pkgversion}dist(autocommand)) = 2.2.2
Provides: bundled(python%{python3_pkgversion}dist(backports-tarfile)) = 1.2
Provides: bundled(python%{python3_pkgversion}dist(importlib-metadata)) = 8
Provides: bundled(python%{python3_pkgversion}dist(inflect)) = 7.3.1
Provides: bundled(python%{python3_pkgversion}dist(jaraco-collections)) = 5.1
Provides: bundled(python%{python3_pkgversion}dist(jaraco-context)) = 5.3
Provides: bundled(python%{python3_pkgversion}dist(jaraco-functools)) = 4.0.1
Provides: bundled(python%{python3_pkgversion}dist(jaraco-text)) = 3.12.1
Provides: bundled(python%{python3_pkgversion}dist(more-itertools)) = 10.3
Provides: bundled(python%{python3_pkgversion}dist(packaging)) = 24.2
Provides: bundled(python%{python3_pkgversion}dist(platformdirs)) = 4.2.2
Provides: bundled(python%{python3_pkgversion}dist(tomli)) = 2.0.1
Provides: bundled(python%{python3_pkgversion}dist(typeguard)) = 4.3
Provides: bundled(python%{python3_pkgversion}dist(typing-extensions)) = 4.12.2
Provides: bundled(python%{python3_pkgversion}dist(wheel)) = 0.45.1
Provides: bundled(python%{python3_pkgversion}dist(zipp)) = 3.19.2
}

%package -n python%{python3_pkgversion}-setuptools
Summary:        Easily build and distribute Python 3 packages
%{bundled}

# For users who might see ModuleNotFoundError: No module named 'pkg_resoureces'
# NB: Those are two different provides: one contains underscore, the other hyphen
%py_provides    python%{python3_pkgversion}-pkg_resources
%py_provides    python%{python3_pkgversion}-pkg-resources

%description -n python%{python3_pkgversion}-setuptools
Setuptools is a collection of enhancements to the Python 3 distutils that allow
you to more easily build and distribute Python 3 packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.


%package -n     %{python_wheel_pkg_prefix}-%{srcname}-wheel
Summary:        The setuptools wheel
%{bundled}

%description -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
A Python wheel of setuptools to use with venv.


%prep
%autosetup -p1 -n %{srcname}-%{version}
%if %{without bootstrap}
# If we don't have setuptools installed yet, we use the pre-generated .egg-info
# See https://github.com/pypa/setuptools/pull/2543
# And https://github.com/pypa/setuptools/issues/2550
# WARNING: We cannot remove this folder since Python 3.11.1,
#          see https://github.com/pypa/setuptools/issues/3761
#rm -r %%{srcname}.egg-info
%endif

# Strip shbang
find setuptools pkg_resources -name \*.py | xargs sed -i -e '1 {/^#!\//d}'
# Remove bundled exes
rm -f setuptools/*.exe
# Don't ship these
rm -r docs/conf.py

%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x test}
%endif

%build
%if %{with bootstrap}
%{python3} setup.py bdist_wheel
mkdir -p %{_pyproject_wheeldir}
mv dist/%{python_wheel_name} %{_pyproject_wheeldir}
%else
%pyproject_wheel
%endif


%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{python3_sitelib}
unzip %{_pyproject_wheeldir}/%{python_wheel_name} -d %{buildroot}%{python3_sitelib} -x setuptools-%{version}.dist-info/RECORD
echo rpm > %{buildroot}%{python3_sitelib}/setuptools-%{version}.dist-info/INSTALLER
%else
%pyproject_install
%pyproject_save_files -l setuptools pkg_resources _distutils_hack
sed -Ei '/\/tests\b/d' %{pyproject_files}
%endif

# https://github.com/pypa/setuptools/issues/2709
find %{buildroot}%{python3_sitelib} -name tests -print0 | xargs -0 rm -r

# Install the wheel for the python-setuptools-wheel package
# and inject SBOM into it (if the macro is available)
mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}
%{?python_wheel_inject_sbom:%python_wheel_inject_sbom %{buildroot}%{python_wheel_dir}/%{python_wheel_name}}


%check
%if %{without bootstrap}
# Verify bundled provides are up to date
%{python3} -m pip freeze --path setuptools/_vendor > vendored.txt
%{_rpmconfigdir}/pythonbundles.py vendored.txt --namespace 'python%{python3_pkgversion}dist' --compare-with '%{bundled}'

# Regression test, the wheel should not be larger than 1300 kB
# https://bugzilla.redhat.com/show_bug.cgi?id=1914481#c3
test $(stat --format %%s %{_pyproject_wheeldir}/%{python_wheel_name}) -lt 1300000

%pyproject_check_import -e '*.tests' -e '*.tests.*'
%endif

# Regression test, the tests are not supposed to be installed
test ! -d %{buildroot}%{python3_sitelib}/pkg_resources/tests
test ! -d %{buildroot}%{python3_sitelib}/setuptools/tests
test ! -d %{buildroot}%{python3_sitelib}/setuptools/_distutils/tests

%if %{with tests}
# Upstream tests
# PIP_NO_BUILD_ISOLATION allows us to run more tests offline with pip 25.3+,
# or else they fecth setuptools from the internet,
# see https://bugzilla.redhat.com/2417963.
# --ignore=setuptools/tests/integration/
# --ignore=setuptools/tests/config/test_apply_pyprojecttoml.py
# -k "not not test_equivalent_output"
#   the tests require internet connection
# --ignore=setuptools/tests/test_editable_install.py
#   the tests require pip-run which we don't have in Fedora
# -k "not test_wheel_includes_cli_scripts"
#   the test expects removed .exe files to be installed
# --ignore=tools
#   the tests test various upstream release tools we don't use/ship
PRE_BUILT_SETUPTOOLS_WHEEL=%{_pyproject_wheeldir}/%{python_wheel_name} \
PIP_NO_BUILD_ISOLATION=0 \
PYTHONPATH=$(pwd) %pytest \
 --ignore=setuptools/tests/integration/ \
 --ignore=setuptools/tests/test_editable_install.py \
 --ignore=setuptools/tests/config/test_apply_pyprojecttoml.py \
 --ignore=tools \
 -k "not test_wheel_includes_cli_scripts and not test_equivalent_output"
%endif # with tests


%files -n python%{python3_pkgversion}-setuptools %{?!with_bootstrap:-f %{pyproject_files}}
%doc docs/* NEWS.rst README.rst
%{python3_sitelib}/distutils-precedence.pth
%if %{with bootstrap}
%{python3_sitelib}/setuptools-%{version}.dist-info/
%license %{python3_sitelib}/setuptools-%{version}.dist-info/licenses/LICENSE
%{python3_sitelib}/pkg_resources/
%{python3_sitelib}/setuptools/
%{python3_sitelib}/_distutils_hack/
%endif

%files -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
%license LICENSE
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}


%changelog
%autochangelog
