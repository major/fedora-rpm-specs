Name:           python-email-validator
Version:        2.1.0
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
#
# Upstream was asked to consider relicensing:
#
# Please consider an alternative license
# https://github.com/JoshData/python-email-validator/issues/113
License:        CC0-1.0
URL:            https://github.com/JoshData/python-email-validator
Source:         %{url}/archive/v%{version}/python-email-validator-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# test_requirements.txt pins exact versions and includes unwanted coverage and
# linting dependencies, so we fall back to manual BuildRequires:
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
This library validates that a string is of the form name@example.com and
optionally checks that the domain name is set up to receive email. This is the
sort of validation you would want when you are identifying users by their email
address like on a registration/login form (but not necessarily for composing an
email message).

Key features:

  • Checks that an email address has the correct syntax – good for
    registration/login forms or other uses related to identifying users.
  • Gives friendly English error messages when validation fails that you can
    display to end-users.
  • Checks deliverability (optional): Does the domain name resolve? (You can
    override the default DNS resolver to add query caching.)
  • Supports internationalized domain names and internationalized local parts.
  • Rejects addresses with unsafe Unicode characters, obsolete email address
    syntax that you’d find unexpected, special use domain names like
    @localhost, and domains without a dot by default. This is an opinionated
    library!
  • Normalizes email addresses (important for internationalized and
    quoted-string addresses!)
  • Python type annotations are used.}

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
%pyproject_save_files -l email_validator

%check
# Even though we have disabled the “network” mark, these still require DNS.
ignore="${ignore-} --ignore=tests/test_deliverability.py"
ignore="${ignore-} --ignore=tests/test_main.py"
%pytest -v tests -m 'not network' ${ignore-}
# Just to be sure, since we have disabled some tests:
%pyproject_check_import

%files -n python3-email-validator -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/email_validator

%changelog
%autochangelog
