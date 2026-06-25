Name:           tmux
Version:        3.6b
Release:        %autorelease
Summary:        A terminal multiplexer

License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND SSH-short AND LicenseRef-Fedora-Public-Domain
URL:            https://tmux.github.io/
Source0:        https://github.com/tmux/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source2:        tmux@.service
Source3:        README.polkit

# related to https://github.com/tmux/tmux/commit/f58b8d0d6abb2477b584547a4e72cc362ecbbcdb
# this patch should be removed during next tmux upgrade since it's in the master branch
Patch0:         0001-Setting-working-directory-after-fork-means-there-is-.patch

BuildRequires:  byacc
BuildRequires:  gcc
BuildRequires:  systemd-devel
BuildRequires:  libutempter-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libevent_core) >= 2
BuildRequires:  pkgconfig(tinfo)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncursesw)
%if "%0{?commit}" != "0"
BuildRequires:  automake
%endif

Requires(post):   coreutils
Requires(post):   grep
Requires(postun): sed

%description
tmux is a "terminal multiplexer."  It enables a number of terminals (or
windows) to be accessed and controlled from a single terminal.  tmux is
intended to be a simple, modern, BSD-licensed alternative to programs such
as GNU Screen.


%prep
%autosetup


%build
%configure --enable-sixel --enable-systemd --enable-utempter
%make_build


%install
%make_install
# Install the systemd file
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/tmux@.service
# Install the polkit example file
install -Dpm 644 %{SOURCE3} %{buildroot}%{_docdir}/tmux/README.polkit


%check
%{buildroot}%{_bindir}/tmux -V


%post
# Add login shell entries to /etc/shells only when installing the package
# for the first time:
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ]; then
    echo "%{_bindir}/tmux" > %{_sysconfdir}/shells
    echo "/bin/tmux" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/tmux$" %{_sysconfdir}/shells || echo "%{_bindir}/tmux" >> %{_sysconfdir}/shells
    grep -q "^/bin/tmux$" %{_sysconfdir}/shells || echo "/bin/tmux" >> %{_sysconfdir}/shells
  fi
fi

%postun
# Remove the login shell lines from /etc/shells only when uninstalling:
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ]; then
  sed -i -e '\!^%{_bindir}/tmux$!d' -e '\!^/bin/tmux$!d' %{_sysconfdir}/shells
fi

%files
%license COPYING
%doc CHANGES README* example_tmux.conf README.polkit
%{_bindir}/tmux
%{_mandir}/man1/tmux.1.*
%{_unitdir}/tmux@.service

%changelog
%autochangelog
