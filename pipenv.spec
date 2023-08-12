# pipenv rebase checklist
# - Update version, release tag, add changelog
# - Update the test_artifacts_commit macro to point to the correct commit
# - Upload both new sources to the side cache
# - Update the `bundled-licenses` file (see guidance inside)
# - Update the License tag (see guidance above it)
# - Update licenses in %%files section (see guidance in that section)
# - Update versions of bundled packages (see files
#     * pipenv/vendor/vendor.txt
#     * pipenv/patched/patched.txt
#     * pipenv/patched/pip/_vendor/vendor.txt [previously: pipenv/patched/notpip/_vendor/vendor.txt and pipenv/vendor/vendor_pip.txt]
#     * pipenv/vendor/pythonfinder/_vendor/vendor.txt
#   inside the sources, and possibly diff them with the previous version)

%global base_version        2023.6.12
# %%global prerelease_version  --

# Test artifacts are not released, we have to download the commit tree
# Upstream issue: https://github.com/pypa/pipenv/issues/4237
# To update: go to GitHub, find to what commit the submodule `tests/pypi`
#   pointed at the time of the release of pipenv
%global test_artifacts_commit f5530013426d6392d67cd1703f379d20a768c1cf

%global upstream_version %{base_version}%{?prerelease_version}

Name:           pipenv
Version:        %{base_version}%{?prerelease_version:~%{prerelease_version}}
Release:        1%{?dist}
Summary:        The higher level Python packaging tool

# Pipenv source code is MIT, there are bundled packages having different licenses
# - See file `bundled-licenses` on instructions how to generate the License field here.
License:        MIT and (ASL 2.0 or BSD) and ASL 2.0 and BSD and ISC and LGPLv2+ and MPLv2.0 and Python
URL:            https://github.com/pypa/pipenv
Source0:        https://github.com/pypa/%{name}/archive/v%{upstream_version}/%{name}-%{upstream_version}.tar.gz

Source1:        https://github.com/sarugaku/pipenv-test-artifacts/archive/%{test_artifacts_commit}/pipenv-test-artifacts-%{test_artifacts_commit}.tar.gz

# List of licenses of the bundled packages
Source2:        bundled-licenses

# Use the system level root certificate instead of the one bundled in certifi
# https://bugzilla.redhat.com/show_bug.cgi?id=1655253
Patch4:         dummy-certifi.patch

# Remove the bundled windows executables from the bundled
# pip and distlib
Patch6:         remove-bundled-exe-files.patch

BuildArch:      noarch

BuildRequires:  ca-certificates
# gcc is only needed for tests, this is a noarch package
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(parver)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(sphinx-click)
BuildRequires:  python3dist(sphinxcontrib-spelling)
BuildRequires:  python3dist(twine)
BuildRequires:  python3dist(linkify-it-py)

# Runtime dependencies required for tests
# (even though they're also bundled...)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(virtualenv-clone)
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)

# Optional condition that makes "python" mean Python 2
# Useful to tests if pipenv can manage python 2 venvs, but unnecessary dep
%bcond_with python2_tests

%if %{with python2_tests}
BuildRequires:  python2-devel
%endif

%{?python_provide:%python_provide python3-%{name}}

Requires:       ca-certificates
Requires:       which


# Important:
# - Dont use apostrophe inside comments in this block
# - Remove all trailing zero-blocks from versions (i.e. use `40` instead of `40.0.0`)
#
# We've made an attempt to unbundle pipenv's libraries and make the rpm smaller in size
# However, the different velocities of pipenv and libraries it depends on
# started to cause incompatibilities, breaking pipenv more & more often.
# Therefore we've decided to stop the devendoring attempts and use the stuff
# pipenv bundles and has proven working - staying close to what upstream brings
# will hopefully spare some maintenance burden in the future
%global bundled %{expand:
Provides: bundled(python3dist(click-didyoumean)) = 0.3
Provides: bundled(python3dist(pipdeptree)) = 2.8
Provides: bundled(python3dist(ruamel-yaml)) = 0.17.21
# This library uses pip.internals. Some changes in init methods happened there.
# So version 1.3.3 is useless with pip 19+ and newer versions will break pipenv
# because pipenv has bundled patched pip.
Provides: bundled(python3dist(requirementslib)) = 2.3

# The sources contains patched versions of following packages:
Provides: bundled(python3dist(pip)) = 23.1.2
Provides: bundled(python3dist(safety)) = 2.3.2

# We cannot unbundle this easily,
# See https://bugzilla.redhat.com/show_bug.cgi?id=1767003
Provides: bundled(python3dist(tomlkit)) = 0.11.7

# The packages bundled with pip:
Provides: bundled(python3dist(cachecontrol)) = 0.12.11
Provides: bundled(python3dist(chardet)) = 5.1
Provides: bundled(python3dist(colorama)) = 0.4.6
Provides: bundled(python3dist(distlib)) = 0.3.6
Provides: bundled(python3dist(distro)) = 1.8
Provides: bundled(python3dist(idna)) = 3.4
Provides: bundled(python3dist(msgpack)) = 1.0.5
Provides: bundled(python3dist(packaging)) = 21.3
Provides: bundled(python3dist(platformdirs)) = 3.2
Provides: bundled(python3dist(pydantic)) = 1.10.9
Provides: bundled(python3dist(pygments)) = 2.14
Provides: bundled(python3dist(pyproject-hooks)) = 1
Provides: bundled(python3dist(requests)) = 2.28.2
Provides: bundled(python3dist(resolvelib)) = 1.0.1
Provides: bundled(python3dist(rich)) = 13.3.3
Provides: bundled(python3dist(setuptools)) = 67.7.2
Provides: bundled(python3dist(six)) = 1.16
Provides: bundled(python3dist(tenacity)) = 8.2.2
Provides: bundled(python3dist(tomli)) = 2.0.1
Provides: bundled(python3dist(typing-extensions)) = 4.5
Provides: bundled(python3dist(webencodings)) = 0.5.1

# The packages bundles with pipenv
# Some occur twice - with pip and pipenv, possibly with different versions
Provides: bundled(python3dist(attrs)) = 23.1
Provides: bundled(python3dist(certifi)) = 2022.12.7
Provides: bundled(python3dist(click)) = 8.1.3
Provides: bundled(python3dist(dparse)) = 0.6.2
Provides: bundled(python3dist(markupsafe)) = 2.1.2
Provides: bundled(python3dist(packaging)) = 21.3
Provides: bundled(python3dist(pep517)) = 0.13
Provides: bundled(python3dist(pexpect)) = 4.8
Provides: bundled(python3dist(plette)) = 0.4.4
Provides: bundled(python3dist(ptyprocess)) = 0.7
Provides: bundled(python3dist(pyparsing)) = 3.0.9
Provides: bundled(python3dist(pythonfinder)) = 2.0.4
Provides: bundled(python3dist(python-dotenv)) = 1
Provides: bundled(python3dist(shellingham)) = 1.5^post1
Provides: bundled(python3dist(urllib3)) = 1.26.15
}
%{bundled}


%description
The Python packaging tool that aims to bring
the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.)
to the Python world. It automatically creates and manages a virtualenv for
your projects, as well as adds/removes packages from your Pipfile as you
install/uninstall packages. It also generates the ever–important Pipfile.lock,
which is used to produce deterministic builds.

%package -n %{name}-doc
Summary:        Pipenv documentation
%description -n %{name}-doc
Documentation for Pipenv


%prep
%autosetup -p1 -n %{name}-%{upstream_version}

tar -xf %{SOURCE1} --strip-components 1 -C tests/pypi

# this goes together with patch4
rm pipenv/patched/pip/_vendor/certifi/*.pem

# Remove python2 parts because they fail bytecompilation
rm -rf pipenv/patched/yaml2/


# Remove setup_requires, as we cannot install invoke
sed -i /setup_requires/d setup.py

# Remove windows executable binaries
# This goes together with patch6
rm -v pipenv/patched/pip/_vendor/distlib/*.exe


%build
%py3_build
# generate html docs
export PYTHONPATH=$PWD/build/lib
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
rm -rf html/_sources/


%install
%py3_install
# Remove shebang lines from scripts in project directory
grep "/usr/bin/env python" -lR %{buildroot}%{python3_sitelib}/%{name} | xargs sed -i '/^#!/,1d'


%check
# Verify bundled provides are up to date
# Remove unversioned `packaging` (it's listed twice there and confuses pythonbundles.py)
sed  -i '/packaging$/d' pipenv/vendor/vendor.txt

%{_rpmconfigdir}/pythonbundles.py pipenv/vendor/vendor*.txt pipenv/vendor/*/_vendor/vendor.txt \
    pipenv/patched/*/_vendor/vendor.txt pipenv/patched/patched.txt \
    --compare-with '%{bundled}'

# we make sure "python" exists and means something
mkdir check_path
%if %{with python2_tests}
ln -s %{__python2} check_path/python
%else
ln -s %{__python3} check_path/python
%endif
test -f %{_bindir}/virtualenv || ln -s %{_bindir}/virtualenv-3 check_path/virtualenv

export PATH=$PWD/check_path:$PATH:%{buildroot}%{_bindir}
export PYPI_VENDOR_DIR="$(pwd)/tests/pypi/"

# There are 2 types of tests: unit and integration:
# - integration tests require internet and are disabled
# - unit tests that need network are disabled
%pytest -m "not needs_internet" -vv -s tests/unit

rm -rf check_path


%files
%license LICENSE

# To regenerate list of licenses, use:
#  $ ./license-helper.py --bundled-modules bundled-licenses \
#                        --sources <directory created by fedpkg prep> \
#                        --list-license-files
#
# Ignore RPM warnings about these license files being listed twice.

# Keep this list alphabetically sorted
%license %{python3_sitelib}/%{name}/patched/pip/COPYING
%license %{python3_sitelib}/%{name}/patched/pip/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/pip/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/pip/LICENSE.md
%license %{python3_sitelib}/%{name}/patched/pip/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/cachecontrol/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/certifi/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/chardet/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/colorama/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/distlib/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/distro/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/idna/LICENSE.md
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/msgpack/COPYING
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/packaging/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/packaging/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/packaging/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/pkg_resources/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/platformdirs/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/pygments/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/pyparsing/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/pyproject_hooks/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/requests/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/resolvelib/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/rich/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/six.LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/tenacity/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/tomli/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/typing_extensions.LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/urllib3/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/pip/_vendor/webencodings/LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/six.LICENSE
%license %{python3_sitelib}/%{name}/patched/pip/typing_extensions.LICENSE
%license %{python3_sitelib}/%{name}/patched/safety/LICENSE
%license %{python3_sitelib}/%{name}/vendor/click/LICENSE.rst
%license %{python3_sitelib}/%{name}/vendor/click_didyoumean/LICENSE
%license %{python3_sitelib}/%{name}/vendor/colorama/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/dotenv/LICENSE
%license %{python3_sitelib}/%{name}/vendor/dparse/LICENSE
%license %{python3_sitelib}/%{name}/vendor/markupsafe/LICENSE.rst
%license %{python3_sitelib}/%{name}/vendor/pep517/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pexpect/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pipdeptree/LICENSE
%license %{python3_sitelib}/%{name}/vendor/plette/LICENSE
%license %{python3_sitelib}/%{name}/vendor/ptyprocess/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pydantic/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pythonfinder/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/requirementslib/LICENSE
%license %{python3_sitelib}/%{name}/vendor/ruamel.yaml-0.17.21-py3.9-nspkg.pth.LICENSE
%license %{python3_sitelib}/%{name}/vendor/ruamel.yaml.LICENSE
%license %{python3_sitelib}/%{name}/vendor/shellingham/LICENSE
%license %{python3_sitelib}/%{name}/vendor/tomli/LICENSE
%license %{python3_sitelib}/%{name}/vendor/tomlkit/LICENSE

%doc README.md NOTICES CHANGELOG.rst HISTORY.txt
%{_bindir}/pipenv
%{_bindir}/pipenv-resolver
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{upstream_version}-*.egg-info

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Thu Aug 10 2023 Tomas Orsava <torsava@redhat.com> - 2023.6.12-1
- Rebase to version 2023.6.12
Resolves: rhbz#2179550

* Sun Jul 30 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2023.2.18-4
- Backport minimum patch from setuptools upstream for python 3.12
  (setuptools is vendored in pipenv)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 2023.2.18-2
- Rebuilt for Python 3.12

* Wed Mar 15 2023 Tomas Orsava <torsava@redhat.com> - 2023.2.18-1
- Rebase to version 2023.2.18
Resolves: rhbz#2140230

* Mon Mar 13 2023 Miro Hrončok <mhroncok@redhat.com> - 2022.10.25-4
- Do not include [extras] in bundled(python3dist()) Provides
- See https://bugzilla.redhat.com/2140230#c12

* Tue Mar 07 2023 Miro Hrončok <mhroncok@redhat.com> - 2022.10.25-3
- Explicitly BuildRequire pytz for tests, it has been brought transitively before

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.10.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Tomas Orsava <torsava@redhat.com> - 2022.10.25-1
- Rebase to version 2022.10.25
Resolves: rhbz#2115908

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2022.5.2-2
- Rebuilt for Python 3.11

* Tue May 03 2022 Tomas Orsava <torsava@redhat.com> - 2022.5.2-1
- Rebase to a new upstream version
Resolves: rhbz#2020608

* Thu Feb 24 2022 Tomas Orsava <torsava@redhat.com> - 2021.5.29-7
- Fix for CVE-2022-21668
Resolves: rhbz#2039830

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.5.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Charalampos Stratakis <cstratak@redhat.com> - 2021.5.29-5
- Remove bundled windows executables
Resolves: rhbz#2005460

* Mon Aug 02 2021 Karolina Surma <ksurma@redhat.com> - 2021.5.29-4
- Use bundled packaging, requests, urllib3, chardet to keep supporting Python 2
- Vendor the rest of unbundled libraries
- Let %%pytest set PYTHONPATH
- Compare vendored vs bundled packages in %%check

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.5.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Lumír Balhar <lbalhar@redhat.com> - 2021.5.29-2
- Use bundled click to be able to update it in Fedora

* Mon Jun 21 2021 Lumír Balhar <lbalhar@redhat.com> - 2021.5.29-1
- Update to 2021.5.29
Resolves: rhbz#1965736

* Fri Jun 18 2021 Karolina Surma <ksurma@redhat.com> - 2020.11.15-4
- Enable documentation build with Sphinx 4.x

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2020.11.15-3
- Rebuilt for Python 3.10

* Tue Apr 13 2021 Tomas Orsava <torsava@redhat.com> - 2020.11.15-2
- First draft of the patch provided by Laurent Almeras <lalmeras@gmail.com>
- Revendored: pipdeptree

* Wed Feb 03 2021 Petr Viktorin <pviktori@redhat.com> - 2020.11.15-1
- Update to 2020.11.15

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Tomas Orsava <torsava@redhat.com> - 2020.8.13-1
- Rebase to a new upstream version (#1868686)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Tomas Orsava <torsava@redhat.com> - 2020.6.2-1
- Rebase to a new upstream version (#1842795)

* Thu May 28 2020 Tomas Orsava <torsava@redhat.com> - 2020.5.28-1
- Rebase to a new final upstream version (#1829161)

* Thu Apr 30 2020 Tomas Orsava <torsava@redhat.com> - 2020.4.1~b2-1
- Rebase to a new beta version 2 (#1829161)
- Remove upstreamed patches

* Thu Apr 30 2020 Tomas Orsava <torsava@redhat.com> - 2020.4.1~b1-1
- Rebase to a new beta version (#1829161)
  - Added an upstream patch to not fallback to python unconstrained version
- Fixed unbundling machinery, tomlkit was partially unbundled by mistake
- Added helper script for handling bundled licenses
- Add to files new and missing LICENSE files
- Re-bundled:
  - pip_shims
  - pythonfinder
  - yaspin
  - vistir

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-12
- Keep pathlib2, scandir, click-completion and backports.* bundled (#1767003)
- Keep tomlkit bundled for the same reason

* Fri Oct 11 2019 Patrik Kopkan <pkopkan@redhat.com> - 2018.11.26-11
- Devendored: yaspin vistir pythonfinder plette pipreqs pipdeptree pip_shims tomlkit

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-7
- Require which (#1688145)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-5
- Fix a fix of unbundling of packaging (sorry)

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-4
- Fix unbundling of packaging
- Fixes https://github.com/pypa/pipenv/issues/3469

* Wed Jan  9 2019 Owen Taylor <otaylor@redhat.com> - 2018.11.26-3
- Fix pexpect import for compatibility mode of pipenv shell

* Wed Dec 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-2
- Use the system level root certificate instead of the one bundled in certifi

* Thu Nov 29 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-1
- Update to 2018.11.26 (bugfixes only)

* Fri Nov 23 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.14-1
- Update to 2018.11.14 (#1652091)
- Should fix incompatibility with pip (#1651317)

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.7.1-2
- Correct the name of bundled dotenv to python-dotenv

* Fri Jul 27 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.7.1-1
- Update to 2018.7.1 (#1609432)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-3
- Do not require pathlib2, it's intended for Python < 3.5

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-2
- Rebuilt for Python 3.7
- Add patch for patched/bundled prettytoml to work with 3.7

* Fri Apr 13 2018 Michal Cyprian <mcyprian@redhat.com> - 11.10.4-1
- Initial package.
