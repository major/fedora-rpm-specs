# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license as the packaged software itself.

# Rationale for choosing a post release:
#
# The version that I use from git is a couple commits *after* 0.3.0 and there
# is no more recent tag in the upstream repository. Previously I have used
# xss-lock 0.3.0 on Ubuntu 15.04 and had a bug with it, it would not exit when
# I logged out of the graphics session. Then it would hammer one CPU core. The
# repository contains commits which suggest that this bug has been addressed
# but not yet released.

%global checkout 20140302git
%global commit0 1e158fb20108058dbd62bd51d8e8c003c0a48717
%global shortcommit0 %(c=%{commit0}; echo ${c:0:12})

Name:		xss-lock
Version:	0.3.0
Release:	19.%{checkout}%{?dist}
Summary:	Use external locker as X screen saver

#Group:		
License:	MIT
Url:		https://bitbucket.org/raymonad/xss-lock
Source0:	https://bitbucket.org/raymonad/%{name}/get/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:  gcc
BuildRequires:	glib2-devel
BuildRequires:	libxcb-devel
BuildRequires:  python3-docutils
BuildRequires:	xcb-util-devel
Requires:	xcb-util

# Description is a verbatim copy of the manual formatted to Markdown.

%description
*xss-lock* hooks up your favorite locker to the MIT screen saver extension for
X and also to systemd's login manager. The locker is executed in response to
events from these two sources:

- X signals when screen saver activation is forced or after a period of user
  inactivity (as set with `xset s TIMEOUT`). In the latter case, the notifier
  command, if specified, is executed first.

- The login manager can also request that the session be locked; as a result of
  `loginctl lock-sessions`, for example. Additionally, **xss-lock** uses the
  inhibition logic to lock the screen before the system goes to sleep.

*xss-lock* waits for the locker to exit -- or kills it when screen saver
deactivation or session unlocking is forced -- so the command should not fork.

Also, *xss-lock* manages the idle hint on the login session. The idle state of
the session is directly linked to user activity as reported by X (except when
the notifier runs before locking the screen). When all sessions are idle, the
login manager can take action (such as suspending the system) after a
preconfigured delay.

%prep
%setup -qn raymonad-%{name}-%{shortcommit0}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/xss-lock
%{_datadir}/bash-completion/completions/
%{_datadir}/zsh/
%{_mandir}/man1/xss-lock.1*
%doc NEWS
%doc doc/dim-screen.sh
%doc doc/transfer-sleep-lock-generic-delay.sh
%doc doc/transfer-sleep-lock-i3lock.sh
%doc doc/xdg-screensaver.patch
%license LICENSE

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-19.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-17.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.0-11.20140302git
- Fix FTBFS rhbz#1606760 and rhbz#1676252

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5.20140302git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 06 2016 Martin Ueding <von.fedora@martin-ueding.de> 0.3.0-4.20140302git
- Own `zsh` directory

* Tue Jan 05 2016 Martin Ueding <von.fedora@martin-ueding.de> 0.3.0-3.20140302git
- Include full commit has
- Let RPM find library dependencies automatically

* Mon Jan 04 2016 Martin Ueding <von.fedora@martin-ueding.de> 0.3.0-2.20140302git
- Use downloading and renaming support from `%%setup -qn` and `spectool -g`
- Replace `%%define` with `%%global`
- Own shell completion directory as this package does not explicitly depend on
  the shells
- Add a wildcard to catch all manual page compression formats
- Add a `Url` tag

* Sat Jan 02 2016 Martin Ueding <von.fedora@martin-ueding.de> 0.3.0-1
- Initial RPM
