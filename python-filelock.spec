%global srcname filelock

%if 0%{?fedora}
%bcond_without docs
%else
%bcond_with docs
%endif
%bcond_without tests

Name:           python-%{srcname}
Version:        3.7.1
Release:        %autorelease
Summary:        A platform independent file lock

License:        Unlicense
URL:            https://github.com/tox-dev/py-filelock
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%if %{with tests}
# We cannot install extra dependencies because there are some
# we do not have in Fedora like covdefaults in testing or furo in docs.
# Test dependencies
BuildRequires:  python3-pytest
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
%autosetup -n %{srcname}-%{version}
# furo theme is not available in Fedora
sed -i "/html_theme =.*/d" docs/conf.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with docs}
pushd docs
PYTHONPATH=../src sphinx-build ./ html --color -b html
PYTHONPATH=../src sphinx-build ./ man --color -b man
rm html/.buildinfo
popd
%endif

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with docs}
install -p -m0644 -D docs/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1
%endif

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
%if %{with docs}
%{_mandir}/man1/%{srcname}.1.gz
%endif


%changelog
%autochangelog
