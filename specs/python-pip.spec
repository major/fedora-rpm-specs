# The original RHEL N+1 content set is defined by (build)dependencies
# of the packages in Fedora ELN. Hence we disable tests here
# to prevent pulling many unwanted packages in.
# We intentionally keep this enabled on EPEL.
%bcond tests %[%{defined fedora} || %{defined epel}]
# Whether to build the manual pages (useful for bootstrapping Sphinx)
%bcond man 1

%global srcname pip
%global base_version 25.1.1
%global upstream_version %{base_version}%{?prerel}
%global python_wheel_name %{srcname}-%{upstream_version}-py3-none-any.whl

Name:           python-%{srcname}
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        %autorelease
Summary:        A tool for installing and managing Python packages

# We bundle a lot of libraries with pip, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:

# certifi: MPL-2.0
# CacheControl: Apache-2.0
# dependency-groups: MIT
# distlib: Python-2.0.1
# distro: Apache-2.0
# idna: BSD-3-Clause
# msgpack: Apache-2.0
# packaging: Apache-2.0 OR BSD-2-Clause
# platformdirs: MIT
# pygments: BSD-2-Clause
# pyproject-hooks: MIT
# requests: Apache-2.0
# resolvelib: ISC
# rich: MIT
# setuptools: MIT
# truststore: MIT
# tomli: MIT
# tomli-w: MIT
# typing-extensions: Python-2.0.1
# urllib3: MIT

License:        MIT AND Python-2.0.1 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MPL-2.0 AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://pip.pypa.io/
Source0:        https://github.com/pypa/pip/archive/%{upstream_version}/%{srcname}-%{upstream_version}.tar.gz

# The following sources are wheels used only for tests.
# They are not bundled in the built package and do not contribute to the overall license.
# They are pre-built but only contain text files, rebuilding them in %%build has very little benefit.

# setuptools.whl
# We cannot use RPM-packaged python-setuptools-wheel because upstream pins to <80.
# See https://github.com/pypa/pip/pull/13357 for rationale.
Source1:        https://files.pythonhosted.org/packages/0d/6d/b4752b044bf94cb802d88a888dc7d288baaf77d7910b7dedda74b5ceea0c/setuptools-79.0.1-py3-none-any.whl

# wheel.whl
# We cannot use RPM-packaged python-wheel-wheel because we intent to drop that package in wheel 0.46+.
# That version of wheel has runtime dependencies and is generally useless as a standalone wheel.
# See https://github.com/pypa/pip/pull/13382 as an attempt to drop the requirement from pip tests.
Source2:        https://files.pythonhosted.org/packages/0b/2c/87f3254fd8ffd29e4c02732eee68a83a1d3c346ae39bc6822dcbcb697f2b/wheel-0.45.1-py3-none-any.whl

# coverage.whl
# There is no RPM-packaged python-coverage-wheel, the package is archful.
# Upstream uses this to measure coverage, which we don't.
# This is a dummy placeholder package that only contains empty coverage.process_startup().
# That way, we don't need to patch the usage out of conftest.py.
Source3:        coverage-0-py3-none-any.whl

BuildArch:      noarch

%if %{with tests}
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/hg
BuildRequires:  /usr/bin/bzr
BuildRequires:  /usr/bin/svn
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
%endif

%if %{with man}
# docs/requirements.txt contains many sphinx extensions
# however, we only build the manual pages thanks to
# https://github.com/pypa/pip/pull/13168
# We also always use the "main" Sphinx, not python%%{python3_pkgversion}-sphinx
BuildRequires:  python3-sphinx
%endif

# Prevent removing of the system packages installed under /usr/lib
# when pip install -U is executed.
# https://bugzilla.redhat.com/show_bug.cgi?id=1550368#c24
# Could be replaced with https://www.python.org/dev/peps/pep-0668/
Patch:          remove-existing-dist-only-if-path-conflicts.patch

# Use the system level root certificate instead of the one bundled in certifi
# https://bugzilla.redhat.com/show_bug.cgi?id=1655253
# The same patch is a part of the RPM-packaged python-certifi
Patch:          dummy-certifi.patch

# Don't warn the user about pip._internal.main() entrypoint
# In Fedora, we use that in ensurepip and users cannot do anything about it,
# this warning is juts moot. Also, the warning breaks CPython test suite.
Patch:          nowarn-pip._internal.main.patch

# Adjust path_to_url et al. to produce the same results on Python 3.14+
# https://github.com/pypa/pip/pull/13423
Patch:          python3.14-file-urls.patch

# Remove -s from Python shebang - ensure that packages installed with pip
# to user locations are seen by pip itself
%undefine _py3_shebang_s

%description
pip is a package management system used to install and manage software packages
written in Python. Many packages can be found in the Python Package Index
(PyPI). pip is a recursive acronym that can stand for either "Pip Installs
Packages" or "Pip Installs Python".



# Virtual provides for the packages bundled by pip.
# You can generate it with:
# %%{_rpmconfigdir}/pythonbundles.py --namespace 'python%%{1}dist' src/pip/_vendor/vendor.txt
%global bundled() %{expand:
Provides: bundled(python%{1}dist(cachecontrol)) = 0.14.2
Provides: bundled(python%{1}dist(certifi)) = 2025.1.31
Provides: bundled(python%{1}dist(dependency-groups)) = 1.3.1
Provides: bundled(python%{1}dist(distlib)) = 0.3.9
Provides: bundled(python%{1}dist(distro)) = 1.9
Provides: bundled(python%{1}dist(idna)) = 3.10
Provides: bundled(python%{1}dist(msgpack)) = 1.1
Provides: bundled(python%{1}dist(packaging)) = 25
Provides: bundled(python%{1}dist(platformdirs)) = 4.3.7
Provides: bundled(python%{1}dist(pygments)) = 2.19.1
Provides: bundled(python%{1}dist(pyproject-hooks)) = 1.2
Provides: bundled(python%{1}dist(requests)) = 2.32.3
Provides: bundled(python%{1}dist(resolvelib)) = 1.1
Provides: bundled(python%{1}dist(rich)) = 14
Provides: bundled(python%{1}dist(setuptools)) = 70.3
Provides: bundled(python%{1}dist(tomli)) = 2.2.1
Provides: bundled(python%{1}dist(tomli-w)) = 1.2
Provides: bundled(python%{1}dist(truststore)) = 0.10.1
Provides: bundled(python%{1}dist(typing-extensions)) = 4.13.2
Provides: bundled(python%{1}dist(urllib3)) = 1.26.20
}

# Some manylinux1 wheels need libcrypt.so.1.
# Manylinux1, a common (as of 2019) platform tag for binary wheels, relies
# on a glibc version that included ancient crypto functions, which were
# moved to libxcrypt and then removed in:
#  https://fedoraproject.org/wiki/Changes/FullyRemoveDeprecatedAndUnsafeFunctionsFromLibcrypt
# The manylinux1 standard assumed glibc would keep ABI compatibility,
# but that's only the case if libcrypt.so.1 (libxcrypt-compat) is around.
# This should be solved in the next manylinux standard (but it may be
# a long time until manylinux1 is phased out).
# See: https://github.com/pypa/manylinux/issues/305
# Note that manylinux is only applicable to x86 (both 32 and 64 bits)
# As of Python 3.12, we no longer use this,
# see https://discuss.python.org/t/29455/
# However, we keep it around for previous Python versions that use the wheel package.
%global crypt_compat_recommends() %{expand:
Recommends: (libcrypt.so.1()(64bit) if python%{1}(x86-64))
Recommends: (libcrypt.so.1 if python%{1}(x86-32))
}



%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A tool for installing and managing Python3 packages

BuildRequires:  python%{python3_pkgversion}-devel
# python3 bootstrap: this is rebuilt before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
# Note that the package prefix is always python3-, even if we build for 3.X
# The minimal version is for bundled provides verification script
BuildRequires:  python3-rpm-generators >= 11-8
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  bash-completion
BuildRequires:  ca-certificates
Requires:       ca-certificates

# Virtual provides for the packages bundled by pip:
%{bundled 3}

Provides:       pip = %{version}-%{release}
Conflicts:      python-pip < %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}
pip is a package management system used to install and manage software packages
written in Python. Many packages can be found in the Python Package Index
(PyPI). pip is a recursive acronym that can stand for either "Pip Installs
Packages" or "Pip Installs Python".


%package -n     %{python_wheel_pkg_prefix}-%{srcname}-wheel
Summary:        The pip wheel
Requires:       ca-certificates

# Virtual provides for the packages bundled by pip:
%{bundled 3}

# This is only relevant for Pythons that are older than 3.12 and don't use their own bundled wheels
# It is also only relevant when this wheel is shared across multiple Pythons
%if "%{python_wheel_pkg_prefix}" == "python"
%{crypt_compat_recommends 3.11}
%{crypt_compat_recommends 3.10}
%{crypt_compat_recommends 3.9}
%endif

%description -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
A Python wheel of pip to use with venv.

%prep
%autosetup -p1 -n %{srcname}-%{upstream_version}

# this goes together with patch4
rm src/pip/_vendor/certifi/*.pem

# Remove windows executable binaries
rm -v src/pip/_vendor/distlib/*.exe
sed -i '/\.exe/d' pyproject.toml

# Remove unused test requirements
sed -Ei '/(pytest-(cov|xdist|rerunfailures)|proxy\.py)/d' tests/requirements.txt

%if %{with tests}
# tests expect wheels in here
mkdir tests/data/common_wheels
cp -a %{SOURCE1} %{SOURCE2} %{SOURCE3} tests/data/common_wheels
%endif


%if %{with tests}
%generate_buildrequires
# we only use this to generate test requires
# the "pyproject" part is explicitly disabled as it generates a requirement on pip
%pyproject_buildrequires -N tests/requirements.txt
%endif


%build
export PYTHONPATH=./src/
%pyproject_wheel

%if %{with man}
sphinx-build --tag man -b man -d docs/build/doctrees/man -c docs/html docs/man docs/build/man
%endif


%install
export PYTHONPATH=./src/
%pyproject_install
%pyproject_save_files -l pip

%if %{with man}
pushd docs/build/man
install -d %{buildroot}%{_mandir}/man1
for MAN in *1; do
install -pm0644 $MAN %{buildroot}%{_mandir}/man1/$MAN
for pip in "pip3" "pip-3" "pip%{python3_version}" "pip-%{python3_version}"; do
echo ".so $MAN" > %{buildroot}%{_mandir}/man1/${MAN/pip/$pip}
done
done
popd
%endif

mkdir -p %{buildroot}%{bash_completions_dir}
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{buildroot}%{_bindir}/pip completion --bash \
    > %{buildroot}%{bash_completions_dir}/pip3

# Make bash completion apply to all the 5 symlinks we install
sed -i -e "s/^\\(complete.*\\) pip\$/\\1 pip pip{,-}{3,%{python3_version}}/" \
    -e s/_pip_completion/_pip3_completion/ \
    %{buildroot}%{bash_completions_dir}/pip3


# Provide symlinks to executables to comply with Fedora guidelines for Python
ln -s ./pip%{python3_version} %{buildroot}%{_bindir}/pip-%{python3_version}
ln -s ./pip-%{python3_version} %{buildroot}%{_bindir}/pip-3


mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}


%check
# Verify bundled provides are up to date
%{_rpmconfigdir}/pythonbundles.py src/pip/_vendor/vendor.txt --compare-with '%{bundled 3}'

# Verify no unwanted files are present in the package
grep "exe$" %{pyproject_files} && exit 1 || true
grep "pem$" %{pyproject_files} && exit 1 || true

# Verify we can at least run basic commands without crashing
%{py3_test_envvars} %{buildroot}%{_bindir}/pip --help
%{py3_test_envvars} %{buildroot}%{_bindir}/pip list
%{py3_test_envvars} %{buildroot}%{_bindir}/pip show pip

%if %{with tests}
# Upstream tests
# bash completion tests only work from installed package
pytest_k='not completion'
# this clashes with our PYTHONPATH
pytest_k="$pytest_k and not environments_with_no_pip"
# this seems to require internet (despite no network marker)
# added in https://github.com/pypa/pip/pull/13378 TODO drop this in the next release
pytest_k="$pytest_k and not test_prompt_for_keyring_if_needed and not test_double_install_fail and not test_install_sdist_links and not test_lock_vcs and not test_lock_archive and not test_backend_sees_config_via_sdist"
# this cannot import breezy, TODO investigate
pytest_k="$pytest_k and not (functional and bazaar)"
# failures to investigate
pytest_k="$pytest_k and not test_all_fields and not test_report_mixed_not_found and not test_basic_show"  # "Editable project location" missing
pytest_k="$pytest_k and not test_basic_install_from_wheel"
pytest_k="$pytest_k and not test_check_unsupported"

%pytest -n auto -m 'not network' -k "$(echo $pytest_k)" \
    --ignore tests/functional/test_proxy.py  # no proxy.py in Fedora
%endif


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst
%if %{with man}
%{_mandir}/man1/pip.*
%{_mandir}/man1/pip-*.*
%{_mandir}/man1/pip3.*
%{_mandir}/man1/pip3-*.*
%endif
%{_bindir}/pip
%{_bindir}/pip3
%{_bindir}/pip-3
%{_bindir}/pip%{python3_version}
%{_bindir}/pip-%{python3_version}
%dir %{bash_completions_dir}
%{bash_completions_dir}/pip3


%files -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
%license LICENSE.txt
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}

%changelog
%autochangelog
