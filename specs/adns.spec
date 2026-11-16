Name:		adns
Version:	1.7.0
Release:	%autorelease
Summary:	Advanced, easy to use, asynchronous-capable DNS client library
License:	GPL-3.0-or-later
URL:		https://www.chiark.greenend.org.uk/~ian/adns/
Source0:	https://www.chiark.greenend.org.uk/~ian/adns/ftp/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	m4

%description
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
 - It is reasonably easy to use for simple programs which just want to
   translate names to addresses, look up MX records, etc.
 - It can be used in an asynchronous, non-blocking, manner. Many
   queries can be handled simultaneously.
 - Responses are decoded automatically into a natural representation
   for a C program - there is no need to deal with DNS packet formats.
 - Sanity checking (eg, name syntax checking, reverse/forward
   correspondence, CNAME pointing to CNAME) is performed automatically.
 - Time-to-live, CNAME and other similar information is returned in an
   easy-to-use form, without getting in the way.
 - There is no global state in the library; resolver state is an opaque
   data structure which the client creates explicitly. A program can have
   several instances of the resolver.
 - Errors are reported to the application in a way that distinguishes
   the various causes of failure properly.
 - Understands conventional resolv.conf, but this can overridden by
   environment variables.
 - Flexibility. For example, the application can tell adns to: ignore
   environment variables (for setuid programs), disable sanity checks eg
   to return arbitrary data, override or ignore resolv.conf in favour of
   supplied configuration, etc.
 - Believed to be correct ! For example, will correctly back off to TCP
   in case of long replies or queries, or to other nameservers if several
   are available. It has sensible handling of bad responses etc.

%package devel
Summary:	Asynchronous-capable DNS client library - development files

%description devel
Asynchronous-capable DNS client library - development files.

%package progs
Summary:	Asynchronous-capable DNS client library - utility programs

%description progs
DNS utility programs: adns also comes with a number of utility
programs for use from the command line and in scripts:
 - adnslogres is a much faster version of Apache's logresolv program,
 - adnsresfilter is a filter which copies its input to its output,
   replacing IP addresses by the corresponding names, without unduly
   delaying the output. For example, you can usefully pipe the output of
   netstat -n, tcpdump -ln, and the like, into it.
 - adnshost is a general-purpose DNS lookup utility which can be used
   easily in from the command line and from shell scripts to do simple
   lookups. In a more advanced mode it can be used as a general-purpose
   DNS helper program for scripting languages which can invoke and
   communicate with subprocesses.

%prep
%autosetup

%build
%set_build_flags
%configure --enable-dynamic
%make_build

%install
make \
    prefix=%{buildroot}%{_prefix} \
    bindir=%{buildroot}%{_bindir} \
    includedir=%{buildroot}%{_includedir} \
    libdir=%{buildroot}%{_libdir} \
    install

rm -f %{buildroot}%{_libdir}/libadns.a

%ldconfig_scriptlets

%check
%make_build check

%files
%license COPYING
%doc GPL-vs-LGPL NEWS README README.html TODO changelog
%{_libdir}/libadns.so.1*

%files devel
%{_includedir}/adns.h
%{_libdir}/libadns.so

%files progs
%{_bindir}/adnshost
%{_bindir}/adnslogres
%{_bindir}/adnsresfilter
%{_bindir}/adnsheloex

%changelog
%autochangelog
