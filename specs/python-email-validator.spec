Name:           python-email-validator
Version:        2.2.0
Release:        %autorelease
Summary:        A robust email syntax and deliverability validation library

License:        Unlicense
URL:            https://github.com/JoshData/python-email-validator
Source0:        %{url}/archive/v%{version}/python-email-validator-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format, based closely on the
# comments in email_validator/__main__.py, email_validator/__init__.py, and
# README.md.
#
# Interest in a man page?
# https://github.com/JoshData/python-email-validator/issues/146
Source1:        email_validator.1

# Fix a few minor typos
# https://github.com/JoshData/python-email-validator/pull/143
Patch:          %{url}/pull/143.patch

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

  • Checks that an email address has the correct syntax – great for
    email-based registration/login forms or validating data.
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
%autosetup -n python-email-validator-%{version} -p1

# Removes test where IPv4 address is embeded into IPv6 address.
# Parsing of this type of IPv6 seems to be broken in Python.
# https://github.com/python/cpython/issues/128840#issuecomment-2914324533
sed -i "/IPv6:1111:2222:3333:4444:5555:6666:255.255.255.255/d" tests/test_syntax.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l email_validator
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'

%check
%pytest -v tests -m 'not network'

%files -n python3-email-validator -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/email_validator
%{_mandir}/man1/email_validator.1*

%changelog
%autochangelog
