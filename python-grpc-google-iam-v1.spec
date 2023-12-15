# Upstream test directory is empty.
%bcond_with     tests

%global         srcname     grpc-google-iam-v1
%global         forgeurl    https://github.com/googleapis/python-grpc-google-iam-v1
Version:        0.13.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        GRPC library for the google-iam-v1 service

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
The IDL-derived library for the google-iam (v1) service in Google Cloud.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup


%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
