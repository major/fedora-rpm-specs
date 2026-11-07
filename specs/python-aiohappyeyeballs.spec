Name:           python-aiohappyeyeballs
Version:        2.7.1
Release:        %autorelease
Summary:        Happy Eyeballs for asyncio

License:        PSF-2.0
URL:            https://github.com/aio-libs/aiohappyeyeballs
# The GitHub archive contains CHANGELOG.md and other ancillary files that the
# PyPI sdist lacks.
Source:         %{url}/archive/v%{version}/aiohappyeyeballs-%{version}.tar.gz

# Downstream-only: remove pytest options for coverage analysis
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-remove-pytest-options-for-coverage-a.patch
# Do not restore the default event loop policy in test module teardowns
#
# The event loop policy system, deprecated since Python 3.14, is removed
# in Python 3.16. See https://docs.python.org/dev/whatsnew/3.16.html#id3.
#
# Fixes:
#
# Tests affected by event loop policy system removal in Python 3.16
# https://github.com/aio-libs/aiohappyeyeballs/issues/266
#
# Raised as a potential solution in the upstream issue, but not yet offered as
# a PR because feedback is wanted. Still, this is good enough for a downstream
# patch.
Patch:          0002-Do-not-restore-the-default-event-loop-policy-in-test.patch

BuildSystem:    pyproject
BuildOption(install): --assert-license aiohappyeyeballs

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}

%global common_description %{expand:
This library exists to allow connecting with Happy Eyeballs (RFC 8305) when you
already have a list of addrinfo and not a DNS name.

The stdlib version of loop.create_connection() will only work when you pass in
an unresolved name which is not a good fit when using DNS caching or resolving
names via another method such as zeroconf.}

%description %{common_description}


%package -n     python3-aiohappyeyeballs
Summary:        %{summary}

%description -n python3-aiohappyeyeballs %{common_description}


%check -a
%pytest


%files -n python3-aiohappyeyeballs -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
