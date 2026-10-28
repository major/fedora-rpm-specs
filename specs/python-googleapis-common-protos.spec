%bcond tests 1

# When bootstrapping, we do not include the “grpc” extra in the BR’s. That adds
# a BR on python3dist(grpcio), but this package is required by
# python3dist(grpcio-status), which creates a circular dependency with grpc.
# Flip this back to with when grpc >= 1.59 is built
%bcond_without bootstrap

Name:           python-googleapis-common-protos
Version:        1.75.5
Release:        %autorelease
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python
Source:         %{pypi_source googleapis-common-protos}
BuildArch:      noarch
BuildRequires:  python3-devel

BuildSystem:    pyproject
BuildOption(install):  -l google
%if %{without bootstrap}
BuildOption(generate_buildrequires): -x grpc
%endif


%if 0%{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-googleapis-common-protos
Summary:        %{summary}

%description -n python3-googleapis-common-protos %{common_description}


%if %{without bootstrap}
%pyproject_extras_subpkg -n python3-googleapis-common-protos grpc
%endif

%check
%if %{with bootstrap}
%pyproject_check_import -e "google.longrunning.operations_grpc*" -e "google.longrunning.operations_pb2_grpc"
%else
%pyproject_check_import
%endif
%if %{with tests}
# NOTE(mhayden): Setting PYTHONUSERBASE as a hack for PEP 420 namespaces.
# Thanks to churchyard for the fix.
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit %{?with_bootstrap:--ignore=tests/unit/test_operations.py}
%endif


%files -n python3-googleapis-common-protos -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
