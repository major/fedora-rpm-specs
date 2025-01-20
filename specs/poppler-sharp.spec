%global debug_package %{nil}
Name:		poppler-sharp
Version:	0.0.3
Release:	37%{?dist}
Summary:	C sharp Bindings for Poppler
Summary(es):	Enlaces C# para Poppler
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.github.com/jacintos/poppler-sharp
Source0:	http://github.com/downloads/jacintos/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-gapi
BuildRequires:	gtk-sharp2-devel
BuildRequires:	poppler-glib-devel

Requires:	poppler
Requires:	poppler-glib

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Generates managed bindings for Poppler using the GAPI tools

%description -l es
Genera los vínculos administrados usando las herramientas GAPI

%package devel
Summary:	Development files for %{name}
Summary(es):	Archivos de desarrollo para %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development package for %{name}

%description devel -l es
Paquete de desarrollo para %{name}

%prep
%setup -q
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac
sed -i "s#gmcs#mcs#g" Makefile.am
sed -i "s#gmcs#mcs#g" Makefile.in
sed -i "s#mono/2.0#mono/4.5#g" configure
sed -i "s#mono/2.0#mono/4.5#g" configure.ac

%build
%configure
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license COPYING
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}.dll*

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.3-36
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 David Tardon <dtardon@redhat.com> - 0.0.3-21
- rebuild for poppler 0.62.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild


* Thu Jan 04 2018 Ville SkyttÃ¤ <ville.skytta@iki.fi> - 0.0.3-20
- Own the %%{_libdir}/%%{name} dir
- Mark COPYING as %%license

* Wed Nov 08 2017 David Tardon <dtardon@redhat.com> - 0.0.3-19
- rebuild for poppler 0.61.0

* Fri Oct 06 2017 David Tardon <dtardon@redhat.com> - 0.0.3-18
- rebuild for poppler 0.60.1

* Fri Sep 08 2017 David Tardon <dtardon@redhat.com> - 0.0.3-17
- rebuild for poppler 0.59.0

* Thu Aug 03 2017 David Tardon <dtardon@redhat.com> - 0.0.3-16
- rebuild for poppler 0.57.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 9 2017 Ismael Olea <ismael@olea.org> - 0.0.3-12
- adding missing dep to poppler-glib (#1301269)

* Fri Dec 16 2016 David Tardon <dtardon@redhat.com> - 0.0.3-11
- rebuild for poppler 0.50.0

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-10
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.0.3-7
- Build with mono 4
- Use mono_arches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 8 2012 Ismael Olea <ismael@olea.org> 0.0.3-2
- spec tuning

* Thu Jun 21 2012 Ismael Olea <ismael@olea.org> 0.0.3-1
- update to 0.0.3

* Mon Aug 29 2011 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.0.2-2
- Fix libpoppler-glib missing

* Fri Aug 26 2011 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.0.2-1
- Update to upstream version

* Tue Mar 22 2011 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.0.1-3
- Translate spec summary and description to spanish
- Add poppler-glib-devel dependency

* Mon Oct 04 2010 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.0.1-2
- Patch .pc package for work correctly on x86_64
- Correct license according to http://github.com/jacintos/poppler-sharp

* Wed Jul 07 2010 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.0.1-1
- Initial packaging
