%{?systemd_requires}
%global gdeploymod ansible/modules/gdeploy
%global gdeploytemp %{_datadir}/gdeploy

%global commit 05d894b1024a5e2dba65f3ab772aeaed1dc453cd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20200525

Name:           gdeploy
Version:        3.0.0
Release:        14.%{date}git%{shortcommit}%{?dist}
Summary:        Tool to deploy and manage GlusterFS cluster

License:        GPLv3+
URL:            https://github.com/gluster/gdeploy
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch
Requires:       python3-pyyaml
Requires:       ansible > 2.5
Requires:       python3
Requires:       lvm2

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  systemd

%description
gdeploy is an Ansible based deployment tool. Initially gdeploy was written to
install GlusterFS clusters, eventually it grew out to do lot of other things. On
a given set of hosts, gdeploy can create physical volumes, volume groups, and
logical volumes, install packages, subscribe to RHN channels, run shell
commands, create GlusterFS volumes and more.

See http://gdeploy.readthedocs.io/en/latest/ for more details

%prep
%setup -q -n %{name}-%{commit}

%build
%py3_build
pushd docs
make html
popd

%install
# Install the binary and python libraries
%py3_install

mkdir -p %{buildroot}/%{python3_sitelib}/%{gdeploymod}
install -p -m 755 modules/* \
    %{buildroot}/%{python3_sitelib}/%{gdeploymod}

# Install the playbooks into /usr/share/gdeploy/playbooks
mkdir -p %{buildroot}/%{gdeploytemp}
cp -rp playbooks %{buildroot}/%{gdeploytemp}

# Install scripts
cp -rp extras/scripts %{buildroot}/%{gdeploytemp}

# Install usecases
cp -rp extras/usecases %{buildroot}/%{gdeploytemp}

# Install the script to /usr/bin
mkdir -p %{buildroot}/usr/bin
install -p -m 755 extras/usecases/replace-node/gluster-replace-node \
        %{buildroot}/usr/bin

# Install the vdo service file
# https://fedoraproject.org/wiki/Packaging:Scriptlets#Systemd
# /usr/lib/systemd/system/vdo.service
# install -p -m 644 extras/scripts/vdo.service \
#           %{buildroot}/usr/lib/systemd/system/


# Documentation
mkdir -p %{buildroot}/%{_pkgdocdir}
cp -rp docs/build/html examples %{buildroot}/%{_pkgdocdir}

# Man pages
mkdir -p %{buildroot}/%{_mandir}/man1/ \
       %{buildroot}/%{_mandir}/man5/
cp -p man/gdeploy.1* %{buildroot}/%{_mandir}/man1/
cp -p man/gdeploy.conf* %{buildroot}/%{_mandir}/man5/


%post
%systemd_post vdo.service

%preun
%systemd_preun vdo.service

%postun
%systemd_postun_with_restart vdo.service

%files
%{_bindir}/gdeploy
#%{_unitdir}/vdo.service
%{python3_sitelib}/gdeploy*
%{gdeploytemp}
%{python3_sitelib}/%{gdeploymod}
%{_bindir}/gluster-replace-node

%doc README.md TODO
%license LICENSE
%{_mandir}/man1/gdeploy*
%{_mandir}/man5/gdeploy*

%package doc
Summary: gdeploy documentation
BuildRequires:  python3-sphinx
BuildRequires: make

%description doc
gdeploy is an Ansible based deployment tool, used to deploy and configure
GlusteFS.

gdeploy-doc package provides the documentation for writing gdeploy
configuration files to deploy and configure GlusterFS.

%files doc
%doc %{_pkgdocdir}

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-14.20200525git05d894b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.0-13.20200525git05d894b
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12.20200525git05d894b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11.20200525git05d894b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.0-10.20200525git05d894b
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9.20200525git05d894b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8.20200525git05d894b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.0.0-7.20200525git05d894b
- Fix the sources

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-5
- Add %%dist to the Release tag

* Fri Oct 4 2019 Sachidananda Urs <sac@redhat.com> - 3.0.0-4
- Change the package name pyyaml -> python3-pyyaml rhbz#1754129

* Mon Sep 23 2019 Sachidananda Urs <sac@redhat.com> - 3.0.0-2
- Build for Fedora rawhide rhbz#1738969

* Thu Sep 19 2019 Sachidananda Urs <sac@redhat.com> - 3.0.0
- Port gdeploy to Python3 rhbz#1738969

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Sachidananda Urs <sac@redhat.com> - 2.0.12
- Create samba user on all nodes rhbz#1712904

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> - 2.0.10-1
- New sources uploaded 2.0.10-2

* Mon Jan 28 2019 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> - 2.0.10-1
- Handle LANG gracefully 

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> - 2.0.8-2
- Added vdo service file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> - 2.0.7
- ctdb and regex related bugfixes

* Wed Nov 22 2017 Sachidananda Urs <sac@redhat.com> - 2.0.6-1
- Add vdo support to gdeploy

* Tue Nov 14 2017 Sachidananda Urs <sac@redhat.com> - 2.0.5-1
- Add geo-replication support to gdeploy

* Sun Nov 5 2017 Sachidananda Urs <sac@redhat.com> - 2.0.4-1
- Remove the multiple display support, broken in Ansible-2.4

* Fri Nov 3 2017 Sachidananda Urs <sac@redhat.com> - 2.0.3-1
- Fix the versioning, do not use hypens in version numbers

* Mon Sep 25 2017 Matthew Miller <mtatdm@fedoraproject.org> - 2.0.2-15
- add dist tag as per guidelines https://fedoraproject.org/wiki/Packaging:DistTag

* Wed Aug 16 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-14
- Change the license to GPLv3+
- Fix the source tar ball naming

* Wed Aug 9 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-13
- Fix spec to address comment#28 from bug: 1344276

* Tue Jun 27 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-12
- Do not throw `volume start failed' error if volume is already started
- Add service `glusterfssharedstorage' to NFS Ganesha pre-requisites
- Add service `nfs-ganesha' to NFS Ganesha pre-requisites

* Thu Jun 22 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-11
- Updated extras/scripts to enable multipath

* Thu May 18 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-10
- Use shell module instead of script while executing a script

* Tue May 16 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-9
- Print the status of add-node command

* Mon May 15 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-8
- Do not export a volume unless specified in [nfs-ganesha] section

* Thu May 11 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-7
- Move the modues to ansible/modules from ansible/modules/extras

* Fri May 5 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-6
- Fixes a traceback caused for accessing non-existent key

* Fri May 5 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-5
- Fixes bugs: 1447271 1446509 1446092 1444829

* Tue Apr 25 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-4
- Add cachesize variable to [backend-setup] section

* Thu Apr 13 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-3
- Fix a traceback in RHEL6, catch exception and print message

* Thu Mar 30 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-2
- Fixed an issue where playbooks were installed wrongly

* Wed Mar 22 2017 Sachidananda Urs <sac@redhat.com> 2.0.2-1
- Fixes NFS Ganesha delete node issue
- Add support for RAID5

* Tue Jan 10 2017 Sachidananda Urs <sac@redhat.com> 2.0.1-4
- Fix spec to address comment#19 from bug: 1344276

* Mon Nov 7 2016 Sachidananda Urs <sac@redhat.com> 2.0.1-3
- Fix spec file to conform to Fedora standards

* Wed Nov 2 2016 Sachidananda Urs <sac@redhat.com> 2.0.1-2
- Fixes bugs: 1390872, 1390871, 1387174

* Thu Sep 29 2016 Sachidananda Urs <sac@redhat.com> 2.0.1-1
- Removed ansible dependency from RHEL6

* Tue Aug 23 2016 Sachidananda Urs <sac@redhat.com> 2.0.1
- Add support for configuring NFS Ganesha, Samba, and CTDB

* Fri Jul 15 2016 Sachidananda Urs <sac@redhat.com> dev1
- NFS Ganesha related bug fixes.

* Wed Jun 8 2016 Sachidananda Urs <sac@redhat.com> master-2
- First release after master rebase

* Fri Jun 3 2016 Sachidananda Urs <sac@redhat.com> 2.0-16
- Cleaning up the spec file

* Mon Feb 1 2016 Sachidananda Urs <sac@redhat.com> 2.0
- New design, refer: doc/gdeploy-2

* Fri Nov 6 2015 Sachidananda Urs <sac@redhat.com> 1.1
- Patterns in configs are to be tested
- Backend setup config changes(This includes alot)
- Rerunning the config do not throw error
- Backend reset
- Host specific and group specific changes.
- Quota
- Snapshot
- Geo-replication
- Subscription manager
- Package install
- Firewalld
- samba
- CTDB
- CIFS mount

* Mon Aug 3 2015 Sachidananda Urs <sac@redhat.com> 1.0
- Initial release.
