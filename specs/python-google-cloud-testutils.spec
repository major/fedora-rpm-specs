# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-testutils

Name:           python-%{srcname}
Version:        1.7.1
Release:        %autorelease
Summary:        Python test utilities for Google Cloud APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python
Source0:        %{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-google-auth

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This is a collection of common tools used in system tests of Python client
libraries for Google APIs.}

%description %{_description}


%package -n python3-%{srcname}
%py_provides    python3-test-utils
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files test_utils

# Remove extra scripts and tests.
rm %{buildroot}%{_bindir}/lower-bound-checker

%check
%pyproject_check_import -e "tests*"

%if %{with tests}
# Lower bounds checking tests won't work since installing things via
# pip is not going to work during RPM builds.
%pytest --disable-warnings --ignore tests/unit/test_lower_bound_checker.py
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
