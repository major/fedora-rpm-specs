# When bootstrapping Python, we cannot test this yet
# RHEL does not include the test dependencies and the dependencies for extras
%bcond tests %{undefined rhel}
%bcond extras %[%{undefined rhel} || %{defined eln}]
%bcond extradeps %{undefined rhel}

Name:           python-urllib3
Version:        2.3.0
Release:        %autorelease
Summary:        HTTP library with thread-safe connection pooling, file post, and more

# SPDX
License:        MIT
URL:            https://github.com/urllib3/urllib3
Source0:        %{url}/archive/%{version}/urllib3-%{version}.tar.gz
# A special forked copy of Hypercorn is required for testing. We asked about
# the possiblility of using a released version in the future in:
#   Path toward testing with a released version of hypercorn?
#   https://github.com/urllib3/urllib3/3334
# Upstream would like to get the necessary changes merged into Hypercorn, but
# explained clearly why the forked copy is needed for now.
#
# Note that dev-requirements.txt references the urllib3-changes branch of
# https://github.com/urllib3/hypercorn/, and we should use the latest commit
# from that branch, but we package using a commit hash for reproducibility.
#
# We do not need to treat this as a bundled dependency because it is not
# installed in the buildroot or otherwise included in any of the binary RPMs.
%global hypercorn_url https://github.com/urllib3/hypercorn
%global hypercorn_commit d1719f8c1570cbd8e6a3719ffdb14a4d72880abb
Source1:        %{hypercorn_url}/archive/%{hypercorn_commit}/hypercorn-%{hypercorn_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# Test dependencies are listed only in dev-requirements.txt. Because there are
# linters and coverage tools mixed in, and exact versions are pinned, we resort
# to manual listing.
# h2==4.1.0: also in the h2 extra
BuildRequires:  %{py3_dist h2}
# coverage==7.6.4: omitted linter/coverage tool
# PySocks==1.7.1
BuildRequires:  %{py3_dist PySocks}
# pytest==8.0.2
BuildRequires:  %{py3_dist pytest}
# pytest-timeout==2.1.0
BuildRequires:  %{py3_dist pytest-timeout}
# pyOpenSSL==24.2.1
BuildRequires:  %{py3_dist pyOpenSSL}
# idna==3.7
BuildRequires:  %{py3_dist idna}
# trustme==1.2.0
BuildRequires:  %{py3_dist trustme}
# cryptography==43.0.1
BuildRequires:  %{py3_dist cryptography}
# towncrier==23.6.0: used for generating a changelog
# pytest-memray==1.5.0;python_version<"3.14" and sys_platform!="win32" and
#     implementation_name=="cpython": not packaged, unwanted profiler
# trio==0.26.2
BuildRequires:  %{py3_dist trio}
# # https://github.com/pallets/quart/pull/369
# Quart @ git+https://github.com/pallets/quart@67110bf383d8973bce1619e957b4b6ea088ad9f2
BuildRequires:  %{py3_dist Quart}
# quart-trio==0.11.1
BuildRequires:  %{py3_dist quart-trio}
# # https://github.com/pgjones/hypercorn/issues/62
# # https://github.com/pgjones/hypercorn/issues/168
# # https://github.com/pgjones/hypercorn/issues/169
# hypercorn @ git+https://github.com/urllib3/hypercorn@urllib3-changes
# hypercorn is packaged, but we need the forked/bundled version
# httpx==0.25.2
BuildRequires:  %{py3_dist httpx}
# pytest-socket==0.7.0: not packaged, not strictly required
%endif

%global _description %{expand:
urllib3 is a powerful, user-friendly HTTP client for Python. urllib3 brings
many critical features that are missing from the Python standard libraries:

  • Thread safety.
  • Connection pooling.
  • Client-side SSL/TLS verification.
  • File uploads with multipart encoding.
  • Helpers for retrying requests and dealing with HTTP redirects.
  • Support for gzip, deflate, brotli, and zstd encoding.
  • Proxy support for HTTP and SOCKS.
  • 100% test coverage.}

%description %{_description}


%package -n python3-urllib3
Summary:        %{summary}

BuildRequires:  ca-certificates
Requires:       ca-certificates

# There has historically been a manual hard dependency on python3-idna.
BuildRequires:  %{py3_dist idna}
Requires:       %{py3_dist idna}

%if %{with extradeps}
# There has historically been a manual hard dependency on python3-pysocks;
# since bringing it in is the sole function of python3-urllib3+socks,
# we recommend it, so it is installed by default.
Recommends:     python3-urllib3+socks
%endif

%description -n python3-urllib3 %{_description}


%if %{with extras}
%pyproject_extras_subpkg -n python3-urllib3 brotli zstd socks h2
%endif


%prep
%autosetup -n urllib3-%{version}
%setup -q -n urllib3-%{version} -T -D -b 1

# Make sure that the RECENT_DATE value doesn't get too far behind what the current date is.
# RECENT_DATE must not be older that 2 years from the build time, or else test_recent_date
# (from test/test_connection.py) would fail. However, it shouldn't be to close to the build time either,
# since a user's system time could be set to a little in the past from what build time is (because of timezones,
# corner cases, etc). As stated in the comment in src/urllib3/connection.py:
#   When updating RECENT_DATE, move it to within two years of the current date,
#   and not less than 6 months ago.
#   Example: if Today is 2018-01-01, then RECENT_DATE should be any date on or
#   after 2016-01-01 (today - 2 years) AND before 2017-07-01 (today - 6 months)
# There is also a test_ssl_wrong_system_time test (from test/with_dummyserver/test_https.py) that tests if
# user's system time isn't set as too far in the past, because it could lead to SSL verification errors.
# That is why we need RECENT_DATE to be set at most 2 years ago (or else test_ssl_wrong_system_time would
# result in false positive), but before at least 6 month ago (so this test could tolerate user's system time being
# set to some time in the past, but not to far away from the present).
# Next few lines update RECENT_DATE dynamically.
recent_date=$(date --date "7 month ago" +"%Y, %_m, %_d")
sed -i "s/^RECENT_DATE = datetime.date(.*)/RECENT_DATE = datetime.date($recent_date)/" src/urllib3/connection.py


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
# Generate BR’s from packaged extras even when tests are disabled, to ensure
# the extras metapackages are installable if the build succeeds.
%pyproject_buildrequires %{?with_extradeps:-x brotli,zstd,socks,h2}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l urllib3


%check
# urllib3.contrib.socks requires urllib3[socks]
#
# urllib3.contrib.emscripten is “special” (import js will fail)
# urllib3.contrib.ntlmpool is deprecated and requires ntlm
# urllib3.contrib.securetransport is macOS only
# urllib3.contrib.pyopenssl requires pyOpenSSL
%{pyproject_check_import %{!?with_extradeps:-e urllib3.contrib.socks -e urllib3.http2*}
                         -e urllib3.contrib.emscripten*
                         -e urllib3.contrib.ntlmpool
                         -e urllib3.contrib.securetransport
                         -e urllib3.contrib.pyopenssl}

# Increase the “long timeout” for slower environments; as of this writing, it
# is increased from 0.1 to 0.5 second.
export CI=1
# Interpose the special forked copy of Hypercorn.
hypercorndir="${PWD}/../hypercorn-%{hypercorn_commit}/src"
export PYTHONPATH="${hypercorndir}:%{buildroot}%{python3_sitelib}"

%if %{with tests}
# This test still times out sometimes, especially on certain architectures,
# even when we export the CI environment variable to increase timeouts.
k="${k-}${k+ and }not (TestHTTPProxyManager and test_tunneling_proxy_request_timeout[https-https])"

%pytest -v -rs ${ignore-} -k "${k-}"
%pytest -v -rs ${ignore-} -k "${k-}" --integration
%endif


%files -n python3-urllib3 -f %{pyproject_files}
%doc CHANGES.rst README.md


%changelog
%autochangelog
