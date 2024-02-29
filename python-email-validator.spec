Name:           python-email-validator
Version:        2.1.1
Release:        %autorelease
Summary:        A robust email syntax and deliverability validation library

License:        Unlicense
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

  • Checks that an email address has the correct syntax – great for
    email-based registration/login forms or validing data.
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
%pytest -v tests -m 'not network'

%files -n python3-email-validator -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/email_validator

%changelog
%autochangelog
