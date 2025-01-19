Name:           oddjob-gpupdate
Version:        0.2.1
Release:        9%{?dist}
Summary:        An oddjob helper which applies group policy objects
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/altlinux/oddjob-gpupdate.git
Source0:        https://github.com/altlinux/%{name}/archive/refs/tags/v%{version}/%{name}.%{version}.tar.gz

# https://github.com/openSUSE/oddjob-gpupdate/commit/0b3734e6da74aeb0f97c2d0fc71fb3a94d4079ba.patch
Patch0:         0001-Use-samba-gpupdate-to-apply-policy.patch
# https://github.com/openSUSE/oddjob-gpupdate/commit/85c13a8c3bb1dac4bd505bbf2a60fc72ea2d18b2.patch
Patch1:         0002-Hardening-to-protect-against-malicous-usernames.patch
# https://github.com/openSUSE/oddjob-gpupdate/commit/ccffce92cdd64b2607edf0e12d5352ebb5be69fa.patch
Patch2:         0003-execl-requires-the-exe-as-the-first-arg.patch
# https://github.com/altlinux/oddjob-gpupdate/pull/4.patch
Patch3:         0004-Let-autoupdate-to-fix-obsolete-AC_PROG_LIBTOOL.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  dbus-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  oddjob
BuildRequires:  pam-devel
BuildRequires:  xmlto

Requires: oddjob
Requires(post): /usr/bin/dbus-send
Requires(post): psmisc

%description
This package contains the oddjob helper which can be used by the
pam_oddjob_gpupdate module to apply group policy objects at login-time.

%prep
%autosetup -p1


%build
autoreconf -if
%configure \
    --disable-static \
    --enable-pie \
    --enable-now \
    --with-selinux-acls \
    --with-selinux-labels
%make_build


%install
%make_install

rm -f %{buildroot}%{_pam_moduledir}/pam_oddjob_gpupdate.la

%post
if test $1 -eq 1 ; then
    killall -HUP dbus-daemon 2>&1 > /dev/null
fi
if [ -f /var/lock/subsys/oddjobd ] ; then
    /usr/bin/dbus-send --system --dest=com.redhat.oddjob /com/redhat/oddjob com.redhat.oddjob.reload
fi

%files
%license COPYING
%doc src/gpupdatefor src/gpupdateforme
%{_libexecdir}/oddjob/gpupdate
%{_pam_moduledir}/pam_oddjob_gpupdate.so
%{_mandir}/man8/pam_oddjob_gpupdate.8*
%{_mandir}/man5/oddjob-gpupdate.conf.5*
%{_mandir}/man5/oddjobd-gpupdate.conf.5*
%config(noreplace) %{_sysconfdir}/dbus-*/system.d/oddjob-gpupdate.conf
%config(noreplace) %{_sysconfdir}/oddjobd.conf.d/oddjobd-gpupdate.conf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 2 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.1-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Pavel Filipenský <pfilipen@redhat.com> - 0.2.1-1
- Initial import (fedora#2091668).
