Name:           libchrony
Version:        0.2
Release:        1%{?dist}
Summary:        Library for monitoring chronyd

License:        LGPL-2.1-or-later
URL:            https://gitlab.com/chrony/libchrony
Source0:        https://gitlab.com/chrony/libchrony/-/archive/%{version}/libchrony-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
libchrony is a C library for monitoring chronyd. It communicates with
chronyd directly over Unix domain or UDP socket, not relying on chronyc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
%make_install libdir=%{_libdir} includedir=%{_includedir}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%{?ldconfig_scriptlets}

%files
%license COPYING
%doc README.adoc
%{_libdir}/libchrony.so.0*

%files devel
%{_includedir}/*
%{_libdir}/libchrony.so
%{_libdir}/pkgconfig/libchrony.pc

%changelog
* Wed Sep 10 2025 Miroslav Lichvar <mlichvar@redhat.com> 0.2-1
- update to 0.2

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Feb 26 2025 Miroslav Lichvar <mlichvar@redhat.com> 0.1-1
- initial release
