# ansible-core is built for alternative Python stacks in RHEL which do not have
# the necessary test deps packaged.
%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif


Name:           ansible-collection-community-docker
Version:        4.1.0
Release:        2%{?dist}
Summary:        Ansible modules and plugins for working with Docker

# All files are GPL-3.0-or-later, except the following files, which are originally
# from the Docker Python SDK.
# rg --pcre2 -g '!tests/sanity/extra/licenses.py' 'SPDX-License-Identifier: (?!GPL-3\.0-or-later)' | sort | sed 's|^|# |'
#
# plugins/module_utils/_api/api/client.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/api/daemon.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/auth.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/constants.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/credentials/constants.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/credentials/errors.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/credentials/store.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/credentials/utils.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/errors.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/_import_helper.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/tls.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/basehttpadapter.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/npipeconn.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/npipesocket.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/sshconn.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/ssladapter.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/transport/unixconn.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/types/daemon.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/build.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/config.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/decorators.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/fnmatch.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/json_stream.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/ports.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/proxy.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/socket.py:# SPDX-License-Identifier: Apache-2.0
# plugins/module_utils/_api/utils/utils.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/api/test_client.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/fake_api.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/fake_stat.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/test_auth.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/test_errors.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/transport/test_sshconn.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/transport/test_ssladapter.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_build.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_config.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/testdata/certs/ca.pem:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/testdata/certs/cert.pem:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/testdata/certs/key.pem:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_decorators.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_json_stream.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_ports.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_proxy.py:# SPDX-License-Identifier: Apache-2.0
# tests/unit/plugins/module_utils/_api/utils/test_utils.py:# SPDX-License-Identifier: Apache-2.0
License:        GPL-3.0-or-later AND Apache-2.0
URL:            %{ansible_collection_url community docker}
%global forgeurl https://github.com/ansible-collections/community.docker
Source0:        %{forgeurl}/archive/%{version}/community.docker-%{version}.tar.gz
Patch0:         build_ignore-unnecessary-files.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  ansible-collection(community.library_inventory_filtering_v1)
BuildRequires:  %{py3_dist requests}
%endif

# This collection contains vendored code from the Docker Python SDK.
Provides:       bundled(python3dist(docker))


%description
ansible-collection-community-docker provides the community.docker Ansible
collection. The collection includes Ansible modules and plugins for working
with Docker.


%prep
%autosetup -p1 -n community.docker-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +


%build
%ansible_collection_build


%install
%ansible_collection_install


%check
%if %{with tests}
%ansible_test_unit -c community.library_inventory_filtering_v1
%endif


%files -f %{ansible_collection_filelist}
%license COPYING LICENSES .reuse/dep5
%doc README.md CHANGELOG.rst*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Maxwell G <maxwell@gtmx.me> - 4.1.0-1
- Update to 4.1.0. Fixes rhbz#2319299.

* Fri Oct 11 2024 Maxwell G <maxwell@gtmx.me> - 3.13.0-1
- Update to 3.13.0. Fixes rhbz#2316730.

* Thu Sep 26 2024 Maxwell G <maxwell@gtmx.me> - 3.12.2-1
- Update to 3.12.2. Fixes rhbz#2242856.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Maxwell G <maxwell@gtmx.me> - 3.5.0-1
- Update to 3.5.0.

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Maxwell G <maxwell@gtmx.me> - 3.4.6-3
- Fix FTBFS. Closes rhbz#2215512.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 20 2023 Maxwell G <maxwell@gtmx.me> - 3.4.6-1
- Update to 3.4.6.

* Sat May 06 2023 Maxwell G <maxwell@gtmx.me> - 3.4.5-1
- Update to 3.4.5. Fixes rhbz#2181482.

* Fri Mar 31 2023 Maxwell G <maxwell@gtmx.me> - 3.4.3-1
- Update to 3.4.3. Fixes rhbz#2181482.

* Wed Mar 01 2023 Maxwell G <maxwell@gtmx.me> - 3.4.2-1
- Update to 3.4.2. Fixes rhbz#2172008.

* Tue Jan 24 2023 Maxwell G <gotmax@e.email> - 3.4.0-1
- Update to 3.4.0. Fixes rhbz#2161016.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Maxwell G <gotmax@e.email> - 3.3.2-1
- Update to 3.3.2. Fixes rhbz#2150678.

* Fri Dec 09 2022 Maxwell G <gotmax@e.email> - 3.3.1-1
- Update to 3.3.1. Fixes rhbz#2150678.

* Sat Dec 03 2022 Maxwell G <gotmax@e.email> - 3.3.0-1
- Update to 3.3.0.

* Tue Nov 29 2022 Maxwell G <gotmax@e.email> - 3.2.2-1
- Update to 3.2.2.

* Thu Nov 03 2022 Maxwell G <gotmax@e.email> - 3.2.0-2
- Remove unexpanded macros from %%description
- Handle .reuse/dep5

* Wed Nov 02 2022 Maxwell G <gotmax@e.email> - 3.2.0-1
- Update to 3.2.0. Fixes rhbz#2139344.

* Thu Sep 08 2022 Maxwell G <gotmax@e.email> - 3.1.0-1
- Update to 3.1.0. Fixes rhbz#2125151.

* Tue Aug 16 2022 Maxwell G <gotmax@e.email> - 3.0.2-1
- Update to 3.0.2.

* Tue Aug 16 2022 Maxwell G <gotmax@e.email> - 3.0.1-1
- Update to 3.0.1.

* Fri Aug 12 2022 Maxwell G <gotmax@e.email> - 3.0.0-1
- Update to 3.0.0 (rhbz#2105298).
- Follow Fedora's new licensing guidelines

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 02 2022 Maxwell G <gotmax@e.email> - 2.7.0-1
- Update to 2.7.0. Fixes rhbz#2103337.
- Fix shebangs

* Wed May 25 2022 Maxwell G <gotmax@e.email> - 2.6.0-1
- Update to 2.6.0. Fixes rhbz#2089991.

* Mon May 16 2022 Maxwell G <gotmax@e.email> - 2.5.1-1
- Update to 2.5.1. Fixes rhbz#2086832.
- Change license from `GPLv3+` > `GPLv3+ and Python`

* Sat May 14 2022 Maxwell G <gotmax@e.email> - 2.5.0-1
- Update to 2.5.0. Fixes rhbz#2086185.
- Run unit tests.
- Rebuild for new ansible-packaging.

* Mon Apr 25 2022 Maxwell G <gotmax@e.email> - 2.4.0-1
- Update to 2.4.0.

* Wed Apr 06 2022 Maxwell G <gotmax@e.email> - 2.3.0-1
- Preform initial import (rhbz#2028702).

* Fri Apr 01 2022 Maxwell G <gotmax@e.email> - 2.3.0-0
- Update to 2.3.0.

* Mon Feb 21 2022 Maxwell G <gotmax@e.email> - 2.2.0-1
- Update to 2.2.0. Fix shebangs. Switch to ansible-packaging.

* Thu Dec 16 2021 Maxwell G <gotmax@e.email> - 2.0.2-1
- Update to 2.0.2.

* Thu Dec 02 2021 Maxwell G <gotmax@e.email> - 2.0.1-1
- Initial package
