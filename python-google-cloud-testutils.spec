# F35: Do not update past 1.3.1. F35's protobuf is too old.

# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-testutils
%global         forgeurl    https://github.com/googleapis/python-test-utils
Version:        1.3.3
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python test utilities for Google Cloud APIs

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

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
%forgesetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files test_utils

# Remove extra scripts and tests.
rm -rf %{buildroot}%{python3_sitelib}/{scripts,tests}
rm -f %{buildroot}%{_bindir}/lower-bound-checker


%check
%pyproject_check_import -e "tests*"

%if %{with tests}
# Lower bounds checking tests won't work since installing things via
# pip is not going to work during RPM builds.
%pytest --disable-warnings --ignore tests/unit/test_lower_bound_checker.py
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md


%changelog
%autochangelog
