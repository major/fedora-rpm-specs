%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-community-mysql
Version:        3.11.0
Release:        2%{?dist}
Summary:        MySQL collection for Ansible

# All files are GPL-3.0-or-later except:
# PSF-2.0:      plugins/module_utils/_version.py
# BSD-2-Clause: plugins/module_utils/user.py
# BSD-2-Clause: plugins/module_utils/mysql.py
# BSD-2-Clause: plugins/module_utils/database.py
License:        GPL-3.0-or-later AND PSF-2.0 AND BSD-2-Clause
URL:            %{ansible_collection_url community mysql}
Source:         https://github.com/ansible-collections/community.mysql/archive/%{version}/%{name}-%{version}.tar.gz
# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
Patch:          build_ignore.patch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n community.mysql-%{version}
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
%license COPYING PSF-license.txt simplified_bsd.txt CONTRIBUTORS
%doc README.md CHANGELOG.rst

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Orion Poplawski <orion@nwra.com> - 3.11.0-1
- Update to 3.11.0

* Mon Sep 23 2024 Maxwell G <maxwell@gtmx.me> - 3.10.3-1
- Update to 3.10.3. Fixes rhbz#2265589.

* Mon Sep 02 2024 Orion Poplawski <orion@nwra.com> - 3.10.0-1
- Update to 3.10.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 02 2023 Maxwell G <maxwell@gtmx.me> - 3.8.0-1
- Update to 3.8.0. Fixes rhbz#2209137.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 28 2023 Orion Poplawski <orion@nwra.com> - 3.7.2-1
- Update to 3.7.2

* Sat May 06 2023 Maxwell G <maxwell@gtmx.me> - 3.7.0-1
- Update to 3.7.0. Fixes rhbz#2168430.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 06 2022 Maxwell G <gotmax@e.email> - 3.5.1-1
- Update to 3.5.1. Fixes rhbz#1956098.

* Sat Aug 27 2022 Maxwell G <gotmax@e.email> - 3.4.0-2
- Update license from "GPLv3+ and Python" to "GPL-3.0-or-later AND PSF-2.0 AND BSD-2-Clause"
- Run unit tests

* Fri Aug 05 2022 Orion Poplawski <orion@nwra.com> - 3.4.0-1
- Update to 3.4.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 02 2022 Orion Poplawski <orion@nwra.com> - 3.3.0-1
- Update to 3.3.0

* Wed May 18 2022 Orion Poplawski <orion@nwra.com> - 3.2.1-1
- Update to 3.2.1
- Update license

* Fri May 13 2022 Orion Poplawski <orion@cora.nwra.com> - 3.2.0-1
- Update to 3.2.0

* Wed May 04 2022 Orion Poplawski <orion@nwra.com> - 3.1.3-1
- Update to 3.1.3

* Sat Feb 26 2022 Orion Poplawski <orion@nwra.com> - 3.1.1-1
- Update to 3.1.1

* Sat Jan 29 2022 Maxwell G <gotmax@e.email> - 3.1.0-2
- Switch to ansible-packaging.

* Thu Jan 20 2022 Orion Poplawski <orion@nwra.com> - 3.1.0-1
- Update to 3.1.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Orion Poplawski <orion@nwra.com> - 3.0.0-1
- Update to 3.0.0

* Wed Dec 01 2021 Orion Poplawski <orion@nwra.com> - 2.3.2-1
- Update to 2.3.2

* Wed Oct 20 2021 Orion Poplawski <orion@nwra.com> - 2.3.1-1
- Update to 2.3.1

* Tue Sep 28 2021 Orion Poplawski <orion@nwra.com> - 2.3.0-1
- Update to 2.3.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 02 2021 Orion Poplawski <orion@nwra.com> - 2.1.0-1
- Update to 2.1.0

* Thu Mar 11 2021 Orion Poplawski <orion@nwra.com> - 1.3.0-1
- Initial package
