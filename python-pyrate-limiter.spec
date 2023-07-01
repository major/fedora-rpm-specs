Name:           python-pyrate-limiter
Version:        2.10.0
Release:        2%{?dist}
Summary:        The request rate limiter using Leaky-bucket algorithm 
License:        MIT
URL:            https://github.com/vutran1710/PyrateLimiter
Source0:        %{pypi_source pyrate_limiter}

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
BuildRequires:  %{py3_dist pytest-xdist} >= 2.5
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
%autosetup -n pyrate_limiter-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyrate_limiter

%check
# Needs python3dist(fakeredis)
ignore="${ignore-} --ignore=tests/test_02.py"
# Needs python3dist(django-redis)
ignore="${ignore-} --ignore=tests/test_with_django.py"
# Flaky failures in
# tests/test_context_decorator.py::test_ratelimit__delay_synchronous
# https://github.com/vutran1710/PyrateLimiter/issues/101
k="${k-}${k+ and }not test_ratelimit__delay_synchronous"
%pytest -v -n auto ${ignore-} -k "${k-}"

%files -n python3-pyrate-limiter -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.10.0-2
- Rebuilt for Python 3.12

* Tue May 2 2023 Steve Cossette <farchord@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Sun Feb 26 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 2.9.1-1
- Update to 2.9.1

* Tue Feb 21 2023 Steve Cossette <farchord@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Thu Jan 26 2023 Steve Cossette <farchord@gmail.com> - 2.8.5-1
- Initital release of pyratelimiter (2.8.5)
