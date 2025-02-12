Name:           python-aiohappyeyeballs
Version:        2.4.4
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

# fix: ensure all timers are cancelled when after staggered race finishes
# https://github.com/aio-libs/aiohappyeyeballs/pull/136
# Backported from 2.4.6, which is blocked waiting for poetry-core 2:
# https://src.fedoraproject.org/rpms/python-poetry-core/pull-request/31#comment-245187
# (Applies on top of the downstream coverage patch.)
Patch:          0002-fix-ensure-all-timers-are-cancelled-when-after-stagg.patch

BuildArch:      noarch

BuildRequires:  python3-devel

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


%prep
%autosetup -n aiohappyeyeballs-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L aiohappyeyeballs


%check
%pytest


%files -n python3-aiohappyeyeballs -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
