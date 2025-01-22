Name:           libtins
Version:        4.5
Release:        6%{?dist}
Summary:        A high-level, multiplatform C++ network packet sniffing and crafting library

License:        BSD
URL:            https://github.com/mfontanini/libtins
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  boost-devel
BuildRequires:  doxygen

%description
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Document files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
The %{name}-docs package contains document files for
developing applications that use %{name}.

%prep
%autosetup -p1
# Fix GCC 13 build
# https://github.com/mfontanini/libtins/pull/496
sed -i 's|stdint.h|cstdint|' include/tins/ip_address.h

%build
%cmake -DLIBTINS_BUILD_TESTS=OFF -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
%cmake_build --target docs

%install
%cmake_install


%files
%license LICENSE
%doc CHANGES.md CONTRIBUTING.md README.md THANKS
%{_libdir}/%{name}.so.4.5

%files devel
%{_includedir}/tins
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%files doc
%doc %{__cmake_builddir}/docs


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 31 2023 Vasiliy Glazov <vascom2@gmail.com> - 4.5-1
- Update to 4.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 01 2022 Vasiliy Glazov <vascom2@gmail.com> - 4.4-1
- Initial packaging for Fedora
