Name: kstart
Version: 4.3
Release: %autorelease
Summary: Daemon version of kinit for Kerberos v5
License: MIT
URL: http://www.eyrie.org/~eagle/software/kstart/
Source0: http://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
# Add krenew systemd user and system units
Patch0: https://github.com/rra/kstart/pull/13.patch
# For Patch0
BuildRequires: automake
BuildRequires: gcc
BuildRequires: krb5-devel
BuildRequires: make
BuildRequires: pkgconfig(systemd)
BuildRequires: systemd-rpm-macros
# For tests
BuildRequires: fakeroot
BuildRequires: perl
ExcludeArch: %{ix86}

%description
k5start is a modified version of kinit which can use keytabs to authenticate, 
can run as a daemon and wake up periodically to refresh a ticket, and can run 
single commands with its own authentication credentials and refresh those 
credentials until the command exits. 

%prep
%setup -q
%patch -P0 -p1

%build
# For Patch0
./bootstrap
%configure --enable-setpag --enable-reduced-depends --with-aklog=%{_bindir}/aklog

%make_build

%install
%make_install

%files
%license LICENSE
%doc NEWS README
%{_bindir}/k5start
%{_bindir}/krenew
%{_unitdir}/k5start@.service
%{_userunitdir}/krenew.service
%{_mandir}/man1/k5start.1.gz
%{_mandir}/man1/krenew.1.gz

%check
make check

%post
%systemd_post k5start@\*.service
%systemd_user_post krenew.service

%preun
%systemd_preun k5start@\*.service
%systemd_user_preun krenew.service

%changelog
%autochangelog
