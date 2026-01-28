%global make_vars COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="%{?__global_ldflags}"

Name:           libnsgif
Version:        0.1.2
Release:        2%{?dist}
Summary:        Decoding library for the GIF image file format
License:        MIT
URL:            http://www.netsurf-browser.org/projects/libnsgif/
Source0:        http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
BuildRequires:  netsurf-buildsystem

%description
Libnsgif is a decoding library for the GIF image file format written in C.
It was developed as part of the NetSurf project.

Features:
* Decodes GIF files
* Example usage demonstration

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

sed -i -e s@-Werror@@ Makefile

chmod -x examples/*

%build
%make_build %{make_vars} %{build_vars}

%install
%make_install %{make_vars}

%check
make test %{make_vars} %{build_vars}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%doc examples/
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 Christopher Meng <rpm@cicku.me> - 0.1.2-1
- Update to 0.1.2
- Include examples in devel package.

* Thu May 01 2014 Christopher Meng <rpm@cicku.me> - 0.1.1-1
- Initial Package.
