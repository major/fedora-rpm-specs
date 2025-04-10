Name:           tang
Version:        15
Release:        %autorelease
Summary:        Network Presence Binding Daemon

License:        GPL-3.0-or-later
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        tang.sysusers

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  git-core
BuildRequires:  jose >= 8
BuildRequires:  libjose-devel >= 8
BuildRequires:  libjose-zlib-devel >= 8
BuildRequires:  libjose-openssl-devel >= 8

BuildRequires:  llhttp-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig

BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  curl

BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  grep
BuildRequires:  socat
BuildRequires:  sed
BuildRequires:  iproute

%{?systemd_ordering}
Requires:       coreutils
Requires:       jose >= 8
Requires:       llhttp
Requires:       grep
Requires:       sed


%description
Tang is a small daemon for binding data to the presence of a third party.

%prep
%autosetup -S git

%build
%meson
%meson_build

%install
%meson_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/tang.conf
%{__mkdir_p} $RPM_BUILD_ROOT/%{_localstatedir}/db/%{name}

%check
%meson_test \
%ifarch riscv64
    --timeout-multiplier 10 \
%endif
    %{nil}


%post
%systemd_post %{name}d.socket

# Let's make sure any existing keys are readable only
# by the owner/group.
if [ -d /var/db/tang ]; then
    for k in /var/db/tang/*.jwk; do
        test -e "${k}" || continue
        chmod 0440 -- "${k}"
    done
    for k in /var/db/tang/.*.jwk; do
        test -e "${k}" || continue
        chmod 0440 -- "${k}"
    done
    chown tang:tang -R /var/db/tang
fi

%preun
%systemd_preun %{name}d.socket

%postun
%systemd_postun_with_restart %{name}d.socket

%files
%license COPYING
%attr(0700, %{name}, %{name}) %{_localstatedir}/db/%{name}
%{_unitdir}/%{name}d@.service
%{_unitdir}/%{name}d.socket
%{_libexecdir}/%{name}d-keygen
%{_libexecdir}/%{name}d-rotate-keys
%{_libexecdir}/%{name}d
%{_mandir}/man8/tang.8*
%{_bindir}/%{name}-show-keys
%{_mandir}/man1/tang-show-keys.1*
%{_mandir}/man1/tangd-rotate-keys.1.*
%{_sysusersdir}/tang.conf

%changelog
%autochangelog
