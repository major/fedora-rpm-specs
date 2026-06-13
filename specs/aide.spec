Summary:        Intrusion detection environment
Name:           aide
Version:        0.19.2
Release:        %autorelease
URL:            https://github.com/aide/aide
License:        GPL-2.0-or-later

Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
# gpg2 --recv-keys 2BBBD30FAAB29B3253BCFBA6F6947DAB68E7B931
# gpg2 --export --export-options export-minimal 2BBBD30FAAB29B3253BCFBA6F6947DAB68E7B931 >gpgkey-aide.gpg
Source2:        gpgkey-aide.gpg
Source3:        aide.conf
Source4:        README.quickstart
Source5:        aide.logrotate
Source6:        aide-check.service
Source7:        aide-check.timer

Patch0:         aide-include-permission-checks.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  bison flex
BuildRequires:  pcre2-devel
BuildRequires:  libgpg-error-devel nettle-devel
BuildRequires:  zlib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libacl-devel
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  libattr-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  audit-libs-devel
BuildRequires:  autoconf automake libtool
BuildRequires:  systemd-rpm-macros
# For verifying signatures
BuildRequires:  gnupg2
# For being able to run 'make check'
BuildRequires:  check-devel


Requires:       logrotate

%description
AIDE (Advanced Intrusion Detection Environment) is a file integrity
checker and intrusion detection program.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp -a %{SOURCE4} .

%build
#autoreconf -ivf
%configure  \
  --disable-static \
  --with-config_file=%{_sysconfdir}/aide.conf \
  --without-gcrypt \
  --with-nettle \
  --with-zlib \
  --with-curl \
  --with-posix-acl \
  --with-selinux \
  --with-xattr \
  --with-e2fsattrs \
  --with-audit
%make_build

%check
make check

%install
%make_install bindir=%{_sbindir}
install -Dpm0644 -t %{buildroot}%{_sysconfdir} %{SOURCE3}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/aide
mkdir -p %{buildroot}%{_localstatedir}/log/aide
mkdir -p -m0700 %{buildroot}%{_localstatedir}/lib/aide
# Create /etc/aide.d/
mkdir -p -m0700 %{buildroot}%{_sysconfdir}/aide.d
# Install systemd timer and service for scheduled integrity checks
install -Dpm0644 %{SOURCE6} %{buildroot}%{_unitdir}/aide-check.service
install -Dpm0644 %{SOURCE7} %{buildroot}%{_unitdir}/aide-check.timer

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc README.quickstart
%{_sbindir}/aide
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/aide.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/aide
%dir %attr(0700,root,root) %{_sysconfdir}/aide.d
%dir %attr(0700,root,root) %{_localstatedir}/lib/aide
%dir %attr(0700,root,root) %{_localstatedir}/log/aide
%{_unitdir}/aide-check.service
%{_unitdir}/aide-check.timer

%post
%systemd_post aide-check.timer

%preun
%systemd_preun aide-check.timer

%postun
%systemd_postun_with_restart aide-check.timer

%changelog
%autochangelog
