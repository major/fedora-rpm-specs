%global srcname tac_plus
%global srcversion F4.0.4.28
%global commit 4fdf17890ef777a91b4558ae39adf5ed830050a0
%global date 20231005

%global srcdir %{name}-%{srcversion}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           tacacs
# Upstream declares its version as F4.0.4.28-7fb
Version:        %{srcversion}.7fb~%{date}g%{shortcommit}
Release:        %autorelease
Summary:        Daemon to run AAA via TACACS+ Protocol via IPv4 and IPv6

# tac_plus itself is MIT, do_auth.py is GPLv3
License:        MIT and GPL-3.0-or-later
URL:            https://github.com/facebook/tac_plus
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
Patch:          tacacs-c99.patch

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  sed

BuildRequires:  libxcrypt-devel
BuildRequires:  pam-devel

Recommends:     %{name}-extra = %{version}-%{release}

%description
Tacacs+ (tac_plus) is a C daemon that authenticates requests via the Tacacs+
Protocol and logs accounting information.

This is a fork of Cisco + Shruberry's Tacacs+ daemons
(http://www.shrubbery.net/tac_plus/).

%package        libs
Summary:        Shared librares for %{name}

%description    libs
This package contains shared libraries for %{name}.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}

%description    devel
This package contains development headers and libraries for %{name}.

%package        extra
Summary:        Additional tools and utilities for %{name}
Requires:       %{name} = %{version}-%{release}

%description    extra
This package contains additional tools and utilities for %{name} that pull in
extra dependencies that aren't required for the main package.

%prep
%autosetup -p1 -n %{srcname}-%{commit}

# Fix Python shebang
sed -i 's:#!/usr/bin/python:#!/usr/bin/python3:' %{srcdir}/do_auth.py

%build
pushd %{srcdir}
# Only used for tac_convert shebang
export PERLV_PATH="%{_bindir}/perl"
%configure \
  --enable-acls \
  --enable-uenable \
  --without-libwrap \
  --disable-static
%make_build

%install
pushd %{srcdir}
%make_install

# Install systemd unit
install -Dpm0644 -t %{buildroot}%{_unitdir} %{srcname}.service

# Relocate data files to more appropriate paths
install -Ddpm0755 %{buildroot}%{_docdir}/%{name} %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/users_guide %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/do_auth.py %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/tac_convert %{buildroot}%{_bindir}
chmod +x %{buildroot}%{_libexecdir}/%{name}/do_auth.py %{buildroot}%{_bindir}/tac_convert
rmdir %{buildroot}%{_datadir}/%{name}

%post
%systemd_post %{srcname}.service

%preun
%systemd_preun %{srcname}.service

%postun
%systemd_postun_with_restart %{srcname}.service

%files
%license LICENSE %{srcdir}/COPYING
%doc README.md %{srcdir}/CHANGES %{srcdir}/FAQ
%doc %{_docdir}/%{name}/users_guide
%{_bindir}/tac_pwd
%{_sbindir}/%{srcname}
%{_mandir}/man5/%{srcname}.conf.5*
%{_mandir}/man8/%{srcname}.8*
%{_mandir}/man8/tac_pwd.8*
%{_unitdir}/%{srcname}.service

%files libs
%license LICENSE %{srcdir}/COPYING
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files extra
%license LICENSE %{srcdir}/COPYING
%{_bindir}/tac_convert
%{_libexecdir}/%{name}

%changelog
%autochangelog
