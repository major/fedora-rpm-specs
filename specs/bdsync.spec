Name: bdsync
Summary: Remote sync for block devices
Version: 0.11.2
Release: 14%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Source: https://github.com/rolffokkens/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
URL: http://bdsync.rolf-fokkens.nl/

Patch1: bdsync-0.10-buildflags.patch

BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: pandoc
BuildRequires: make


%description
Bdsync can be used to synchronize block devices over a network. It generates
a "binary patchfile" in an efficient way by comparing MD5 checksums of 32k
blocks of the local block device LOCDEV and the remote block device REMDEV.

This binary patchfile can be sent to the remote machine and applied to its
block device DSTDEV, after which the local blockdev LOCDEV and the remote
block device REMDEV are synchronized.

bdsync was built to do the only thing rsync isn't able to do: synchronize
block devices.


%prep
%setup -q
%patch -P1 -p1


%build
%set_build_flags
%make_build


%check
make test


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
cp %{name} %{buildroot}/%{_bindir}/%{name}
cp %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1


%files 
%if 0%{?fedora}
%license COPYING
%else
%doc COPYING
%endif
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.11.2-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.11.2-5
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Michael Hampton <error@ioerror.us> - 0.11.2-1
- Update to upstream 0.11.2 including LTO patch

* Tue Jul 14 2020 Michael Hampton <error@ioerror.us> - 0.11.1-5
- Corrected upstream Source: URL

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 0.11.1-4
- Fix broken ASM exposed by LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Michael Hampton <error@ioerror.us> 0.11.1-1
- Rebase to 0.11.1

* Mon Jul 15 2019 Michael Hampton <error@ioerror.us> 0.10.2-3
- Initial import into Fedora (BZ#1402656)

* Fri Feb 08 2019 Michael Hampton <error@ioerror.us> 0.10.2-2
- Improvements from Fedora package review (BZ#1402656)
- Patch to use Fedora build flags (BZ#1583329)

* Thu Feb 07 2019 Michael Hampton <error@ioerror.us> 0.10.2-1
- Rebase to 0.10.2

* Thu Dec 08 2016 Michael Hampton <error@ioerror.us> 0.10-2
- General cleanup to meet Fedora/EPEL package guidelines
- Added new description from upstream

* Wed Dec 07 2016 Michael Hampton <error@ioerror.us> 0.10-1
- Update to upstream 0.10

* Thu May 07 2015 Michael Hampton <error@ioerror.us> 0.9-1
- Various cleanups, based on upstream spec file

* Tue Jan 20 2015 Rolf Fokkens <rolf.fokkens@target-holding.nl>
- rebased on github 0.8

* Thu Oct 02 2014 Rolf Fokkens <rolf.fokkens@target-holding.nl>
- rebased on github 0.7

* Thu Jun 28 2012 Rolf Fokkens <rolf@rolffokkens.nl>
- bump release (0.3)

* Sun Jun 24 2012 Rolf Fokkens <rolf@rolffokkens.nl>
- initial package (0.1)
