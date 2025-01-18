Name:           d0_blind_id
Version:        1.0
Release:        12%{?dist}
Summary:        Cryptographic library to perform identification

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/divVerent/d0_blind_id
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Patches from https://gitlab.com/xonotic/d0_blind_id
Patch0001:      0001-main.c-missing-va_end-ap.patch
Patch0002:      0002-Fixed-version-info.patch
Patch0003:      0003-Using-modern-secure-function-to-clear-memory-when-av.patch

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gmp-devel

%description
Cryptographic library to perform identification using Schnorr Identification
scheme and Blind RSA.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
autoreconf -vfi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -print -delete

%files
%license COPYING
%{_bindir}/blind_id
%{_libdir}/libd0_blind_id.so.0*
%{_libdir}/libd0_rijndael.so.0*

%files devel
%{_includedir}/d0_blind_id/
%{_libdir}/libd0_blind_id.so
%{_libdir}/libd0_rijndael.so
%{_libdir}/pkgconfig/d0_blind_id.pc
%{_libdir}/pkgconfig/d0_rijndael.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0-1
- Initial package
