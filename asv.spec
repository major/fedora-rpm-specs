%global srcname asv

%global jquery_version 3.3.1

# Testing using conda requires the network to install packages.
%bcond_with network

Name:           %{srcname}
Version:        0.5.1
Release:        %autorelease
Summary:        Airspeed Velocity: A simple Python history benchmarking tool

# Mostly BSD-3-Clause; MIT for extern & www/vendor/*.{css,js}
License:        BSD-3-Clause and MIT
URL:            https://github.com/airspeed-velocity/asv
Source0:        %{pypi_source}
# Not needed upstream.
Patch0001:      0001-Don-t-allow-extension-build-errors-to-be-ignored.patch
# Not wanted upstream: https://github.com/airspeed-velocity/asv/pull/762
Patch0002:      0002-Unbundle-JSON-minify.patch
# Fedora-specific.
Patch0003:      0003-Remove-unnecessary-shebang.patch
Patch0004:      0004-Fix-pypy-version-environment-test-on-latest-pypy.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  web-assets-devel
BuildRequires:  (js-jquery >= %{jquery_version} with js-jquery < 4)

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-bootstrap-theme

%if %{with network}
BuildRequires:  conda
BuildRequires:  python3dist(selenium)
%endif
%ifarch x86_64 aarch64
BuildRequires:  chromedriver
BuildRequires:  chromium
%endif
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  hg
%ifnarch aarch64 %{power64} %{ix86}
BuildRequires:  pypy
%endif
BuildRequires:  python3dist(feedparser)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(rpy2)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(wheel)

%py_provides python3-%{srcname}
Provides:       bundled(python-asizeof) = 5.10
Provides:       bundled(nodejs-blueimp-md5) = 2.10.0
Provides:       bundled(nodejs-flot) = 0.8.3
Provides:       bundled(nodejs-flot-axislabels) = 0.20120405ga0d11e5
Provides:       bundled(nodejs-flot-orderbars) = 0.20100920
Provides:       bundled(nodejs-stupid-table) = 1.0.1

Requires:       (js-jquery >= %{jquery_version} with js-jquery < 4)
Suggests:       conda
Suggests:       python3-virtualenv
Suggests:       python3-hglib >= 1.5
Suggests:       hg
Suggests:       git

# Recommend "all the Pythons", like tox.
Recommends:     python27
Recommends:     python34
Recommends:     python35
Recommends:     python36
Recommends:     python37
Recommends:     python38
Recommends:     python39
Recommends:     pypy
Recommends:     pypy3
Recommends:     python2
Recommends:     python3

%description
Airspeed Velocity (asv) is a tool for benchmarking Python packages over
their lifetime. It is primarily designed to benchmark a single project
over its lifetime using a given suite of benchmarks. The results are
displayed in an interactive web frontend that requires only a basic static
webserver to host.


%package -n %{srcname}-doc
Summary:        asv documentation
%description -n %{srcname}-doc
Documentation for asv


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove useless shebang
sed -i -e '/^#!\//, 1d' asv/extern/asizeof.py

%generate_buildrequires
%pyproject_buildrequires -r -x hg

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}" \
    sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install

# Unbundle jQuery
pushd %{buildroot}%{python3_sitearch}/asv/www/vendor
rm jquery-%{jquery_version}.min.js
ln -s %{_jsdir}/jquery/3/jquery.min.js jquery-%{jquery_version}.min.js
popd

%pyproject_save_files asv


%check
# Must do this to load from buildroot
rm -rf asv

# Without this, test_git_submodule fails on git 2.38.1 and later due to
# mitigations for CVE-2022-39253. See:
#
# https://github.blog/2022-10-18-git-security-vulnerabilities-announced/#cve-2022-39253
# https://bugzilla.redhat.com/show_bug.cgi?id=2137127
git config --global protocol.file.allow always

%ifarch x86_64 aarch64
WEBDRIVER="--webdriver=ChromeHeadless"
%endif
# Since Python 3.12, virtualenv no longer installs the setuptools and wheel
# packages which are needed to run the tests. The following environment
# variables restore the old behaviour
export VIRTUALENV_SETUPTOOLS=bundle VIRTUALENV_WHEEL=bundle
%{pytest} -ra $WEBDRIVER \
%if %{fedora} >= 34
    -k 'not test_web' \
%endif
    %{nil}


%files -n %{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/asv


%files -n %{srcname}-doc
%doc html
%license LICENSE.rst


%changelog
%autochangelog
