#TODO: gradient-convert is a Python script

Name:      cptutils
Version:   1.77
Release:   3%{?dist}
Summary:   Utilities to manipulate and translate color gradients
License:   GPLv2+
URL:       http://soliton.vm.bytemark.co.uk/pub/jjg/en/code/cptutils.html
Source0:   http://soliton.vm.bytemark.co.uk/pub/jjg/src/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires: make

%description
The cptutils package contains a number of utilities for the manipulation of
color gradients; mainly for translating between different formats. Formats
supported include ggr (GIMP gradient), cpt (GMT color palette table),
avl (Arcview Legend), lut (xmedcon), svg, and version 3 of the grd format. 

The cptutils package was written to aid the construction of the cpt archive
cpt-city http://soliton.vm.bytemark.co.uk/pub/cpt-city where thousands of
gradients can be downloaded.


%prep
%setup -q


%build
%configure
make


%install
make install DESTDIR=%{buildroot}

# Don't run tests, because some of them require data
# from other packages, for instance GIMP


%files 
%doc CHANGELOG.md COPYING README.md
%{_bindir}/*
%{_mandir}/man1/*.1*


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 13 2023 Sandipan Roy <bytehackr@fedoraproject.org> - 1.77-1
- rhbz#2169209 
- New upstream release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 Sumit Garg <sumitgarg44@gmail.com> - 1.74-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Volker Fröhlich <volker27@gmx.at> - 1.73-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Volker Fröhlich <volker27@gmx.at> - 1.72-1
- New upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Volker Fröhlich <volker27@gmx.at> 1.70-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Volker Fröhlich <volker27@gmx.at> 1.69-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Volker Fröhlich <volker27@gmx.at> 1.66-1
- New upstream release

* Mon Mar 21 2016 Volker Fröhlich <volker27@gmx.at> 1.63-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Volker Fröhlich <volker27@gmx.at> 1.62-1
- New upstream release

* Tue Dec 22 2015 Volker Fröhlich <volker27@gmx.at> 1.61-1
- New upstream release

* Sat Dec 19 2015 Volker Fröhlich <volker27@gmx.at> 1.60-1
- New upstream release

* Mon Jul  6 2015 Volker Fröhlich <volker27@gmx.at> 1.59-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 13 2015 Volker Fröhlich <volker27@gmx.at> 1.58-1
- New upstream release

* Wed Oct  1 2014 Volker Fröhlich <volker27@gmx.at> 1.56-1
- New upstream release
- Add jansson as BR

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Volker Fröhlich <volker27@gmx.at> 1.55-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun  5 2014 Volker Fröhlich <volker27@gmx.at> 1.54-1
- New upstream release

* Thu Apr 24 2014 Volker Fröhlich <volker27@gmx.at> 1.53-1
- New upstream release

* Fri Mar 14 2014 Volker Fröhlich <volker27@gmx.at> 1.52-1
- New upstream release

* Fri Feb 28 2014 Volker Fröhlich <volker27@gmx.at> 1.51-1
- New upstream release

* Wed Feb 12 2014 Volker Fröhlich <volker27@gmx.at> 1.50-1
- New upstream release

* Tue Feb 11 2014 Volker Fröhlich <volker27@gmx.at> 1.49-1
- New upstream release

* Mon Nov  4 2013 Volker Fröhlich <volker27@gmx.at> 1.48-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Volker Fröhlich <volker27@gmx.at> 1.47-1
- New upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 15 2012 Volker Fröhlich <volker27@gmx.at> 1.46-1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Volker Fröhlich <volker27@gmx.at> 1.45-1
- New upstream release

* Wed Feb 15 2012 Volker Fröhlich <volker27@gmx.at> 1.42-2
- Remove unnecessary BR flex

* Sat Jan 21 2012 Volker Fröhlich <volker27@gmx.at> 1.42-1
- New upstream release
- All patches and wishes were implemented by the author

* Sat Jan 21 2012 Volker Fröhlich <volker27@gmx.at> 1.41-1
- Initial packaging for Fedora
