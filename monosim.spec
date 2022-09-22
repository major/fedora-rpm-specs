Summary: Manage your SIM Card contacts
Name: monosim
Version: 1.5.2
Release: 26%{?dist}
License: GPLv2
URL: http://www.integrazioneweb.com/monosim
Source: http://www.integrazioneweb.com/repository/SOURCES/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gtk-sharp2-devel >= 2.8.3
BuildRequires: mono-core >= 1.2.3
BuildRequires: pkgconfig
#BuildRequires: desktop-file-utils

# Mono only available on these:
ExclusiveArch: %mono_arches

Requires: gtk-sharp2 >= 2.8.3
Requires: mono-core >= 1.2.3
Requires: pcsc-lite >= 1.0.0
Requires: pcsc-lite-libs >= 1.0.0
Requires: pcsc-lite-devel >= 1.0.0

%define debug_package %{nil}

%description
is a simple application that can be used to read, write,
update, delete and backup your sim card contacts. It open
and save also some format files to manage your contacts
also in a text files. To connect monosim to your smartcard
you need use a standard PCSC smartcard reader as towitoko,
acs, athena, blutronics, etc.

%prep
%setup -q

sed -i "s#gmcs#mcs#g" configure*
sed -i "s#gmcs#mcs#g" */Makefile*

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# desktop-file-install --vendor="fedora"               \
#   --dir=%{buildroot}%{_datadir}/applications    \
#   monoSIM/images/%{name}.desktop


%files
%doc monosim/copying.gpl
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/monosim.desktop


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-13
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-10
- Rebuild (mono4)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Dan Horák <dan[at]danny.cz> - 1.5.2-3
- updated the supported arch list

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 30 2009 A.Basile <hmandevteam@gmail.com> 1.5.2-1
- bug fixed: issue 4/5 - fix verified (pin1 enable/disable)
- bug fixed: issue 6 - fix verified (monosim on 64 bit)
- bug fixed: issue 7 - fix verified (international numbers)
- bug fixed: issue 8  - fix verified (closing main window)
- bug fixed: cross compile compatibility (monodevelop, #develop)
- deleted pkgconfig file for monopcsclib
- modified monosim.desktop file (compliant to desktop-file-validate)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Xavier Lamien <laxathom@fedoraproject.org> - 1.3.0.2-3
- build arch ppc64.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 02 2007 hman <hmandevteam@gmail.com> 1.3.0.2-1
- bug fixed: Fixed wrong label position reference in language files
- added support informations in language files
- added xml settings file to store selected language

* Sat Jun 30 2007 hman <hmandevteam@gmail.com> 1.2.0-1
- bug fixed: Many bugs fixed
- multilanguage support added (with text files in [languages] subfolder)
- erase sim phonebook function added

* Mon Jun 11 2007 hman <hmandevteam@gmail.com> 1.0.1-1
- first public release
