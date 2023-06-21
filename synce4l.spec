Name:		synce4l
Version:	0.9.0
Release:	1%{?dist}
Summary:	SyncE implementation for Linux

License:	GPL-2.0-or-later
URL:		https://github.com/intel/synce4l
Source0:	https://github.com/intel/synce4l/archive/%{version}/synce4l-%{version}.tar.gz
Source1:	synce4l.service
Source2:	synce4l.conf
Patch1:		synce4l-gcc-warn.patch

BuildRequires:	gcc make systemd

%{?systemd_requires}

%description
synce4l is a software implementation of Synchronous Ethernet (SyncE) according
to ITU-T Recommendation G.8264. The design goal is to provide logic to
supported hardware by processing Ethernet Synchronization Messaging Channel
(ESMC) and control Ethernet Equipment Clock (EEC) on Network Card Interface
(NIC).

%prep
%autosetup
# Fix building outside of git repository
sed -i 's|\(^VERSION := \).*|\1%{version}|' Makefile

%build
%{make_build} \
	EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
	EXTRA_LDFLAGS="$RPM_LD_FLAGS"

%install
# make_install doesn't work here
%makeinstall

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_unitdir},%{_mandir}/man5}
install -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}
install -m 644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}

echo '.so man8/synce4l.8' > $RPM_BUILD_ROOT%{_mandir}/man5/synce4l.conf.5

%check
./synce4l -h 2>&1 | grep 'usage:.*synce4l'

%post
%systemd_post synce4l.service

%preun
%systemd_preun synce4l.service

%postun
%systemd_postun_with_restart synce4l.service

%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/synce4l.conf
%{_unitdir}/synce4l.service
%{_sbindir}/synce4l
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%changelog
* Mon Jun 19 2023 Miroslav Lichvar <mlichvar@redhat.com> 0.9.0-1
- update to 0.9.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20221114gitca51d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Miroslav Lichvar <mlichvar@redhat.com> 0-3.20221114gitca51d5
- update to 20221114gitca51d5 (#2141038)

* Thu Nov 10 2022 Miroslav Lichvar <mlichvar@redhat.com> 0-2.20221108git079577
- fix compiler warning (#2141038)
- add simple test (#2141038)

* Tue Nov 08 2022 Miroslav Lichvar <mlichvar@redhat.com> 0-1.20221108git079577
- make initial release
