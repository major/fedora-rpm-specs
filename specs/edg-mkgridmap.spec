%global         forgeurl https://gitlab.cern.ch/curios/edg-mkgridmap

Name:		edg-mkgridmap
Version:	4.0.6

%global         tag v%{version}
%forgemeta

Release:	%autorelease
Summary:	A tool to build the grid map-file from VO servers
License:	Apache-2.0
Url:		%forgeurl

Source0:	%{forgesource}
Source1:        edg-mkgridmap.conf
Source2:        edg-mkgridmap.service
Source3:        edg-mkgridmap.timer

# https://gitlab.cern.ch/curios/edg-mkgridmap/-/merge_requests/2
Patch0:         sbin-bin.patch

BuildArch:	noarch
BuildRequires:	perl-generators
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

Requires:	perl(URI)
Requires:	perl(Net::LDAP)
Requires:	perl(Net::LDAPS)
Requires:	perl(Term::ReadKey)
Requires:	perl(IO::Socket::SSL) >= 0.90
Requires:	perl(Net::SSLeay) >= 1.16
Requires:	perl(LWP)
Requires:	perl(XML::DOM)
Requires:	perl(Date::Manip)
Requires:       perl(LWP::Protocol::https)

%description
edg-mkgridmap is a tool to build the grid map-file from VO servers,
taking into account both VO and local policies.


%prep
%forgesetup
%patch -P 0 -p 1

cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .


%build


%install
make install prefix=%{buildroot}

mkdir %{buildroot}%{_sysconfdir}
install -p -m 0600 edg-mkgridmap.conf %{buildroot}%{_sysconfdir}/edg-mkgridmap.conf

mkdir %{buildroot}%{_sysconfdir}/grid-security

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 edg-mkgridmap.service %{buildroot}%{_unitdir}/edg-mkgridmap.service
install -p -m 0644 edg-mkgridmap.timer   %{buildroot}%{_unitdir}/edg-mkgridmap.timer


%post
%systemd_post edg-mkgridmap.service edg-mkgridmap.timer


%preun
%systemd_preun edg-mkgridmap.service edg-mkgridmap.timer


%postun
%systemd_postun_with_restart edg-mkgridmap.service edg-mkgridmap.timer


%files
%doc AUTHORS MAINTAINERS
%license LICENSE
%dir %{_libexecdir}/edg-mkgridmap
%{_libexecdir}/edg-mkgridmap/edg-mkgridmap.pl
%{_bindir}/edg-mkgridmap
%{_mandir}/man5/edg-mkgridmap.conf.5*
%{_mandir}/man8/edg-mkgridmap.8*
%dir %{_sysconfdir}/grid-security
%{_unitdir}/edg-mkgridmap.service
%{_unitdir}/edg-mkgridmap.timer
%config(noreplace) %{_sysconfdir}/edg-mkgridmap.conf


%changelog
%autochangelog
