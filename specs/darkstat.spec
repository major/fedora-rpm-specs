Name:		darkstat
Summary:	Network traffic analyzer
Version:	3.0.721
Release:	9%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only

URL:		https://unix4lyfe.org/darkstat
Source:		https://github.com/emikulic/darkstat/archive/%{version}/%{name}-%{version}.tar.gz

Source1:	%{name}.service
Source2:	%{name}.sysconfig

Patch1:		getaddrinfo.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libpcap-devel
BuildRequires:	make
BuildRequires:	systemd-rpm-macros
BuildRequires:	zlib-devel

Requires(post):	systemd
Requires(preun): systemd
Requires(postun): systemd

%description
darkstat is a network traffic analyzer. It's basically a packet sniffer
which runs as a background process on a cable/DSL router and gathers
all sorts of useless but interesting statistics.

%prep
%autosetup -p1

%build
autoreconf -ifv
%configure --disable-silent-rules
%make_build

%install
%make_install
install -Dpm444 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%pre
getent group darkstat >/dev/null || groupadd -r darkstat
getent passwd darkstat >/dev/null || \
	useradd -r -g darkstat -d /var/lib/darkstat -s /sbin/nologin \
	-c "Network traffic analyzer" darkstat
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING.GPL LICENSE
%doc AUTHORS NEWS README.md
%attr(0755, darkstat, root) %{_sbindir}/%{name}
%attr(0644, darkstat, root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man8/%{name}*
%{_unitdir}/%{name}.service

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.721-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.721-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.721-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.721-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.721-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.721-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.721-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.721-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Ali Erdinc Koroglu <ali.erdinc.koroglu@intel.com> - 3.0.721-1
- Upstream update to 3.0.721

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.719-13
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.719-1
- Update to upstream version 3.0.719.
- Lib exit should be fixed (https://unix4lyfe.org/gitweb/darkstat/commitdiff/dbd25d7f8f06770f46fe9f3d460385e699439186).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.718-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.718-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.718-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.718-3
- Add --disable-silent-rules to configure call.

* Thu Apr 24 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.718-2
- Do not mark man as %%doc.
- Add systemd stuff.
- Provide separate user for service.

* Fri Mar 14 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.718-1
- Imported from http://pkgs.repoforge.org/darkstat/darkstat-3.0.717-1.rf.src.rpm and rework to prepare for Fedora.
- Update to 3.0.718.
- Cleanup.
- Update URLs.
- Remove INSTALL file from docs (install-file-in-docs rpmlint warning).
- darkstat.x86_64: E: missing-call-to-setgroups /usr/sbin/darkstat, darkstat.x86_64: E: incorrect-fsf-address /usr/share/doc/darkstat/COPYING.GPL issues mailed to author.
- Add BR zlib-devel
