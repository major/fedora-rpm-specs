# The original RHEL N+1 content set is defined by (build)dependencies
# of the packages in Fedora ELN. Hence we disable tests and documentation here
# to prevent pulling many unwanted packages in.
# We intentionally keep this enabled on EPEL.
%bcond tests %[%{defined fedora} || %{defined epel}]
%bcond doc %[%{defined fedora} || %{defined epel}]

%global srcname pip
%global base_version 23.3.2
%global upstream_version %{base_version}%{?prerel}
%global python_wheel_name %{srcname}-%{upstream_version}-py3-none-any.whl

Name:           python-%{srcname}
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        %autorelease
Summary:        A tool for installing and managing Python packages

# We bundle a lot of libraries with pip, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:

# appdirs: MIT
# certifi: MPL-2.0
# chardet: LGPL-2.1-only
# colorama: BSD-3-Clause
# CacheControl: Apache-2.0
# distlib: Python-2.0.1
# distro: Apache-2.0
# html5lib: MIT
# idna: BSD-3-Clause
# ipaddress: Python-2.0.1
# msgpack: Apache-2.0
# packaging: Apache-2.0 OR BSD-2-Clause
# progress: ISC
# pygments: BSD-2-Clause
# pyparsing: MIT
# pyproject-hooks: MIT
# requests: Apache-2.0
# resolvelib: ISC
# rich: MIT
# setuptools: MIT
# six: MIT
# tenacity: Apache-2.0
# truststore: MIT
# tomli: MIT
# typing-extensions: Python-2.0.1
# urllib3: MIT
# webencodings: BSD-3-Clause

License:        MIT AND Python-2.0.1 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-2.1-only AND MPL-2.0 AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://pip.pypa.io/
Source0:        https://github.com/pypa/pip/archive/%{upstream_version}/%{srcname}-%{upstream_version}.tar.gz

BuildArch:      noarch

%if %{with tests}
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/hg
BuildRequires:  /usr/bin/bzr
BuildRequires:  /usr/bin/svn
BuildRequires:  python-setuptools-wheel
BuildRequires:  python-wheel-wheel
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

# Don't warn the user about packaging's LegacyVersion being deprecated.
# (This also breaks Python's test suite when warnings are treated as errors.)
# Upstream issue: https://github.com/pypa/packaging/issues/368
Patch:          no-version-warning.patch

%description
pip is a package management system used to install and manage software packages
written in Python. Many packages can be found in the Python Package Index
(PyPI). pip is a recursive acronym that can stand for either "Pip Installs
Packages" or "Pip Installs Python".



# Virtual provides for the packages bundled by pip.
# You can generate it with:
# %%{_rpmconfigdir}/pythonbundles.py --namespace 'python%%{1}dist' src/pip/_vendor/vendor.txt
%global bundled() %{expand:
Provides: bundled(python%{1}dist(cachecontrol)) = 0.13.1
Provides: bundled(python%{1}dist(certifi)) = 2023.7.22
Provides: bundled(python%{1}dist(chardet)) = 5.1
Provides: bundled(python%{1}dist(colorama)) = 0.4.6
Provides: bundled(python%{1}dist(distlib)) = 0.3.6
Provides: bundled(python%{1}dist(distro)) = 1.8
Provides: bundled(python%{1}dist(idna)) = 3.4
Provides: bundled(python%{1}dist(msgpack)) = 1.0.5
Provides: bundled(python%{1}dist(packaging)) = 21.3
Provides: bundled(python%{1}dist(platformdirs)) = 3.8.1
Provides: bundled(python%{1}dist(pygments)) = 2.15.1
Provides: bundled(python%{1}dist(pyparsing)) = 3.1
Provides: bundled(python%{1}dist(pyproject-hooks)) = 1
Provides: bundled(python%{1}dist(requests)) = 2.31
Provides: bundled(python%{1}dist(resolvelib)) = 1.0.1
Provides: bundled(python%{1}dist(rich)) = 13.4.2
Provides: bundled(python%{1}dist(setuptools)) = 68
Provides: bundled(python%{1}dist(six)) = 1.16
Provides: bundled(python%{1}dist(tenacity)) = 8.2.2
Provides: bundled(python%{1}dist(truststore)) = 0.8
Provides: bundled(python%{1}dist(tomli)) = 2.0.1
Provides: bundled(python%{1}dist(typing-extensions)) = 4.7.1
Provides: bundled(python%{1}dist(urllib3)) = 1.26.17
Provides: bundled(python%{1}dist(webencodings)) = 0.5.1
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
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
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

%if %{with doc}
%package doc
Summary:        A documentation for a tool for installing and managing Python packages

BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx-inline-tabs
BuildRequires:  python%{python3_pkgversion}-sphinx-copybutton
BuildRequires:  python%{python3_pkgversion}-myst-parser

%description doc
A documentation for a tool for installing and managing Python packages

%endif

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
%{crypt_compat_recommends 3.8}
%{crypt_compat_recommends 3.7}
%endif

%description -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
A Python wheel of pip to use with venv.

%prep
%autosetup -p1 -n %{srcname}-%{upstream_version}

# this goes together with patch4
rm src/pip/_vendor/certifi/*.pem

# Do not use furo as HTML theme in docs
# furo is not available in Fedora
sed -i '/html_theme = "furo"/d' docs/html/conf.py

# towncrier extension for Sphinx is not yet available in Fedora
sed -i '/"sphinxcontrib.towncrier",/d' docs/html/conf.py

# tests expect wheels in here
ln -s %{python_wheel_dir} tests/data/common_wheels

# Remove windows executable binaries
rm -v src/pip/_vendor/distlib/*.exe
sed -i '/\.exe/d' setup.py

# Remove RIGHT-TO-LEFT OVERRIDE from AUTHORS.txt
# https://github.com/pypa/pip/pull/12046
%{python3} -c 'from pathlib import Path; p = Path("AUTHORS.txt"); p.write_text("".join(c for c in p.read_text() if c != "\u202e"))'

# Remove unused test requirements
sed -Ei '/pytest-(cov|xdist|rerunfailures)/d' tests/requirements.txt


%if %{with tests}
%generate_buildrequires
# we only use this to generate test requires
# the "pyproject" part is explicitly disabled as it generates a requirement on pip
%pyproject_buildrequires -N tests/requirements.txt
%endif


%build
%py3_build_wheel

%if %{with doc}
export PYTHONPATH=./src/
# from tox.ini
sphinx-build-3 -b html docs/html docs/build/html
sphinx-build-3 -b man  docs/man  docs/build/man  -c docs/html
rm -rf docs/build/html/{.doctrees,.buildinfo}
%endif


%install
# The following is similar to %%pyproject_install, but we don't have
# /usr/bin/pip yet, so we install using the wheel directly.
# (This is not standard wheel usage, but the pip wheel supports it -- see
#  pip/__main__.py)
%{python3} dist/%{python_wheel_name}/pip install \
    --root %{buildroot} \
    --no-deps \
    --disable-pip-version-check \
    --progress-bar off \
    --verbose \
    --ignore-installed \
    --no-warn-script-location \
    --no-index \
    --no-cache-dir \
    --find-links dist \
    'pip==%{upstream_version}'

%if %{with doc}
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


# Make sure the INSTALLER is not pip and remove RECORD
# %%pyproject macros do this for all packages
echo rpm > %{buildroot}%{python3_sitelib}/pip-%{upstream_version}.dist-info/INSTALLER
rm %{buildroot}%{python3_sitelib}/pip-%{upstream_version}.dist-info/RECORD

mkdir -p %{buildroot}%{python_wheel_dir}
install -p dist/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}


%check
# Verify bundled provides are up to date
%{_rpmconfigdir}/pythonbundles.py src/pip/_vendor/vendor.txt --compare-with '%{bundled 3}'

# Verify we can at least run basic commands without crashing
%{py3_test_envvars} %{buildroot}%{_bindir}/pip --help
%{py3_test_envvars} %{buildroot}%{_bindir}/pip list
%{py3_test_envvars} %{buildroot}%{_bindir}/pip show pip

%if %{with tests}
# Upstream tests
# bash completion tests only work from installed package
pytest_k='not completion'

# --deselect'ed tests are not compatible with the latest virtualenv
# These files contain almost 500 tests so we should enable them back
# as soon as pip will be compatible upstream
# https://github.com/pypa/pip/pull/8441
%pytest -m 'not network' -k "$(echo $pytest_k)" \
    --deselect tests/functional --deselect tests/lib/test_lib.py
%endif


%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license %{python3_sitelib}/pip-%{upstream_version}.dist-info/LICENSE.txt
%if %{with doc}
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
%{python3_sitelib}/pip*
%dir %{bash_completions_dir}
%{bash_completions_dir}/pip3

%if %{with doc}
%files doc
%license LICENSE.txt
%doc README.rst
%doc docs/build/html
%endif

%files -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
%license LICENSE.txt
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}

%changelog
%autochangelog
