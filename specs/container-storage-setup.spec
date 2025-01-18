%global git0 https://github.com/projectatomic/%{name}
%global csslibdir %{_datadir}/%{name}
%global commit0 413b4080c0b9346a242d88137bb3e9e0a6aa25f9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: container-storage-setup
Version: 0.11.0
Release: 18.dev.git%{shortcommit0}%{?dist}
Summary: A simple service to setup container storage devices
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildArch: noarch
BuildRequires: git
BuildRequires: make
Requires: lvm2
Requires: xfsprogs
Requires: parted

%description
This is a simple service to configure Container Runtimes to use an LVM-managed
thin pool.  It also supports auto-growing both the pool as well
as the root logical volume and partition table.

%prep
%autosetup -Sgit -n %{name}-%{commit0}

%build

%install
install -dp %{buildroot}%{_datadir}/%{name}
install -dp %{buildroot}%{_mandir}/man1
install -D -p -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -p -m 644 %{name}.conf %{buildroot}%{csslibdir}/%{name}
install -p -m 755 libcss.sh %{buildroot}/%{csslibdir}
install -p -m 755 css-child-read-write.sh %{buildroot}/%{csslibdir}/css-child-read-write
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
#%{__make} install-core DESTDIR=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{csslibdir}
%{_mandir}/man1/%{name}.1*
%{csslibdir}/%{name}
%{csslibdir}/css-child-read-write
%{csslibdir}/libcss.sh

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-18.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.11.0-17.dev.git413b408
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-16.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-15.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-14.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-13.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-12.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-11.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-10.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-8.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-7.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5.dev.git413b408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.11.0-4.dev.git413b408
- autobuilt 413b408

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3.dev.git5eaf76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.11.0-2.git5eaf76c
- autobuilt 5eaf76c

* Fri Jun 08 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.11.0-1.git42c9d9c
- bump to 0.11.0
- autobuilt 42c9d9c

* Thu Jun 07 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.10.0-1.gitdf0dcd5
- bump to 0.10.0
- autobuilt df0dcd5

* Fri May 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.11.0-1.git42c9d9c.git42c9d9c
- bump to 0.11.0
- autobuilt 42c9d9c

* Wed May 02 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 0.10.0-1.gitdf0dcd5.gitdf0dcd5
- bump to 0.10.0
- autobuilt commit df0dcd5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3.git1d27ecf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Frantisek Kluknavsky <fkluknav@redhat.com> - 0.8.0-2.git1d27ecf
- Requires: parted, https://bugzilla.redhat.com/show_bug.cgi?id=1416928

* Fri Sep 29 2017 Dan Walsh <dwalsh@redhat.com> - 0.8.0-1.git1d27ecf
- Bump to 0.8.0
- Allow for extents based size for ROOT_SIZE

* Fri Sep 8 2017 Dan Walsh <dwalsh@redhat.com> - 0.7.0-1.git4ca59c5
- Mount xfs filesystem with pquota option
- Add a knob POOL_META_SIZE

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2.giteb688d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 6 2017 Dan Walsh <dwalsh@redhat.com> - 0.6.0-1.giteb688d4
- Fix sfdisk failure on older sfdisk

* Wed Jun 07 2017 Frantisek Kluknavsky <fkluknav@redhat.com> - 0.5.0-1.git9b77bcb
- rebase

* Wed Apr 12 2017 Dan Walsh <dwalsh@redhat.com> - 0.3.0-1
- Rewrite to handle new CLI

* Tue Apr 04 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.0-2
- Resolves: #1437604
- built commit aa1a54f

* Fri Mar 03 2017 Dan Walsh <dwalsh@redhat.com> - 0.2.0-1
- Add License
- Add compatibility mode flag to only do docker specific stuff if INPUTFILE
not specified.
- Minor Bug fixes for non docker use cases

* Thu Mar 02 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.0-2
- Resolves: #1427295 - initial package on rawhide
- misc macro changes
- preserve timestamps

* Mon Feb 27 2017 Dan Walsh <dwalsh@redhat.com> - 0.1.0-1
- Initial version of container-storage-setup
- Building to push through the fedora release cycle

* Thu Oct 16 2014 Andy Grimm <agrimm@redhat.com> - 0.0.1-2
- Fix rpm deps and scripts

* Thu Oct 16 2014 Andy Grimm <agrimm@redhat.com> - 0.0.1-1
- Initial build

