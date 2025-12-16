%global forgeurl https://github.com/Snaipe/BoxFort
Version:        0.1.5
%forgemeta

Name:           boxfort
Release:        %autorelease
Summary:        Convenient & cross-platform sandboxing C library
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

# https://github.com/Snaipe/BoxFort/blob/master/meson.build#L81-L93
# ppc64le and s390x are not supported
ExcludeArch:    ppc64le s390x

BuildRequires:  gcc
BuildRequires:  meson

%description
BoxFort is a simple, cross-platform sandboxing C library powering Criterion.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%meson -Ddefault_library=shared
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libboxfort.so.0*

%files devel
%{_includedir}/boxfort.h
%{_libdir}/libboxfort.so
%{_libdir}/pkgconfig/boxfort.pc

%changelog
%autochangelog
