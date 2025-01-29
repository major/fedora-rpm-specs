%if %{defined fedora}
# dmenu requirement currently missing in epel8
%bcond_without passmenu
%endif

Name:           pass
Summary:        A password manager using standard Unix tools
Version:        1.7.4
Release:        14%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            http://zx2c4.com/projects/password-store/
BuildArch:      noarch
Source:         http://git.zx2c4.com/password-store/snapshot/password-store-%{version}.tar.xz
Patch:          0001-Default-to-xclip-if-wl-clip-is-not-found.patch

BuildRequires: make
BuildRequires:       git-core
BuildRequires:       gnupg2
BuildRequires:       perl-generators
BuildRequires:       tree >= 1.7.0
Recommends:          (wl-clipboard if libwayland-client else xclip)
Recommends:          (xclip if xorg-x11-server-Xorg else wl-clipboard)
Requires:            git-core
Requires:            gnupg2
Requires:            qrencode
Requires:            tree >= 1.7.0

%description
Stores, retrieves, generates, and synchronizes passwords securely using gpg
and git.

%if %{with passmenu}
%package -n passmenu
Summary:        A dmenu based interface to pass.
Requires:       pass
Recommends:     (dmenu-wayland if libwayland-client)
Recommends:     (dmenu if xorg-x11-server-Xorg)
Requires:       xdotool

%description -n passmenu
A dmenu based interface to pass, the standard Unix password manager. This
design allows you to quickly copy a password to the clipboard without having to
open up a terminal window if you don't already have one open. If `--type` is
specified, the password is typed using xdotool instead of copied to the
clipboard.
%endif

%prep
%autosetup -p 1 -n password-store-%{version}
rm -f contrib/emacs/.gitignore

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
     BINDIR=%{_bindir} SYSCONFDIR=%{_sysconfdir} \
     MANDIR=%{_mandir} WITH_ALLCOMP="yes" \
     install

%if %{with passmenu}
install -D -p -m 0755 contrib/dmenu/passmenu %{buildroot}%{_bindir}/passmenu
%endif

# Used by extensions
mkdir -p %{buildroot}%{_prefix}/lib/password-store/extensions

%check
make test

%files
%doc README COPYING contrib/emacs contrib/importers contrib/vim
%{_bindir}/pass
%{_datadir}/bash-completion/completions/pass
%{_datadir}/fish/vendor_completions.d/pass.fish
%{_datadir}/zsh/site-functions/_pass
%doc %{_mandir}/man1/*
%dir %{_prefix}/lib/password-store
%dir %{_prefix}/lib/password-store/extensions

%if %{with passmenu}
%files -n passmenu
%doc contrib/dmenu/README.md
%{_bindir}/passmenu
%endif

%changelog
* Mon Jan 27 2025 Łukasz Wojniłowicz <lukasz.wojnilowicz@gmail.com> - 1.7.4-14
- Set dmenu-wayland and dmenu to Recommends instead of Requires to have
  a choice to install one or the other or both. Helpful when using Wayland
  and having xorg-x11-server-Xorg for XWayland purpose only.
  Resolves: rhbz#2335143
  
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.4-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 22 2022 Peter Georg <peter.georg@physik.uni-regensburg.de> - 1.7.4-6
- Set wl-copy/xclip requires to recommends
  Resolves: rhbz#2022909
- Cherry-pick upstream commit handling wl-copy/xclip selection

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Christophe Fergeau <cfergeau@redhat.com> - 1.7.4-3
- adjust wl-copy/xclip requires so that they are actually installed when needed
  Resolves: rhbz#1996323

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.7.4-1
- New upstream release 1.7.4
- Fixes rhbz#1948181

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Carl George <carl@george.computer> - 1.7.3-7
- Only build passmenu package on Fedora, not EPEL8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Brian Exelbierd <bexelbie@redhat.com> - 1.7.3-3
- Add pass extension directories

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.7.3-1
- Update to latest upstream version

* Fri Jun 15 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.7.2-1
- Update to new upstream release
  Resolves: rhbz#1591573

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 01 2017 Carl George <carl@george.computer> - 1.7.1-5
- Passmenu requires pass

* Tue Aug 01 2017 Carl George <carl@george.computer> - 1.7.1-4
- Require git-core instead of git rhbz#1471608
- Add passmenu subpackage rhbz#1474833

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Christophe Fergeau <cfergeau@redhat.com> 1.7.1-2
- New minor upstream release

* Fri Mar 10 2017 Christophe Fergeau <cfergeau@redhat.com> 1.7-2
- Adjust dependencies, pwgen is no longer used, and pass show --qrcode
  needs qrencode
  Resolves: rhbz#1427594

* Mon Feb 27 2017 Christophe Fergeau <cfergeau@redhat.com> 1.7.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Christophe Fergeau <cfergeau@redhat.com> 1.6.5-1
- Update to pass 1.6.5

* Thu Dec 04 2014 Christophe Fergeau <cfergeau@redhat.com> 1.6.3-1
- Update to pass 1.6.3

* Sat Jun 07 2014 Christophe Fergeau <cfergeau@redhat.com> 1.6.2-1
- Update to pass 1.6.2

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Christophe Fergeau <cfergeau@redhat.com> 1.6.1-2
- Make sure tree 1.7 is present
- Run test suite when building package
- Various small spec cleanups

* Fri Apr 25 2014 Christophe Fergeau <cfergeau@redhat.com> 1.6.1-1
- Update to 1.6.1

* Wed Apr 23 2014 Christophe Fergeau <cfergeau@redhat.com> 1.5-2
- Fix location of bash completion files

* Thu Apr 17 2014 Christophe Fergeau <cfergeau@redhat.com> - 1.5-1
- Update to 1.5.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 30 2012 Christophe Fergeau <cfergeau@redhat.com> - 1.4.1-1
- Update to 1.4.1
- Fix gnupg dependency (pass needs gnupg2)

* Mon Sep 24 2012 Christophe Fergeau <cfergeau@redhat.com> - 1.4-1
- Update to 1.4

* Tue Sep 11 2012 Christophe Fergeau <cfergeau@redhat.com> - 1.2.0-1
- Update to 1.2 release

* Thu Sep 06 2012 Christophe Fergeau <cfergeau@redhat.com> - 1.1.4-1
- Initial import

