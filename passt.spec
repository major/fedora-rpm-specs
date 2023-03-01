# PASST - Plug A Simple Socket Transport
#  for qemu/UNIX domain socket mode
#
# PASTA - Pack A Subtle Tap Abstraction
#  for network namespace/tap device mode
#
# Copyright (c) 2022 Red Hat GmbH
# Author: Stefano Brivio <sbrivio@redhat.com>

%global git_hash c538ee8d695de053dc9da8965c85997a79fb6cb2

Name:		passt
Version:	0^20230227.gc538ee8
Release:	1%{?dist}
Summary:	User-mode networking daemons for virtual machines and namespaces
License:	AGPLv3+ and BSD
Group:		System Environment/Daemons
URL:		https://passt.top/
Source:		https://passt.top/passt/snapshot/passt-%{git_hash}.tar.xz

BuildRequires:	gcc, make, checkpolicy, selinux-policy-devel

%description
passt implements a translation layer between a Layer-2 network interface and
native Layer-4 sockets (TCP, UDP, ICMP/ICMPv6 echo) on a host. It doesn't
require any capabilities or privileges, and it can be used as a simple
replacement for Slirp.

pasta (same binary as passt, different command) offers equivalent functionality,
for network namespaces: traffic is forwarded using a tap interface inside the
namespace, without the need to create further interfaces on the host, hence not
requiring any capabilities or privileges.

%package    selinux
BuildArch:  noarch
Summary:    SELinux support for passt and pasta
Requires:   %{name} = %{version}-%{release}
Requires:   selinux-policy
Requires(post): %{name}
Requires(post): policycoreutils
Requires(preun): %{name}
Requires(preun): policycoreutils

%description selinux
This package adds SELinux enforcement to passt(1) and pasta(1).

%prep
%setup -q -n passt-%{git_hash}

%build
%set_build_flags
%make_build VERSION="%{version}-%{release}.%{_arch}"

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix} bindir=%{_bindir} mandir=%{_mandir} docdir=%{_docdir}/%{name}
%ifarch x86_64
ln -sr %{buildroot}%{_mandir}/man1/passt.1 %{buildroot}%{_mandir}/man1/passt.avx2.1
ln -sr %{buildroot}%{_mandir}/man1/pasta.1 %{buildroot}%{_mandir}/man1/pasta.avx2.1
%endif

pushd contrib/selinux
make -f %{_datadir}/selinux/devel/Makefile
install -p -m 644 -D passt.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/passt.pp
install -p -m 644 -D pasta.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/pasta.pp
popd

%post selinux
semodule -i %{_datadir}/selinux/packages/%{name}/passt.pp 2>/dev/null || :
semodule -i %{_datadir}/selinux/packages/%{name}/pasta.pp 2>/dev/null || :

%preun selinux
semodule -r passt 2>/dev/null || :
semodule -r pasta 2>/dev/null || :

%files
%license LICENSES/{AGPL-3.0-or-later.txt,BSD-3-Clause.txt}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/demo.sh
%{_bindir}/passt
%{_bindir}/pasta
%{_bindir}/qrap
%{_mandir}/man1/passt.1*
%{_mandir}/man1/pasta.1*
%{_mandir}/man1/qrap.1*
%ifarch x86_64
%{_bindir}/passt.avx2
%{_mandir}/man1/passt.avx2.1*
%{_bindir}/pasta.avx2
%{_mandir}/man1/pasta.avx2.1*
%endif

%files selinux
%dir %{_datadir}/selinux/packages/%{name}
%{_datadir}/selinux/packages/%{name}/passt.pp
%{_datadir}/selinux/packages/%{name}/pasta.pp

%changelog
* Mon Feb 27 2023 Stefano Brivio <sbrivio@redhat.com> - 0^20230227.gc538ee8-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2023_02_22.4ddbcb9..2023_02_27.c538ee8

* Wed Feb 22 2023 Stefano Brivio <sbrivio@redhat.com> - 0^20230222.g4ddbcb9-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2023_02_16.4663ccc..2023_02_22.4ddbcb9

* Thu Feb 16 2023 Stefano Brivio <sbrivio@redhat.com> - 0^20230216.g4663ccc-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_11_16.ace074c..2023_02_16.4663ccc

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0^20221116.gace074c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20221116.gace074c-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_11_10.4129764..2022_11_16.ace074c

* Thu Nov 10 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20221110.g4129764-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_11_04.e308018..2022_11_10.4129764

* Fri Nov  4 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20221104.ge308018-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_10_26.f212044..2022_11_04.e308018

* Wed Oct 26 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20221026.gf212044-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_10_26.e4df8b0..2022_10_26.f212044

* Wed Oct 26 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20221026.ge4df8b0-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_10_24.c11277b..2022_10_26.e4df8b0

* Mon Oct 24 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20221024.gc11277b-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_10_22.b68da10..2022_10_24.c11277b

* Sat Oct 22 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20221022.gb68da10-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_10_15.b3f3591..2022_10_22.b68da10

* Sat Oct 15 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20221015.gb3f3591-1
- Add versioning information
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_09_29.06aa26f..2022_10_15.b3f3591

* Thu Sep 29 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220929.g06aa26f-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_09_24.8978f65..2022_09_29.06aa26f

* Sat Sep 24 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220924.g8978f65-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_09_23.d6f865a..2022_09_24.8978f65

* Fri Sep 23 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220923.gd6f865a-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_09_06.e2cae8f..2022_09_23.d6f865a

* Wed Sep  7 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220907.ge2cae8f-1
- Escape %% characters in spec file's changelog
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_09_01.7ce9fd1..2022_09_06.e2cae8f

* Fri Sep  2 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220902.g7ce9fd1-1
- Add selinux-policy Requires: tag
- Add %%dir entries for own SELinux policy directory and documentation
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_08_29.0cb795e..2022_09_01.7ce9fd1

* Tue Aug 30 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220830.g0cb795e-1
- Pass explicit bindir, mandir, docdir, and drop OpenSUSE override
- Use full versioning for SELinux subpackage Requires: tag
- Define git_hash in spec file and reuse it
- Drop comment stating the spec file is an example file
- Drop SPDX identifier from spec file
- Adopt versioning guideline for snapshots
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_08_24.60ffc5b..2022_08_29.0cb795e

* Wed Aug 24 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220824.g60ffc5b-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_08_21.7b71094..2022_08_24.60ffc5b

* Sun Aug 21 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220821.g7b71094-1
- Use more GNU-style directory variables, explicit docdir for OpenSUSE
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_08_20.f233d6c..2022_08_21.7b71094

* Sat Aug 20 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220820.gf233d6c-1
- Fix man pages wildcards in spec file
- Don't hardcode CFLAGS setting, use %%set_build_flags macro instead
- Build SELinux subpackage as noarch
- Change source URL to HEAD link with explicit commit SHA
- Drop VCS tag from spec file
- Start Release tag from 1, not 0
- Introduce own rpkg macro for changelog
- Install "plain" README, instead of web version, and demo script
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_08_04.b516d15..2022_08_20.f233d6c

* Mon Aug  1 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220801.gb516d15-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_07_20.9af2e5d..2022_08_04.b516d15

* Wed Jul 20 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220720.g9af2e5d-1
- Upstream changes: https://passt.top/passt/log/?qt=range&q=2022_07_14.b86cd00..2022_07_20.9af2e5d

* Thu Jul 14 2022 Stefano Brivio <sbrivio@redhat.com> - 0^20220714.gb86cd00-1
- Use pre-processing macros in spec file
- Drop dashes from version
- Add example spec file for Fedora
- Upstream changes: https://passt.top/passt/log/?qt=range&q=e653f9b3ed1b60037e3bc661d53b3f9407243fc2..2022_07_14.b86cd00
