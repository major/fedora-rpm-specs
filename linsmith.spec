Name:           linsmith
Version:        0.99.31
Release:        10%{?dist}
Summary:        A Smith charting program

License:        GPLv2
URL:            http://jcoppens.com/soft/linsmith/index.en.php
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils gettext libgnomeui-devel
BuildRequires: make
Requires:       electronics-menu tcl

%description
linSmith is a Smith Charting program.
It's main features are:
  * Definition of multiple load impedances
  * Addition of discrete and line components
  * A 'virtual' component switches from impedance
    to admittance to help explaining parallel components
  * The chart works in real impedances
  * Load and circuit configuration is stored separately,
    permitting several solutions without re-defining the other

%prep
%autosetup

%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure
%make_build


%install
%make_install

desktop-file-install \
    --dir=%{buildroot}/%{_datadir}/applications \
    --delete-original                           \
    --remove-category GTK                       \
    --remove-category GNOME                     \
    --add-category "Electronics"                \
    %{_builddir}/%{name}-%{version}/%{name}.desktop

# icon
cp -p linsmith_icon.xpm %{buildroot}/%{_datadir}/pixmaps/%{name}/

# man file
%{__mkdir} -p %{buildroot}/%{_datadir}/man/man1
cp -p doc/linsmith.1 %{buildroot}/%{_datadir}/man/man1

#examples
mv %{buildroot}/%{_datadir}/%{name} examples/

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS doc/manual.pdf examples/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_datadir}/man/man1/%{name}.1.gz


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.99.31-5
- Fix FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.99.31-1
- Update to new upstream version 0.99.31 + spec cleanup and modernization

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Filipe Rosset <rosset.filipe@gmail.com> - 0.99.30-1
- Rebuilt for new upstream version 0.99.30 fixes rhbz #1285579

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.99.28-1
- Rebuilt for new upstream version 0.99.28

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.99.26-1
- Rebuilt for new upstream version, spec cleanup, fixes rhbz #971701

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.99.24-3
- Drop desktop vendor tag.

* Fri Apr 19 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.99.24-2
- Use autoreconf

* Fri Mar 15 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.99.24-1
- Updated package to 0.99.24 upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.99.12-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.99.12-1
- new upstream release
- fixes segmentation fault during saving of log

* Wed Jan 07 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.99.11-4
- fixed vendor

* Wed Jan 07 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.99.11-3
- added vendor to skip build failure on EL-5

* Mon Dec 29 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.99.11-2
- spec file updated as suggested in the #478368c2

* Mon Dec 29 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.99.11-1
- Initial package
