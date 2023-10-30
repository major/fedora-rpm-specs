# The original RHEL N+1 content set is defined by (build)dependencies
# of the packages in Fedora ELN. Hence we disable tests and documentation here
# to prevent pulling many unwanted packages in.
# We intentionally keep this enabled on EPEL.
%bcond tests %[%{defined fedora} || %{defined epel}]
%bcond doc %[%{defined fedora} || %{defined epel}]

%global srcname pip
%global base_version 23.2.1
%global upstream_version %{base_version}%{?prerel}
%global python_wheel_name %{srcname}-%{upstream_version}-py3-none-any.whl

%global bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)

Name:           python-%{srcname}
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        1%{?dist}
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
Provides: bundled(python%{1}dist(cachecontrol)) = 0.12.11
Provides: bundled(python%{1}dist(certifi)) = 2023.5.7
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
Provides: bundled(python%{1}dist(tomli)) = 2.0.1
Provides: bundled(python%{1}dist(typing-extensions)) = 4.7.1
Provides: bundled(python%{1}dist(urllib3)) = 1.26.16
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
BuildRequires:  bash-completion
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pretend
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-scripttest
BuildRequires:  python%{python3_pkgversion}-virtualenv
BuildRequires:  python%{python3_pkgversion}-werkzeug
BuildRequires:  python%{python3_pkgversion}-pyyaml
BuildRequires:  python%{python3_pkgversion}-tomli-w
BuildRequires:  python%{python3_pkgversion}-installer
%endif
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  ca-certificates
Requires:       ca-certificates

# This was previously required and we keep it recommended because a lot of
# sdists installed via pip will try to import setuptools.
# But pip doesn't actually require setuptools.
# It can install wheels without them and it can build wheels in isolation mode
# (using setuptools/flit/poetry/... installed from PyPI).
# Side note: pip bundles pkg_resources from setuptools for internal usage.
Recommends:     python%{python3_pkgversion}-setuptools

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

mkdir -p %{buildroot}%{bashcompdir}
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{buildroot}%{_bindir}/pip completion --bash \
    > %{buildroot}%{bashcompdir}/pip3

# Make bash completion apply to all the 5 symlinks we install
sed -i -e "s/^\\(complete.*\\) pip\$/\\1 pip pip{,-}{3,%{python3_version}}/" \
    -e s/_pip_completion/_pip3_completion/ \
    %{buildroot}%{bashcompdir}/pip3


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
%dir %{bashcompdir}
%{bashcompdir}/pip3

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
* Fri Aug 04 2023 Miro Hrončok <mhroncok@redhat.com> - 23.2.1-1
- Update to 23.2.1
Resolves: rhbz#2223082

* Fri Aug 04 2023 Miro Hrončok <mhroncok@redhat.com> - 23.1.2-7
- Actually run the tests and build the docs when building this package

* Wed Jul 26 2023 Miro Hrončok <mhroncok@redhat.com> - 23.1.2-6
- Drop no-longer-needed custom changes to /usr/bin/pip*
- Stop Recommending libcrypt.so.1 on Python 3.12+
Resolves: rhbz#2150373

* Tue Jul 25 2023 Python Maint <python-maint@redhat.com> - 23.1.2-5
- Rebuilt for Python 3.12

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 20 2023 Python Maint <python-maint@redhat.com> - 23.1.2-3
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 23.1.2-2
- Bootstrap for Python 3.12

* Fri May 19 2023 Miro Hrončok <mhroncok@redhat.com> - 23.1.2-1
- Update to 23.1.2
Resolves: rhbz#2186979

* Mon Mar 27 2023 Karolina Surma <ksurma@redhat.com> - 23.0.1-2
- Fix compatibility with Sphinx 6+
Resolves: rhbz#2180479

* Mon Feb 20 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 23.0.1-1
- Update to 23.0.1
Resolves: rhbz#2165760

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Karolina Surma <ksurma@redhat.com> - 22.3.1-1
- Update to 22.3.1
Resolves: rhbz#2135044

* Mon Sep 05 2022 Python Maint <python-maint@redhat.com> - 22.2.2-2
- Fix crash when an empty dist-info/egg-info is present
Resolves: rhbz#2115001
- No longer use the rpm_install prefix to determine RPM-installed packages
Related: rhbz#2026979

* Wed Aug 03 2022 Charalampos Stratakis <cstratak@redhat.com> - 22.2.2-1
- Update to 22.2.2
Resolves: rhbz#2109468

* Fri Jul 22 2022 Charalampos Stratakis <cstratak@redhat.com> - 22.2-1
- Update to 22.2
Resolves: rhbz#2109468

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 22.0.4-4
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 22.0.4-3
- Bootstrap for Python 3.11

* Tue Apr 26 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 22.0.4-2
- Fallback to pep517 if setup.py is present and setuptools cannot be imported
- Fixes: rhbz#2020635

* Mon Mar 21 2022 Karolina Surma <ksurma@redhat.com> - 22.0.4-1
- Update to 22.0.4
Resolves: rhbz#2061262

* Wed Feb 16 2022 Lumír Balhar <lbalhar@redhat.com> - 22.0.3-1
- Update to 22.0.3
Resolves: rhbz#2048243

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Miro Hrončok <mhroncok@redhat.com> - 21.3.1-1
- Update to 21.3.1
- Resolves: rhbz#2016682

* Wed Oct 13 2021 Miro Hrončok <mhroncok@redhat.com> - 21.3-1
- Update to 21.3
- Resolves: rhbz#2013026
- Fix incomplete pip-updates in virtual environments

* Wed Oct 06 2021 Charalampos Stratakis <cstratak@redhat.com> - 21.2.3-4
- Remove bundled windows executables
- Resolves: rhbz#2005453

* Thu Sep 23 2021 Miro Hrončok <mhroncok@redhat.com> - 21.2.3-3
- Detect paths not to uninstall from via sysconfig's rpm_prefix install scheme

* Mon Aug 16 2021 Miro Hrončok <mhroncok@redhat.com> - 21.2.3-2
- Fix broken uninstallation by a bogus downstream patch

* Mon Aug 09 2021 Miro Hrončok <mhroncok@redhat.com> - 21.2.3-1
- Update to 21.2.3
- Resolves: rhbz#1985635

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Lumír Balhar <lbalhar@redhat.com> - 21.1.3-1
- Update to 21.1.3
Resolves: rhbz#1976449

* Mon Jun 07 2021 Karolina Surma <ksurma@redhat.com> - 21.1.2-1
- Update to 21.1.2
Resolves: rhbz#1963433

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 21.1.1-3
- Rebuilt for Python 3.10

* Tue Jun 01 2021 Python Maint <python-maint@redhat.com> - 21.1.1-2
- Bootstrap for Python 3.10

* Mon May 10 2021 Karolina Surma <ksurma@redhat.com> - 21.1.1-1
- Update to 21.1.1

* Sat Mar 13 2021 Miro Hrončok <mhroncok@redhat.com> - 21.0.1-2
- python-pip-wheel: Remove bundled provides and libcrypt recommends for Python 2
  (The wheel is Python 3 only for a while)

* Wed Feb 17 2021 Lumír Balhar <lbalhar@redhat.com> - 21.0.1-1
- Update to 21.0.1
Resolves: rhbz#1922592

* Tue Jan 26 2021 Lumír Balhar <lbalhar@redhat.com> - 21.0-1
- Update to 21.0 (#1919530)

* Thu Dec 17 2020 Petr Viktorin <pviktori@redhat.com> - 20.3.3-1
- Update to 20.3.3

* Mon Nov 30 2020 Miro Hrončok <mhroncok@redhat.com> - 20.3-1
- Update to 20.3
- Add support for PEP 600: Future manylinux Platform Tags
- New resolver
- Fixes: rhbz#1893470

* Mon Oct 19 2020 Lumír Balhar <lbalhar@redhat.com> - 20.2.4-1
- Update to 20.2.4 (#1889112)

* Wed Aug 05 2020 Tomas Orsava <torsava@redhat.com> - 20.2.2-1
- Update to 20.2.2 (#1838553)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Lumír Balhar <lbalhar@redhat.com> - 20.1.1-6
- Do not emit a warning about root privileges when --root is used

* Wed Jul 08 2020 Miro Hrončok <mhroncok@redhat.com> - 20.1.1-5
- Update bundled provides to match 20.1.1

* Tue Jun 16 2020 Lumír Balhar <lbalhar@redhat.com> - 20.1.1-4
- Deselect tests incompatible with the latest virtualenv

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 20.1.1-3
- Rebuilt for Python 3.9

* Thu May 21 2020 Miro Hrončok <mhroncok@redhat.com> - 20.1.1-2
- Bootstrap for Python 3.9

* Wed May 20 2020 Tomas Hrnciar <thrnciar@redhat.com> - 20.1.1-1
- Update to 20.1.1

* Wed Apr 29 2020 Tomas Hrnciar <thrnciar@redhat.com> - 20.1-1
- Update to 20.1

* Mon Apr 27 2020 Tomas Hrnciar <thrnciar@redhat.com> - 20.1~b1-1
- Update to 20.1~b1

* Wed Apr 15 2020 Miro Hrončok <mhroncok@redhat.com> - 20.0.2-4
- Only recommend setuptools, don't require them

* Fri Apr 10 2020 Miro Hrončok <mhroncok@redhat.com> - 20.0.2-3
- Allow setting $TMPDIR to $PWD/... during pip wheel (#1806625)

* Tue Mar 10 2020 Miro Hrončok <mhroncok@redhat.com> - 20.0.2-2
- Don't warn the user about pip._internal.main() entrypoint to fix ensurepip

* Mon Mar 02 2020 Miro Hrončok <mhroncok@redhat.com> - 20.0.2-1
- Update to 20.0.2 (#1793456)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Tomas Orsava <torsava@redhat.com> - 19.3.1-1
- Update to 19.3.1 (#1761508)
- Drop upstreamed patch that fixed expected output in test to not break with alpha/beta/rc Python versions

* Wed Oct 30 2019 Miro Hrončok <mhroncok@redhat.com> - 19.2.3-2
- Make /usr/bin/pip(3) work with user-installed pip 19.3+ (#1767212)

* Mon Sep 02 2019 Miro Hrončok <mhroncok@redhat.com> - 19.2.3-1
- Update to 19.2.3 (#1742230)
- Drop patch that should strip path prefixes from RECORD files, the paths are relative

* Wed Aug 21 2019 Petr Viktorin <pviktori@redhat.com> - 19.1.1-8
- Remove python2-pip
- Make pip bootstrap itself, rather than with an extra bootstrap RPM build

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-7
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-6
- Bootstrap for Python 3.8

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-5
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Petr Viktorin <pviktori@redhat.com> - 19.1.1-3
- Recommend libcrypt.so.1 for manylinux1 compatibility
- Make /usr/bin/pip Python 3

* Mon Jun 10 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-2
- Fix root warning when pip is invoked via python -m pip
- Remove a redundant second WARNING prefix form the abovementioned warning

* Wed May 15 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-1
- Update to 19.1.1 (#1706995)

* Thu Apr 25 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1-1
- Update to 19.1 (#1702525)

* Wed Mar 06 2019 Miro Hrončok <mhroncok@redhat.com> - 19.0.3-1
- Update to 19.0.3 (#1679277)

* Wed Feb 13 2019 Miro Hrončok <mhroncok@redhat.com> - 19.0.2-1
- Update to 19.0.2 (#1668492)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Miro Hrončok <mhroncok@redhat.com> - 18.1-2
- Use the system level root certificate instead of the one bundled in certifi

* Thu Nov 22 2018 Miro Hrončok <mhroncok@redhat.com> - 18.1-1
- Update to 18.1 (#1652089)

* Tue Sep 18 2018 Victor Stinner <vstinner@redhat.com> - 18.0-4
- Prevent removing of the system packages installed under /usr/lib
  when pip install -U is executed. Original patch by Michal Cyprian.
  Resolves: rhbz#1550368.

* Wed Aug 08 2018 Miro Hrončok <mhroncok@redhat.com> - 18.0-3
- Create python-pip-wheel package with the wheel

* Tue Jul 31 2018 Miro Hrončok <mhroncok@redhat.com> - 18.0-2
- Remove redundant "Unicode" from License

* Mon Jul 23 2018 Marcel Plch <mplch@redhat.com> - 18.0-7
- Update to 18.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.3-5
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.3-4
- Bootstrap for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.3-3
- Bootstrap for Python 3.7

* Fri May 04 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.3-2
- Allow to import pip10's main from pip9's /usr/bin/pip
- Do not show the "new version of pip" warning outside of venv
Resolves: rhbz#1569488
Resolves: rhbz#1571650
Resolves: rhbz#1573755

* Thu Mar 29 2018 Charalampos Stratakis <cstratak@redhat.com> - 9.0.3-1
- Update to 9.0.3

* Wed Feb 21 2018 Lumír Balhar <lbalhar@redhat.com> - 9.0.1-16
- Include built HTML documentation (in the new -doc subpackage) and man page

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Charalampos Stratakis <cstratak@redhat.com> - 9.0.1-14
- Reintroduce the ipaddress module in the python3 subpackage.

* Mon Nov 20 2017 Charalampos Stratakis <cstratak@redhat.com> - 9.0.1-13
- Add virtual provides for the bundled libraries. (rhbz#1096912)

* Tue Aug 29 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-12
- Switch macros to bcond's and make Python 2 optional to facilitate building
  the Python 2 and Python 3 modules

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-10
- Modernized package descriptions
Resolves: rhbz#1452568

* Tue Mar 21 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-9
- Fix typo in the sudo pip warning

* Fri Mar 03 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-8
- Patch 1 update: No sudo pip warning in venv or virtualenv

* Thu Feb 23 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-7
- Patch 1 update: Customize the warning with the proper version of the pip
  command

* Tue Feb 14 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-6
- Added patch 1: Emit a warning when running with root privileges

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-4
- Provide symlinks to executables to comply with Fedora guidelines for Python
Resolves: rhbz#1406922

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 9.0.1-3
- Rebuild for Python 3.6 with wheel

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 9.0.1-2
- Rebuild for Python 3.6 without wheel

* Fri Nov 18 2016 Orion Poplawski <orion@cora.nwra.com> - 9.0.1-1
- Update to 9.0.1

* Fri Nov 18 2016 Orion Poplawski <orion@cora.nwra.com> - 8.1.2-5
- Enable EPEL Python 3 builds
- Use new python macros
- Cleanup spec

* Fri Aug 05 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-4
- Updated the test sources

* Fri Aug 05 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-3
- Moved python-pip into the python2-pip subpackage
- Added the python_provide macro

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-1
- Update to 8.1.2
- Moved to a new PyPI URL format
- Updated the prefix-stripping patch because of upstream changes in pip/wheel.py

* Mon Feb 22 2016 Slavek Kabrda <bkabrda@redhat.com> - 8.0.2-1
- Update to 8.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 7.1.0-3
- Rebuilt for Python3.5 rebuild
- With wheel set to 1

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 7.1.0-2
- Rebuilt for Python3.5 rebuild

* Wed Jul 01 2015 Slavek Kabrda <bkabrda@redhat.com> - 7.1.0-1
- Update to 7.1.0

* Tue Jun 30 2015 Ville Skyttä <ville.skytta@iki.fi> - 7.0.3-3
- Install bash completion
- Ship LICENSE.txt as %%license where available

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 7.0.3-1
- Update to 7.0.3

* Fri Mar 06 2015 Matej Stuchlik <mstuchli@redhat.com> - 6.0.8-1
- Update to 6.0.8

* Thu Dec 18 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.5.6-5
- Only enable tests on Fedora.

* Mon Dec 01 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-4
- Add tests
- Add patch skipping tests requiring Internet access

* Tue Nov 18 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-3
- Added patch for local dos with predictable temp dictionary names
  (http://seclists.org/oss-sec/2014/q4/655)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-1
- Update to 1.5.6

* Fri Apr 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-4
- Rebuild as wheel for Python 3.4

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-3
- Disable build_wheel

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-2
- Rebuild as wheel for Python 3.4

* Mon Apr 07 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-1
- Updated to 1.5.4

* Mon Oct 14 2013 Tim Flink <tflink@fedoraproject.org> - 1.4.1-1
- Removed patch for CVE 2013-2099 as it has been included in the upstream 1.4.1 release
- Updated version to 1.4.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-4
- Fix for CVE 2013-2099

* Thu May 23 2013 Tim Flink <tflink@fedoraproject.org> - 1.3.1-3
- undo python2 executable rename to python-pip. fixes #958377
- fix summary to match upstream

* Mon May 06 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.1-2
- Fix main package Summary, it's for Python 2, not 3 (#877401)

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.1-1
- Update to 1.3.1, fix for CVE-2013-1888.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-2
- Fixing files for python3-pip

* Thu Oct 04 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-1
- Update to upstream 1.2.1
- Change binary from pip-python to python-pip (RHBZ#855495)
- Add alias from python-pip to pip-python, to be removed at a later date

* Tue May 15 2012 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Update to upstream 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- update to 1.0.2 and added python3 subpackage

* Wed Jun 22 2011 Tim Flink <tflink@fedoraproject.org> - 0.8.3-1
- update to 0.8.3 and project home page

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Luke Macken <lmacken@redhat.com> - 0.8.2-1
- update to 0.8.2 of pip
* Mon Aug 30 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.8-1
- update to 0.8 of pip
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 7 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.2-1
- update to 0.7.2 of pip
* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.1-1
- update to 0.7.1 of pip
* Fri Jan 1 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1.4
- fix dependency issue
* Fri Dec 18 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-2
- fix spec file
* Thu Dec 17 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-1
- upgrade to 0.6.1 of pip
* Mon Aug 31 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.4-1
- Initial package

