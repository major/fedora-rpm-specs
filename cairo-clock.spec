Summary:	Cairo-rendered on-screen clock 
Name:		cairo-clock
Version:	0.3.4
Release:	30%{?dist}
URL:		http://macslow.thepimp.net/?page_id=23
Source0:	http://macslow.thepimp.net/projects/%{name}/%{name}-%{version}.tar.gz
Patch0:		cairo-clock-0.3.4-fix-ldflags.patch
License:	GPLv2
BuildRequires:	gettext
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils
BuildRequires:	librsvg2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires: make

%description
Cairo-Clock is a desktop clock using cairo for rendering and taking advantage
of the Composite extension on newer Xorg servers.

%prep
%setup -q
%patch0 -p1 -b .fix-ldflags
sed 's/Application;//' -i desktop/%{name}.desktop

%build
%configure
make %{?_smp_mflags}

%install
make install INSTALL="install -p"  DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
       desktop/%{name}.desktop

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.3.4-12
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Tom Callaway <spot@fedoraproject.org> - 0.3.4-9
- fix ldflags

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.4-7
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Benoît Marcelin <sereinity@online.fr> 0.3.4-5
- Increase release for 564959

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 26 2008 Benoît Marcelin <sereinity@online.fr> 0.3.4-2
- Fix BuildRequires for Fedora 10
* Thu Feb 04 2008 Benoît Marcelin <sereinity@online.fr> 0.3.4-1
- Update to 0.3.4
- Clean BuildRequires and changelog
* Thu Dec 19 2007 Benoît Marcelin <sereinity@online.fr> 0.3.3-3
- Clean version need on BuildRequire
- Clean Require
- use %%{__make} INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
- drop INSTALL doc file
- change vendor Fedora to fedora
* Sun Dec 09 2007 Benoît Marcelin <sereinity@online.fr> 0.3.3-2
- Correct the url, vendor
- use make install instead of %%makeinstall
- add a upstream for sources
- clean BuildRequires and Requires
* Thu Oct 04 2007 Benoît Marcelin <sereinity@online.fr> 0.3.3-1
- Update to 0.3.3
* Sun Mar 11 2007 Benoît Marcelin <sereinity@online.fr> 0.3.2-1
- Spec file correction with rpmlint
* Tue Nov 14 2006 homer <nobodyhome@swaziland.cz> 0.3.1-1
- Spec file updated for FC6
* Mon Feb 27 2006 Hyun-Jin Moon <moonhyunjin@gmail.com> 0.3.1-1
- Just rebuild for Fedora Core 5 Test 3.
  This should works official Fedora Core 5 in later.
* Sat Feb 04 2006 Milosz Derezynski <internalerror@gmail.com> 0.3-1 
- Initial spec file 
