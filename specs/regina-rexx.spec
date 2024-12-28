# Regina does not support parallel builds
%global _smp_build_ncpus 1

Name:           regina-rexx
Version:        3.9.6
Release:        %autorelease
Summary:        Regina Rexx Interpreter

# regina-rexx itself is LGPL-2.0-only, but the larger body of libraries and
# scripts is under various licenses
License:        LGPL-2.0-only and LGPL-2.0-or-later and LGPL-2.1-or-later and MPL-1.0 and GPL-2.0-or-later and BSD-4-Clause and Unlicense
URL:            https://regina-rexx.sourceforge.io
Source:         https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  systemd-devel
BuildRequires:  sed

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Regina is a Rexx interpreter that has been ported to most Unix platforms and
operating systems. Rexx is a programming language that was designed to be easy
to use for inexperienced programmers yet powerful enough for experienced users.
It is also a language ideally suited as a macro language for other applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs
The %{name}-libs package contains shared libraries for %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains additional documentation for %{name}.

%prep
%autosetup -p1
# Do not strip on install
sed -i Makefile.in -e 's:$(INSTALL) -s:$(INSTALL):g'
# Fix permissions
chmod -x BUGS
# Fix encoding
iconv -f iso8859-1 -t utf-8 README.38 > README.38.conv && mv -f README.38.conv README.38
# Fix scripts shebangs
sed -i 's:/usr/bin/env regina:/usr/bin/regina:' demo/*.rexx regutil/*.rexx

%build
%configure
%make_build

%install
# make install will fail if these don't exist
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_libdir}/%{name}/%{version}

%make_install

# Install systemd service
install -Dpm0644 -t %{buildroot}%{_unitdir} rxstack.service

# Get rid of some cruft
rm %{buildroot}%{_libdir}/libregina.a

# Install examples
mv %{buildroot}%{_datadir}/%{name}/examples .

# Replace duplicate manpage with symlink
ln -sf regina.1.gz %{buildroot}%{_mandir}/man1/rexx.1.gz

%post
%systemd_post rxstack.service

%preun
%systemd_preun rxstack.service

%postun
%systemd_postun_with_restart rxstack.service

%files
%license COPYING-LIB
%doc README.* BUGS TODO HACKERS.txt
%{_bindir}/*
%exclude %{_bindir}/regina-config
%{_mandir}/man1/*
%exclude %{_mandir}/man1/regina-config.1*
%config(noreplace) %{_sysconfdir}/rxstack.conf
%dir %{_systemd_util_dir}
%dir %{_unitdir}
%{_unitdir}/rxstack.service

%files libs
%license COPYING-LIB
%{_libdir}/libregina.so.3*
%{_libdir}/%{name}
%{_datadir}/%{name}

%files devel
%license COPYING-LIB
%{_bindir}/regina-config
%{_includedir}/*
%{_libdir}/libregina.so
%{_libdir}/pkgconfig/libregina.pc
%{_mandir}/man1/regina-config.1*

%files doc
%license COPYING-LIB
%doc doc examples

%changelog
%autochangelog
