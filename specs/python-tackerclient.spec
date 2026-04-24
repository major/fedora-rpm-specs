%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff

%global client python-tackerclient
%global sclient tackerclient
%global executable tacker
%global with_doc 1

Name:       %{client}
Version:    2.5.0
Release:    %autorelease
Summary:    OpenStack Tacker client
License:    Apache-2.0
URL:        http://launchpad.net/%{client}/

Source0:    http://tarballs.openstack.org/%{client}/python_%{sclient}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{client}/python_%{sclient}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

BuildRequires:  python3-devel

%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core

%description
OpenStack tacker client.


%package -n python3-%{sclient}
Summary:    OpenStack tacker client


%description -n python3-%{sclient}
OpenStack tacker client


%package -n python3-%{sclient}-tests-unit
Summary:    OpenStack taker client unit tests
Requires:   python3-%{sclient} = %{version}-%{release}
Requires:   python3-fixtures
Requires:   python3-subunit
Requires:   python3-testtools
Requires:   python3-stestr
Requires:   python3-oslo-log


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


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python_%{sclient}-%{version} -S git -p1

# Fix rpmlint warning for CRLF line termination
sed -i 's/\r$//' ./doc/source/cli/vnf_package_commands.rst ./doc/source/cli/commands.rst

# Skip flaky test test_take_action_with_filter
sed -i '/^import sys/a import unittest' tackerclient/tests/unit/osc/v1/test_vnflcm_op_occs.py
sed -i '/test_take_action_with_filter/i \    @unittest.skip(reason="Skip flaky test until its fixed upstream lp#1919350")' tackerclient/tests/unit/osc/v1/test_vnflcm_op_occs.py


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt

# https://review.opendev.org/c/openstack/python-tackerclient/+/985793
sed -i "s/'reno.sphinxext',//" doc/source/conf.py

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

%pyproject_save_files -l tackerclient

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


%check
%tox -e %{default_toxenv}


%files -n python3-%{sclient} -f %{pyproject_files}
%license LICENSE
%exclude %{python3_sitelib}/%{sclient}/tests
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
%autochangelog
