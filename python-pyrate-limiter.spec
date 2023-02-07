Name:           python-pyrate-limiter
Version:        2.8.5
Release:        1%{?dist}
Summary:        The request rate limiter using Leaky-bucket algorithm 
License:        MIT
URL:            https://github.com/vutran1710/PyrateLimiter
# Missing git tag:
#   Build on pypi is not on github?
#   https://github.com/vutran1710/PyrateLimiter/issues/91
# It is clear which commit corresponds to the PyPI release. We eschew the
# snapinfo field that would normally be needed for packaging from a particular
# commit, since this is equivalent to packaging from the missing tag.
%global commit 103252ca8d5336dc19b69fda6b65798eac932fd2
Source0:        %{url}/archive/%{commit}/PyrateLimiter-%{commit}.tar.gz

# Allow for sleep to be called more times than expected
# https://github.com/vutran1710/PyrateLimiter/pull/93
Patch:          %{url}/pull/93.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies, taken from [tool.poetry.dev-dependencies]:

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# Don’t BR: coverage, flake8_polyfill, pre-commit, pytest-cov.
#
# We use pytest directly, so we don’t need: nox, nox-poetry
#
# These appear to be unused: logzero, PyYAML, schedule

# Since we can only work with what’s packaged, let’s convert SemVer pins to
# lower bounds for test dependencies, dealing with possible future test
# failures if and when they happen.

# Django = "^3.2.8"
BuildRequires:  %{py3_dist Django} >= 3.2.8
# pytest-xdist = "^2.5.0"
BuildRequires:  %{py3_dist pytest-xdist} >= 0.12
# django-redis = "^5.0.0"
# Currently too old:
# https://bugzilla.redhat.com/show_bug.cgi?id=1445556
# BuildRequires:  %%{py3_dist django-redis} >= 5
# fakeredis = "^1.1.0"
# Not yet packaged:
# BuildRequires:  %%{py3_dist fakeredis} >= 1.1
# pytest = "^6.2"
BuildRequires:  %{py3_dist pytest} >= 6.2
# pytest-asyncio = "^0.12"
BuildRequires:  %{py3_dist pytest-asyncio} >= 0.12


%global _description \
The request rate limiter using Leaky-bucket algorithm.


%description %{_description}


%package -n python3-pyrate-limiter
Summary:        %{summary}


%description -n python3-pyrate-limiter %{_description}


%prep
%autosetup -p1 -n PyrateLimiter-%{commit}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyrate_limiter
# LICENSE file is installed directly in site-packages
# https://github.com/vutran1710/PyrateLimiter/issues/92
rm '%{buildroot}%{python3_sitelib}/LICENSE'

%check
# Needs python3dist(fakeredis)
ignore="${ignore-} --ignore=tests/test_02.py"
# Needs python3dist(django-redis)
ignore="${ignore-} --ignore=tests/test_with_django.py"
# Flaky failures in test_concurrency
# https://github.com/vutran1710/PyrateLimiter/issues/94
k="${k-}${k+ and }not test_concurrency[ProcessPoolExecutor-SQLiteBucket]"
%pytest -v -n auto ${ignore-} -k "${k-}"

%files -n python3-pyrate-limiter -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%license LICENSE

%changelog
* Thu Jan 26 2023 Steve Cossette <farchord@gmail.com> - 2.8.5-1
- Initital release of pyratelimiter (2.8.5)
