%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %define tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Name:           iwidgets
Version:        4.1.1
Release:        14%{?dist}
Summary:        A set of useful widgets based on itcl and itk

License:        MIT
URL:            http://incrtcl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/incrtcl/iwidgets-%{version}.tar.gz
Patch0:         iwidgets-calls.patch
Patch1:         iwidgets4.0.1-wish85.diff

BuildArch:      noarch
Requires:       tcl(abi) = 8.6 itk
BuildRequires:  tcl itcl-devel

%description
A set of useful widgets based on itcl and itk.

%prep
%setup -q
%patch -P0 -p1 -b .calls
%patch -P1 -p1 -b .wish85

%build
# The configure script and Makefile for this package is horribly broken.
# Installation is simple enough that it's easier to manually install the
# files than try to patch the configure script and Makefile to work.

sed -e "s#@itcl_VERSION@#4.0#" -e "s#@PACKAGE_VERSION@#%{version}#" < iwidgets.tcl.in > iwidgets.tcl
sed -e "s#@PACKAGE_VERSION@#%{version}#" < pkgIndex.tcl.in > pkgIndex.tcl

%install
mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}
install -p -m 644 generic/*.* %{buildroot}/%{tcl_sitelib}/%{name}%{version}
install -p -m 644 generic/tclIndex %{buildroot}/%{tcl_sitelib}/%{name}%{version}
install -p -m 644 iwidgets.tcl %{buildroot}/%{tcl_sitelib}/%{name}%{version}
install -p -m 644 pkgIndex.tcl %{buildroot}/%{tcl_sitelib}/%{name}%{version}

mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos
for i in demos/* ; do
    if [ -f $i ] ; then
        install -p -m 644 $i %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos
    fi
done
chmod 755 %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/catalog
# Remove rpmlint warning.
chmod 755 %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/scopedobject

mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/images
install -p -m 644 demos/images/*.* %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/images

# These html pages are part of the demonstration scripts, so they aren't
# packaged with the rest of the documentation.
mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/html
install -p -m 644 demos/html/*.html %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/html

mkdir -p %{buildroot}/%{_mandir}/mann
install -p -m 644 doc/*.n %{buildroot}/%{_mandir}/mann/
# This file conflicts with the one from tk-devel
rm %{buildroot}/%{_mandir}/mann/panedwindow.n
# This file conflicts with the one from tklib
rm %{buildroot}/%{_mandir}/mann/datefield.n

%files
%{tcl_sitelib}/iwidgets%{version}
%{_mandir}/mann/*
%license license.terms
%doc README doc/iwidgets.ps

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 4.1.1-3
- Fix var substitution.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Orion Poplawski <orion@nwra.com> - 4.1.1-1
- Update to 4.1.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 4.0.2-22
- Fix /bin/env.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 4.0.2-16
- Fix compatibility with Itk4.

* Sat Oct 18 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 4.0.2-15
- Fix itcl/itk calls (to lowercase).

* Fri Aug 29 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 4.0.2-14
- Fix itcl/itk verstion requirement.
- Some cleanup of spec (clean section, buildroot tag).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.2-12
- Bump tcl(abi) requires

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 4.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 28 2012 Dmitrij S. Kryzhevich <krege@land.ru>  - 4.0.2-8
- Fix demos (rhbz #800404).

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 5 2009 Wart <wart at kobold.org> - 4.0.2-4
- Remove version requirement on Tk

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 11 2008 Wart <wart at kobold.org> - 4.0.2-1
- Update to 4.0.2 using a patch from CVS
- Rebuild for tcl 8.5

* Sun Aug 19 2007 Wart <wart at kobold.org> - 4.0.1-5
- License tag clarification
- Better download URL

* Mon Aug 28 2006 Wart <wart at kobold.org> - 4.0.1-4
- Rebuild for Fedora Extras

* Fri Dec 30 2005 Wart <wart at kobold.org> - 4.0.1-3
- Updated source url
- Change Requires: based on bz #174265
- Manually install all files instead of depending on the broken
  configure script and Makefile.

* Fri Nov 25 2005 Wart <wart at kobold.org> - 4.0.1-2
- Initial spec file for Fedora Extras

* Thu Nov 24 2005 Wart <wart at kobold.org> - 4.0.1-1
- Initial spec file for personal use
