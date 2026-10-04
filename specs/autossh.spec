Summary: Utility to autorestart SSH tunnels
Name: autossh
Version: 1.4g
Release: %autorelease
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/653
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/654
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/655
License: ISC AND LicenseRef-Fedora-UltraPermissive
URL: https://www.harding.motd.ca/autossh/
Source0: https://www.harding.motd.ca/autossh/autossh-1.4g.tgz
Source1: autossh@.service
Source2: README.service
Source3: autossh.sysusers.conf
Patch0: autossh-configure-c99.patch
BuildRequires:  gcc
BuildRequires: /usr/bin/ssh
BuildRequires: systemd
BuildRequires: make
%{?systemd_requires}
Requires: /usr/bin/ssh

%description
autossh is a utility to start and monitor an ssh tunnel. If the tunnel
dies or stops passing traffic, autossh will automatically restart it.

%prep
%setup -q
%patch -P0 -p1
cp -p %{SOURCE2} .

%build
%configure
make %{?_smp_mflags}

%install

gzip autossh.1

install -m 0755 -Dp autossh %{buildroot}%{_bindir}/autossh
install -m 0644 -Dp autossh.1.gz %{buildroot}%{_mandir}/man1/autossh.1.gz

install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_unitdir}/autossh@.service
install -m 0644 -Dp %{SOURCE3} %{buildroot}%{_sysusersdir}/autossh.conf

mkdir -p %{buildroot}%{_sysconfdir}/autossh

%post
%systemd_post autossh@.service

%preun
# https://bugzilla.redhat.com/1996234
if [ $1 -eq 0 ] && [ -x /usr/bin/systemctl ]; then
    # Package removal, not upgrade
    if [ -d /run/systemd/system ]; then
        /usr/bin/systemctl --no-reload disable --now autossh@.service || :
	systemctl stop "autossh@*.service" || :
    else
        /usr/bin/systemctl --no-reload disable autossh@.service || :
    fi
fi

%postun
%systemd_postun_with_restart "autossh@*.service"


%files
%doc CHANGES README README.service
%{_bindir}/*
%attr(750,autossh,autossh) %dir %{_sysconfdir}/autossh/
%{_mandir}/man1/*
%{_unitdir}/*
%{_sysusersdir}/autossh.conf

%changelog
%autochangelog
