%global srcname twine

%bcond_without tests
%bcond_without docs
%bcond_with internet

Name:           python-%{srcname}
Version:        6.2.0
Release:        %autorelease
Summary:        Collection of utilities for interacting with PyPI

License:        Apache-2.0
URL:            https://github.com/pypa/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

%description
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.

%package -n %{srcname}
Summary:        Twine is a utility for publishing Python packages on PyPI

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
# Test dependencies
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(jaraco-envs)
BuildRequires:  python3dist(munch)
BuildRequires:  python3dist(portend)
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
%if %{with docs}
# Doc (manpage) deps
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-programoutput)
%endif
# with docs
%if %{with internet}
# pytest-services and pytest-socket are not packaged yet
#BuildRequires:  python3dist(pytest-services)
#BuildRequires:  python3dist(pytest-socket)
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  git-core
%endif
# with internet

%endif
# with tests

Obsoletes:      python2-%{srcname} < 1.12.2-3
Obsoletes:      python3-%{srcname} < 1.12.2-3

%description -n %{srcname}
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%if %{without internet}
sed -i '/--disable-socket/d' pytest.ini
%endif

%build
%pyproject_wheel
%if %{with docs}
PYTHONPATH=$PWD sphinx-build-3 -b man docs/ docs/build/man -c docs/
rm -r docs/build/man/.doctrees
%endif

%install
%pyproject_install
%pyproject_save_files twine
%if %{with docs}
install -p -D -T -m 0644 docs/build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1
%endif

%if %{with tests}
%check
%pytest -v \
%if %{without internet}
      --deselect tests/test_integration.py \
      --deselect tests/test_upload.py::test_check_status_code_for_wrong_repo_url \
%endif
;
# without internet
%endif
# with tests

%files -n %{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst AUTHORS
%if %{with docs}
%{_mandir}/man1/%{srcname}.1*
%endif
%{_bindir}/twine

%changelog
%autochangelog
