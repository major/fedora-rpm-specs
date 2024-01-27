# Tests are enabled by default
%bcond tests 1

Name:           python-flit
Version:        3.9.0
Release:        %autorelease
Summary:        Simplified packaging of Python modules

# ./flit/log.py: Apache-2.0
# ./flit/upload.py: PSF-2.0
License:        BSD-3-Clause AND Apache-2.0 AND PSF-2.0

URL:            https://flit.pypa.io/
Source:         https://github.com/pypa/flit/archive/%{version}/flit-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  /usr/bin/python
BuildRequires:  python3-pytest
BuildRequires:  python3-responses
# Used for generating an offline cache of trove classifiers
BuildRequires:  python3-trove-classifiers
BuildRequires:  python3-testpath
BuildRequires:  python3-requests-download
BuildRequires:  git-core
%endif

%global _description %{expand:
Flit is a simple way to put Python packages and modules on PyPI.
It tries to require less thought about packaging and help you avoid common
mistakes.

Flit packages a single importable module or package at a time, using the import
name as the name on PyPI. All sub-packages and data files within a package are
included automatically.}

%description %_description


%package -n flit
Summary:        %{summary}
%py_provides    python3-flit
# Remove this in Fedora 41+:
Obsoletes:      python3-flit < 3.9.0

# https://pypi.python.org/pypi/tornado
# ./flit/log.py unknown version
Provides:       bundled(python3dist(tornado))

%description -n flit %_description


%prep
%autosetup -p1 -n flit-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flit


%check
%pyproject_check_import

%if %{with tests}
# flit attempts to download list of classifiers from PyPI, but not if it's cached
# test_invalid_classifier fails without the list
mkdir -p fake_cache/flit
%{python3} -m trove_classifiers >fake_cache/flit/classifiers.lst
export XDG_CACHE_HOME=$PWD/fake_cache

# This also runs tests of flit_core but deselecting them breaks the flit tests,
# so we run them anyway:
%pytest
%endif


%files -n flit -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/flit


%changelog
%autochangelog
