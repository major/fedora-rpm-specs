Name:           free42
URL:            http://www.thomasokken.com/free42/
Epoch:          1
Version:        1.4.77
Release:        17%{?dist}
License:        GPLv2 and MIT
Summary:        42S Calculator Simulator
Source:         http://www.thomasokken.com/free42/upstream/free42-nologo-%{version}.tgz

BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  gtk2-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires: make
Patch0:         free42-Wno-narrowing.patch

%description
Free42 is a complete re-implementation of the 42S calculator and the
82240 printer.  It was written from scratch, without using any HP code.

%prep
%setup -q -n free42-nologo-%{version}
%patch0 -p1

%build
cd gtk
sed -i 's/^\(LIBS := .*\)/\1 -lX11/' Makefile
sed -i "/^CXXFLAGS :=/s@-MMD -Wall -g@%{optflags}@" Makefile
# make fails when using %{?_smp_mflags}
make -e BCD_MATH=1
convert icon.xpm free42.png
cat <<EOF >free42.desktop
[Desktop Entry]
Name=free42
GenericName=Free42 calculator simulator
Exec=free42dec
Icon=free42
Terminal=false
Type=Application
Categories=Utility;Calculator;
EOF

%install
install -D -p -m 755 gtk/free42dec %{buildroot}%{_bindir}/free42dec
install -D -p -m 644 gtk/free42.png %{buildroot}/usr/share/pixmaps/%{name}.png
install -D -p -m 644 gtk/free42.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/free42dec
%doc CREDITS HISTORY README TODO VERSION
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1:1.4.77-9
- -Wno-narrowing to fix FTBFS on rawhide fixes rhbz#1603998 and rhbz#1674894

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Eric Smith <brouhaha@fedoraproject.org> 1:1.4.77-1
- Revert to 1.4.77 and bump epoch, due to problems with Intel decimal
  floating point library. See also package review #1098820 for idfpml.
- Changed / to @ in second sed command because optflags may contain a
  slash in a path.

* Sun Jul  5 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.5-1
- Update to 1.5.5, fix FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Eric Smith <eric@brouhaha.com> 1.5-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 Eric Smith <eric@brouhaha.com> 1.4.77-1
- Update to latest upstream.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Eric Smith <eric@brouhaha.com> 1.4.74-1
- Update to latest upstream.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 08 2011 Eric Smith <eric@brouhaha.com> 1.4.70-1
- Update to latest upstream.
- Removed BuildRoot, clean, defattr, etc.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 21 2010 Eric Smith <eric@brouhaha.com> 1.4.66-1
- update to latest upstream

* Sun Mar 28 2010 Eric Smith <eric@brouhaha.com> 1.4.62-2
- Edit Makefile to add -lX11 to libs, necessary for Fedora 13. Not sure why
  I didn't need that for Fedora 12. Sed command from package review by
  Martin Gieseking.
- Edit Makefile to define CXXFLAGS based on RPM optflags. Sed command from
  package review by Martin Gieseking.

* Sat Mar 27 2010 Eric Smith <eric@brouhaha.com> 1.4.62-1
- update to latest upstream

* Sun Jan 31 2010 Eric Smith <eric@brouhaha.com> 1.4.61-1
- initial version
