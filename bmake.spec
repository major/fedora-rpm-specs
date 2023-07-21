Summary:       The NetBSD make(1) tool
Name:          bmake
Version:       20230711
Release:       %autorelease
License:       BSD-3-Clause AND BSD-4-Clause-UC AND BSD-2-Clause AND BSD-2-Clause-NetBSD
URL:           https://ftp.netbsd.org/pub/NetBSD/misc/sjg/
Source0:       %{url}/bmake-%{version}.tar.gz
Source1:       %{url}/bmake-%{version}.tar.gz.asc
Source2:       https://www.crufty.net/ftp/pub/sjg/Crufty.pub.asc
Requires:      mk-files

#Patch1:       

BuildRequires: gcc
BuildRequires: sed
BuildRequires: util-linux
# Required by tests
BuildRequires: tcsh ksh
%if 0%{?fedora}
# source verification
BuildRequires: gnupg2
%endif

%description
bmake, the NetBSD make tool, is a program designed to simplify the
maintenance of other programs.  The input of bmake is a list of specifications
indicating the files upon which the targets (programs and other files) depend.
bmake then detects which targets are out of date based on their dependencies
and triggers the necessary commands to bring them up to date when that happens.

bmake is similar to GNU make, even though the syntax for the advanced features
supported in Makefiles is very different.

%package -n mk-files
Summary:   Support files for bmake, the NetBSD make(1) tool
BuildArch: noarch

%description -n mk-files
The mk-files package provides some bmake macros derived from the NetBSD
bsd.*.mk macros.  These macros allow the creation of simple Makefiles to
build all kinds of targets, including, for example, C/C++ programs and/or
shared libraries.

%prep
%if 0%{?fedora}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -n %{name} -p1
sed -i.python -e '1 s|^#!/usr/bin/env python|#!/usr/bin/python3|' mk/meta2deps.py

%build
%configure --with-default-sys-path=%{_datadir}/mk
sh ./make-bootstrap.sh

%install
./bmake -m mk install DESTDIR="%{buildroot}" INSTALL='install -p' STRIP_FLAG=''
chmod a-x %{buildroot}%{_datadir}/mk/mkopt.sh

%files
%doc ChangeLog README
%license LICENSE
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*

%files -n mk-files
%license LICENSE
%doc mk/README
%{_datadir}/mk

%changelog
%autochangelog
