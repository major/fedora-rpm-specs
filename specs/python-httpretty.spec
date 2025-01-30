%global github_owner    gabrielfalcao
%global github_name     HTTPretty
%global srcname         httpretty

%if 0%{?fedora}
%global run_tests 1
%else
# missing deps in epel9
%global run_tests 0
%endif

Name:           python-httpretty
Version:        1.1.4
Release:        %autorelease
Summary:        HTTP request mock tool for Python

License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        %{pypi_source}
# Avoid unnecessary remote access requirement (note: test only actually
# does a remote connection after PR #313)
Patch1:         python-httpretty-fakesock_getpeercert_noconnect.patch
# Remote access (these tests were skipped upstream in <= 0.9.7)
Patch2:         skip-test_passthrough.patch
# Remove timeout, which causes some tests to fail in Koji
# 
# Fixes RHBZ#2046877
Patch3:         test_response-no-within.patch
# https://github.com/gabrielfalcao/HTTPretty/issues/457
Patch4:         test_handle_slashes.patch
# https://github.com/gabrielfalcao/HTTPretty/pull/479/files
# Fixes RHBZ#2261569
Patch5:         chunked_requests_handled_by_urllib3.patch  
# Mock socket.shutdown for compatibility with urllib3 >= 2.3
Patch6:         https://github.com/gabrielfalcao/HTTPretty/pull/485.patch

BuildArch:      noarch

%global _description\
Once upon a time a python developer wanted to use a RESTful API, everything was\
fine but until the day he needed to test the code that hits the RESTful API:\
what if the API server is down? What if its content has changed?\
Don't worry, HTTPretty is here for you.

%description %_description

%package -n python3-httpretty
Summary:        HTTP request mock tool for Python 3
Requires:       python3-six

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{run_tests}
BuildRequires:  python3-boto3
BuildRequires:  python3-httplib2
BuildRequires:  python3-httpx
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-sure
BuildRequires:  python3-urllib3
BuildRequires:  python3-tornado
%if %{defined fc40} || %{defined el9}
BuildRequires:  python3-eventlet
%endif
BuildRequires:  python3-freezegun
BuildRequires:  python3-redis
%endif

%description -n python3-httpretty
Once upon a time a python developer wanted to use a RESTful API, everything was
fine but until the day he needed to test the code that hits the RESTful API:
what if the API server is down? What if its content has changed?
Don't worry, HTTPretty is here for you.


%prep
%autosetup -n httpretty-%{version} -p1

# Alternative for building from commit tarball
#autosetup -n %%{github_name}-%%{github_commit} -p1

%build
%py3_build

%install
%py3_install

%check
%if %{run_tests}
# test_httpretty_should_handle_paths_starting_with_two_slashes
# is broken with requests 2.32.3 but the change might be reverted.
# See:
# - https://github.com/gabrielfalcao/HTTPretty/issues/457
# - https://github.com/psf/requests/issues/6711
# test_426_mypy_segfault seems to fail without real internet connection ?
# test_bypass+test_debug+test_recording_calls rely on undefined pytest fixture ?
%pytest -v \
  --ignore tests/bugfixes/pytest/test_426_mypy_segfault.py \
  --ignore tests/functional/test_bypass.py \
  --ignore tests/functional/test_debug.py \
  --ignore tests/bugfixes/nosetests \
  -k "not test_httpretty_should_handle_paths_starting_with_two_slashes and not test_recording_calls"
%endif

%files -n python3-httpretty
%doc README.rst
%license COPYING
%{python3_sitelib}/httpretty
%{python3_sitelib}/httpretty-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
