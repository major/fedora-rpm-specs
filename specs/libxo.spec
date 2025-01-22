Name:           libxo
Version:        1.6.0
Release:        9%{?dist}
Summary:        A Library for Generating Text, XML, JSON, and HTML Output


# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/Juniper/libxo
Source0:        https://github.com/Juniper/libxo/releases/download/%{version}/libxo-%{version}.tar.gz

# Remove include line for header file not present in glibc
Patch0:         libxo-1.6.0-sysctl.patch

BuildRequires:  make
BuildRequires:  gcc

%description
The libxo library allows an application to generate text, XML, JSON, and HTML 
output using a common set of function calls. The application decides at run 
time which output style should be produced. The application calls a function
"xo_emit" to product output that is described in a format string.
A "field descriptor" tells libxo what the field is and what it means.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build


%install
#remove .la files
%make_install
find %{buildroot} -type f -name "*.la" | xargs rm -f
rm -f %{buildroot}%{_docdir}/libxo/Copyright

%{?ldconfig_scriptlets}


%files
%license Copyright
%doc README.md INSTALL.md
%{_libdir}/libxo.so.0*
%{_bindir}/libxo-config
%{_bindir}/xo
%{_bindir}/xohtml
%{_bindir}/xolint
%{_bindir}/xopo
%dir %{_libdir}/libxo
%dir %{_libdir}/libxo/encoder
%{_libdir}/libxo/encoder/*.enc
%{_libdir}/libxo/encoder/libenc*.so.0*
%{_datadir}/libxo
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*

%files devel
%{_includedir}/*
%{_libdir}/libxo.so
%{_mandir}/man3/*.3*
%{_libdir}/pkgconfig/libxo.pc
%{_libdir}/libxo/encoder/libenc*.so

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 2 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Aug 11 2021 Kanitha Chim <kchim@redhat.com> - 1.6.0-1
- Initial package
