# Generated from vagrant-sshfs-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant-sshfs

Name: %{vagrant_plugin_name}
Version: 1.3.7
Release: 11%{?dist}
Summary: A Vagrant synced folder plugin that mounts folders via SSHFS
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/dustymabe/vagrant-sshfs
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem

Requires: vagrant >= 1.9.1
Recommends: /usr/bin/fusermount
Recommends: /usr/bin/sshfs
BuildRequires: ruby(release)
BuildRequires: vagrant >= 1.9.1
BuildRequires: rubygems-devel
BuildRequires: rubygem(rdoc)
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
A Vagrant synced folder plugin that mounts folders via SSHFS. 
This is the successor to Fabio Kreusch's implementation:
https://github.com/fabiokr/vagrant-sshfs.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -b 0 -q -n %{vagrant_plugin_name}-%{version}

# remove dependencies on windows libraries (needed for windows, not linux)
%gemspec_remove_dep -s ../%{vagrant_plugin_name}-%{version}.gemspec -g win32-process

%build
gem build ../%{vagrant_plugin_name}-%{version}.gemspec
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

%files
%dir %{vagrant_plugin_instdir}
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}
# Ingore some files that probbaly shouldn't be in the gem
%exclude %{vagrant_plugin_instdir}/.gitignore
%exclude %{vagrant_plugin_instdir}/test
%exclude %{vagrant_plugin_instdir}/features
%exclude %{vagrant_plugin_instdir}/build.sh

%files doc
%license %{vagrant_plugin_instdir}/LICENSE
%doc %{vagrant_plugin_docdir}
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.adoc
%doc %{vagrant_plugin_instdir}/RELEASE.txt
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/vagrant-sshfs.gemspec

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.7-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Dusty Mabe <dusty@dustymabe.com> - 1.3.7-4
- version: bump to 1.3.7 (Dusty Mabe)
- Gemfile: bump to latest versions of vagrant and vagrant-libvirt (Dusty Mabe)
- sshfs_reverse_mount: use ruby Etc lib for owner/group (Dusty Mabe)
- sshfs_reverse_mount: create guest directory if not exists (Dusty Mabe)
- sshfs_reverse_mount: fixup botched copy/paste (Dusty Mabe)
- guest: upload fuse module loading for FreeBSD (Dusty Mabe)
- Update to Fedora 36 for build container and test VM (Dusty Mabe)
- tests: switch config.ssh.insert_key to boolean in Vagrantfile (Dusty Mabe)
- add support for owner, group, and mount_options (Dusty Mabe)
- guest: handle Alma/Rocky until fixes land upstream (Dusty Mabe)
- guest: add Alma Linux support (Dusty Mabe)
- guest: Enterprise Linux 9 has landed (Dusty Mabe)
- Remove superfluous case/when (only rocky_8 exists) (Even Onsager)
- Add Rocky guest_capability to plugin.rb (Even Onsager)
- Add guest capabilities file for Rocky (based on CentOS) (Even Onsager)

* Mon Jun 13 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.3.6-4
- Add recommends for fusermount and sshfs for reverse mounting

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 03 2021 Dusty Mabe <dusty@dustymabe.com> - 1.3.6-1
- new upstream release: 1.3.6

* Mon May 03 2021 Dusty Mabe <dusty@dustymabe.com> - 1.3.5-4
- specfile updates from Pavel Valena

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Dusty Mabe <dusty@dustymabe.com> - 1.3.5-1
- new upstream release: 1.3.5

* Mon Mar 16 2020 Dusty Mabe <dusty@dustymabe.com> - 1.3.4-1
- new upstream release: 1.3.4

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Dusty Mabe <dusty@dustymabe.com> - 1.3.3-1
- new upstream release: 1.3.3

* Wed Dec 11 2019 Dusty Mabe <dusty@dustymabe.com> - 1.3.2-1
- new upstream release: 1.3.2

* Tue Dec 10 2019 Dusty Mabe <dusty@dustymabe.com> - 1.3.1-5
- Change to build from tar archive. Preparing for packit.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Dusty Mabe <dusty@dustymabe.com> - 1.3.1-1
- New version of sshfs: 1.3.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Vít Ondruch <vondruch@redhat.com> - 1.3.0-3
- Drop registration macros for Vagrant 1.9.1 compatibility.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Dusty Mabe <dusty@dustymabe.com> - 1.3.0-1
- New version of sshfs: 1.3.0

* Fri Nov 11 2016 Dusty Mabe <dusty@dustymabe.com> - 1.2.1-2
- Use release '2' because I messed up the last changelog entry.

* Fri Nov 11 2016 Dusty Mabe <dusty@dustymabe.com> - 1.2.1-1
- New version of sshfs out: 1.2.1

* Tue Aug 30 2016 Dusty Mabe <dusty@dustymabe.com> - 1.2.0-2
- Bump release to 2 because vagrant-sshfs-1.2.0-1.fc2{2,3,4} is what
  is available from copr. Bumping to 2 will make sure we don't
  have any confusion.

* Tue Aug 30 2016 Dusty Mabe <dusty@dustymabe.com> - 1.2.0-1
- Remove unnecessary provides of bundled fonts
- Update to 1.2.0 release
- Add patch to remove requirement of win32-process rubygem

* Wed Mar 30 2016 Dusty Mabe <dusty@dustymabe.com> - 1.1.0-1
- Initial package for Fedora
