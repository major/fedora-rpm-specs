%bcond_without  tests

# When bootstrapping, we do not include the “grpc” extra in the BR’s. That adds
# a BR on python3dist(grpcio), but this package is required by
# python3dist(grpcio-status), which creates a circular dependency with grpc.
%bcond_with bootstrap

%global         srcname     googleapis-common-protos
%global         forgeurl    https://github.com/googleapis/python-api-common-protos/
Version:        1.61.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}


%pyproject_extras_subpkg -n python3-%{srcname} grpc


%prep
%forgeautosetup


%generate_buildrequires
%pyproject_buildrequires -r %{?!with_bootstrap:-x grpc}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
# Upstream has no tests.
#
# Note that google and google.logging are namespace packages.
%pyproject_check_import %{?with_bootstrap:-e 'google.longrunning.*grpc*'}

%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc CODE_OF_CONDUCT.md
%doc README.rst
%{python3_sitelib}/googleapis_common_protos-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
