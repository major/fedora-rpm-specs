Name:           boinc-tui
Version:        2.7.1
Release:        2%{?dist}
Summary:        Fullscreen Text Mode Manager For BOINC Client

License:        GPL-3.0-or-later
URL:            https://github.com/suleman1971/boinctui

%global commit       6338b8e718dd429aca35f7d0f9b62328740dde18
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20231214
Source0:        https://github.com/suleman1971/boinctui/archive/%{commit}/boinctui-%{shortcommit}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  expat-devel
BuildRequires:  openssl-devel
BuildRequires:  gcc-c++
BuildRequires: make

%description
 boinc-tui is a fullscreen text mode control tool for BOINC client
 It can manage local and remote clients (via boinc RPC), and allows
 you to switch between  clients with a hot key.
 boinctui uses curses library and provides the following features:
  * Fullscreen curses based text user interface
  * Switch between several BOINC clients hosts via hot key
  * View task list (run, queue, suspend e.t.c state)
  * View message list
  * Suspend/Resume/Abort tasks
  * Update/Suspend/Resume/Reset/No New Task/Allow New Task for projects
  * Toggle activity state GPU and CPU tasks
  * Run benchmarks
  * Manage BOINC client on remote hosts via boinc_gui protocol

%prep
%autosetup -n boinctui-%{commit}


%build
autoreconf -vif
%configure --without-gnutls
%make_build


%install
%make_install DOCDIR=%{_pkgdocdir}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 boinctui.1 %{buildroot}%{_mandir}/man1/


%files
%doc %{_pkgdocdir}/changelog
%license gpl-3.0.txt
%{_bindir}/boinctui
%{_mandir}/man1/boinctui.1.*



%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.7.1-1
- Update to 2.7.1 (fix RHBZ#2254604; fix RHBZ#2300581; fix RHBZ#2261015)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 2.7.0-1
- Update to 2.7.0 (fix RHBZ#2113125)
- Stop listing the changelog file twice
- Preserve the timestamp when installing the man page
- Update License to SPDX

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.5.0-7
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 24 2020 Germano Massullo <germano.massullo@gmail.com> - 2.5.0-2
- Renamed package to boinc-tui

* Sun Aug 04 2019 Timothy Mullican <timothy.j.mullican@gmail.com> 2.5.0-1
- Generate new RPM SPEC file to conform with best practices

* Tue Feb 12 2013 Sergey Suslov <suleman1971@gmail.com> 2.2.1-0
- Initial version of the package
