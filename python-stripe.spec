Name:           python-stripe
Version:        5.4.0
Release:        2%{?dist}
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
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.4.0-2
- Rebuilt for Python 3.12

* Fri Mar 31 2023 Roman Inflianskas <rominf@aiven.io> - 5.4.0-1
- Update to 5.4.0 (resolve rhbz#2183323)

* Mon Mar 27 2023 Roman Inflianskas <rominf@aiven.io> - 5.3.0-1
- Update to 5.3.0 (resolve rhbz#2173125)

* Mon Feb 20 2023 Roman Inflianskas <rominf@aiven.io> - 5.2.0-1
- Update to 5.2.0 (resolve rhbz#2152039)
- Update testing instructions

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Roman Inflianskas <rominf@aiven.io> - 5.0.0-1
- Update to 5.0.0 (resolve rhbz#2133045)

* Tue Oct 04 2022 Roman Inflianskas <rominf@aiven.io> - 4.2.0-1
- Update to 4.2.0 (resolve rhbz#2130038)

* Fri Sep 02 2022 Paul Wouters <paul.wouters@aiven.io - 4.1.0-1
- Resolves rhbz#2120817 python-stripe-4.1.0 is available

* Fri Aug 12 2022 Roman Inflianskas <rominf@aiven.io> - 4.0.2-1
- Update to 4.0.2  (resolve rhbz#2110016)

* Fri Aug 12 2022 Roman Inflianskas <rominf@aiven.io> - 3.5.0-1
- Update to 3.5.0
- Update testing instructions

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Roman Inflianskas <rominf@aiven.io> - 3.4.0-1
- Resolves rhbz#2081427 python-stripe-3.4.0 is available

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Roman Inflianskas <rominf@aiven.io> - 3.3.0-1
- Update to 3.3.0 (#2081427)

* Tue May 03 2022 Paul Wouters <paul.wouters@aiven.io> - 2.74.0-1
- Resolves rhbz#2070208 python-stripe-2.74.0 is available

* Wed Mar 30 2022 Roman Inflianskas <rominf@aiven.io> - 2.69.0-1
- Update to 2.69.0 (#2067325), remove unneeded license line

* Mon Mar 07 2022 Roman Inflianskas <rominf@aiven.io> - 2.67.0-1
- Update to 2.67.0 (#2055335)

* Fri Jan 21 2022 Roman Inflianskas <rominf@aiven.io> - 2.65.0-1
- Update to 2.65.0 (#2043177)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Roman Inflianskas <rominf@aiven.io> - 2.64.0-1
- Initial package
