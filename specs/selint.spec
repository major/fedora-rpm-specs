# check in RHEL-7 is too old
%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with tests
%else
%bcond_without tests
%endif


Summary: Static code analysis tool for SELinux policy source files
Name: selint
Version: 1.5.0
Release: 4%{?dist}
URL: https://github.com/SELinuxProject/selint
License: Apache-2.0
Source: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0001: 0001-Add-check-for-fcontext-lines-containing-only-spaces.patch
# Patch0002: 0002-Run-CI-whitespace-check-only-on-changes-introduced-i.patch
Patch0003: 0003-Drop-useless-self-assignment.patch
Patch0004: 0004-Support-CIDR-address-notation-in-nodecon-statement.patch
# Patch0005: 0005-ci-bump-to-LLVM-19.patch
Patch0006: 0006-Support-m4-quoted-strings-in-interface-call-argument.patch
Patch0007: 0007-Call-bison-with-Wno-other.patch
Patch0008: 0008-Markdownify-README.patch
Patch0009: 0009-Add-parse-check-for-new-netlink-xperm-support.patch
Patch0010: 0010-Allow-in-quoted-string-token.patch

BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: bison
%if %{with tests}
BuildRequires: pkgconfig(check) >= 0.11.0
%endif
BuildRequires: flex
BuildRequires: gcc
BuildRequires: help2man
BuildRequires: libconfuse-devel
BuildRequires: make
BuildRequires: uthash-devel


%description
SELint is a program to perform static code analysis on SELinux policy source
files. SELint seeks to help policy developers write policy that is more
maintainable, readable and secure, and to reduce the time spent debugging
challenging policy issues.


%prep
%autosetup -p 1


%build
autoreconf -fiv -Wall -Wno-portability
%configure %{!?with_tests:--without-check}

%make_build


%install
%make_install


%if %{with tests}
%check
%make_build check
%endif


%files
%license LICENSE NOTICE
%doc CHANGELOG README.md
%{_bindir}/selint
%config(noreplace) %{_sysconfdir}/selint.conf
%{_mandir}/man1/selint.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 12 2024 Petr Lautrbach <lautrbach@redhat.com> - 1.5.0-3
- Update to latest upstream sources

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Juraj Marcin <juraj@jurajmarcin.com> - 1.5.0-1
- v 1.5.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Juraj Marcin <juraj@jurajmarcin.com> - 1.4.0-1
- v 1.4.0

* Mon Dec 19 2022 Vit Mojzis <vmojzis@redhat.com> - 1.3.0-1
- v 1.3.0
- Silence warning in bison generated code
- Drop dead stores
- Declare file local variable static
- Drop duplicate semicolons
- Add missing fall through comment
- Drop duplicate include
- Update URLs after repository move
- Add check example for W-012
- Add new check to warn about incorrect usage of audit_access permission
- Warn on duplicate policy configuration files
- Reduce recursion in free_policy_node
- Support disable commands for tunable conditions
- Support ifn?def in .if files

* Fri Sep 02 2022 Vit Mojzis <vmojzis@redhat.com> - 1.2.1-3
- v 1.2.1

* Tue Sep 22 2020 Vit Mojzis <vmojzis@redhat.com> - 1.1.0-1
- First build
