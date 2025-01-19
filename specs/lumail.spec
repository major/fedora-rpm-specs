Name:           lumail
Version:        3.1
Release:        19%{?dist}
Summary:        Modern console-based e-mail client

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://lumail.org/
Source0:        https://lumail.org/download/%{name}-%{version}.tar.gz
# Upstream https://github.com/lumail/lumail/commit/16c437fd6
Patch0:         0001-Makefile-fix-Makefile-installation-re-introduce-DEST.patch
# Upstream https://github.com/lumail/lumail/commit/929c21b96
Patch1:         0002-Makefile-allow-changing-CPPFLAGS.patch

Patch2:         https://github.com/lumail/lumail/commit/fe9337e.patch#/0001-imap_proxy-terminate-the-proxy-child-on-failure-to-e.patch
Patch3:         https://github.com/lumail/lumail/commit/ddd4078.patch#/0002-global_state-include-the-response-from-the-IMAP-prox.patch
Patch4:         https://github.com/lumail/lumail/commit/1edffc9.patch#/0003-imap_proxy-spin-for-10-seconds-for-the-IMAP-proxy-so.patch
Patch5:         https://github.com/lumail/lumail/commit/05079ed.patch#/0004-perl-imap-proxy-avoid-calling-a-noop-on-an-empty-han.patch
Patch6:         https://github.com/lumail/lumail/commit/9650e8b.patch#/0005-perl-imap-proxy-croak-early-on-bad-params.patch
Patch7:         lumail-3.1-lua54.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pcre-devel
BuildRequires:  file-devel

%description
Lumail is a modern console-based email-client, with fully integrated
scripting, implemented in the Lua programming language.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1


%build
make %{?_smp_mflags} CPPFLAGS="%{optflags}" LVER=lua


%install
%make_install


%files
%{_sysconfdir}/lumail
%config(noreplace) %{_sysconfdir}/lumail/lumail.lua
%{_prefix}/lib/lumail
%{_bindir}/lumail2
%{_datadir}/lumail
%doc *.md
%license LICENSE


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Than Ngo <than@redhat.com> - 3.1-8
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Lubomir Rintel <lkundrak@v3.sk> - 3.1-2
- Apply a handful of IMAP Proxy fixes

* Sat Oct 27 2018 Lubomir Rintel <lkundrak@v3.sk> - 3.1-1
- Initial packaging
