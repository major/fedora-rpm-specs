# Enable tests by default.
%bcond_without  tests

%global         srcname         google-api-core
%global         forgeurl        https://github.com/googleapis/python-api-core
Version:        2.11.1
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Core Library for Google Client Libraries

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  python3-devel

Epoch:          1

%if %{with tests}
BuildRequires:  python3dist(google-auth)
BuildRequires:  python3dist(googleapis-common-protos)
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(grpcio-gcp)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(proto-plus)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(six)
%endif

BuildArch:      noarch

%global _description %{expand:This library is not meant to stand-alone.
Instead it defines common helpers used by all Google API clients.}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
# Extras
Requires:       python3dist(grpcio)
Requires:       python3dist(grpcio-status)

%description -n python3-%{srcname}
%{_description}

%pyproject_extras_subpkg -n python3-%{srcname} grpc


%prep
%forgeautosetup -p1

# Allow a slightly older protobuf.
sed -i 's/"protobuf.*",/"protobuf>=3.19.4",/' setup.py

# Allow a slightly older version of grpcio.
# NOTE(mhayden): All of the tests pass fine with 1.48.3
# which is in rawhide/f38 as of 2023-02-20.
sed -i 's/1.49.1/1.48.3/g' setup.py

# Replace mock imports with unittest.mock.
grep -rl "^[[:space:]]*import mock" tests | \
    xargs sed -i -E 's/^([[:space:]]*)import mock/\1from unittest import mock/'

%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
%if %{with tests}
# Work around an unusual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest tests/unit \
    -k "not test_wrap_unary_errors \
        and not test_wrap_stream_errors_invocation \
        and not test_wrap_stream_errors_iterator_initialization \
        and not test_wrap_stream_errors_during_iteration"
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md SECURITY.md
%{python3_sitelib}/google_api_core-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
