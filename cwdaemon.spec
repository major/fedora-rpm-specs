%global forgeurl https://github.com/acerion/cwdaemon
Version:  0.12.0
%forgemeta

Name:           cwdaemon
Release:        %autorelease
Summary:        Morse daemon for the parallel or serial port

License:        GPL-2.0-only
URL:            http://cwdaemon.sourceforge.net
Source0:        %{forgesource}
Source1:        cwdaemon.sysconfig
Source2:        cwdaemon.service

BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  unixcw-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  make

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
cwdaemon is a small daemon which uses the pc parallel or serial port and a
simple transistor switch to output morse code to a transmitter from a text
message sent to it via udp port 6789. The program also uses the soundcard or PC
speaker (console buzzer) to generate a sidetone.

%prep
%forgeautosetup -p1

%build
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_unitdir}
install -pDm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/cwdaemon
install -pDm644 %{SOURCE2} %{buildroot}%{_unitdir}/cwdaemon.service

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_sbindir}/%{name} %{buildroot}%{_bindir}/%{name}

%check
make check

%post
%systemd_post cwdaemon.service

%preun
%systemd_preun cwdaemon.service

%postun
%systemd_postun_with_restart cwdaemon.service

%files
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/%{name}
%{_unitdir}/cwdaemon.service
%config(noreplace) %{_sysconfdir}/sysconfig/cwdaemon
%{_mandir}/man8/%{name}.8.gz
%{_datadir}/%{name}/

%changelog
%autochangelog
