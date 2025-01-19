%{?mingw_package_header}

%global pkgname djvulibre

Name:          mingw-%{pkgname}
Version:       3.5.28
Release:       11%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       GPL-2.0-or-later
URL:           http://djvu.sourceforge.net/
Source0:       http://downloads.sourceforge.net/djvu/%{pkgname}-%{version}.tar.gz
# Downstream fix for CVE-2021-32490
# See https://bugzilla.redhat.com/show_bug.cgi?id=1943408
Patch100:      CVE-2021-32490.patch
# Downstream fix for CVE-2021-32491
# See https://bugzilla.redhat.com/show_bug.cgi?id=1943409
Patch101:      CVE-2021-32491.patch
# Downstream fix for CVE-2021-32492
# See https://bugzilla.redhat.com/show_bug.cgi?id=1943410
Patch102:      CVE-2021-32492.patch
# Downstream fix for CVE-2021-32493
# See https://bugzilla.redhat.com/show_bug.cgi?id=1943424
Patch103:      CVE-2021-32493.patch
# Downstream fix for CVE-2021-3500
# See https://bugzilla.redhat.com/show_bug.cgi?id=1943411
Patch104:      CVE-2021-3500.patch


BuildRequires: automake autoconf libtool make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libjpeg-turbo

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libjpeg-turbo

%description
%{summary}.


%package -n mingw32-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the  MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
%{summary}.


%package -n mingw64-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the  MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%mingw_configure
# Parallel build is broken
%mingw_make


%install
%{mingw_make} install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Remove shell scripts
rm -f %{buildroot}%{mingw32_bindir}/{any2djvu,djvudigital}
rm -f %{buildroot}%{mingw64_bindir}/{any2djvu,djvudigital}

# Remove data
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libdjvulibre-21.dll
%{mingw32_includedir}/libdjvu/
%{mingw32_libdir}/libdjvulibre.dll.a
%{mingw32_libdir}/pkgconfig/ddjvuapi.pc

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libdjvulibre-21.dll
%{mingw64_includedir}/libdjvu/
%{mingw64_libdir}/libdjvulibre.dll.a
%{mingw64_libdir}/pkgconfig/ddjvuapi.pc

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.5.28-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Sandro Mani <manisandro@gmail.com> - 3.5.28-1
- Update to 3.5.28

* Wed May 26 2021 Sandro Mani <manisandro@gmail.com> - 3.5.27-12
- Apply fix for CVE-2021-3500

* Tue May 25 2021 Sandro Mani <manisandro@gmail.com> - 3.5.27-11
- Apply fix for CVE-2021-32490, CVE-2021-32491, CVE-2021-32492, CVE-2021-32493

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 3.5.27-7
- Backport fix for CVE-2019-15142
- Backport fix for CVE-2019-15143
- Backport fix for CVE-2019-15144
- Backport fix for CVE-2019-15145
- Backport fix for CVE-2019-18804

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.5.27-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 3.5.27-1
- Initial package
