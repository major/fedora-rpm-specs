%global srcname carbon

%global desc %{expand: \
Carbon is one of the components of Graphite, and is responsible for
receiving metrics over the network and writing them down to disk using
a storage back-end.}

Name:           python-%{srcname}
Version:        1.1.10
Release:        11%{?dist}

Summary:        Back-end data caching and persistence daemon for Graphite
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/graphite-project/carbon

Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

Source10:       carbon-aggregator.1
Source11:       carbon-cache.1
Source13:       carbon-relay.1
Source14:       validate-storage-schemas.1
Source20:       %{name}.logrotate

Source30:       carbon-aggregator.service
Source31:       carbon-cache.service
Source32:       carbon-relay.service
Source33:       carbon-aggregator@.service
Source34:       carbon-cache@.service
Source35:       carbon-relay@.service

Source43:       %{name}.sysconfig

# Set sane default filesystem paths.
Patch1:         %{name}-0.10.0-Set-sane-defaults.patch
# Fix path to storage-schemas.conf.
Patch2:         %{name}-0.9.13-Fix-path-to-storage-schemas.conf.patch
# Python 3.12 support https://github.com/graphite-project/carbon/issues/946
Patch3:         %{name}-1.1.10-Py3.12-support.patch

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-protobuf
BuildRequires:	python3-whisper
BuildRequires:	pyproject-rpm-macros
BuildRequires:	systemd
%py_provides python3-%{pypi_name}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:	logrotate
Requires(pre):	shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}

# ugly prefix hack..
export GRAPHITE_NO_PREFIX=True
sed -i -e '/data_files=install_files,/d' setup.py
cat << EOF >> setup.cfg
[install]
install-lib=
EOF

# txAMQP is orphaned in 2020
sed -i "s/, 'txAMQP'//" setup.py
sed -i '/txAMQP/d' requirements.txt
# shebangs shebang..
sed -i '1s|^#!/usr/bin/env python|#!/usr/bin/python3|' lib/carbon/amqp_listener.py
sed -i '1s|^#!/usr/bin/env python|#!/usr/bin/python3|' lib/carbon/amqp_publisher.py
# disable tests which use mmh3 hash
sed -i "s|plugin == 'rules'|plugin == 'rules' or plugin.startswith('fast-')|" lib/carbon/tests/test_routers.py
# Disable internal log rotation.
sed -i -e 's/ENABLE_LOGROTATION.*/ENABLE_LOGROTATION = False/g' conf/carbon.conf.example
# Skip Ceres database test, not actively maintained
rm lib/carbon/tests/test_database.py

# Use the standard library instead of a backport
sed -i -e 's/^import mock/from unittest import mock/' \
       -e 's/^from mock import /from unittest.mock import /' \
    lib/carbon/tests/*.py

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname} twisted

rm -rf %{buildroot}%{_localstatedir}/lib/carbon/*
mkdir -p %{buildroot}%{_localstatedir}/lib/carbon/lists
mkdir -p %{buildroot}%{_localstatedir}/lib/carbon/rrd
mkdir -p %{buildroot}%{_localstatedir}/lib/carbon/whisper

# default config
mkdir -p %{buildroot}%{_sysconfdir}/carbon
install -D -p -m0644 conf/carbon.conf.example \
    %{buildroot}%{_sysconfdir}/carbon/carbon.conf
install -D -p -m0644 conf/storage-aggregation.conf.example \
    %{buildroot}%{_sysconfdir}/carbon/storage-aggregation.conf
install -D -p -m0644 conf/storage-schemas.conf.example \
    %{buildroot}%{_sysconfdir}/carbon/storage-schemas.conf

# man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE10} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE11} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE13} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE14} %{buildroot}%{_mandir}/man1

# log files
mkdir -p %{buildroot}%{_localstatedir}/log/carbon
install -D -p -m0644 %{SOURCE20} \
    %{buildroot}%{_sysconfdir}/logrotate.d/python3-%{srcname}

# init scripts
install -D -p -m0644 %{SOURCE30} \
    %{buildroot}%{_unitdir}/carbon-aggregator.service
install -D -p -m0644 %{SOURCE31} \
    %{buildroot}%{_unitdir}/carbon-cache.service
install -D -p -m0644 %{SOURCE32} \
    %{buildroot}%{_unitdir}/carbon-relay.service
install -D -p -m0644 %{SOURCE33} \
    %{buildroot}%{_unitdir}/carbon-aggregator@.service
install -D -p -m0644 %{SOURCE34} \
    %{buildroot}%{_unitdir}/carbon-cache@.service
install -D -p -m0644 %{SOURCE35} \
    %{buildroot}%{_unitdir}/carbon-relay@.service

# remove .py suffix
for i in %{buildroot}%{_bindir}/*.py; do
    mv ${i} ${i%%.py}
done

# fix permissions
chmod 755 %{buildroot}%{python3_sitelib}/carbon/amqp_listener.py
chmod 755 %{buildroot}%{python3_sitelib}/carbon/amqp_publisher.py


%pre -n python3-%{srcname}
getent group carbon >/dev/null || groupadd -r carbon
getent passwd carbon >/dev/null || \
    useradd -r -g carbon -d %{_localstatedir}/lib/carbon \
    -s /sbin/nologin -c "Carbon cache daemon" carbon


%post -n python3-%{srcname}
%systemd_post carbon-aggregator.service
%systemd_post carbon-cache.service
%systemd_post carbon-relay.service


%preun -n python3-%{srcname}
%systemd_preun carbon-aggregator.service
%systemd_preun carbon-cache.service
%systemd_preun carbon-relay.service


%postun -n python3-%{srcname}
%systemd_postun_with_restart carbon-aggregator.service
%systemd_postun_with_restart carbon-cache.service
%systemd_postun_with_restart carbon-relay.service


%check
%pytest -v


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%doc conf/ examples/ distro/redhat/init.d/

%dir %{_sysconfdir}/carbon
%config(noreplace) %{_sysconfdir}/carbon/carbon.conf
%config(noreplace) %{_sysconfdir}/carbon/storage-aggregation.conf
%config(noreplace) %{_sysconfdir}/carbon/storage-schemas.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/python3-%{srcname}

%attr(0755,carbon,carbon) %dir %{_localstatedir}/lib/carbon
%attr(0755,carbon,carbon) %dir %{_localstatedir}/lib/carbon/lists
%attr(0755,carbon,carbon) %dir %{_localstatedir}/lib/carbon/rrd
%attr(0755,carbon,carbon) %dir %{_localstatedir}/lib/carbon/whisper
%attr(0755,carbon,carbon) %dir %{_localstatedir}/log/carbon

%{_bindir}/carbon-aggregator
%{_bindir}/carbon-aggregator-cache
%{_bindir}/carbon-cache
%{_bindir}/carbon-relay
%{_bindir}/validate-storage-schemas

%{_mandir}/man1/carbon-aggregator.1*
%{_mandir}/man1/carbon-cache.1*
%{_mandir}/man1/carbon-relay.1*
%{_mandir}/man1/validate-storage-schemas.1*

%{_unitdir}/carbon-aggregator.service
%{_unitdir}/carbon-cache.service
%{_unitdir}/carbon-relay.service
%{_unitdir}/carbon-aggregator@.service
%{_unitdir}/carbon-cache@.service
%{_unitdir}/carbon-relay@.service


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.10-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.1.10-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 04 2023 Jonathan Steffan <jsteffan@fedoraproject.org> - 1.1.10-5
- Patch for Python 3.12 (RHBZ#2226168)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.1.10-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.1.10-1
- Update to 1.1.10 (RHBZ #2056668 and #2101243)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.1.6-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-9
- Fix tests for mock 4+

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.6-7
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.6-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Piotr Popieluch <piotr1212@gmail.com> - 1.1.6-1
- Update to 1.1.6
- -- adds options to py3_install after \ #1792050

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Piotr Popieluch <piotr1212@gmail.com> - 1.1.5-3
- Remove requires on configparser

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Piotr Popieluch <piotr1212@gmail.com> - 1.1.5-1
- Update to 1.1.5

* Thu Sep 27 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.4-2
- Remove Python 2 Subpackage

* Sat Sep 15 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.4-1
- Update to 1.1.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.3-2
- Switch to Python 3 by default
- Remove sys-v init

* Mon Apr 09 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.3-1
- Update to 1.1.3

* Wed Feb 28 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-1
- Update to 1.1.2
- Build python3-carbon

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.1.1-2
- Add tests
- Add missing Requires

* Tue Dec 26 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 piotr1212@gmail.com - 0.10.0-0.2.rc1
- Fix requires
- Fix logrotate name

* Thu Sep 22 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.10.0-0.1.rc1
- Update to 0.10.0-rc1

* Sun Sep 18 2016 Piotr Popieluch <piotr1212@gmail.com> - - 0.9.15-6
- Set correct interpreter for amqp listener and publiser

* Sun Sep 18 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.9.15-5
- Add example init script to upstream, rhbz#1360469
- Enable logrotate by default, fixes rhbz#1285727
- Add storage-aggregation.conf, fixes rhbz#1285725
- Update to newer package guidelines
- Remove el5 support
- Remove obsoleted macros
- Update URL

* Wed Aug 03 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.9.15-4
- Add systemd unit files with instances

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.9.15-1
- Update to new version

* Sun Nov 08 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.9.14-1
- Update to new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-0.2.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.9.13-0.1.pre1
- update to 0.9.13-pre1

* Mon Nov 24 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.12-7
- patch setup.py to prevent installation of upstream init scripts

* Fri Nov 14 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.12-6
- conditionally define macros for EPEL 6 and below

* Wed Oct 01 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.12-5
- update URL
- improve description
- use commit hash for Source URL
- use loop to rename files
- include README.md and examples/
- amend patch for filesystem default paths
- fix path to storage-schemas.conf
- add man pages from Debian
- disable internal log rotation and include logrotate configuration
  for Fedora >= 21 and EPEL >= 7
- be more explicit in %%files
- include python egg
- migrate to systemd on Fedora >= 21 and EPEL >= 7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.9.12-3
- Update default runtime user to carbon for carbon-aggregator and
  carbon-relay (RHBZ#1013813)

* Tue Sep 24 2013 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.9.12-2
- Add strict python-whisper Requires (RHBZ#1010432)
- Don't cleanup user and user data on package remove (RHBZ#1010430)

* Mon Sep 02 2013 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.9.10-2
- Update spec to build on el5
- Fix python_sitelib definition

* Wed May 30 2012 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.9.10-1
- Initial Package
