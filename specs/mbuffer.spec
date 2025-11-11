Name:           mbuffer
Version:        20251025
Release:        %autorelease
Summary:        Measuring Buffer is an enhanced version of buffer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.maier-komor.de/mbuffer.html
Source0:        http://www.maier-komor.de/software/mbuffer/mbuffer-%{version}.tgz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mt-st
BuildRequires:  mhash-devel
BuildRequires:  autoconf
BuildRequires:  automake

%description
Measuring Buffer is an enhanced version of buffer. It features displayof
throughput, memory-mapped file I/O for huge buffers, and multithreading.

%prep
%autosetup

%build
#autoconf
# suppress detection of MD5_Init functions if openssl-devel
# is available on build system, let only mhash_init be
# detected if the md5 hash feature is enabled
export ac_cv_search_MD5_Init=no
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}/usr/etc/mbuffer.rc

%files
%doc AUTHORS ChangeLog NEWS README
%license LICENSE
%{_mandir}/man1/mbuffer.1*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/mbuffer.rc

%changelog
%autochangelog
