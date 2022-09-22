Summary   : Gtk application to use themonospot (multimedia files parser/editor)
Name      : themonospot-gui-gtk
Version   : 0.2.2
Release   : 30%{?dist}
License   : GPLv2
Group     : Applications/Multimedia
URL       : http://www.integrazioneweb.com/themonospot
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-gui-gtk-%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: make
BuildRequires: mono-devel
BuildRequires: gtk-sharp2-devel
BuildRequires: themonospot-base-devel
BuildRequires: desktop-file-utils

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
themonospot-gui-gtk is a Mono framework application to create a
graphic frontend to use themonospot base component and his plugins.

%prep
%setup -q

sed -i "s#gmcs#mcs#g" configure*
sed -i "s#gmcs#mcs#g" Makefile.in
sed -i "s#gmcs#mcs#g" themonospot-gui-gtk.make

%build
%configure
make

%install
make DESTDIR=%{buildroot} install

desktop-file-install \
 --dir %{buildroot}%{_datadir}/applications \
 --delete-original \
 %{buildroot}%{_datadir}/applications/themonospot-gtk.desktop


%files
%doc copying.gpl
%{_bindir}/themonospot-gtk
%{_libdir}/themonospot/%{name}.exe
%{_datadir}/pixmaps/themonospot-gtk.png
%{_datadir}/applications/themonospot-gtk.desktop


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-17
- mono rebuild for aarch64 support

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.2-14
- Rebuild (mono4)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 29 2011 Dan Horák <dan[at]danny.cz> - 0.2.2-7
- updated the supported arch list

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.2.2-5
- Rebuild against new mono

* Sun Mar 14 2010 Armando Basile <hmandevteam@gmail.com> 0.2.2-4
- removed "% {?_smp_mflags}" from make command, parallel make sometimes fails

* Fri Jan 01 2010 Armando Basile <hmandevteam@gmail.com> 0.2.2-3
- modified desktop-file-install macro parameters

* Fri Jan 01 2010 Armando Basile <hmandevteam@gmail.com> 0.2.2-2
- added themonospot-base-devel and gtk-sharp2-devel as BuildRequire

* Thu Dec 31 2009 Armando Basile <hmandevteam@gmail.com> 0.2.2-1
- bug fix: scan process without plugin installed

* Thu Dec 31 2009 Armando Basile <hmandevteam@gmail.com> 0.2.1-2
- only mono-devel and desktop-file-utils as BuildRequire

* Wed Dec 30 2009 Armando Basile <hmandevteam@gmail.com> 0.2.1-1
- removed GAC use

* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.2.0-2
- first release of new Gtk application to use themonospot
