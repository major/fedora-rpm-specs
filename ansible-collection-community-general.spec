Name:           ansible-collection-community-general
Version:        6.0.0~a1
Release:        1%{?dist}
Summary:        Modules and plugins supported by Ansible community

# rg --pcre2 -g '!tests/sanity/extra/licenses.py' 'SPDX-License-Identifier: (?!GPL-3\.0-or-later)' | sed 's|^|# |'
#
# plugins/doc_fragments/lxca_common.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/_mount.py:# SPDX-License-Identifier: PSF-2.0
# plugins/module_utils/alicloud_ecs.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/database.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/gandi_livedns_api.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/heroku.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/hwc_utils.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/ibm_sa_utils.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/identity/keycloak/keycloak.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/influxdb.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/ipa.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/known_hosts.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/linode.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/lxd.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/manageiq.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/memset.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/base.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/deco.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/exceptions.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/cmd.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/deprecate_attrs.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/deps.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/state.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/mixins/vars.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/mh/module_helper.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/module_helper.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/oneandone.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/onepassword.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/oneview.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/online.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/opennebula.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/pure.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/rax.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/redhat.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/remote_management/lxca/common.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/saslprep.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/source_control/bitbucket.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/storage/emc/emc_vnx.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/storage/hpe3par/hpe3par.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/univention_umc.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/utm_utils.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/vexata.py:# SPDX-License-Identifier: BSD-2-Clause
# tests/unit/plugins/module_utils/test_utm_utils.py:# SPDX-License-Identifier: BSD-2-Clause
# tests/unit/plugins/modules/packaging/language/test_gem.py:# SPDX-License-Identifier: MIT
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT AND PSF-2.0
URL:            %{ansible_collection_url community general}
%global furl    https://github.com/ansible-collections/community.general
Source:         %{furl}/archive/%{version_no_tilde}/%{name}-%{version}.tar.gz
# Remove unnecessary/development files from the built collection.
# Docs and licenses that are already installed to the standard locations are
# also removed.
# This is a downstream only patch.
Patch:          build_ignore.patch

BuildRequires:  ansible-packaging
# Version 5 specifically requires ansible-core 2.11 or above
Requires:       ansible-core > 2.11

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n community.general-%{version_no_tilde} -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%license COPYING LICENSES .reuse/dep5
%doc README.md CHANGELOG.rst*

%changelog
* Wed Nov 02 2022 Maxwell G <gotmax@e.email> - 6.0.0~a1-1
- Update to 6.0.0~a1.

* Wed Oct 26 2022 Maxwell G <gotmax@e.email> - 5.8.0-1
- Update to 5.8.0.

* Wed Oct 05 2022 Maxwell G <gotmax@e.email> - 5.7.0-1
- Update to 5.7.0. Fixes rhbz#2132125.

* Tue Sep 13 2022 Maxwell G <gotmax@e.email> - 5.6.0-1
- Update to 5.6.0.

* Thu Aug 25 2022 Maxwell G <gotmax@e.email> - 5.5.0-1
- Update to 5.5.0. Fixes rhbz#2120735.

* Tue Aug 02 2022 Maxwell G <gotmax@e.email> - 5.4.0-1
- Update to 5.4.0. Fixes rhbz#2113929.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Maxwell G <gotmax@e.email> - 5.3.0-1
- Update to 5.3.0. Fixes rhbz#2106952.

* Fri Jun 24 2022 Maxwell G <gotmax@e.email> - 5.2.0-1
- Update to 5.2.0. Fixes rhbz#2099904.

* Wed Jun 15 2022 Maxwell G <gotmax@e.email> - 5.1.1-1
- Update to 5.1.1. Fixes rhbz#2097228.

* Wed Jun 08 2022 Maxwell G <gotmax@e.email> - 5.1.0-1
- Update to 5.1.0. Fixes rhbz#2094871.

* Mon Jun 06 2022 Maxwell G <gotmax@e.email> - 5.0.2-1
- Update to 5.0.2. Fixes rhbz#2093939.
- Add missing license file from upstream. The overall package license remains the same.

* Mon May 30 2022 Maxwell G <gotmax@e.email> - 5.0.1-1
- Update to 5.0.1.

* Thu May 19 2022 Maxwell G <gotmax@e.email> - 5.0.0-1
- Update to 5.0.0. Fixes rhbz#2080541.

* Mon May 16 2022 Maxwell G <gotmax@e.email> - 4.8.1-1
- Update to 4.8.1.
- Add missing license file now that upstream added it.

* Wed Apr 27 2022 Maxwell G <gotmax@e.email> - 4.8.0-1
- Update to 4.8.0.

* Tue Apr 05 2022 Maxwell G <gotmax@e.email> - 4.7.0-1
- Update to 4.7.0. Fixes rhbz#2072281.

* Tue Mar 22 2022 Maxwell G <gotmax@e.email> - 4.6.1-1
- Update to 4.6.1. Fixes rhbz#2064712.

* Tue Feb 22 2022 Maxwell G <gotmax@e.email> - 4.5.0-1
- Update to 4.5.0.

* Wed Feb 02 2022 Maxwell G <gotmax@e.email> - 4.4.0-1
- Update to 4.4.0. Fixes rhbz#2049667.

* Mon Jan 24 2022 Maxwell G <gotmax@e.email> - 4.3.0-3
- Migrate to new ansible-packaging package.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Maxwell G <gotmax@e.email> - 4.3.0-1
- Update to 4.3.0.

* Tue Dec 21 2021 Maxwell G <gotmax@e.email> - 4.2.0-1
- Update to 4.2.0. Fixes rhbz#2034691.

* Tue Nov 23 2021 Maxwell G <gotmax@e.email> - 4.1.0-1
- Update to 4.1.0. Fixes rhbz#2025969.
- Fix licensing

* Tue Nov 16 2021 Maxwell G <gotmax@e.email> - 4.0.2-1
- Update to 4.0.2. Fixes rhbz#2023894

* Tue Nov 9 2021 Maxwell G <gotmax@e.email> - 4.0.1-1
- Update 4.0.1. Fixes rhbz#2021679.

* Wed Nov 03 2021 Sagi Shnaidman (@sshnaidm) <sshnaidm@redhat.com> - 4.0.0-1
- Update to 4.0.0

* Tue Oct 12 2021 Maxwell G (@gotmax23) <gotmax@e.email - 3.8.0-1
- Update to 3.8.0. Fixes rhbz#2013282

* Sat Sep 25 2021 Kevin Fenzi <kevin@scrye.com> - 3.7.0-1
- Update to 3.7.0. Fixes rhbz#1999899

* Thu Sep 23 2021 Alfredo Moralejo <amoralej@redhat.com> - 3.5.0-2
- Use ansible or ansible-core as BuildRequires

* Wed Aug 11 2021 Kevin Fenzi <kevin@scrye.com> - 3.5.0-1
- Update to 3.5.0. Fixes rhbz#1992481

* Wed Aug 4 2021 Maxwell G <gotmax@e.email> - 3.4.0-1
- Update to 3.4.0. Fixes rhbz#1983969 .

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Kevin Fenzi <kevin@scrye.com> - 3.3.2-1
- Update to 3.3.2. Fixes rhbz#1977438

* Tue Jun 08 2021 Kevin Fenzi <kevin@scrye.com> - 3.2.0-1
- Update to 3.2.0. Fixes rhbz#1969570

* Sat May 29 2021 Kevin Fenzi <kevin@scrye.com> - 3.1.0-2
- Fix sed issue that caused python33 to be required.

* Sat May 29 2021 Kevin Fenzi <kevin@scrye.com> - 3.1.0-1
- Update to 3.1.0. Fixes rhbz#1957092

* Tue May 11 2021 Kevin Fenzi <kevin@scrye.com> - 3.0.2-1
- Update to 3.0.2. Fixes rhbz#1957092

* Wed May 05 2021 Kevin Fenzi <kevin@scrye.com> - 3.0.1-1
- Update to 3.0.1. Fixes rhbz#1957092

* Tue Apr 27 2021 Kevin Fenzi <kevin@scrye.com> - 3.0.0-1
- Update to 3.0.0. Fixes rhbz#1953895

* Sat Apr 24 2021 Kevin Fenzi <kevin@scrye.com> - 2.5.1-1
- Update to 2.5.1.

* Thu Feb 04 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.3.1-2
- Rebuild against new ansible-generator and allow usage by ansible-base-2.10.x

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
