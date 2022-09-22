Name:           ncmpc
Version:        0.47
Release:        2%{?dist}
Summary:        A curses client for the Music Player Daemon (MPD)

License:        GPLv2+
URL:            http://www.musicpd.org/
Source0:        http://www.musicpd.org/download/ncmpc/0/ncmpc-%{version}.tar.xz
Source1:        http://www.musicpd.org/download/ncmpc/0/ncmpc-%{version}.tar.xz.sig

# Created with
#   $ gpg2 --receive-keys C6DB4512
#   $ gpg2 --export --export-options export-minimal 236E8A58C6DB4512
Source2:        gpgkey-236E8A58C6DB4512.gpg

BuildRequires:  cmake
BuildRequires:  gnupg2
BuildRequires:  g++
BuildRequires:  gettext
BuildRequires:  meson >= 0.47
BuildRequires:  libmpdclient-devel >= 2.16
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  lirc-devel
BuildRequires:  python%{python3_pkgversion}-sphinx

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc connects to
a MPD running on a machine on the local network, and controls this with an
interface inspired by cplay.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%meson \
    -Dchat_screen=true \
    -Dlyrics_screen=true \
    -Dlyrics_plugin_dir=%{_datadir}/ncmpc/lyrics
%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc
install -p -m644 doc/config.sample \
    $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc/config
install -p -m644 doc/keys.sample $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc/keys

%find_lang ncmpc


%files -f ncmpc.lang
%doc README.rst NEWS AUTHORS COPYING doc/ncmpc.lirc doc/index.rst
%{_bindir}/ncmpc
%{_mandir}/man1/*
%dir %{_sysconfdir}/ncmpc
%config(noreplace) %{_sysconfdir}/ncmpc/config
%config(noreplace) %{_sysconfdir}/ncmpc/keys
%dir %{_datadir}/ncmpc
%dir %{_datadir}/ncmpc/lyrics
%{_datadir}/ncmpc/lyrics/*

%exclude %{_datadir}/doc/ncmpc/*
%doc %{_datadir}/doc/ncmpc/html


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.47-1
- New upstream release

* Sat May 07 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.46-1
- New upstream release
- Drop patches for issues fixed upstream
- Re-enable signature verification for source tarballs

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.45-3
- Patch out build-time rsync dependency

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 18 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.45-1 
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 1 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.42-1
- Update to 0.42 (#1888935)

* Wed Oct 7 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.40-1
- New upstream release

* Fri Aug 21 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.39-1
- New upstream release
- Comment out signature checking until process issues are sorted out

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.38-1
- New upstream release, drop upstreamed patches

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.36-1
- New upstream release, switch to meson+ninja build, add signature verification

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Adrian Reber <adrian@lisas.de> - 0.27-4
- Rebuilt for new libmpdclient

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 0.27-1
- version upgrade

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.24-1
- update to upstream release 0.24

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.21-1
- update to upstream release 0.21
- add --enable-lyrics-screen and BR: ruby-devel
- remove redundant `configure` options

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 0.20-1
- update to upstream release 0.20
- remove obsolete BuildRoot tag, %%clean section and %%defattr

* Tue Mar 01 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.18-1
- version upgrade (#680985)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.14-1
- version upgrade

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 09 2009 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.13-1
- version upgrade (#479240)

* Sat Nov 22 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.12-0.1.beta1
- version upgrade

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0.11.1-9
- Rebuilt for gcc43

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.11.1-2
- new license tag
- rebuild for buildid

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.11.1-7
- FE6 rebuild

* Tue Aug 01 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.11.1-6
- fix #200423

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.11.1-5
- Rebuild for Fedora Extras 5

* Fri Jun 24 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.11.1-4
- correct summary

* Thu Jun 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.11.1-3
- add dist tag

* Thu Jun 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.11.1-2
- some changes suggested by Aurélien Bompard

* Wed Jun 01 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.11.1-1
- Initial Release
