Name:           bonnie++
Version:        2.00a
Release:        %autorelease
Summary:        Filesystem and disk benchmark & burn-in suite
License:        GPL-2.0-only
URL:            http://www.coker.com.au/bonnie++/
Source0:        http://www.coker.com.au/bonnie++/experimental/bonnie++-%{version}.tgz
# Modernize Makefile: support LDFLAGS and DESTDIR
Patch0:         %{name}-makefile-modernize.patch
# Fix build warnings (mismatched-dealloc, format-overflow, etc.)
Patch1:         %{name}-2.00a-warnings.patch
# Address security issue: missing-call-to-setgroups-before-setuid
Patch2:         %{name}-2.00a-security.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
bonnie++ filesystem and disk benchmark suite aggressively reads & writes
in various ways on your filesystem then outputs useful benchmark performance
data.  bonnie++ is also useful as a hardware, disk, and filesystem stability
test, exposing some types of hardware or kernel failures that would otherwise
be difficult to detect.

Do not leave bonnie++ installed on a production system.  Use only while you
test servers.

%prep
%autosetup -p1

%build
# CFLAGS needs to be passed to make because Makefile.in doesn't use it from env
%configure --disable-stripping
%make_build CFLAGS="-std=c++14 $RPM_OPT_FLAGS"

%install
%make_install

%files
%license copyright.txt
%doc readme.html credits.txt debian/changelog
%{_mandir}/man1/bon_csv2html.1*
%{_mandir}/man1/bon_csv2txt.1*
%{_mandir}/man1/generate_randfile.1*
%{_mandir}/man8/bonnie++.8*
%{_mandir}/man8/getc_putc.8*
%{_mandir}/man8/zcav.8*
%{_bindir}/bonnie++
%{_bindir}/getc_putc
%{_bindir}/getc_putc_helper
%{_bindir}/zcav
%{_bindir}/bon_csv2html
%{_bindir}/bon_csv2txt
%{_bindir}/generate_randfile


%changelog
%autochangelog
