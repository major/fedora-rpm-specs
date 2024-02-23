Name:           python-stripe
Version:        8.3.0
Release:        %autorelease
Summary:        Python library for the Stripe API

License:        MIT
URL:            https://github.com/stripe/stripe-python
Source0:        %{url}/archive/v%{version}/stripe-python-%{version}.tar.gz

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
%autosetup -p1 -n stripe-python-%{version}


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
# 3. python3-pytest
# 4. python3-pytest-mock
#
# Then execute:
# In first shell:
# $ go install github.com/stripe/stripe-mock@latest
# $ stripe-mock
# In second shell (replace `~/stripe-python` with actual path with sources):
# $ cd /  # So that pytest use installed stripe version, not sources
# $ pytest --ignore ~/stripe-python/stripe/ ~/stripe-python/


%files -n python3-stripe -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
