
%global forgeurl    https://github.com/dns-lexicon/dns-lexicon
%global forgeversion 3.20.1
Version:            3.20.1
%forgemeta

%global pypi_name dns-lexicon

%if 0%{?rhel} >= 8
# EPEL is currently missing dependencies used by the extras metapackages
# EPEL is currently missing dependencies used by the tests
%bcond_with tests
%bcond_with extras
%else
%bcond_without tests
%bcond_without extras
%endif

# disable tests for now
%bcond_without tests

Name:           python-%{pypi_name}
Release:        2%{?dist}
Summary:        Manipulate DNS records on various DNS providers in a standardized/agnostic way

License:        MIT
URL:            %{forgeurl}
# pypi releases don't contain necessary data to run the tests
Source0:        %{forgesource}
Source1:        create-local-tld-cache.py
Patch:          python-dns-lexicon-tox-config.patch
BuildArch:      noarch

BuildRequires:  python3-devel

# epel is missing full poetry and light packages needed for tests
%if 0%{?rhel >= 8}
#Patch:		disable-poetry-light.patch
%endif

# required to run the test suite
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-vcr
BuildRequires:  python3-pytest-xdist
BuildRequires:  publicsuffix-list
BuildRequires:  python3-tldextract
%endif


%description
Lexicon provides a way to manipulate DNS records on multiple DNS providers in a
standardized way. Lexicon has a CLI but it can also be used as a python
library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}


# Both packages install a Python module named lexicon
# TODO: Remove this once resolved upstream (see upstream #222)
Conflicts:      python3-lexicon

# These "extras" were previously present in upstream lexicon but are not there
# anymore.
# {{{
%if %{with extras}
Obsoletes: python3-%{pypi_name}+easyname < 3.4
Provides: python3dist(%{pypi_name}[easyname]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[easyname]) = %{version}

Obsoletes: python3-%{pypi_name}+gratisdns < 3.4
Provides: python3dist(%{pypi_name}[gratisdns]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[gratisdns]) = %{version}

Obsoletes: python3-%{pypi_name}+henet < 3.4
Provides: python3dist(%{pypi_name}[henet]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[henet]) = %{version}

Obsoletes: python3-%{pypi_name}+hetzner < 3.4
Provides: python3dist(%{pypi_name}[hetzner]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[hetzner]) = %{version}

# lexicon 3.6.0 removed the xmltodict dependency (and the "plesk" extra)
Obsoletes: python3-%{pypi_name}+plesk < 3.6
Provides: python3dist(%{pypi_name}[plesk]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[plesk]) = %{version}
%endif
# }}}

%description -n python3-%{pypi_name}
Lexicon provides a way to manipulate DNS records on multiple DNS providers in a
standardized way. Lexicon has a CLI but it can also be used as a python
library.

This is the Python 3 version of the package.



%package -n     python3-%{pypi_name}+gransy
Summary:        Meta-package for python3-%{pypi_name} and gransy provider
%{?python_provide:%python_provide python3-%{pypi_name}+gransy}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}+gransy
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the gransy provider.



%package -n     python3-%{pypi_name}+localzone
Summary:        Meta-package for python3-%{pypi_name} and localzone provider
%{?python_provide:%python_provide python3-%{pypi_name}+localzone}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}+localzone
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the localzone provider.



%package -n     python3-%{pypi_name}+oci
Summary:        Meta-package for python3-%{pypi_name} and oci provider
%{?python_provide:%python_provide python3-%{pypi_name}+oci}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}+oci
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the oci provider.



%package -n     python3-%{pypi_name}+route53
Summary:        Meta-package for python3-%{pypi_name} and Route 53 provider
%{?python_provide:%python_provide python3-%{pypi_name}+route53}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}+route53
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the Route 53 provider.



%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -f uv.lock

%generate_buildrequires
%if %{with extras}
%pyproject_buildrequires -r -t -e light -x gransy,localzone,oci,route53
%else
%pyproject_buildrequires -r
%endif


%build
# remove shebang
sed -i '1d' src/lexicon/_private/cli.py
%pyproject_wheel

%if %{with tests}
%check
export TLDEXTRACT_CACHE=%{_builddir}/tldextract-cache

# tldextract tries to fetch "public_suffix_list.dat" from the internet on first
# invocation.
# (see https://github.com/john-kurkowski/tldextract/tree/master#note-about-caching)
# The "publicsuffix-list" package provides that data however we need to use
# that to populate a local cache directory.Most of the work is done via:
#   $ tldextract --update --suffix_list_url "file:///usr/share/publicsuffix/public_suffix_list.dat"
#
# However tldextract uses the "file://" url as cache key while the tests use
# "https://publicsuffix.org/list/public_suffix_list.dat". I did not find a way
# get tldextract to use the https url so a small Python script will handle that.
/usr/bin/python3 %{SOURCE1} %{buildroot}%{python3_sitelib}

# lexicon providers which do not work in Fedora due to missing dependencies:
# - SoftLayerProviderTests
TEST_SELECTOR="not SoftLayerProviderTests"

%if %{without extras}
TEST_SELECTOR+=" and not GransyProviderTests and not LocalzoneProviderTests and not OciProviderTests and not OciInstancePrincipalProviderTests and not Route53ProviderTests"
%endif

# We do not use "--xfail-providers-with-missing-deps" because we want to detect
# missing dependencies unless we already know that a certain provider will not
# work.
%pytest -v -k "${TEST_SELECTOR}" -n auto --dist=loadfile tests/
%endif

%install
%pyproject_install
install -pm 0755 %{buildroot}/%{_bindir}/lexicon %{buildroot}/%{_bindir}/lexicon-%{python3_version}
cd %{buildroot}/%{_bindir}
ln -s lexicon-%{python3_version} lexicon-3


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/lexicon
%{_bindir}/lexicon-3
%{_bindir}/lexicon-%{python3_version}
%{python3_sitelib}/lexicon
%{python3_sitelib}/dns_lexicon-%{version}.dist-info

# Extras meta-packages
# {{{
%if %{with extras}

%files -n python3-%{pypi_name}+gransy
%{?python_extras_subpkg:%ghost %{python3_sitelib}/dns_lexicon-%{version}.dist-info}

%files -n python3-%{pypi_name}+localzone
%{?python_extras_subpkg:%ghost %{python3_sitelib}/dns_lexicon-%{version}.dist-info}

%files -n python3-%{pypi_name}+oci
%{?python_extras_subpkg:%ghost %{python3_sitelib}/dns_lexicon-%{version}.dist-info}

%files -n python3-%{pypi_name}+route53
%{?python_extras_subpkg:%ghost %{python3_sitelib}/dns_lexicon-%{version}.dist-info}

%endif
# }}}

%changelog
* Thu Jan 23 2025 Felix Schwarz <fschwarz@fedoraproject.org> - 3.20.1-1
- update to 3.20.1

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 23 2024 Ben Maconi <turboben@fedoraproject.org> - 3.18.0-1
- Updated to 3.18.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Python Maint <python-maint@redhat.com> - 3.17.0-5
- Rebuilt for Python 3.13

* Thu Feb 29 2024 Jonathan Wright <jonathan@almalinux.org> - 3.17.0-4
- Update spec for building on epel9

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 16 2023 Nick Bebout <nb@fedoraproject.org> - 3.17.0-1
- Update to 3.17.0

* Fri Oct 13 2023 Jonathan Wright <jonathan@almalinux.org> - 3.15.1-1
- Update to 3.15.1 rhbz#2232054

* Tue Aug 8 2023 Christian Schuermann <spike@fedoraproject.org> 3.13.0-1
- Update to 3.13.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 3.12.0-2
- Rebuilt for Python 3.12

* Sun Jun 11 2023 Christian Schuermann <spike@fedoraproject.org> 3.12.0-1
- Update to 3.12.0
- Add new duckdns extra package
- Add localzone and oci extra packages since dependancies are now available on Fedora

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 27 2022 Christian Schuermann <spike@fedoraproject.org> 3.11.7-1
- Update to 3.11.7

* Wed Oct 12 2022 Christian Schuermann <spike@fedoraproject.org> 3.11.6-1
- Update to 3.11.6

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-1
- Update to 3.11.4
- rhbz#2117798

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Christian Schuermann <spike@fedoraproject.org> 3.11.3-1
- Update to 3.11.3

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.11.2-2
- Rebuilt for Python 3.11

* Wed May 18 2022 Christian Schuermann <spike@fedoraproject.org> 3.11.2-1
- Update to 3.11.2
- Disable OciInstancePrincipalProviderTests

* Mon May 9 2022 Christian Schuermann <spike@fedoraproject.org> 3.11.0-2
- Disable tests that use tldextract until "suffix_list_url" cli flag is available

* Mon May 9 2022 Christian Schuermann <spike@fedoraproject.org> 3.11.0-1
- Update to 3.11.0

* Sun May 1 2022 Christian Schuermann <spike@fedoraproject.org> 3.10.0-1
- Update to 3.10.0

* Thu Apr 28 2022 Christian Schuermann <spike@fedoraproject.org> 3.9.5-3
- Add "tests" conditional to make tests optional on EPEL
- Ensure that BuildRequires resolve correctly and only relevant tests run when building without extras

* Tue Apr 26 2022 Christian Schuermann <spike@fedoraproject.org> 3.9.5-2
- Reenable tests for GoDady, Transip, Namecheap and NamecheapManaged providers
- Add gransy and ddns extra packages
- Remove explicit BuildRequires (handled by the pyproject_buildrequires macro)
- Remove explicit extra package Requires (handled by automatic dependency generator)
- Remove unused rhel7 macro

* Tue Apr 19 2022 Christian Schuermann <spike@fedoraproject.org> 3.9.5-1
- update to 3.9.5

* Tue Feb 15 2022 Christian Schuermann <spike@fedoraproject.org> 3.9.4-1
- update to 3.9.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Christian Schuermann <spike@fedoraproject.org> 3.9.2-1
- update to 3.9.2

* Mon Jan 17 2022 Christian Schuermann <spike@fedoraproject.org> 3.9.1-1
- update to 3.9.1

* Thu Jan 6 2022 Christian Schuermann <spike@fedoraproject.org> 3.9.0-1
- update to 3.9.0

* Wed Dec 29 2021 Christian Schuermann <spike@fedoraproject.org> 3.8.5-1
- update to 3.8.5

* Tue Dec 28 2021 Christian Schuermann <spike@fedoraproject.org> 3.8.4-1
- update to 3.8.4

* Sat Nov 13 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.8.3-1
- update to 3.8.3 (#2020433)

* Sat Oct 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.8.1-1
- update to 3.8.1 (#2014726)

* Mon Oct 04 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.8.0-1
- update to 3.8.0

* Thu Aug 19 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.7.0-1
- update to 3.7.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.5.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.5.3-1
- update to 3.5.3

* Tue Nov 24 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.5.2-1
- update to 3.5.2

* Mon Nov 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.5.1-1
- update to 3.5.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.17-4
- Add metadata for Python extras subpackages

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.17-3
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.17-2
- add missing sources

* Tue Mar 03 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.17-1
- Update to 3.3.17 (#1764339)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Eli Young <elyscape@gmail.com> - 3.3.4-2
- Rebuild due to Koji issues

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 3.3.4-1
- Update to 3.3.4 (#1725208)
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Eli Young <elyscape@gmail.com> - 3.2.8-1
- Update to 3.2.8 (#1722190)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 3.2.6-1
- Update to 3.2.6 (#1685778)

* Fri Feb 15 2019 Eli Young <elyscape@gmail.com> - 3.1.5-1
- Update to 3.1.5 (#1671162)
- Add meta-subpackages for specific providers

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Eli Young <elyscape@gmail.com> - 3.0.6-1
- Update to 3.0.6
- Declare conflict with python-lexicon
- Remove Python 2 package in Fedora 30+

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 3.0.2-2
- Fix dependencies on Fedora 28

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Mon Oct 08 2018 Eli Young <elyscape@gmail.com> - 2.7.9-1
- Update to 2.7.9 (#1637142)

* Mon Aug 27 2018 Eli Young <elyscape@gmail.com> - 2.7.0-2
- Add dependency on python-cryptography (#1622418)

* Mon Jul 23 2018 Nick Bebout <nb@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Eli Young <elyscape@gmail.com> - 2.4.5-1
- Update to 2.4.5 (#1599479)

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.4-3
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Eli Young <elyscape@gmail.com> - 2.4.4-2
- Remove unnecessary shebang

* Tue Jun 26 2018 Eli Young <elyscape@gmail.com> - 2.4.4-1
- Update to 2.4.4 (#1594777)

* Tue Jun 19 2018 Eli Young <elyscape@gmail.com> - 2.4.3-1
- Update to 2.4.3 (#1592158)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Eli Young <elyscape@gmail.com> - 2.4.0-1
- Update to 2.4.0 (#1589596)

* Tue May 29 2018 Eli Young <elyscape@gmail.com> - 2.3.0-1
- Update to 2.3.0 (#1582799)

* Mon May 07 2018 Eli Young <elyscape@gmail.com> - 2.2.3-1
- Update to 2.2.3 (#1575598)

* Thu May 03 2018 Eli Young <elyscape@gmail.com> - 2.2.2-1
- Update to 2.2.2 (#1574265)

* Sat Mar 24 2018 Eli Young <elyscape@gmail.com> - 2.2.1-1
- Update to 2.2.1
- Use Python 3 by default when available

* Mon Feb 19 2018 Nick Bebout <nb@fedoraproject.org> - 2.1.19-1
- Initial package.
