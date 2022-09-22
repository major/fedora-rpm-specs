#this is to prevent empty debuginfo failur
%global debug_package %{nil}

Name:           monobristol
Version:        0.60.3.1
Release:        22%{?dist}
Summary:        GUI launcher for Bristol in Mono

License:        GPL+
URL:            http://www.dacr.hu/monobristol/
Source:         http://www.dacr.hu/monobristol/%{name}-%{version}.tar.gz
# No upstrem bugtracker. Patch emailed upstream 20120626
# The patch removes shebang from the top and removes .png extension from icon key
Patch1:         %{name}-0.60.3-desktop.patch
Requires:       bristol
Requires:       mono-core 
Requires:       hicolor-icon-theme

BuildRequires: make
BuildRequires:  gtk-sharp2-devel
BuildRequires:  desktop-file-utils

ExclusiveArch:  %{mono_arches}


%description
monoBristol is very simple Gui for Bristol Synthesiser.
Bristol is an emulation package for a number of different 'classic' 
synthesizers including additive and subtractive and a few organs.

%prep
%setup -q
%patch1 -p1

sed -i "s#gmcs#mcs#g" configure*
sed -i "s#gmcs#mcs#g" Makefile.in
sed -i "s#gmcs#mcs#g" monoBristol.make

%build
%configure
# not parallel safe
make

%install
#removal of buildroot is no longer necassary, except for EPEL5
make install DESTDIR=%{buildroot}

# install the AppData file
mkdir -p %{buildroot}%{_datadir}/appdata
cp monoBristol.appdata.xml %{buildroot}%{_datadir}/appdata/

#install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

desktop-file-install    \
    --dir %{buildroot}%{_datadir}/applications \
     monoBristol.desktop

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/monoBristol.desktop
%{_libdir}/%{name}/
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/appdata/monoBristol.appdata.xml

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.60.3.1-12
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.3.1-8
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.60.3.1-5
- Rebuild (mono4)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.60.3.1-3
- Avoid parallel make race condition (#992286, #1106234)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Richard Hughes <richard@hughsie.com> - 0.60.3.1-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Dan Horák <dan[at]danny.cz> 0.60.3-9
- set ExclusiveArch

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Jørn Lomax <northlomax@gmail.com> 0.60.3-7
- fixed spelling error
* Thu Jun 28 2012 Jørn Lomax <northlomax@gmail.com> 0.60.3-6
- Changed licence and fixed ownerships
* Wed Jun 27 2012 Jørn Lomax <northlomax@gmail.com> 0.60.3-5
- Added installation of icon and spelling
- removed unused dependencies 
* Tue Jun 26 2012 Jørn Lomax <northlomax@gmail.com> 0.60.3-4
- removed no arch and disabled empty debug warning
- fixed directories in files
* Thu Jun 21 2012 Jørn Lomax <northlomax@gmail.com> 0.60.3-3
- Clean up some more, change to added archbuild and quieted setup 
* Thu Jun 21 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.60.3-2
- clean up package, correct files
* Mon Jun 18 2012 Jørn Lomax <northlomax@gmail.com> 0.60.3-1
- inital package
