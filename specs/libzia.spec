Name:		libzia
Version:	4.64
Release:	2%{?dist}
Summary:	Platform abstraction layer for the tucnak package
License:	GPL-2.0-only
URL:		http://tucnak.nagano.cz/
Source:		http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	SDL2-devel
BuildRequires:	libpng-devel
BuildRequires:	libftdi-devel
BuildRequires:	binutils-devel
BuildRequires:	gnutls-devel
BuildRequires:	gtk3-devel
# Used for direct control of display power saving features (via exec)
Requires:	xset
# This is to fulfill Fedora requirement - it marks the interface with
# version number 0. Upstream uses --release versioning in libtool.
# They do not support linking between different versions of tucnak and
# libzia, i.e. tucnak-4.18 needs to be linked to libzia-4.18.
Patch0:		libzia-4.26-soname-fix.patch

%description
Platform abstraction layer for the tucnak package.

%package devel
Summary:	Development files for libzia
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	SDL2-devel
Requires:	gtk2-devel
Requires:	libftdi-devel
Requires:	pkgconf-pkg-config

%description devel
Development files for libzia

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install

# drop .la
rm -f %{buildroot}%{_libdir}/libzia.la

# drop unneeded files
rm -f %{buildroot}%{_datadir}/libzia/doc/*
rm -f %{buildroot}%{_datadir}/libzia/settings
rm -f %{buildroot}%{_prefix}/lib/libzia/*
rmdir %{buildroot}%{_datadir}/libzia/doc/ %{buildroot}%{_datadir}/libzia %{buildroot}%{_prefix}/lib/libzia

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libzia-%{version}.so.0*

%files devel
%{_bindir}/zia-config
%{_includedir}/libzia
%{_libdir}/libzia.so
%{_libdir}/pkgconfig/libzia.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 17 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.64-1
- New version
  Related: rhbz#2319324

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.61-1
- New version
  Related: rhbz#2295685

* Thu Jun 20 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.60-1
- New version
  Related: rhbz#2292994

* Thu Apr 11 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.59-1
- New version
  Related: rhbz#2274467

* Tue Mar  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.58-1
- New version
  Related: rhbz#2267216

* Tue Feb 27 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.56-1
- New version
  Related: rhbz#2266261

* Wed Jan 24 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.55-1
- New version
  Related: rhbz#2259794

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.54-1
- New version
  Related: rhbz#2256914

* Tue Jan  2 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.53-1
- New version
  Related: rhbz#2254900

* Tue Nov 21 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.52-1
- New version
  Related: rhbz#2250444

* Tue Oct 31 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.49-1
- New version
  Related: rhbz#2247143

* Mon Oct 16 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.48-1
- New version
  Related: rhbz#2244314
- Converted license to SPDX

* Tue Oct 10 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.47-1
- New version
  Related: rhbz#2242200

* Mon Sep 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.46-1
- New version
  Related: rhbz#2238100

* Fri Sep  1 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.45-1
- New version
  Related: rhbz#2234925

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun  5 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.44-1
- New version
  Related: rhbz#2212154

* Wed Apr 26 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.43-1
- New version
  Related: rhbz#2186987

* Tue Mar 28 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.42-2
- Added missing xset requirement (reported by David Jež <djez@redhat.com>)

* Mon Mar 13 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.42-1
- New version
  Related: rhbz#2177170

* Tue Mar  7 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.41-1
- New version
  Related: rhbz#2175029

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.40-1
- New version
  Related: rhbz#2159136

* Tue Dec 13 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.39-1
- New version
  Related: rhbz#2152850

* Thu Dec  1 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.38-1
- New version
  Related: rhbz#2148552

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.37-1
- New version
  Related: rhbz#2128090

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 27 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.36-4
- Dropped bfd from the pkgconfig requirement
  Resolves: rhbz#2086525

* Mon May 16 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.36-3
- Rebuilt for bfd changes
  Resolves: rhbz#2084314

* Mon May  9 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.36-2
- Fixed crash with some network interfaces (e.g. tun)
- Enabled gtk3, bfd, and gnutls support

* Tue May  3 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.36-1
- New version
  Related: rhbz#2080501

* Tue Apr 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.35-1
- New version
  Related: rhbz#2074482

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan  6 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.34-2
- Switched to SDL2

* Thu Dec 23 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.34-1
- New version
  Related: rhbz#2033563

* Tue Oct  5 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.32-1
- New version
  Related: rhbz#2009257

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.30-1
- New version
  Related: rhbz#1977455

* Mon May 24 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.29-1
- New version
  Related: rhbz#1963426

* Wed Apr 21 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.28-1
- New version
  Related: rhbz#1952087

* Wed Apr 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.27-1
- New version
  Related: rhbz#1949451

* Fri Apr  2 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.26-1
- New version

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.24-1
- New version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.20-1
- New version

* Tue Jan 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.19-1
- New version
- Added missing requirements
- Dropped configure-fix, fsf-address-fix patch (both upstreamed)

* Wed Jan  8 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18-3
- More fixes according to review

* Tue Jan  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18-2
- Fixed according to review

* Fri Jan  3 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18-1
- Initial version
