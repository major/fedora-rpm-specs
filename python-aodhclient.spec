%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa7475c5f2122fec3f90343223fe3bf5aad1080e4
%global pypi_name aodhclient

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

%global common_desc \
This is a client library for Aodh built on the Aodh API. It \
provides a Python API (the aodhclient module) and a command-line tool.

Name:             python-aodhclient
Version:          3.2.0
Release:          2%{?dist}
Summary:          Python API and CLI for OpenStack Aodh

License:          ASL 2.0
URL:              https://launchpad.net/python-aodhclient
Source0:          https://tarballs.openstack.org/%{name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
Patch0:           0001-Revert-Add-OSprofiler-support-for-Aodh-client.patch

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:          Python API and CLI for OpenStack Aodh
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:    python3-setuptools
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    git-core

Requires:         python3-pbr
Requires:         python3-cliff >= 1.14.0
Requires:         python3-oslo-i18n >= 1.5.0
Requires:         python3-oslo-serialization >= 1.4.0
Requires:         python3-oslo-utils >= 2.0.0
Requires:         python3-keystoneauth1 >= 1.0.0
Requires:         python3-osc-lib >= 1.0.1
Requires:         python3-pyparsing

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package  doc
Summary:          Documentation for OpenStack Aodh API Client

BuildRequires:    python3-sphinx
BuildRequires:    python3-openstackdocstheme
BuildRequires:    python3-keystoneauth1
BuildRequires:    python3-oslo-utils
BuildRequires:    python3-oslo-serialization
BuildRequires:    python3-cliff


%description doc
%{common_desc}
(aodh).

This package contains auto-generated documentation.
%endif

%package -n python3-%{pypi_name}-tests
Summary:          Python API and CLI for OpenStack Aodh Tests
Requires:         python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Let RPM handle the requirements
rm -f {,test-}requirements.txt


%build
%{py3_build}

%install
%{py3_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s aodh %{buildroot}%{_bindir}/aodh-3

%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/aodhclient
%{python3_sitelib}/*.egg-info
%{_bindir}/aodh
%{_bindir}/aodh-3
%exclude %{python3_sitelib}/aodhclient/tests

%files -n python3-%{pypi_name}-tests
%license LICENSE
%{python3_sitelib}/aodhclient/tests

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Mon Apr 17 2023 Karolina Kula <kkula@redhat.com> 3.2.0-2
- Reapply osprofiler support removal

* Fri Apr 14 2023 Karolina Kula <kkula@redhat.com> 3.2.0-1
- Update to upstream version 3.2.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Alfredo Moralejo <amoralej@redhat.com> 3.0.0-2
- Removed support for osprofiler

* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 3.0.0-1
- Update to upstream version 3.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.1-4
- Rebuilt for pyparsing-3.0.9

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.4.1-3
- Rebuilt for Python 3.11

* Thu May 19 2022 Joel Capitao <jcapitao@redhat.com> 2.4.1-2
- Removed support for osprofiler

* Wed May 18 2022 Joel Capitao <jcapitao@redhat.com> 2.4.1-1
- Update to upstream version 2.4.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.10

* Mon Nov 22 2021 Joel Capitao <amoralej@redhat.com> - 2.2.0-2
- Removed support for osprofiler

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 2.2.0-1
- Update to upstream version 2.2.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Alfredo Moralejo <amoralej@redhat.com> - 2.1.1-3
- Removed support for osprofiler

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 2.1.1-2
- Update to upstream version 2.1.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Joel Capitao <jcapitao@redhat.com> 2.0.1-3
- Removed Requires osprofiler

* Wed Jun 24 2020 Joel Capitao <jcapitao@redhat.com> 2.0.1-2
- Removed support for osprofiler

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 2.0.1-1
- Update to upstream version 2.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-2
- Removed support for osprofiler

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-1
- Update to upstream version 1.3.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 1.2.0-1
- Update to 1.2.0

