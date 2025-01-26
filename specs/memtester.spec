%define _legacy_common_support 1
Name:		memtester
Version:	4.7.1
Release:	%autorelease
Summary:	Utility to test for faulty memory subsystem

License:	GPL-2.0-only
URL:		http://pyropus.ca/software/memtester/
Source0:	http://pyropus.ca/software/memtester/old-versions/%{name}-%{version}.tar.gz
Patch0:		memtester-4.0.8-debuginfo.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	dos2unix

%description
memtester is a utility for testing the memory subsystem in a computer to
determine if it is faulty.

%prep
%setup -q
%patch -P0 -p1 -b .debuginfo

%build
make %{?_smp_mflags} -e OPT="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
mv README README.iso88591
iconv -o README -f iso88591 -t utf8 README.iso88591
touch -r README.iso88591 README
rm -f README.iso88591
dos2unix -k BUGS
make -e INSTALLPATH=$RPM_BUILD_ROOT%{_prefix} install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
#fix location of manual
mv $RPM_BUILD_ROOT%{_prefix}/man/man8/memtester.8.gz $RPM_BUILD_ROOT%{_mandir}/man8

%files
%license COPYING
%doc BUGS CHANGELOG README README.tests
%{_bindir}/memtester
%{_mandir}/man8/memtester.8.gz

%changelog
%autochangelog
