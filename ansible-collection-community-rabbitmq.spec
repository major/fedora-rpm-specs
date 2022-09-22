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

%global collection_namespace community
%global collection_name rabbitmq

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        1.2.2
Release:        1%{?dist}
Summary:        RabbitMQ collection for Ansible

# plugins/module_utils/_version.py: Python Software Foundation License version 2
License:        GPL-3.0-or-later and PSF-2.0
URL:            %{ansible_collection_url}
Source0:        https://github.com/ansible-collections/community.rabbitmq/archive/%{version}/%{name}-%{version}.tar.gz
# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
Patch0:         build_ignore.patch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
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


%files
%license COPYING PSF-license.txt
%doc README.md CHANGELOG.rst
%{ansible_collection_files}

%changelog
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
