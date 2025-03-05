%global commit 546fed9a83b84501d54f471862ded3855b2d579b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: Real-time Game Server Status for FPS game servers
Name: qstat
Version: 2.17
Release: %autorelease
License: Artistic-2.0
URL: https://github.com/multiplay/qstat
Source0: https://github.com/multiplay/qstat/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0: qstat-2.17-c23.patch
BuildRequires: make
BuildRequires: autoconf, automake, libtool

%description
QStat is a command-line program that gathers real-time statistics
from Internet game servers. Most supported games are of the first
person shooter variety (Quake, Half-Life, etc)

%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1 -b .c23
sed -i 's/m4_esyscmd\(.*\),/%{version},/g' configure.ac
autoreconf -ifv

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Rename binary as discussed in https://bugzilla.redhat.com/show_bug.cgi?id=472750
mv %{buildroot}%{_bindir}/qstat %{buildroot}%{_bindir}/quakestat

# prepare for including to documentation
find template -name "Makefile*" -type f | xargs rm -f

%files
%doc CHANGES.txt
%license LICENSE.txt
%doc contrib.cfg info/*.txt qstatdoc.html template/
%config(noreplace) %{_sysconfdir}/qstat.cfg
%{_bindir}/quakestat

%changelog
%autochangelog
