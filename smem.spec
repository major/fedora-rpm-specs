Name:           smem
Version:        1.5
Release:        %autorelease
Summary:        Report application memory usage in a meaningful way

License:        GPLv2+
URL:            http://www.selenic.com/smem/
Source0:        https://selenic.com/repo/smem/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: 	smem-1.5-python3path.patch
BuildRequires:  gcc

%description
smem is a tool that can give numerous reports on memory usage on Linux
systems. Unlike existing tools, smem can report proportional set size (PSS),
which is a more meaningful representation of the amount of memory used by
libraries and applications in a virtual memory system.

Because large portions of physical memory are typically shared among
multiple applications, the standard measure of memory usage known as
resident set size (RSS) will significantly overestimate memory usage. PSS
instead measures each application's "fair share" of each shared area to give
a realistic measure.

%prep
%autosetup -p1

%build
gcc %{build_cflags} %{build_ldflags} -o smemcap smemcap.c

%install
install -Dpm0755 -t %{buildroot}%{_bindir} smem smemcap
install -Dpm0644 -t %{buildroot}%{_mandir}/man8 smem.8

%files
%license COPYING
%{_bindir}/smem
%{_bindir}/smemcap
%{_mandir}/man8/smem.8*

%changelog
%autochangelog
