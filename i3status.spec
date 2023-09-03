Name:           i3status
Version:        2.14
Release:        %autorelease
Summary:        Status bar generator for i3bar, dzen2, xmobar or similar programs
License:        BSD-3-Clause
URL:            https://i3wm.org/i3status/
Source0:        %{url}/%{name}-%{version}.tar.xz
Source1:        %{url}/%{name}-%{version}.tar.xz.asc
# Michael Stapelberg's GPG key:
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D#./gpgkey-424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D.gpg
Source3:        fedora-i3-status-config

BuildRequires:  gcc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(yajl)
# man pages
BuildRequires:  asciidoc
BuildRequires:  xmlto
# gpg verification
BuildRequires:  gnupg2
# tests
BuildRequires:  perl
BuildRequires:  make
BuildRequires:  meson

Recommends:     i3status-config
Requires:       (i3status-config or i3status-config-fedora)

%description
i3status is a program for generating a status bar for i3bar, dzen2,
xmobar or similar programs. It issues a small number of system
calls, as one generally wants to update such status lines every
second so that the bar is updated even under load. It saves a bit of
energy by being more efficient than shell commands.

%package        config
Summary:        Upstream configuration for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name}-config-fedora

%description    config
This is the upstream/vanilla configuration file of %{name}.

%package        config-fedora
RemovePathPostfixes: .fedora
Summary:        Configuration of %{name} for the Fedora i3 Spin
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name}-config

%description    config-fedora
This is the configuration file of %{name} used for the Fedora i3 Spin.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}.conf.fedora


%check
# this need the testcases/ dir from upstream git repository
# unfortunately this fails on koji
# make check -C build || (cat test-suite.log; false)

%files
%doc CHANGELOG
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.1*

%files config
%config(noreplace) %{_sysconfdir}/%{name}.conf

%files config-fedora
%config(noreplace) %{_sysconfdir}/%{name}.conf.fedora

%changelog
%autochangelog
