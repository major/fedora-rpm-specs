%bcond_without  tests

Name:           python-daphne
Version:        4.1.2
Release:        %autorelease
Summary:        Django ASGI (HTTP/WebSocket) server
License:        BSD-3-Clause
URL:            https://github.com/django/daphne
# PyPI tarball is missing a file needed to run tests.
# https://github.com/django/daphne/issues/522
# Should be resolved in 4.1.3.
# https://github.com/django/daphne/pull/530
Source:         %{url}/archive/%{version}/daphne-%{version}.tar.gz
# https://github.com/django/daphne/pull/526
Patch:          0001-fix-tests-with-Twisted-24.7.0-526.patch
BuildArch:      noarch
BuildRequires:  python3-devel

%global common_description %{expand:
Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP,
developed to power Django Channels.  It supports automatic negotiation of
protocols; there is no need for URL prefixing to determine WebSocket endpoints
versus HTTP endpoints.}


%description %{common_description}


%package -n python3-daphne
Summary:        %{summary}


%description -n python3-daphne %{common_description}


%prep
%autosetup -p 1 -n daphne-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files daphne twisted


%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif


%files -n python3-daphne -f %{pyproject_files}
%doc README.rst CHANGELOG.txt
%{_bindir}/daphne


%changelog
%autochangelog
