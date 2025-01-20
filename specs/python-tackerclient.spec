%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif

%global client python-tackerclient
%global sclient tackerclient
%global executable tacker
%global with_doc 1

Name:       %{client}
Version:    2.1.0
Release:    2%{?dist}
Summary:    OpenStack Tacker client
License:    Apache-2.0
URL:        http://launchpad.net/%{client}/

Source0:    http://tarballs.openstack.org/%{client}/%{client}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{client}/%{client}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core

%package -n python3-%{sclient}
Summary:    OpenStack tacker client
Obsoletes: python2-%{sclient} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%description -n python3-%{sclient}
OpenStack tacker client


%package -n python3-%{sclient}-tests-unit
Summary:    OpenStack taker client unit tests
Requires:   python3-%{sclient} = %{version}-%{release}

Requires:  python3-fixtures
Requires:  python3-flake8
Requires:  python3-hacking
Requires:  python3-oslo-log
Requires:  python3-oslo-serialization
Requires:  python3-pbr
Requires:  python3-setuptools
Requires:  python3-subunit
Requires:  python3-testtools
Requires:  python3-mock
Requires:  python3-stestr

%description -n python3-%{sclient}-tests-unit
OpenStack tacker client unit tests

This package contains the tacker client test files.


%if 0%{?with_doc}
%package -n python-%{sclient}-doc
Summary:    OpenStack tacker client documentation

%description -n python-%{sclient}-doc
OpenStack tacker client documentation

This package contains the documentation for tacker client.
%endif

%description
OpenStack tacker client.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{client}-%{upstream_version} -S git -p1

# Fix rpmlint warning for CRLF line termination
sed -i 's/\r$//' ./doc/source/cli/vnf_package_commands.rst ./doc/source/cli/commands.rst

# Use assertCountEqual instead of assertItemsEqual until
# https://review.opendev.org/c/openstack/python-tackerclient/+/791095 is in next tag release
sed -i 's/assertItemsEqual/assertCountEqual/g' tackerclient/tests/unit/osc/v1/test_vnflcm_op_occs.py

# Skip flaky test test_take_action_with_filter
sed -i '/^import sys/a import unittest' tackerclient/tests/unit/osc/v1/test_vnflcm_op_occs.py
sed -i '/test_take_action_with_filter/i \    @unittest.skip(reason="Skip flaky test until its fixed upstream lp#1919350")' tackerclient/tests/unit/osc/v1/test_vnflcm_op_occs.py


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%install
%pyproject_install

%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

sphinx-build -b man doc/source doc/build/man
%endif


%if 0%{?with_doc}
install -p -D -m 644 -v doc/build/man/tacker.1 %{buildroot}%{_mandir}/man1/tacker.1
%endif

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s %{executable} %{buildroot}%{_bindir}/%{executable}-3

%check
%tox -e %{default_toxenv}

%files -n python3-%{sclient}
%license LICENSE
%{python3_sitelib}/%{sclient}
%{python3_sitelib}/*.dist-info
%exclude %{python3_sitelib}/%{sclient}/tests
%{_bindir}/%{executable}-3
%{_bindir}/%{executable}

%if 0%{?with_doc}
%{_mandir}/man1/*
%endif

%files -n python3-%{sclient}-tests-unit
%license LICENSE
%{python3_sitelib}/%{sclient}/tests

%if 0%{?with_doc}
%files -n python-%{sclient}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 07 2024 Joel Capitao <jcapitao@redhat.com> 2.1.0-1
- Update to upstream version 2.1.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Python Maint <python-maint@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.13

* Mon May 06 2024 Alfredo Moralejo <amoralej@redhat.com> 2.0.0-1
- Update to upstream version 2.0.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Alfredo Moralejo <amoralej@gmail.com> 1.14.0-1
- Update to upstream version 1.14.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 14 2023 Karolina Kula <kkula@redhat.com> 1.13.0-1
- Update to upstream version 1.13.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Joel Capitao <jcapitao@redhat.com> 1.10.0-1
- Update to upstream version 1.10.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Javier Peña <jpena@redhat.com> - 1.6.0-4
- Fix build with testtools 2.5.0 (#1987893)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 RDO <dev@lists.rdoproject.org> 1.6.0-1
- Update to 1.6.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-2
- Update to upstream version 1.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 1.1.0-1
- Update to upstream version 1.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.16.1-4
- Rebuilt for Python 3.9

* Fri Mar 13 2020 Alfredo Moralejo <amoralej@redhat.com> - 0.16.1-3
- Replace assertItemsEqual with assertCountEqual

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 0.16.1-1
- Update to upstream version 0.16.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.15.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.15.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 0.15.0-1
- Update to 0.15.0


