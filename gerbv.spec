# gerbv Package description for Fedora/Free Electronic Lab
#
Name:             gerbv
Version:          2.9.2
Release:          2%{?dist}
Summary:          Gerber file viewer from the gEDA toolkit
License:          GPLv2
URL:              https://github.com/gerbv/gerbv
Source:           https://github.com/gerbv/gerbv/archive/refs/tags/v%{version}.tar.gz
# Report upstream about bad tag version naming. Should be :
#Source:           https://github.com/gerbv/gerbv/archive/refs/tags/%%{name}-%%{version}.tar.gz
# Report upstream about bad tag version naming : WARNING: Cannot download url: https://github.com/gerbv/gerbv/archive/refs/tags/gerbv-2.9.2.tar.gz


BuildRequires:    gcc-c++
BuildRequires:    make
BuildRequires:    automake
BuildRequires:    gettext-devel
BuildRequires:    libtool
BuildRequires:    desktop-file-utils
BuildRequires:    ImageMagick-devel
BuildRequires:    libpng-devel
BuildRequires:    pkgconfig(gtk+-2.0)

#Requires:         electronics-menu

%description
Gerber Viewer (gerbv) is a viewer for Gerber files. Gerber files
are generated from PCB CAD system and sent to PCB manufacturers
as basis for the manufacturing process. The standard supported
by gerbv is RS-274X.

gerbv also supports drill files. The format supported are known
under names as NC-drill or Excellon. The format is a bit undefined
and different EDA-vendors implement it different.

gerbv is listed among Fedora Electronic Lab (FEL) packages.


%package      doc
Summary:          Documentation for %{name}
BuildArch:        noarch

%description  doc
Examples and documentation files for %{name}.

%package      devel
Summary:          Header files, libraries and development documentation for %{name}
Requires:         %{name} = %{version}-%{release}

%description  devel
This package contains the header files, libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%autosetup
# use explicit version for compilation and not a git-derived one
sed -i -e "s/m4_esyscmd(utils\/git-version-gen.sh [0-9.]*)/%{version}/" configure.ac


%build
./autogen.sh
# default measurement units set to millimeters
%configure                              \
  --enable-unit-mm                      \
  --disable-update-desktop-database     \
  --disable-static   --disable-rpath    \
  CFLAGS="%{build_cflags}"              \
  LDFLAGS="%{build_ldflags}"
#  CFLAGS="${RPM_OPT_FLAGS}"             \
#  LIBS="-ldl -lpthread"

# Don't use rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# Clean unused-direct-shlib-dependencies. This should have been already removed in 2.5.0-2 ?
#sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%install
%make_install

desktop-file-install --vendor ""               \
    --remove-category Education                \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original                          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%{__rm} -f %{buildroot}%{_libdir}/libgerbv.la
%{__rm} -f  {doc,example}/Makefile*

pushd example/
for dir in * ; do
  [ -d $dir ] && %{__rm} -f $dir/Makefile*
done
popd

pushd doc/
for dir in * ; do
  [ -d $dir ] && %{__rm} -f $dir/Makefile*
done
popd

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README.md CONTRIBUTORS HACKING
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/gerbv.*
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.geda-user.gerbv.gschema.xml
%{_libdir}/lib%{name}.so.1*

%files doc
%doc example/
%doc doc/example-code
%doc doc/eagle
%doc doc/sources.txt
%doc doc/aperturemacro.txt
%doc doc/PNG-print

%files devel
%dir %{_includedir}/%{name}-%{version}
%{_includedir}/%{name}-%{version}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libgerbv.pc


%Changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Alain Vigne <avigne@fedoraproject.org> - 2.9.2-1
- new upstream release

* Mon Apr 18 2022 Alain Vigne <avigne@fedoraproject.org> - 2.8.2-1
- Project is forked. Now maintained in GitHub
- Split doc into -doc package

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 2.7.0-6
- Enable legacy common support

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.7.0-2
- Explicitely BR a C++ compiler, to solve FTBFS: libtool did not build the shared lib. libgerbv.so.1*
- Simplify .spec file

* Sun Feb 03 2019 Alain <alain DOT vigne DOT 14 AT gmail DOT com> - 2.7.0-1
- new upstream release
- add patch to cope with gcc compiler options. Upstream has updated this, for next release => Remove the patch for > 2.7.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.6.2-1
- new upstream release 2.6.2 fixes rhbz #1100403

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.6.0-14
- spec cleanup / modernization

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.0-12
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 03 2012 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.6.0-1
- new upstream release

* Tue Jul 05 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-2
- Hack libtool to not add rpath.
- Propagate RPM_OPT_FLAGS to CFLAGS.
- Pass -ldl through LIBS.
- Fix date of previous changelog entry.
- Remove "unused-direct-shlib-dependencies" libtool hacking.

* Sun Jul 03 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.5.0-1
- new upstream release

* Thu Jul 01 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.4.0-1
- new upstream release

* Sun Sep 13 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.3.0-3
- Fixed gerbv-2.3.0-1 png failed to open - FEL ticket #47
- Fixed bug 2841371 (segfault on edit->orientation with no layer loaded)

* Sat Jul 11 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.3.0-1
- new upstream release

* Sat Mar 07 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.2.0-3
- added requires electronics-menu #485585

* Thu Jan 22 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.2.0-1
- new upstream release

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.0-3
- Include unowned headers directory.

* Thu Nov 13 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.1.0-2
- BR ImageMagick-devel added

* Thu Nov 13 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.1.0-1
- New upstream release and split into -devel package

* Fri Feb 01 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.0.0-1
- New upstream release

* Tue Dec 04 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0.3-1
- new upstream release

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0.2-3
- mass rebuild for fedora 8 - ppc

* Thu Jun 28 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0.2-2
- remove gdk-pixbuf-devel as BR

* Thu Sep 14 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0.2-1
- Initial package for Fedora Core
