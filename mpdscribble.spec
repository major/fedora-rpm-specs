Name:           mpdscribble
Version:        0.24
Release:        1%{?dist}
Summary:        A mpd client which submits information about tracks being played to Last.fm
License:        GPLv2+
URL:            https://www.musicpd.org/clients/mpdscribble/
Source0:        https://www.musicpd.org/download/mpdscribble/%{version}/mpdscribble-%{version}.tar.xz
Source1:        %{name}.service
Source2:        %{name}.tmpfiles.conf

Patch1: 0001-Fix-build-with-GCC-12-missing-time.h-include.patch

BuildRequires: cmake
BuildRequires: gcc-g++
BuildRequires: git
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libmpdclient-devel >= 2.2
BuildRequires: meson
BuildRequires: systemd-devel

Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
mpdscribble is a music player daemon (mpd) client which submits information
about tracks being played to Last.fm (formerly audioscrobbler)

%prep
%autosetup -S git_am

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d %{buildroot}%{_localstatedir}/run/%{name}

# Make room for logs
install -d %{buildroot}%{_localstatedir}/cache/%{name}

# Remove installed docs (this will mess with versione/unversioned docdirs)
rm -rf %{buildroot}%{_defaultdocdir}

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{_localstatedir}/cache/%{name} -s /sbin/nologin \
-c "Mpdscribble" %{name} 2>/dev/null || :

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%doc AUTHORS COPYING NEWS README.rst
%attr(0644,%{name},%{name}) %config(noreplace) %{_sysconfdir}/mpdscribble.conf
%{_bindir}/mpdscribble
%{_mandir}/man1/mpdscribble.1.gz
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%attr(0755,%{name},%{name}) %dir %{_localstatedir}/run/%{name}
%attr(0755,%{name},%{name}) %dir %{_localstatedir}/cache/%{name}

%changelog
* Sun Apr 30 2023 Robbie Harwood <rharwood@pm.me> - 0.24-1
- Under new management (update to 0.24)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Adrian Reber <adrian@lisas.de> - 0.22-15
- Rebuilt for new libmpdclient

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Jaroslaw Gorny <jaroslaw dot gorny at gmail dot com> - 0.22-10
- Add systemd-units as build requirement

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 06 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.22-6
- Spec-file cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.22-3
- Fixed tmpfiles entry (see rhbz #894364)

* Sun Sep 16 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.22-2
- Fix building

* Tue Sep 04 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.22-1
- Ver. 0.22
- Switch to systemd
- Dropped outdated stuff from spec-file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 26 2009 Jaroslaw Gorny <jaroslaw dot gorny at gmail dot com> - 0.18.1-1
- Version bumped to 0.18.1
- init-script added

* Tue Feb 03 2009 Jaroslaw Gorny <jaroslaw dot gorny at gmail dot com> - 0.16-1
- Version bumped to 0.16
- There's a systemwide config file now

* Sun Dec 21 2008 Jaroslaw Gorny <jaroslaw dot gorny at gmail dot com> - 0.13-1
- Initial RPM
