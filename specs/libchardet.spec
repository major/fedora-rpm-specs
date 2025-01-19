Name:           libchardet
Version:        1.0.5
Release:        21%{?dist}
Summary:        Mozilla's universal character set detector
# Automatically converted from old format: MPLv1.1 or LGPLv2+ or GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MPLv1.1 OR LicenseRef-Callaway-LGPLv2+ OR GPL-2.0-or-later
URL:            http://ftp.oops.org/pub/oops/libchardet/
Source0:        https://github.com/Joungkyun/libchardet/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.0.4-pc.in.patch

BuildRequires:  libstdc++-devel
BuildRequires:  glibc-common
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  sed
BuildRequires:  perl-interpreter

%description
libchardet provides an interface to Mozilla's universal charset detector,
which detects the charset used to encode data.

%package devel
Summary:        Header and object files for development using libchardet
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libchardet-devel package contains the header and object files necessary
for developing programs which use the libchardet libraries.

%prep
%setup -q
%patch -P0 -p1

# Fix rpmlint file-not-utf8
pushd man/en
for i in detect_init.3 detect_obj_free.3 detect_obj_init.3 detect_reset.3 ; do
  iconv --from=ISO-8859-1 --to=UTF-8 $i > $i.conv
  mv $i.conv $i
done
popd

%build
%configure --disable-static --enable-shared

%make_build

%install
%make_install

%find_lang %{name}-devel --with-man --all-name

# remove all '*.la' files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# remove LICENSE file from %%_docdir
rm -rf %{buildroot}%{_datadir}/doc/%{name}/LICENSE

%ldconfig_scriptlets

%files
%doc Changelog README.md
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel -f %{name}-devel.lang
%{_bindir}/chardet-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/chardet.pc
%{_includedir}/chardet/*.h
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.5-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 14 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5
- Dropped %%{name}-1.0.4-man.patch

* Wed May 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-5
- Rebuilt

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-3
- renamed %%version macro for patches
- added BR glibc-common
- added BR coreutils
- added BR make
- added BR findutils
- added BR gcc
- added BR gcc-c++
- added BR sed
- added BR perl
- moved Korean manual pages to devel sub-package

* Thu Dec 10 2015 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-2
- fixed url address
- fixed license tag
- removed %%path_man_en macro, used %%pushd %%popd instead
- added README to using %%doc macro.
- corrected libchardet-1.0.4-man.patch
- renamed libchardet-man.patch to libchardet-1.0.4-man.patch
- renamed summary descripton
- removed LICENSE file from %%_docdir
- added patch to remove hardcodes CFLAGS from chardet.pc.in

* Tue Dec 08 2015 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-1
- initial build

