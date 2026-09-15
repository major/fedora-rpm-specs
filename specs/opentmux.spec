# use git tag as source. requires regenerating manpage
%bcond use_tag 0

Name:           opentmux
Version:        0.1
Release:        %autorelease
Summary:        An AI-free terminal multiplexer

License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND SSH-short AND LicenseRef-Fedora-Public-Domain
URL:            https://codeberg.org/opentmux/opentmux
%if %{with use_tag}
Source:         %{url}/archive/v%{version}.tar.gz#/opentmux-v%{version}.tar.gz
%else
Source:         https://codeberg.org/opentmux/opentmux/releases/download/v%{version}/opentmux-%{version}.tar.gz
%endif
# command-order: consistently fails on aarch64
# new-session-size: flaky on i686/x86_64
Patch:          opentmux-disable-some-regression-tests.diff

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  libutempter-devel
%if %{with use_tag}
BuildRequires:  lowdown >= 3.0.1
%endif
BuildRequires:  pkgconfig(libevent_core)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(tinfo)
BuildRequires:  systemd-rpm-macros

Requires(post):   coreutils
Requires(post):   grep
Requires(postun): sed      

%description
This is a fork of tmux-3.6a before any AI was introduced into the project.

tmux is a terminal multiplexer: it enables a number of terminals to be created,
accessed, and controlled from a single screen. tmux may be detached from a
screen and continue running in the background, then later reattached.


%prep
%autosetup -p1 %{?with_use_tag:-n %{name}}


%conf
%meson -Dsixel=true -Dsystemd=enabled -Dutempter=enabled


%build
%meson_build


%install
%meson_install
# rename so we can parallel-install with tmux
mv %{buildroot}%{_bindir}/{,open}tmux
pushd %{buildroot}%{_mandir}/man1
for m in tmux.1*; do
  mv ${m} open${m}
done
popd


%check
%{buildroot}%{_bindir}/opentmux -V

%meson_test


%post
# Add login shell entries to /etc/shells only when installing the package
# for the first time:
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ]; then
    echo "%{_bindir}/opentmux" > %{_sysconfdir}/shells
    echo "/bin/opentmux" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/opentmux$" %{_sysconfdir}/shells || echo "%{_bindir}/opentmux" >> %{_sysconfdir}/shells
    grep -q "^/bin/opentmux$" %{_sysconfdir}/shells || echo "/bin/opentmux" >> %{_sysconfdir}/shells
  fi
fi


%postun
# Remove the login shell lines from /etc/shells only when uninstalling:
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ]; then
  sed -i -e '\!^%{_bindir}/opentmux$!d' -e '\!^/bin/opentmux$!d' %{_sysconfdir}/shells
fi


%files
%license COPYING
%doc README.md CHANGELOG.md CHANGES example_tmux.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
