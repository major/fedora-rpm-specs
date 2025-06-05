%global _without_tests 1
# When bootstrapping Python, we cannot test this yet
# RHEL does not include the test dependencies
%bcond tests    %{undefined rhel}
# The extras are disabled on RHEL to avoid pysocks and deprecated requests[security]
%bcond extras    %[%{undefined rhel} || %{defined eln}]
%bcond extradeps %{undefined rhel}

Name:           python-requests
Version:        2.32.3
Release:        %autorelease
Summary:        HTTP library, written in Python, for human beings

License:        Apache-2.0
URL:            https://pypi.io/project/requests
Source:         https://github.com/requests/requests/archive/v%{version}/requests-v%{version}.tar.gz

# Explicitly use the system certificates in ca-certificates.
# https://bugzilla.redhat.com/show_bug.cgi?id=904614
Patch:          system-certs.patch

# Add support for IPv6 CIDR in no_proxy setting
# This functionality is needed in Openshift and it has been
# proposed for upstream in 2021 but the PR unfortunately stalled.
# Upstream PR: https://github.com/psf/requests/pull/5953
# This change is backported also into RHEL 9.4 (via CS)
Patch:          support_IPv6_CIDR_in_no_proxy.patch

# Fix crash on import if /etc/pki/tls/certs/ca-bundle.crt is missing
# https://bugzilla.redhat.com/show_bug.cgi?id=2297632
# https://github.com/psf/requests/pull/6781
# Note: this can be replaced by https://github.com/psf/requests/pull/6767
# when it is ready, or dropped in a release where that is merged
Patch:          0001-Don-t-create-default-SSLContext-if-CA-bundle-isn-t-p.patch

# Add CA constraint to test CA
#
# Otherwise recent versions of OpenSSL reject it as an invalid CA certificate
# (at least once the test certificates are regenerated).
#
# https://github.com/psf/requests/commit/507409661335bd3dd8a7e39f04d07b42e519becc
Patch:         https://github.com/psf/requests/commit/507409661335bd3dd8a7e39f04d07b42e519becc.patch
# Regenerate test certificates
# https://github.com/psf/requests/commit/9ebebdef98a6aacfbedcf2ca61ba0eaecc2563f4
Patch:         https://github.com/psf/requests/commit/9ebebdef98a6aacfbedcf2ca61ba0eaecc2563f4.patch
# Add key usage extension to test ca.crt
# https://github.com/psf/requests/pull/6924
Patch:          https://github.com/psf/requests/pull/6924.patch
# Together, these three patches fix one of the three regressions reported in
# the following issue, and the only one that we see downstream:
#
# Test regressions with urllib3 2.4.0 on Python 3.13
# https://github.com/psf/requests/issues/6934
#
# See also:
#
# https://github.com/urllib3/urllib3/pull/3577#issuecomment-2765190031

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-httpbin)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(trustme)
%endif

%description
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.


%package -n python%{python3_pkgversion}-requests
Summary:        %{summary}

%description -n python%{python3_pkgversion}-requests
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.


%if %{with extras}
%pyproject_extras_subpkg -n python%{python3_pkgversion}-requests security socks
%endif


%generate_buildrequires
%pyproject_buildrequires %{?with_extradeps:-x security,socks}


%prep
%autosetup -p1 -n requests-%{version}

# env shebang in nonexecutable file
sed -i '/#!\/usr\/.*python/d' src/requests/certs.py

# Some doctests use the internet and fail to pass in Koji. Since doctests don't have names, I don't
# know a way to skip them. We also don't want to patch them out, because patching them out will
# change the docs. Thus, we set pytest not to run doctests at all.
sed -i 's/ --doctest-modules//' pyproject.toml


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files requests


%check
%pyproject_check_import
%if %{with tests}
# test_unicode_header_name - reported: https://github.com/psf/requests/issues/6734
# test_use_proxy_from_environment needs pysocks
%pytest -v tests -k "not test_unicode_header_name %{!?with_extradeps:and not test_use_proxy_from_environment}"
%endif


%files -n python%{python3_pkgversion}-requests -f %{pyproject_files}
%license LICENSE
%doc README.md HISTORY.md


%changelog
%autochangelog
