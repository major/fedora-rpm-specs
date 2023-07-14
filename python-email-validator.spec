Name:           python-email-validator
Version:        2.0.0
Release:        %autorelease
Summary:        A robust email syntax and deliverability validation library

# The CC0-1.0 license is *not allowed* in Fedora for code, but this package
# falls under the following blanket exception:
#
#   Existing uses of CC0-1.0 on code files in Fedora packages prior to
#   2022-08-01, and subsequent upstream versions of those files in those
#   packages, continue to be allowed. We encourage Fedora package maintainers
#   to ask upstreams to relicense such files.
#
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/91#note_1151947383
License:        CC0-1.0
URL:            https://github.com/JoshData/python-email-validator
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# test_requirements.txt pins exact versions and includes unwanted coverage and
# linting dependencies, so we fall back to manual BuildRequires:
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
This library validates that address are of the form x@y.com. This is the sort
of validation you would want for a login form on a website.

Key features:

- Good for validating email addresses used for logins/identity.
- Friendly error messages when validation fails (appropriate to show to end
  users).
- (optionally) Checks deliverability: Does the domain name resolve?
- Supports internationalized domain names and (optionally) internationalized
  local parts.
- Normalizes email addresses (important for internationalized addresses!).}

%description %{_description}

%package -n     python3-email-validator
Summary:        %{summary}

%description -n python3-email-validator %{_description}

%prep
%autosetup -n python-email-validator-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files email_validator

%check
# Even though we have disabled the “network” mark, these still require DNS.
ignore="${ignore-} --ignore=tests/test_deliverability.py"
ignore="${ignore-} --ignore=tests/test_main.py"
%pytest -v tests -m 'not network' ${ignore-}
# Just to be sure, since we have disabled some tests:
%pyproject_check_import

%files -n python3-email-validator -f %{pyproject_files}
%doc CONTRIBUTING.md README.md
%{_bindir}/email_validator

%changelog
%autochangelog
