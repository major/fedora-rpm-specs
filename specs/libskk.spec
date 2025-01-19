Name:		libskk
Version:	1.0.4
Release:	17%{?dist}
Summary:	Library to deal with Japanese kana-to-kanji conversion method

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://github.com/ueno/libskk
Source0:	https://bitbucket.org/libskk/libskk/downloads/%{name}-%{version}.tar.xz
Patch:		libskk-1.0.5-int-conversion.patch
Patch:		libskk-1.0.5-json-escape.patch

BuildRequires:	vala
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	json-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gettext-devel

%description
The libskk project aims to provide GObject-based interface of Japanese
input methods.  Currently it supports SKK (Simple Kana Kanji) with
various typing rules including romaji-to-kana, AZIK, ACT, TUT-Code,
T-Code, and NICOLA.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:	Tools for %{name}
BuildRequires:	libfep-devel
BuildRequires: make
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	tools
The %{name}-tools package contains tools for developing applications
that use %{name}.


%prep
%autosetup -p1
find -name '*.vala' -exec touch {} \;

%build
%configure --disable-static --enable-fep
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}


%ldconfig_scriptlets


%files -f %{name}.lang
%doc README rules/README.rules COPYING
%{_libdir}/*.so.*
%{_datadir}/libskk
%{_libdir}/girepository-1.0/Skk*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Skk*.gir
%{_datadir}/vala/vapi/*

%files tools
%{_bindir}/skk*
%{_libexecdir}/skk*
%{_mandir}/man1/skk*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov  7 2024 Daiki Ueno <dueno@redhat.com> - 1.0.4-16
- Fix invalid escape on json file
- Fix build with GCC 14

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.4-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Daiki Ueno <dueno@redhat.com> - 1.0.4-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec  3 2017 Daiki Ueno <dueno@redhat.com> - 1.0.3-1
- new upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Daiki Ueno <dueno@redhat.com> - 1.0.2-1
- new upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.1-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  1 2013 Daiki Ueno <dueno@redhat.com> - 1.0.1-1
- new upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Daiki Ueno <dueno@redhat.com> - 0.0.13-1
- new upstream release

* Thu Mar 29 2012 Daiki Ueno <dueno@redhat.com> - 0.0.12-1
- new upstream release

* Tue Feb 14 2012 Daiki Ueno <dueno@redhat.com> - 0.0.11-2
- split out skk and skkfep programs into -tools subpackage

* Mon Feb 13 2012 Daiki Ueno <dueno@redhat.com> - 0.0.11-1
- new upstream release
- build with --enable-fep

* Wed Jan 25 2012 Daiki Ueno <dueno@redhat.com> - 0.0.9-1
- new upstream release

* Wed Jan 11 2012 Daiki Ueno <dueno@redhat.com> - 0.0.8-1
- new upstream release

* Fri Jan  6 2012 Daiki Ueno <dueno@redhat.com> - 0.0.7-1
- new upstream release

* Mon Dec 26 2011 Daiki Ueno <dueno@redhat.com> - 0.0.5-1
- new upstream release

* Tue Dec 20 2011 Daiki Ueno <dueno@redhat.com> - 0.0.4-1
- new upstream release
- wrap %%description
- add COPYING and README.rules to %%doc

* Fri Dec 16 2011 Daiki Ueno <dueno@redhat.com> - 0.0.2-1
- initial packaging for Fedora

