Name:           ansible-packaging
Version:        1
Release:        7%{?dist}
Summary:        RPM packaging macros and generators for Ansible collections

License:        GPL-3.0-or-later

Source0:        ansible-generator
Source1:        ansible.attr
Source2:        macros.ansible
Source3:        macros.ansible-srpm
Source4:        COPYING

# Require ansible-core for building. Collections still have a boolean runtime
# dependency on either ansible 2.9 OR ansible-core.
Requires:       ansible-core

Requires:       ansible-srpm-macros = %{version}-%{release}

# Conflict with anything providing its own copies of these files
%if ! (0%{?rhel} >= 8)
Conflicts:      ansible-core < 2.12.1-3
%endif
Conflicts:      ansible < 2.9.27-3

BuildArch:      noarch

%description
%{summary}.


%package -n ansible-srpm-macros
Summary:        SRPM stage RPM packaging macros for Ansible collections

%description -n ansible-srpm-macros
%{summary}.

%package tests
Summary:        Dependencies for Ansible collection package unit tests
Requires:       %{name} = %{version}-%{release}
Requires:       /usr/bin/ansible-test
# This list is taken from %%{python3_sitelib}/ansible_test/_data/requirements/units.txt
Requires:       %{py3_dist pytest}
Requires:       %{py3_dist pytest-mock}
Requires:       %{py3_dist pytest-xdist}
Requires:       %{py3_dist pytest-forked}
Requires:       %{py3_dist pyyaml}
# mock is included in the list upstream, but is deprecated in Fedora.
# Maintainers should work with upstream to add compat code to support
# both unittest.mock and mock and/or patch it out themselves.
# See https://fedoraproject.org/wiki/Changes/DeprecatePythonMock.
# Requires:     %%{py3_dist mock}

%description tests
This package contains the necessary dependencies to run unit tests for packaged
Ansible collections


%prep
%autosetup -T -c
cp -a %{sources} .


%build
# Nothing to build


%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} ansible.attr
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir} macros.ansible
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir} macros.ansible-srpm
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} ansible-generator


%files
%license COPYING
%{_fileattrsdir}/ansible.attr
%{_rpmmacrodir}/macros.ansible
%{_rpmconfigdir}/ansible-generator


%files -n ansible-srpm-macros
%{_rpmmacrodir}/macros.ansible-srpm

# ansible-core in RHEL 8.6 is built against python38. In c8s and the next RHEL
# 8 minor release, it will be built against python39. The testing dependencies
# are not yet packaged for either python version in EPEL 8.
%if ! (%{defined rhel} && 0%{?rhel} < 9)
%files tests
%endif


%changelog
* Mon Aug 01 2022 Maxwell G <gotmax@e.email> - 1-7
- Implement %%ansible_test_unit and add ansible-packaging-tests metapackage.
- Require ansible-core at buildtime

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 17 2022 Maxwell G <gotmax@e.email> - 1-5
- Split macros required for building SRPMs into a separate package.

* Tue Apr 26 2022 Maxwell G <gotmax@e.email> - 1-4
- Restore compatability with f34 and f35.

* Mon Jan 31 2022 Neal Gompa <ngompa@fedoraproject.org> - 1-3
- Drop vestigial support for the legacy ansible package
- Make compatibile with RHEL 8.6+

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Neal Gompa <ngompa@fedoraproject.org> - 1-1
- Initial packaging split out of ansible-core (#2038591)
