Name:           mbuffer
Version:        20260511
Release:        %autorelease
Summary:        Measuring Buffer is an enhanced version of buffer
License:        GPL-3.0-or-later
URL:            https://www.maier-komor.de/mbuffer.html
Source:         https://www.maier-komor.de/software/mbuffer/mbuffer-%{version}.tgz
Patch:          0001-fix-x86-configure.patch
ExcludeArch:    %{ix86}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mhash-devel
BuildRequires:  mt-st
BuildRequires:  openssl
BuildRequires:  openssl-devel

%description
Measuring Buffer is an enhanced version of buffer. It features display of
throughput, memory-mapped file I/O for huge buffers, and multithreading.

%prep
%autosetup

%build
#autoconf
# suppress detection of MD5_Init functions if openssl-devel
# is available on build system, let only mhash_init be
# detected if the md5 hash feature is enabled
autoreconf -vfi
export ac_cv_search_MD5_Init=no
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}/usr/etc/mbuffer.rc

# tests disabled for now due memory error
# mbuffer: fatal: Cannot address so much memory (17179869184*1023)
# check
# make_build check

%files
%doc AUTHORS ChangeLog NEWS README
%license LICENSE
%{_mandir}/man1/mbuffer.1*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/mbuffer.rc

%changelog
%autochangelog
