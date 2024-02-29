Name:           dbus-test-runner
Version:        19.04.0
Release:        %autorelease
Summary:        Utility to run executables under a new DBus session for testing

License:        GPL-3.0-only
URL:            https://launchpad.net/%{name}
Source0:        https://launchpad.net/%{name}/19.04/19.04.0/+download/%{name}-19.04.0.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  intltool
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       dbus-daemon

%description
dbus-test-runner is a simple little executable for running a couple of
programs under a new DBus session.

Use this DBus tool for unit testing of code that accesses DBus at runtime.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup

%build
%configure --enable-static=no
%make_build

%install
%make_install

# Create man page
mkdir -p %{buildroot}%{_mandir}/man1/
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man --no-info \
    --version-string='%{version}' --help-option='--help-all' \
    -o %{buildroot}%{_mandir}/man1/%{name}-%{version}.1 \
    %{buildroot}%{_bindir}/%{name}

# Remove libtool archives
find %{buildroot} -name "*.la" -delete

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_libdir}/libdbustest.so.1
%{_libdir}/libdbustest.so.1.0.0
%{_libexecdir}/%{name}/
%{_mandir}/man1/%{name}-%{version}.1*

%files devel
%dir %{_includedir}/libdbustest-1/
%{_includedir}/libdbustest-1/libdbustest/
%{_libdir}/libdbustest.so
%{_libdir}/pkgconfig/dbustest-1.pc


%changelog
%autochangelog
