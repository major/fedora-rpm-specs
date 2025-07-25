Summary: Internationalized Domain Name support library
Name: libidn1.34
Version: 1.34
Release: 19%{?dist}
URL: http://www.gnu.org/software/libidn/
# Automatically converted from old format: LGPLv2+ and GPLv3+ and GFDL - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+ AND GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
Source0: http://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
# Allow disabling Emacs support
Patch0: libidn-1.33-Allow-disabling-Emacs-support.patch
# Fix ABI compatibility with libidn-1.33 and earlier
Patch1: libidn-tablesize-revert.patch
Patch2: libidn1.34-configure-c99.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: gettext gettext-devel
BuildRequires: gtk-doc
BuildRequires: make
BuildRequires: pkgconfig
# gnulib is a copylib, bundling is allowed
Provides: bundled(gnulib)

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%prep
%setup -q -n libidn-%{version}
%patch -P0 -p1
%patch -P1 -p1 -b .tablesize-revert
%patch -P2 -p1
autoreconf -vif
# Prevent from regenerating sources by gengetopt because it's broken.
touch src/idn_cmd.c src/idn_cmd.h

# Cleanup
find . -name '*.jar' -print -delete
find . -name '*.class' -print -delete

%build
%configure --disable-csharp --disable-static \
    --disable-doc \
    --disable-emacs \
    --disable-java

# remove RPATH hardcoding
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%check
# without RPATH this needs to be set to test the compiled library
export LD_LIBRARY_PATH=$(pwd)/lib/.libs
make %{?_smp_mflags} -C tests check VALGRIND=env

%install
make install DESTDIR=$RPM_BUILD_ROOT pkgconfigdir=%{_libdir}/pkgconfig \
    ;

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la \
      $RPM_BUILD_ROOT%{_libdir}/libidn.so \
      $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libidn.pc \
      $RPM_BUILD_ROOT%{_bindir}/idn \
      $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/libidn.mo \
      $RPM_BUILD_ROOT%{_includedir}/*.h \

%files
%license COPYING*
%doc AUTHORS NEWS FAQ README THANKS
%{_libdir}/libidn.so.11*

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.34-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 01 2023 Arjun Shankar <arjun@redhat.com> - 1.34-12
- Port configure script to C99 (#2166272)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 14 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.34-7
- add missing build dependency on gtk-doc (fixes rhbz#1943098)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.34-1
- compat library for F29+
