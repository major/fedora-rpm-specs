%global pkgname resynthesizer
%global	commit adfa25ab0d11ed27ff301cb7db4b144c4c2fa112
%global	shortcommit %(c=%{commit}; echo ${c:0:7})
%global with_snapshot 1

%global gimpplugindir %(%___build_pre; gimptool --gimpplugindir)/plug-ins
%global gimpscriptdir %(%___build_pre; gimptool --gimpdatadir)/scripts

Summary: Gimp plug-in for texture synthesis
Name: gimp-resynthesizer
Version: 2.0.3
%if %{with_snapshot}
Release:	16.20190428git%{shortcommit}%{?dist}
%else
Release:	14%{?dist}
%endif
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Requires: gimp
BuildRequires:  gcc
BuildRequires: gimp, gimp-devel
BuildRequires: intltool
BuildRequires: automake
BuildRequires: libappstream-glib
BuildRequires: python2-devel
BuildRequires: make
URL: https://github.com/bootchk/%{pkgname}

# Source tarball generated as follows
# git clone git@github.com:bootchk/resynthesizer.git
# cd resynthesizer
# git archive --format tar.xz --prefix resynthesizer_$(git rev-parse --short HEAD)/ \
# ... HEAD -o resynthesizer_$(git rev-parse --short HEAD).tar.xz

%if %{with_snapshot}
Source:		%{url}/archive/%{shortcommit}.tar.gz#/%{pkgname}-%{shortcommit}.tar.gz
%else
Source:		%{url}/archive/v%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
%endif

%description
Resynthesizer is a Gimp plug-in for texture synthesis. Given a sample of a 
texture, it can create more of that texture. This has uses including: 
- Creating more of a texture (including creation of tileable textures)
- Removing objects from images (great for touching up photos)
- Creating themed images (by transfering a texture from one image to another)

%prep
%if %{with_snapshot}
%autosetup -n resynthesizer-%{commit}
%else
%autosetup -n resynthesizer-%{version}
%endif

# Fix all Python shebangs recursively in .
%py2_shebang_fix . ./PluginScripts/*
  
./autogen.sh

%build
%configure
%make_build

%install
%make_install
mkdir %{buildroot}%{_metainfodir}
cp -v gimp-%{pkgname}.metainfo.xml %{buildroot}%{_metainfodir}

# Use the system Python in the shebangs
%py2_shebang_fix %{buildroot}%{gimpplugindir}/plugin-*

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%find_lang %{pkgname}

%files -f %{pkgname}.lang
%license COPYING
%doc README
%{_datadir}/%{pkgname}/*
%{_metainfodir}/*.metainfo.xml
%{gimpplugindir}/plugin-heal*
%{gimpplugindir}/plugin-map*
%{gimpplugindir}/plugin-render*
%{gimpplugindir}/plugin-resynth*
%{gimpplugindir}/plugin-uncrop*
%{gimpplugindir}/resynthesizer*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-16.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.3-15.20190428gitadfa25a
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-14.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-13.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5.20190428gitadfa25a
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3.20190428gitadfa25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019  Petr Viktorin <pviktori@redhat.com> 2.0.3-2.20190428gitadfa25a
* Fix Python shebangs

* Sat Aug 10 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.0.3-1.20190428gitadfa25a
- Update to 2.0.3 git snapshot
- Use gimp rpm macros
- Clean up spec file

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12.20160601git787ee5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11.20160601git787ee5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10.20160601git787ee5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9.20160601git787ee5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8.20160601git787ee5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7.20160601git787ee5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6.20160601git787ee5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0-5.20160601git%{shortcommit}
- fix appdata filename everywhere

* Thu Jun 02 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0-4.20160601git%{shortcommit}
- Fix appdata filename

* Wed Jun 01 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0-3.20160601git%{shortcommit}
- Add appdata file

* Tue May 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0-2.20160524git%{shortcommit}
- Update the package using git snapshot

* Thu May 19 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0-1
- Update to latest upstream version
- change define flags to global
- minor spec file cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.16-12
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Nils Philippsen <nils@redhat.com> - 0.16-6
- rebuild against gimp 2.8.0 release candidate

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Nils Philippsen <nils@redhat.com> - 0.16-4
- rebuild for GIMP 2.7

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.16-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 02 2009 Ewan Mac Mahon <ewan@macmahon.me.uk> - 0.16-1
- Bump to version 0.16
- Patch makefile to allow Fedora CFLAGS to override defaults.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.15-3
- Autorebuild for GCC 4.3

*Sun Aug 19 2007 Ewan Mac Mahon <ewan@macmahon.me.uk> - 0.15-2
Fixed review problems: Spurious comment, License tag, variable style 
build root, ignoring opt flags.
* Mon Jul 30 2007 Ewan Mac Mahon <ewan@macmahon.me.uk> - 0.15-1
Initial Fedora package
