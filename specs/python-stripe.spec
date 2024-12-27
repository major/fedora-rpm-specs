%global forgeurl https://github.com/stripe/stripe-python
Version:        11.4.1
%forgemeta

Name:           python-stripe
Release:        %autorelease
Summary:        Python library for the Stripe API

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The Stripe Python library provides convenient access to the Stripe API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the
Stripe API.}

%description %_description

%package -n python3-stripe
Summary:        %{summary}

%description -n python3-stripe %_description


%prep
%forgeautosetup -- -n stripe-python-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files stripe


%check
%pyproject_check_import

# Testing suite depends on outdated unpackaged go libraries, hence no test
# here.
#
# To run tests manually, install:
# 1. The package
# 2. go
# 3. python3-aiohttp
# 4. python3-anyio
# 5. python3-httpx
# 6. python3-pytest
# 7. python3-pytest-mock
# 8. python3-trio
#
# Then execute:
# In first shell:
# $ go install github.com/stripe/stripe-mock@master
# $ stripe-mock
# In second shell (replace `~/stripe-python` with actual path with sources):
# $ cd /  # So that pytest use installed stripe version, not sources
# $ pytest --ignore ~/stripe-python/stripe/ ~/stripe-python/


%files -n python3-stripe -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
