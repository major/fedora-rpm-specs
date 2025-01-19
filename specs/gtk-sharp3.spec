%global forgeurl https://github.com/GLibSharp/GtkSharp
%global tag 3.22.2

%forgemeta

%if 0%{?rhel}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%global _monodir %{_prefix}/lib/mono
%global _monogacdir %{_monodir}/gac
%endif

%global debug_package %{nil}
%global _docdir_fmt %{name}

Summary:        GTK+ 3 and GNOME 3 bindings for Mono
Name:           gtk-sharp3
Version:        3.22.2
Release:        11%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2

BuildRequires:  meson
BuildRequires:  mono-devel gtk3-devel libglade2-devel monodoc
BuildRequires:  automake, libtool
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  perl-generators
Patch0:         gtk-sharp3-2.99.3-gui-thread-check.patch
Patch1:         gtk-sharp3-2.99.3-gtkrange.patch
Patch2:         gtk-sharp3-3.22.2-nolibdir.patch
Patch3:         gtk-sharp3-3.22.2-add-cairo-sharp-dll-config.patch

URL:            %forgeurl
Source:         %forgesource

# Mono only available on these:
ExclusiveArch:  %{mono_arches}

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to version 3 of GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk.

%package gapi
Summary:        Tools for creation and maintenance managed bindings for Mono and .NET

%description gapi
This package provides developer tools for the creation and
maintenance of managed bindings to native libraries which utilize
glib and GObject. Some examples of libraries currently bound using
the GAPI tools and found in Gtk# include Gtk, Atk, Pango, Gdk.

%package devel
Summary:        Files needed for developing with gtk-sharp3
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package provides the necessary development libraries and headers
for writing gtk-sharp3 applications.

%package doc
Summary:        Gtk# 3 documentation
Requires:       monodoc
BuildArch:      noarch

%description doc
This package provides the Gtk# 3 documentation for monodoc.

%prep
%forgeautosetup -p1

#fix missing gdk_api_includes references
sed -i "s/gdk_api_includes/gio_api_includes/" Source/gdk/generated/meson.build
sed -i "s/gdk_api_includes/gio_api_includes/" Source/gio/generated/meson.build
sed -i "s/gdk_api_includes/gio_api_includes/" Source/gtk/generated/meson.build
sed -i "s/gdk_api_includes/gio_api_includes/" Source/sample/valtest/generated/meson.build

%build
%meson -Dinstall=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets

# see https://bugzilla.redhat.com/show_bug.cgi?id=2155849
cp redhat-linux-build/Source/gtk/gtk-sharp.dll.config %{buildroot}/%{_monodir}/GtkSharp-3.0

%files
%doc README.md
%license LICENSE
%{_monogacdir}/*
%{_monodir}/GtkSharp-3.0
%{_monodir}/atk-sharp
%{_monodir}/cairo-sharp
%{_monodir}/gdk-sharp
%{_monodir}/gtk-sharp
%{_monodir}/gio-sharp
%{_monodir}/glib-sharp
%{_monodir}/pango-sharp

%files gapi
%{_bindir}/gapi3-codegen
%{_bindir}/gapi3-fixup
%{_bindir}/gapi3-parser
%dir %{_prefix}/lib/gapi-3.0
%{_prefix}/lib/gapi-3.0/gapi_codegen.exe
%{_prefix}/lib/gapi-3.0/gapi-fixup.exe
%{_prefix}/lib/gapi-3.0/gapi-parser.exe
%{_prefix}/lib/gapi-3.0/gapi_pp.pl
%{_prefix}/lib/gapi-3.0/gapi2xml.pl
%{_datadir}/gapi-3.0
%{_libdir}/pkgconfig/gapi-3.0.pc

%files devel
%{_libdir}/pkgconfig/*-sharp-3.0.pc

%files doc
#{_prefix}/lib/monodoc/sources/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.22.2-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.22.2-5
- copy the config file to live beside the gtk-sharp.dll

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.22.2-3
- add upstream patch for adding cairo-sharp.dll.config

* Fri Aug 12 2022 Julian Sikorski <belegdol@fedoraproject.org> - 3.22.2-2
- Fix what is supposed to go to %%{_libdir} vs %%{_prefix}/lib

* Mon Aug 08 2022 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.22.2-1
- Upgrade to new upstream https://github.com/GLibSharp/GtkSharp with the help from Julian Sikorski (see bug 2108677)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.99.3-29
- enable docs again

* Mon Feb 03 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.99.3-28
- fix issue with latest Mono 6: ambiguous reference between System.Range and Gtk.Range
- built without docs because mdoc.exe is not built with Mono 6 and mcs anymore

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 17:46:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.99.3-26
- Rebuilt because of missing mono Provides

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.99.3-24
- fix build error in gui-thread-check.c

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.3-17
- mono rebuild for aarch64 support

* Fri Sep 09 2016 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.99.3-16
- Rebuilt for Mono4 in Epel7

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-14
- Rebuild mono 4 update

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-12
- Rebuild mono 4

* Mon May 18 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-11
- Rebuild in f23-mono4

* Fri May 15 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-10
- Fix url
- Use global insted define for rhel and epel7
- Replace old autotool macros in configure.ac

* Mon May 11 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-9
- Remove virtual provides

* Tue May 05 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-8
- Add /sbin/ldconfig in post and postun
- Remove requiere in gapi

* Tue May 05 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-7
- gtk-sharp-3-doc not requiered gtk-sharp-3 and move to noarch
- gapi summary less than 70 characters
- Fixed for mono 4 moved to prep
- Define _monodir and _monogacdir for rhel and epel7
- Spec clean up

* Mon May 04 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-6
- Use same subpackage criteria as gtk-sharp2
- Spec clean up
- Use license macro

* Mon Apr 20 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-5
- Add mono_arches

* Thu Apr 16 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-4
- Use mcs insted gmcs

* Thu Apr 16 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-3
- Build for Mono 4

* Fri Feb 13 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-2
- Remove version requiered of mono-core

* Fri Oct 17 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 2.99.3-1
- initial version
