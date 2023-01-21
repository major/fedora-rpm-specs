Name:		fontopia
Version:	1.8
Release:	15%{?dist}
Summary:	The console font editor

License:	GPLv3+
URL:		https://sites.google.com/site/mohammedisam2000/home/projects
Source0:	https://sites.google.com/site/mohammedisam2000/home/projects/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	gnudos-devel
BuildRequires: make

%description
Fontopia is an easy-to-use, text-based, console font editor.
Fontopia is not only a conversion tool, it includes complete features to
re-size and manipulate glyphs, edit font metrics and other meta-data.
Unlike other console font tools, fontopia works on both PSF 1 & 2, PCF, CP and 
Raw fonts. Type conversion is as simple as changing font type in memory and 
saving it to disk in the other version. Fontopia allows exporting and 
importing of Unicode tables from external files or other fonts. It provides
a user-friendly, easy-to-use glyph editor. It can easily change font metrics,
e.g. length, width, height, etc. It performs basic glyph operations like 
inversion, flipping, setting/unsetting bits, and much more. Fontopia is the
first dedicated text-based editor for console fonts.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

install -m 0644 -p -D info/fontopia.info* %{buildroot}%{_infodir}/fontopia.info

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
%{_docdir}/fontopia
%exclude %{_docdir}/fontopia/COPYING
%license COPYING

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-9
- Bugfixes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-4
- Bugfixes in the BDF module

* Sat May 12 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-3
- Added missing copyright notice for ChangeLog file
- Updated configure.ac script, README, manpage and info page

* Fri May 11 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-2
- Added THANKS file and fixed missing copyright notices

* Mon May 7 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-1
- Added support for PCF fonts
- Added the Extended Glyph Operations window

* Mon Aug 15 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.7-1
- Improved BDF support (needs more testing)
- Uknown glyph unicodes show uniformly

* Thu Aug 11 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.6-1
- Multiple CP fonts per file (up to 4) can be edited
- Corrected a bug in bdf_write_to_file() and fontopia_show_readme()

* Mon Aug 08 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.5-1
- Fixed a buffer-overflow bug in export_unitab()

* Thu Aug 04 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.4-1
- Fixed a memory-corruption bug in handle_hw_change() function
- Added bdf_helper.c and bdf_hash.c so now BDF module can read
  glyph names in PostScript char names and Adobe Std Encoding names.

* Mon Aug 01 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.3-1
- Fixed a bug in calc_max_zoom() function
- Fixed a bug in load_font_file() function

* Wed Jan 27 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-4
- Fixed spec file

* Tue Jan 26 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-3
- Fixed spec file 

* Sun Jan 10 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-2
- Fixed spec file

* Sat Jan 09 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-1
- Included CP files as part of the executable

* Fri Jan 08 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-2
- Fixed spec file

* Fri Dec 11 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-1
- First release
