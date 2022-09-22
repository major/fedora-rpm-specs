%global         srcname  zeep
%global         desc     Zeep inspects the WSDL document and generates the corresponding\
code to use the services and types in the document. This\
provides an easy to use programmatic interface to a SOAP server.

Name:           python-%{srcname}
Version:        4.1.0
Release:        5%{?dist}
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

BuildRequires:  python3-setuptools


# from setup.py
BuildRequires: python3-attrs
BuildRequires: python3-cached_property
BuildRequires: python3-isodate
BuildRequires: python3-lxml
BuildRequires: python3-platformdirs
BuildRequires: python3-requests
BuildRequires: python3-requests-toolbelt
BuildRequires: python3-pytz

## for tests
BuildRequires: python3-freezegun
BuildRequires: python3-mock
BuildRequires: python3-pretend
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest
BuildRequires: python3-requests-file
BuildRequires: python3-requests-mock
BuildRequires: python3-aioresponses
BuildRequires: python3-pytest-asyncio
BuildRequires: python3-pytest-httpx
BuildRequires: python3-xmlsec

%{?python_enable_dependency_generator}

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
sed -i -e "s/\('\(isort\|flake\)\)/# \1/"  -e "s/\('[A-Za-z_-]\+\)==/\1>=/"  setup.py

# replace deprecated and removed httpx_mock.add_response() keywords (pytest_httpx)
# cf. https://github.com/Colin-b/pytest_httpx/blob/develop/CHANGELOG.md#0140---2021-10-22  0.14
#     https://github.com/Colin-b/pytest_httpx/blob/develop/CHANGELOG.md#0180---2022-01-17  0.18
# XXX TODO remove again when upstream switches to a more recent pytest_httpx version
sed 's/\(url="[^"]\+", \)data\(="[^"]\+"\)/\1text\2/' tests/test_async_transport.py -i

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
