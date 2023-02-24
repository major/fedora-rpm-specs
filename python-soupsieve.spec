%bcond_without tests

Name:           python-soupsieve
Version:        2.4
Release:        %autorelease
Summary:        CSS selector library

License:        MIT
URL:            https://github.com/facelessuser/soupsieve
Source0:        https://github.com/facelessuser/soupsieve/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS
selectors. Soup Sieve currently provides selectors from the CSS level 1
specifications up through the latest CSS level 4 drafts and beyond (though some
are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin
select feature, and as of Beautiful Soup version 4.7.0, it now is. Soup Sieve
can also be imported in order to use its API directly for more controlled,
specialized parsing.

Soup Sieve has implemented most of the CSS selectors up through the latest CSS
draft specifications, though there are a number that don't make sense in a
non-browser environment. Selectors that cannot provide meaningful functionality
simply do not match anything.}

%description %_description

%package -n python3-soupsieve
Summary:        %{summary}

%description -n python3-soupsieve %_description

%prep
%autosetup -n soupsieve-%{version}

# Do not run coverage report during check
sed -Ei 's/ ?--cov(-[^ ]+)? +[^ ]+//g' tox.ini
sed -i 's/coverage.*//' tox.ini

# Support posargs in tox.ini
sed -i 's/\(py\.test.*\)$/\1 \{posargs\}/' tox.ini

%generate_buildrequires
%pyproject_buildrequires -w %{?with_tests:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files soupsieve

%if %{with tests}
%check
# test_contains_cdata_html and test_contains_own_cdata_html are disabled to unblock Python 3.10 rebuild
# downstream report: https://bugzilla.redhat.com/show_bug.cgi?id=1962458
%tox -- -- -k 'not test_namespace_xml_with_namespace and not test_contains_cdata_html and not test_contains_own_cdata_html'
%endif

%files -n python3-soupsieve -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
