%global         srcname  zeep
%global         desc     Zeep inspects the WSDL document and generates the corresponding\
code to use the services and types in the document. This\
provides an easy to use programmatic interface to a SOAP server.

Name:           python-%{srcname}
Version:        4.2.1
Release:        1%{?dist}
Summary:        A fast and modern Python SOAP client

License:        MIT and BSD
URL:            https://github.com/mvantellingen/python-zeep
Source0:        %pypi_source

BuildArch:      noarch
# Since python-aiohttp excludes s390x we have to exclude it, as well
# (because python-aioresponses requires python aiohttp)
# See also:
# https://src.fedoraproject.org/rpms/python-aiohttp/blob/67855c61bee706fcd99305d1715aad02d898cbfc/f/python-aiohttp.spec#_22
# https://fedoraproject.org/wiki/EPEL/FAQ#RHEL_8.2B_has_binaries_in_the_release.2C_but_is_missing_some_corresponding_-devel_package._How_do_I_build_a_package_that_needs_that_missing_-devel_package.3F
%if %{defined el8}
ExcludeArch:    s390x
%endif

# required for py3_build macro
BuildRequires:  python3-devel

# NB: the python dependency auto-generator is enabled by default,
#     we opt-in the build-time dependency generator, cf. below


%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

# disable linting dependencies and exact test dependencies
sed -i -e '/isort\|flake\|coverage\[toml\]/d' -e 's/\([a-z]\)[>=]\{2\}[0-9.]\+/\1/' setup.py


%generate_buildrequires
%pyproject_buildrequires -x xmlsec -x test


%build
%py3_build


%install
%py3_install

%check
PYTHONPATH=src %{__python3} -m pytest tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst examples
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*-py*.egg-info/


%changelog
* Sun Mar 26 2023 Georg Sauthoff <mail@gms.tf> - 4.2.1-1
- bump version (fixes fedora#2144333)
- migrate to build-time dependency generator as proposed in #2079681#c4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 05 2022 Georg Sauthoff <mail@gms.tf> - 4.2.0-1
- bump version (fixes fedora#2139784)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 4.1.0-4
- Rebuilt for Python 3.11

* Sat Feb 05 2022 Georg Sauthoff <mail@gms.tf> - 4.1.0-3
- Adapt tests for pytest_httpx API churn (fixes fedora#2046921)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Georg Sauthoff <mail@gms.tf> - 4.1.0-1
- bump version (fixes fedora#1993701)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Georg Sauthoff <mail@gms.tf> - 4.0.0-1
- bump version

* Fri Sep 11 2020 Georg Sauthoff <mail@gms.tf> - 3.4.0-8
- add tornado dependency for tests
- cleanup dependencies

* Thu Sep 10 2020 Georg Sauthoff <mail@gms.tf> - 3.4.0-7
- EPEL8: exclude s390x because of aiohttp
- activate more tests

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Georg Sauthoff <mail@gms.tf> - 3.4.0-5
- Be more explicit regarding setuptools depenency,
  cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Georg Sauthoff <mail@gms.tf> - 3.4.0-2
- fix date format

* Sun Dec 08 2019 Georg Sauthoff <mail@gms.tf> - 3.4.0-1
- bump to latest upstream

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Georg Sauthoff <mail@gms.tf> - 3.3.1-1
- initial packaging
