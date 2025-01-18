# ansible-core in RHEL 8.6 is built against python38. In c8s and the next RHEL
# 8 minor release, it will be built against python39. The testing dependencies
# are not yet packaged for either python version in EPEL 8.
#
# ansible-test in RHEL 9.0 still needs python3-mock, but this
# requirement has been removed in c9s.
# The conditional should be replaced with the line below once RHEL 9.1 is
# released.
# %%if (%%{defined fedora} || 0%%{?rhel} >= 9)
#
%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-community-rabbitmq
Version:        1.3.0
Release:        3%{?dist}
Summary:        RabbitMQ collection for Ansible

# plugins/module_utils/_version.py: Python Software Foundation License version 2
License:        GPL-3.0-or-later and PSF-2.0
URL:            %{ansible_collection_url community rabbitmq}
%global forgeurl https://github.com/ansible-collections/community.rabbitmq
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
Patch0:         build_ignore.patch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
# Collection specific test dependency
BuildRequires:  glibc-all-langpacks
%endif

BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup -n community.rabbitmq-%{version} -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +


%build
%ansible_collection_build


%install
%ansible_collection_install


%if %{with tests}
%check
%ansible_test_unit
%endif


%files -f %{ansible_collection_filelist}
%license COPYING PSF-license.txt
%doc README.md CHANGELOG.rst

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 30 2024 Kevin Fenzi <kevin@scrye.com> - 1.3.0-1
- Update to 1.3.0. Fixes rhbz#2272471

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Maxwell G <gotmax@e.email> - 1.2.3-1
- Update to 1.2.3. Fixes rhbz#2139970.

* Thu Aug 18 2022 Maxwell G <gotmax@e.email> - 1.2.2-1
- Update to 1.2.2. Fixes rhbz#2106951.
- Adopt new Fedora licensing guidelines
- Run unit tests

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Maxwell G <gotmax@e.email> - 1.2.1-1
- Update to 1.2.1. Fixes rhbz#2086332.

* Mon May 16 2022 Maxwell G <gotmax@e.email> - 1.1.0-2
- Rebuild for new ansible-packaging.

* Thu Oct 14 2021 Pete Buffon <petebuffon@gmail.com> - 1.1.0
- Initial package
