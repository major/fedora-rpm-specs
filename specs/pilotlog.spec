Name:           pilotlog
Version:        11
Release:        1%{?dist}
Summary:        A pilot logbook for logging flight time

License:        AGPL-3.0-or-later
URL:            https://pilotlog.sourceforge.net
Source0:        https://download.stansoft.org/files/%{name}-%{version}.tar.bz2

# Only build on the required primary architectures.
# https://fedoraproject.org/wiki/Architectures#Structure
ExclusiveArch:  x86_64 aarch64

BuildRequires:  aubit4gl-devel
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server

Requires:       aubit4gl
Requires:       libpq
Requires:       postgresql-server
 

%description
Pilot Log is a pilot logbook for logging flight time and calculating
aircraft weight & balance.


%prep
%autosetup


%build
%if "%{getenv:AUBITDIR}" == ""
export AUBITDIR=%{_libdir}/aubit4gl
%endif

%configure
# The database must exist to compile so create it
%make_build createdb
# It does not compile with multiple threads
%make_build -j1


%install
rm -rf %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%make_install

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
# Create a link to the startup script since it references the install dir
ln -sf ../..%{_libdir}/%{name}/pl %{buildroot}%{_bindir}/%{name}

# docs are installed in the system location
rm -f %{buildroot}%{_libdir}/%{name}/README
rm -f %{buildroot}%{_libdir}/%{name}/changelog
rm -f %{buildroot}%{_libdir}/%{name}/COPYING


%check
make check


%files
%license COPYING 
%doc README
%doc changelog
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/bin
%{_libdir}/%{name}/bin/*
%dir %{_libdir}/%{name}/etc
%{_libdir}/%{name}/etc/*
%{_libdir}/%{name}/installpl
%dir %{_libdir}/%{name}/newdb
%{_libdir}/%{name}/newdb/schema.sql
%{_libdir}/%{name}/pl
%{_libdir}/%{name}/updatepl
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Nov 13 2025 Chad Lemmen <rpm@stansoft.org> - 11-1
- initial Fedora RPM packaging

