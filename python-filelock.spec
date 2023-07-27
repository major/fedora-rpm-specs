%global srcname filelock

%if 0%{?fedora}
%bcond_without docs
%else
%bcond_with docs
%endif
%bcond_without tests

Name:           python-%{srcname}
Version:        3.12.2
Release:        %autorelease
Summary:        A platform independent file lock

License:        Unlicense
URL:            https://github.com/tox-dev/py-filelock
Source0:        https://github.com/tox-dev/py-filelock/archive/%{version}/py-%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%if %{with tests}
# We cannot install extra dependencies because there are some
# we do not have in Fedora like covdefaults in testing or furo in docs.
# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-timeout
%endif
%if %{with docs}
# Doc dependencies
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
%endif

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%if 0%{?fedora}
Suggests:       %{name}-doc
%endif

%description -n python%{python3_pkgversion}-%{srcname}
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%if %{with docs}
%package doc
Summary:        Documentation for %{srcname}, %{summary}

%description doc
%{summary}
%endif

%prep
%autosetup -p1 -n py-%{srcname}-%{version}
%if %{with docs}
# furo theme is not available in Fedora
sed -i "/html_theme =.*/d" docs/conf.py
%endif
# setuptools 65.6.3 is not yet in Fedora
sed -i 's/"\(setuptools\)>=.*"/"\1"/' pyproject.toml

%generate_buildrequires
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}; export SETUPTOOLS_SCM_PRETEND_VERSION
%pyproject_buildrequires -r

%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}; export SETUPTOOLS_SCM_PRETEND_VERSION
%pyproject_wheel

%if %{with docs}
pushd docs
PYTHONPATH=../src sphinx-build ./ html --color -b html -d doctrees
rm html/.buildinfo
popd
%endif

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%if %{with docs}
%files doc
%license LICENSE
%doc docs/html
%endif

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
