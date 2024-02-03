# When bootstrapping Python, we cannot test this yet
# RHEL does not include the test dependencies and the dependencies for extras 
%if 0%{?rhel}
%bcond_with tests
%bcond_with extras
%else
%bcond_without tests
%bcond_without extras
%endif

Name:           python-urllib3
Version:        1.26.18
Release:        %autorelease
Summary:        HTTP library with thread-safe connection pooling, file post, and more

# SPDX
License:        MIT
URL:            https://github.com/urllib3/urllib3
Source:         %{url}/archive/%{version}/urllib3-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# Test dependencies are listed only in dev-requirements.txt. Because there are
# linters and coverage tools mixed in, and exact versions are pinned, we resort
# to manual listing.
# mock==3.0.5: patched out in %%prep
# coverage~=6.0;python_version>="3.6": omitted linter/coverage tool
# tornado==6.1.0;python_version>="3.6"
BuildRequires:  %{py3_dist tornado} >= 6.1
# PySocks==1.7.1
BuildRequires:  %{py3_dist PySocks} >= 1.7.1
# win-inet-pton==1.1.0: Windows-only workaround
# pytest==6.2.4; python_version>="3.10"
BuildRequires:  %{py3_dist pytest} >= 6.2.4
# pytest-timeout==1.4.2
BuildRequires:  %{py3_dist pytest-timeout} >= 1.4.2
# pytest-freezegun==0.4.2
BuildRequires:  %{py3_dist pytest-freezegun} >= 0.4.2
# flaky==3.7.0: not really required
# trustme==0.7.0
BuildRequires:  %{py3_dist trustme} >= 0.7
# cryptography==38.0.3;python_version>="3.6": associated with the deprecated
#                                             “secure” extra
# python-dateutil==2.8.1
BuildRequires:  %{py3_dist python-dateutil} >= 2.8.1
# gcp-devrel-py-tools==0.0.16: not used in offline testing
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

# grep __version__ src/urllib3/packages/six.py
Provides:       bundled(python3dist(six)) = 1.16.0

%if %{with extras}
# There has historically been a manual hard dependency on python3-pysocks;
# since bringing it in is the sole function of python3-urllib3+socks,
# we recommend it, so it is installed by default.
Recommends:     python3-urllib3+socks
%endif

%description -n python3-urllib3 %{_description}


%if %{with extras}
# We do NOT package the “secure” extra because it is deprecated; see:
# “Deprecate the pyOpenSSL TLS implementation and [secure] extra”
# https://github.com/urllib3/urllib3/issues/2680
%pyproject_extras_subpkg -n python3-urllib3 brotli socks
%endif


%prep
%autosetup -n urllib3-%{version}
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

# Use the standard library instead of a backport
sed -i -e 's/^import mock/from unittest import mock/' \
       -e 's/^from mock import /from unittest.mock import /' \
    test/*.py docs/conf.py


%generate_buildrequires
# Generate BR’s from packaged extras even when tests are disabled, to ensure
# the extras metapackages are installable if the build succeeds.
%pyproject_buildrequires %{?with_extras:-x brotli,socks}


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files urllib3


%check
# urllib3.contrib.socks requires urllib3[socks]
# urllib3.contrib.ntlmpool is deprecated and requires ntlm
# urllib3.contrib.securetransport is macOS only
# urllib3.contrib.pyopenssl requires urllib3[secure]
%{pyproject_check_import %{!?with_extras:-e urllib3.contrib.socks}
                         -e urllib3.contrib.ntlmpool
                         -e urllib3.contrib.securetransport
                         -e urllib3.contrib.pyopenssl}
%if %{with tests}
# Drop the dummyserver tests in koji.  They fail there in real builds, but not
# in scratch builds (weird).
ignore="${ignore-} --ignore=test/with_dummyserver/"
# Don't run the Google App Engine tests
ignore="${ignore-} --ignore=test/appengine/"
# Lots of these tests started failing, even for old versions, so it has something
# to do with Fedora in particular. They don't fail in upstream build infrastructure
ignore="${ignore-} --ignore=test/contrib/"
# Tests for Python built without SSL, but Fedora builds with SSL. These tests
# fail when combined with the unbundling of backports-ssl_match_hostname
ignore="${ignore-} --ignore=test/test_no_ssl.py"
%pytest -v ${ignore-}
%endif


%files -n python3-urllib3 -f %{pyproject_files}
%doc CHANGES.rst README.rst


%changelog
%autochangelog
