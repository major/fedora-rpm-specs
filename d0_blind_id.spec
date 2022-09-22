Name:           d0_blind_id
Version:        1.0
Release:        5%{?dist}
Summary:        Cryptographic library to perform identification

License:        BSD
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
