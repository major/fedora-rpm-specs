# Created by pyp2rpm-3.2.3
%global pypi_name scitokens

Name:           python-%{pypi_name}
Version:        1.8.1
Release:        8%{?dist}
Summary:        SciToken reference implementation library

License:        Apache-2.0
URL:            https://scitokens.org
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

# build requirements
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# test requirements
%if 0%{?rhel} == 7
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-jwt >= 1.6.1
BuildRequires:  python%{python3_pkgversion}-requests
%else
BuildRequires:  python3-cryptography
BuildRequires:  python3-pytest
BuildRequires:  python3-jwt >= 1.6.1
BuildRequires:  python3-requests
%endif

%description
SciToken reference implementation library

%package -n     python3-%{pypi_name}
Obsoletes:      python3-scitokens < 1.6.2-2
Summary:        %{summary}

%description -n python3-%{pypi_name}
SciToken reference implementation library

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if 0%{?rhel} == 7
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
(cd tests/ && %{__python3} -m pytest --verbose -ra . --no-network)
%else
%pytest --verbose -ra tests/ --no-network
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info
%doc README.rst
%{_bindir}/scitokens-admin-create-key
%{_bindir}/scitokens-admin-create-token
%{_bindir}/scitokens-verify-token

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.8.1-7
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.8.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 09 2023 Derek Weitzel <dweitzel@unl.edu> - 1.8.1-1
- Turn off tests that require networking

* Tue Aug 08 2023 Derek Weitzel <dweitzel@unl.edu> - 1.8.0-1
- Add demo token issuer convenience functions
- Improve testing of deserialization
- Add RPM improvements for EPEL

* Tue Nov 22 2022 Derek Weitzel <dweitzel@unl.edu> - 1.7.4-1
- Fix the version within the package

* Tue Nov 22 2022 Derek Weitzel <dweitzel@unl.edu> - 1.7.3-1
- Remove aud enforcement from deserailize function
- Add configuration for readthedocs
- Remove six dependency

* Tue Oct 04 2022 Derek Weitzel <dweitzel@unl.edu> - 1.7.2-1
- Documentation updates

* Wed Sep 28 2022 Derek Weitzel <dweitzel@unl.edu> - 1.7.1-1
- Documentation updates
- Fix setup tools and add pyproject.toml

* Fri Feb 18 2022 Derek Weitzel <dweitzel@unl.edu> - 1.7.0-1
- Fix serialize mismatch between Python 3 and Python 2
- Fix bug decoding a token with no audience
- Update algorithm used to test UnsupportedKeyException
- Update pyjwt version in requirements.txt
- Default cached public keys set to 4 days

* Wed Nov 3 2021 Brian Lin <blin@cs.wisc.edu> - 1.6.2-1
- Fix Python library version (SOFTWARE-4879)

* Wed Nov 3 2021 Brian Lin <blin@cs.wisc.edu> - 1.6.1-1
- Reduce PyJWT version requirement made possible by #121 (SOFTWARE-4879)

* Mon Oct 11 2021 Derek Weitzel <dweitzel@cse.unl.edu> - 1.6.0-1
- Ensure compatibility with older versions of PyJWT
- Adding multiple aud in token support

* Mon Oct 11 2021 Derek Weitzel <dweitzel@cse.unl.edu> - 1.5.0-1
- Include tests in distribution
- Bump pyjwt version
- Add test run with minimum dependencies
- Run continuous integration on macOS and windows
- Check verified claims for issuer in SciToken.serialize
- Add base SciTokensException class
- Remove verify=False keyword from calls to decode()
- Print package list in CI jobs
- Use python3_pkgversion macro in RPM package names
- Move package version declaration into 'scitokens' module
- Fix deprecation warning from cryptography.utils.int_from_bytes

* Mon Apr 19 2021 Derek Weitzel <dweitzel@cse.unl.edu> - 1.4.0-1
- Add WLCG Token Discovery static function

* Mon Jan 25 2021 Derek Weitzel <dweitzel@cse.unl.edu> - 1.3.1-1
- Fix dependency change of behavior in PyJWT
- Add lifetime argument to scitokens-admin-create-token

* Wed Sep 30 2020 Diego Davila <didavila@ucsd.edu> - 1.2.4-3
- Force the creation of symlinks so it doesn't fail on update (software-4233)

* Mon Sep 28 2020 Diego Davila <didavila@ucsd.edu> - 1.2.4-2
- Avoid overwriting of scripts: scitokens-admin-create-* (software-4233) 

* Tue Sep 22 2020 Derek Weitzel <dweitzel@cse.unl.edu> - 1.2.4-1
- Same version in setup.py and spec

* Fri Sep 11 2020 Diego Davila <didavila@ucsd.edu> - 1.2.2-3
- Add conditions to build both py2 and py3 packages for el7 (software-4233)

* Mon Aug 10 2020 Diego Davila <didavila@ucsd.edu> - 1.2.2-2
- Add conditions to build for el8 (software-4126)

* Fri Feb 22 2019 Derek Weitzel <dweitzel@cse.unl.edu> - 1.2.2-1
- Add EC support to the admin tools

* Sun Oct 21 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.2.1-1
- Support multiple audiences in verifier

* Tue Jul 10 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.2.0-1
- Merge in the "scope" change accidently mentioned in 1.1.0

* Fri Jul 6 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.1.0-1
- Add support for updated RFC for "scope"
- Add support for Elliptic Curve cryptography

* Tue Jan 30 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.0.2-1
- Fix bug when configuration is not specified

* Tue Jan 30 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.0.0-1
- Add optional configuration file
- Fix bug for missing kid
- Add automatic jti generation

* Mon Nov 06 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.3-1
- Add subject testing in the Enforcer

* Mon Nov 06 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.2-3
- Include dependency for python-setuptools

* Fri Nov 03 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.2-2
- Update packaging to not include 2 scripts for the admin-create*
- Include the correct package for python-jwt dependency

* Thu Nov 02 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.2-1
- Version bump to include spec in tag

* Wed Nov 01 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.1-1
- Fix packaging to include internal util module

* Wed Nov 01 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.0-1
- Initial package.
