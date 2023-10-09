# Rationale for choosing a post release:
#
# The version that I use from git is a couple commits *after* 0.3.0 and there
# is no more recent tag in the upstream repository.

%global commit0 1e158fb20108058dbd62bd51d8e8c003c0a48717
%global shortcommit0 %(c=%{commit0}; echo ${c:0:12})

Name:		xss-lock
Version:	0.3.0^20140302git1e158fb20108
Release:	%autorelease
Summary:	Use external locker as X screen saver

#Group:		
License:	MIT
Url:		https://bitbucket.org/raymonad/xss-lock
Source0:	https://bitbucket.org/raymonad/%{name}/get/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	libxcb-devel
BuildRequires:	python3-docutils
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
%autosetup -n raymonad-%{name}-%{shortcommit0}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc NEWS doc/dim-screen.sh doc/transfer-sleep-lock-generic-delay.sh doc/transfer-sleep-lock-i3lock.sh doc/xdg-screensaver.patch
%{_bindir}/xss-lock
%{_datadir}/bash-completion/completions/
%{_datadir}/zsh/
%{_mandir}/man1/xss-lock.1*

%changelog
%autochangelog
