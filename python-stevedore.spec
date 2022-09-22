%{?python_enable_dependency_generator}
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x4c29ff0e437f3351fd82bdf47c5a3bc787dc7035
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc Manage dynamic plugins for Python applications

Name:           python-stevedore
Version:        3.5.0
Release:        3%{?dist}
Summary:        Manage dynamic plugins for Python applications

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/openstack/stevedore
Source0:        https://tarballs.openstack.org/stevedore/stevedore-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source1:        https://tarballs.openstack.org/stevedore/stevedore-%{upstream_version}.tar.gz.asc
Source2:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-mock
BuildRequires:  python3-testrepository
#BuildRequires:  python3-discover
#BuildRequires:  python3-oslotest

%description
%{common_desc}

%package -n python3-stevedore
Summary:        Manage dynamic plugins for Python applications
Group:          Development/Libraries
%{?python_provide:%python_provide python3-stevedore}

%if (0%{?fedora} && 0%{?fedora} < 32) || (0%{?rhel} && 0%{?rhel} < 9)
Requires:       python3-importlib-metadata >= 1.7.0
%endif


%description -n python3-stevedore
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q -n stevedore-%{upstream_version}

# let RPM handle deps
rm -f requirements.txt

%build
%{py3_build}

%install
%{py3_install}

%check
#TODO: reenable when commented test requirements above are available
#
#PYTHONPATH=. nosetests
#
#%if 0%{?with_python3}
#pushd %{py3dir}
#PYTHONPATH=. nosetests-%{python3_version}
#popd
#%endif

%files -n python3-stevedore
%license LICENSE
%doc README.rst
%{python3_sitelib}/stevedore
%{python3_sitelib}/stevedore-*.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.5.0-2
- Rebuilt for Python 3.11

* Thu May 19 2022 Joel Capitao <jcapitao@redhat.com> 3.5.0-1
- Update to upstream version 3.5.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.0-3
- Rebuilt for Python 3.10

* Wed Mar 17 2021 Joel Capitao <jcapitao@redhat.com> 3.3.0-2
- Drop importlib_metadata as requirement

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 3.3.0-1
- Update to upstream version 3.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 3.2.2-3
- Remove importlib_metadata as requirement

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 3.2.2-2
- Update to upstream version 3.2.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 1.32.0-1
- Update to upstream version 1.32.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.31.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.31.0-2
- Update to upstream version 1.31.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.30.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.30.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 1.30.1-1
- Update to 1.30.1

