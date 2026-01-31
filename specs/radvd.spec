Name: radvd
Version: 2.20
Release: %autorelease
Summary: A Router Advertisement daemon
License: radvd
URL: https://radvd.litech.org

Source0: https://radvd.litech.org/dist/%{name}-%{version}.tar.xz
Source1: https://radvd.litech.org/dist/%{name}-%{version}.tar.xz.asc
# Robin Hugh Johnson's public key
Source2: https://github.com/robbat2.gpg
Source3: radvd.sysusers

# allow glibc strlcpy, avoid libbsd dependency
Patch0: https://github.com/radvd-project/radvd/pull/256.patch
Patch1: https://github.com/radvd-project/radvd/pull/262.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: flex-static
BuildRequires: pkgconfig
BuildRequires: check-devel
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
%{?systemd_requires}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gpgverify

%description
radvd is the router advertisement daemon for IPv6.  It listens to router
solicitations and sends router advertisements as described in "Neighbor
Discovery for IP Version 6 (IPv6)" (RFC 2461).  With these advertisements
hosts can automatically configure their addresses and some other
parameters.  They also can choose a default router based on these
advertisements.

Install radvd if you are setting up IPv6 network and/or Mobile IPv6
services.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

for F in CHANGES; do
    iconv -f iso-8859-1 -t utf-8 < "$F" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done

%build
autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS -fPIE " 
export LDFLAGS='-pie -Wl,-z,relro,-z,now,-z,noexecstack,-z,nodlopen'
%configure \
    --with-check \
    --disable-silent-rules \
    --with-pidfile=/run/radvd/radvd.pid
%make_build 

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}/run/radvd
mkdir -p %{buildroot}%{_unitdir}

install -m 644 redhat/SysV/radvd.conf.empty %{buildroot}%{_sysconfdir}/radvd.conf
install -m 644 redhat/SysV/radvd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/radvd

install -d -m 755 %{buildroot}%{_tmpfilesdir}
install -p -m 644 redhat/systemd/radvd-tmpfs.conf %{buildroot}%{_tmpfilesdir}/radvd.conf
install -m 644 redhat/systemd/radvd.service %{buildroot}%{_unitdir}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/radvd.conf

%check
make check

%postun
%systemd_postun_with_restart radvd.service

%post
%systemd_post radvd.service

%preun
%systemd_preun radvd.service


%files
%doc CHANGES COPYRIGHT INTRO.html README TODO
%{_unitdir}/radvd.service
%config(noreplace) %{_sysconfdir}/radvd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/radvd
%{_tmpfilesdir}/radvd.conf
%{_sysusersdir}/radvd.conf
%dir %attr(755,radvd,radvd) /run/radvd/
%doc radvd.conf.example
%{_mandir}/man5/radvd.conf.5*
%{_mandir}/man8/radvd.8*
%{_mandir}/man8/radvdump.8*
%{_sbindir}/radvd
%{_sbindir}/radvdump

%changelog
%autochangelog
