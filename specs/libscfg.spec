%global abi_ver 2

Name:           libscfg
Version:        0.2.0
Release:        %autorelease
Summary:        C library for a simple configuration file format

License:        MIT
URL:            https://codeberg.org/emersion/libscfg
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license LICENSE
%doc README.md
%{_libdir}/libscfg.so.%{abi_ver}
%{_libdir}/libscfg.so.%{version}

%files devel
%{_includedir}/scfg.h
%{_libdir}/libscfg.so
%{_libdir}/pkgconfig/scfg.pc


%changelog
%autochangelog
