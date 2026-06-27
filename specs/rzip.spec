Name:           rzip
Version:        2.1
Release:        %autorelease
Summary:        A large-file compression program
License:        GPL-2.0-or-later
URL:            http://rzip.samba.org
Source0:        http://rzip.samba.org/ftp/rzip/%{name}-%{version}.tar.gz
Patch0:         rzip-configure.patch
Patch1:         rzip-makefile.patch

BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  make

%description
rzip is a compression program, similar in functionality to gzip or
bzip2, but able to take advantage of long distance redundancies in
files, which can sometimes allow rzip to produce much better
compression ratios than other programs.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install INSTALL_BIN=%{buildroot}%{_bindir} INSTALL_MAN=%{buildroot}%{_mandir}

%check
./testfiles.sh main.c rzip.c

%files
%license COPYING
%{_bindir}/rzip
%{_mandir}/man1/*

%changelog
%autochangelog
