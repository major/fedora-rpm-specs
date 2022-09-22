Summary:   General-purpose stream-handling tool
Name:      cstream
Version:   3.2.1
Release:   %autorelease

License:   MIT
URL:       http://www.cons.org/cracauer/cstream.html
Source:    http://www.cons.org/cracauer/download/%{name}-%{version}.tar.gz
Patch2:    %{name}-%{version}-Wextra.patch
Patch3:    %{name}-%{version}-double-assignment.patch
Patch5:    %{name}-%{version}-meh.patch
Patch6:    %{name}-%{version}-Werror=tautological-compare.patch



BuildRequires:  gcc
BuildRequires: make
%description
cstream filters data streams, much like the UNIX tool dd(1).

It has a more traditional commandline syntax, support for precise
bandwidth limiting and reporting and support for FIFOs.

Data limits and throughput rate calculation will work for files > 4 GB.


%prep
%setup -q
%patch2 -p1 -b .Wextra
%patch3 -p1 -b .double-assignment
%patch5 -p1 -b .meh
%patch6 -p1 -b .Werror=autological-compare


%build
%{configure} INSTALL="%{__install} -p"
%make_build CFLAGS="%{optflags} -Wall -Wextra -Wno-unused-parameter -Werror"


%install
%make_install


%check
%{__make} %{?_smp_mflags} check installcheck DESTDIR="%{buildroot}"


%files
%doc CHANGES COPYRIGHT README TODO
%doc %{_mandir}/man1/cstream.1*
%{_bindir}/cstream


%changelog
%autochangelog
