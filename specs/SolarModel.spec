Name:		SolarModel
Summary: 	Real-time 3D Solar System simulation
Version:	2.1
Release:	40%{?dist}
License:	GPL-1.0-or-later
Source0:	http://downloads.sourceforge.net/solarmodel/%{name}_src_2_1.zip
# Upstream only has these .dat files in the binary zip file for 2.1
# http://downloads.sourceforge.net/solarmodel/SolarModel_bin_2_1.zip
Source1:	config.dat
Source2:	data.dat
Source3:	SolarModel.desktop
Source4:	SolarModel.png
# Use system locations for libraries, headers
# Use RPM_OPT_FLAGS
# Fix swprintf/Linux related issues
Patch0:		SolarModel-2.1-Fedora.patch
# Compile against irrlicht 1.6
Patch1:		SolarModel-2.1-irrlicht1.6.patch
URL:		http://www.ffsoftworks.com/solarmodel.php
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	irrlicht-devel, libXext-devel, libX11-devel, desktop-file-utils

%description
Solar Model provides realtime modeling of the solar system. It allows the user 
to navigate in space, to control time counting (speed-up time flow) and 
estimate real movement of space bodies like planets, dwarf planets and moons; 
estimate its nowadays positions in space. You may select two possible views: 
Solar System view or Milky Way galaxy view. It also allows the user to bind 
the camera to space objects (for example, you can look from the Moon onto Earth 
in real-time flow). 

%prep
%setup -q -n %{name}_src
%patch -P0 -p1 -b .Fedora
%patch -P1 -p1 -b .irrlicht1.6

for i in _dev/*.txt "_dev/map/*.txt"; do
	sed -i 's/\r//' $i
done
iconv -o _dev/Changelog.txt.iso88591 -f iso88591 -t utf8 _dev/Changelog.txt
mv _dev/Changelog.txt.iso88591 _dev/Changelog.txt

%build
make %{_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 SolarModel %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}
install	-p -m0644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}
install -p -m0644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE3}


%files
%doc _dev/Changelog.txt _dev/License.txt _dev/Readme.txt _dev/map/* _dev/num/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/SolarModel.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-38
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-30
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1-18
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Tom Callaway <spot@fedoraproject.org> - 2.1-13
- rebuild for new irrlicht

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul  3 2012 Tom Callaway <spot@fedoraproject.org> - 2.1-11
- bump for new irrlicht

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1-8
- bump for new irrlicht (1.7.1)

* Tue May 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1-7
- fix segfault caused by code not looking in correct place for config.dat

* Thu Jan 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1-6
- bump for new irrlicht (1.6)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1-4
- fix desktop file (bz 492751)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 5 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-2
- add desktop file and icon
- fix 32bit build (thanks to Lubomir Rintel)

* Wed Dec 3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-1
- Initial package for Fedora
