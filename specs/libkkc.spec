%global dataversion 1:0.2.7

Name:		libkkc
Version:	0.3.5
Release:	31%{?dist}
Summary:	Japanese Kana Kanji conversion library

License:	GPL-3.0-or-later
URL:		https://github.com/ueno/libkkc
Source0:	https://github.com/ueno/libkkc/releases/download/v%{version}/%{name}-%{version}.tar.gz
# remove for next release:
Source1:        README.md
Patch0:		libkkc-HEAD.patch
Patch1:         libkkc-POT.skip.patch
Patch2:         libkkc-vala-abstract-create.patch
# https://github.com/ueno/libkkc/pull/40
# Fix compilation with gcc14 -Werror=int-conversion
Patch3:         libkkc-pr40-int-conversion-fix.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2306455
# Fix invalid escape on default.json
Patch4:         libkkc-Fix-invalid-escape-on-json-file.patch

BuildRequires:  gcc-c++
BuildRequires:	marisa-devel
BuildRequires:	vala
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	json-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	python3-devel
BuildRequires:	python3-marisa
BuildRequires: make
BuildRequires: chrpath

Requires:	skkdic
Requires:	%{name}-data >= %{dataversion}
Requires:	%{name}-common = %{version}-%{release}

%description
libkkc provides a converter from Kana-string to
Kana-Kanji-mixed-string.  It was named after kkc.el in GNU Emacs, a
simple Kana Kanji converter, while libkkc tries to convert sentences
in a bit more complex way using N-gram language models.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:	Tools for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	tools
The %{name}-tools package contains tools for developing applications
that use %{name}.


%package	common
Summary:	Common data files for %{name}
BuildArch:	noarch

%description	common
The %{name}-common package contains the arch-independent data that
%{name} uses at run time.


%prep
%autosetup -p1

[ -f README.md ] || cp -p %SOURCE1 .
autoreconf -f


%build
%configure --disable-static --disable-silent-rules PYTHON=python3
%make_build


%check
make check


%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# https://bugzilla.redhat.com/show_bug.cgi?id=1987650
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/kkc

%find_lang %{name}


%ldconfig_scriptlets


%files -f %{name}.lang
%doc README data/rules/README.rules COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib

%files common
%{_datadir}/libkkc

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*

%files tools
%{_bindir}/kkc*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 21 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.5-30
- Fix FTBFS with gcc14 -Werror=int-conversion (bug 2300903)
- Fix invalid escape on json file (bug 2306455)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 29 2023 Parag Nemade <pnemade AT fedoraproject DOT org> - 0.3.5-26
- Migrate to SPDX license expression

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Jens Petersen <petersen@redhat.com>
- Use make macros (Tom Stellard, #4)
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Nov 16 2021 Jens Petersen <petersen@redhat.com> - 0.3.5-21
- delete the libdir rpath in the kkc executable for FTBFS (#1987650)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug  9 2019 Daiki Ueno <dueno@redhat.com> - 0.3.5-16
- fix FTBFS with vala 0.45.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.3.5-14
- Update BRs for vala packaging changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Takao Fujiwara <fujiwara@redhat.com> - 0.3.5-12
- enable python3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.5-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Jens Petersen <petersen@redhat.com> - 0.3.5-8
- update to latest github (253fb06)
- fixes FTBFS

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Daiki Ueno <dueno@redhat.com> - 0.3.5-2
- apply libkkc-try-all.patch for better candidate list

* Fri Dec 19 2014 Daiki Ueno <dueno@redhat.com> - 0.3.5-1
- new upstream release
- switch upstream source location to Github

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.4-2
- Rebuilt for gobject-introspection 1.41.4

* Mon Jul  7 2014 Daiki Ueno <dueno@redhat.com> - 0.3.4-1
- new upstream release
- switch to libgee 0.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr  1 2014 Daiki Ueno <dueno@redhat.com> - 0.3.3-1
- new upstream release

* Tue Dec 17 2013 Daiki Ueno <dueno@redhat.com> - 0.3.2-1
- new upstream release

* Fri Sep 20 2013 Daiki Ueno <dueno@redhat.com> - 0.3.1-2
- drop -data subpackage, which is now split into a separate source package

* Sun Sep 15 2013 Daiki Ueno <dueno@redhat.com> - 0.3.1-1
- new upstreamm release
- fix numeric conversion
- add minimum cost of backward search

* Wed Sep 11 2013 Daiki Ueno <dueno@redhat.com> - 0.3.0-1
- new upstream release (Closes: #970863)

* Mon Jul 29 2013 Daiki Ueno <dueno@redhat.com> - 0.2.7-1
- new upstream release
- enable make check on %%check
- drop buildroot cleanup

* Fri Jul  5 2013 Daiki Ueno <dueno@redhat.com> - 0.2.6-1
- new upstream release

* Thu Jul  4 2013 Daiki Ueno <dueno@redhat.com> - 0.2.5-1
- new upstream release

* Fri Jun  7 2013 Daiki Ueno <dueno@redhat.com> - 0.2.4-1
- new upstream release

* Wed May 15 2013 Daiki Ueno <dueno@redhat.com> - 0.2.3-1
- new upstream release

* Wed May  8 2013 Daiki Ueno <dueno@redhat.com> - 0.2.2-1
- new upstream release

* Wed May  1 2013 Daiki Ueno <dueno@redhat.com> - 0.2.1-1
- new upstream release

* Wed May  1 2013 Daiki Ueno <dueno@redhat.com> - 0.2.0-2
- synch with the latest upstream git master

* Tue Apr 30 2013 Daiki Ueno <dueno@redhat.com> - 0.2.0-1
- new upstream release

* Tue Mar 19 2013 Daiki Ueno <dueno@redhat.com> - 0.1.10-1
- new upstream release

* Tue Mar 12 2013 Daiki Ueno <dueno@redhat.com> - 0.1.9-1
- new upstream release

* Fri Feb 22 2013 Daiki Ueno <dueno@redhat.com> - 0.1.7-1
- new upstream release

* Sun Feb 10 2013 Daiki Ueno <dueno@redhat.com> - 0.1.5-1
- new upstream release

* Fri Feb  8 2013 Daiki Ueno <dueno@redhat.com> - 0.1.3-1
- move arch-independent data files to -common subpackage
- remove unnecessary R: from -common and -data subpackages
- add BR: python2-devel

* Thu Feb  7 2013 Daiki Ueno <dueno@redhat.com> - 0.1.3-1
- new upstream release
- add BR: marisa-python to generate -data package

* Wed Feb  6 2013 Daiki Ueno <dueno@redhat.com> - 0.1.2-2
- add ChangeLog to -data subpackages's %%doc
- remove unnecessary BR: libfep-devel

* Tue Feb  5 2013 Daiki Ueno <dueno@redhat.com> - 0.1.2-1
- new upstream release
- fix description of -data subpackage
- use popd instead of "cd -"

* Mon Feb  4 2013 Daiki Ueno <dueno@redhat.com> - 0.1.1-1
- new upstream release
- disable silent rules

* Thu Jan 31 2013 Daiki Ueno <dueno@redhat.com> - 0.1.0-1
- new upstream release

* Thu Jan 24 2013 Daiki Ueno <dueno@redhat.com> - 0.0.1-1
- initial packaging
