# Require network, so run locally in mock with --with=tests --enable-network
# All tests pass
%bcond_with tests

%global commit fd912d80c5c61cc7f65d4b0362fd201608c444e3

%global desc %{expand: \
A new XNAT client that exposes XNAT objects/functions as python objects/functions.
The aim is to abstract as much of the REST API away as possible and make xnatpy feel
like native Python code. This reduces the need for the user to know the details
of the REST API. Low level functionality can still be accessed via the connection object
which has get, head, put, post, delete methods for more directly calling the REST API.}

Name:           python-xnat
Version:        0.4.2
Release:        %autorelease
Summary:        A new XNAT client that exposes XNAT objects/functions as python objects/functions.
License:        ASL 2.0
URL:            https://gitlab.com/radiology/infrastructure/xnatpy/
Source0:        %{url}/-/archive/%{version}/xnat-%{version}.tar.gz

BuildArch:      noarch

%description
%{desc}

%package -n python3-xnat
Summary:        %{summary}

BuildRequires: python3-devel

%description -n python3-xnat
%{desc}

%prep
%autosetup -n xnatpy-%{version}-%{commit}

# Remove version locks etc.
sed -i -e 's/pytest==.*/pytest/' -e 's/pytest-cov==.*/pytest-cov/' -e '/tox/ d' test_requirements.txt
sed -i '/sphinx/d' requirements.txt

%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -r requirements.txt test_requirements.txt}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xnat

%check
%if %{with tests}
%{pytest}
%endif

%files -n python3-xnat -f %{pyproject_files}
%doc README.rst
%{_bindir}/xnat
%{_bindir}/xnat_cp_project
%{_bindir}/xnat_data_integrity-check

%changelog
%autochangelog
