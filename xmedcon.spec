Name:           xmedcon
Version:        0.22.0
Release:        2%{?dist}
Summary:        A medical image conversion utility and library

# Please refer to http://xmedcon.sourceforge.net/pub/readme/README for details
# None of the libraries are bundled, they are appear to be modified versions of code taken
# from the respective sources
# License needs more looking into to confirm correctness. All licenses are FOSS compatible though
License:        LGPLv2+ and Copyright only and MIT and BSD and libtiff
URL:            http://xmedcon.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         xmedcon-configure.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  libappstream-glib
BuildRequires:  libtpcimgio-devel
BuildRequires:  libtpcmisc-devel
BuildRequires:  make
BuildRequires:  nifticlib-devel

%description
This project stands for Medical Image Conversion and is released under the
GNU's (L)GPL license. It bundles the C source code, a library, a flexible
command-line utility and a graphical front-end based on the amazing Gtk+
toolkit.

Its main purpose is image conversion while preserving valuable medical
study information. The currently supported formats are: Acr/Nema 2.0,
Analyze (SPM), Concorde/uPET, DICOM 3.0, CTI ECAT 6/7, InterFile 3.3
and PNG or Gif87a/89a towards desktop applications.

%package devel
Summary: Libraries files for (X)MedCon development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The xmedcon-devel package contains the header and libraries necessary
for developing programs that make use of the (X)MedCon library (libmdc).


%prep
%autosetup

# Remove the sources of the nifti, since we're using fedora nifti here
rm -rvf ./libs/nifti/
rm -rvf ./libs/tpc/
# Removed the directories, so we stop Makefile from looking for them too
sed -ibackup  -e 's/nifti// ' -e 's/tpc//' libs/Makefile.am

# Hardcoded to lib, so I need to correct it everywhere
# easier with sed rather than a patch
sed -i \
       -e  "s|tpc_prefix/lib|tpc_prefix/%{_lib}|" \
       -e  "s|nifti_prefix/lib|nifti_prefix/%{_lib}|" configure.ac

# usr/etc eh?
sed -i 's|$(prefix)||' etc/Makefile.am

%build
autoreconf --install
%configure --disable-static --disable-rpath --with-nifti-prefix=%{_prefix} --with-tpc-prefix=%{_prefix} --enable-shared --includedir=%{_includedir}/xmedcon

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# the shell script can get the value from the system insteasd of hard coding it
# so we'll only have the one common script for all arches
sed -i 's|@libdir@|$(rpm -E %{_libdir})|' xmedcon-config.in

%make_build

%install
%make_install

mv -v $RPM_BUILD_ROOT/%{_includedir}/*.h $RPM_BUILD_ROOT/%{_includedir}/%{name}/

# Need to find a fix for rhbz#990230
# these two headers are arch dependent, so I'll name them accordingly and update any references
# mv -v $RPM_BUILD_ROOT/%{_includedir}/%{name}/m-config.h $RPM_BUILD_ROOT/%{_includedir}/%{name}/m-config-%{_arch}.h
# mv -v $RPM_BUILD_ROOT/%{_includedir}/%{name}/m-depend.h $RPM_BUILD_ROOT/%{_includedir}/%{name}/m-depend-%{_arch}.h
# update the one file that references them
# sed -i "s|m-depend\.h|m-depend-%{_arch}\.h|" $RPM_BUILD_ROOT/%{_includedir}/%{name}/m-defs.h

install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
install -m 0644 -p etc/%{name}.png -t $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_datadir}/appdata/*.appdata.xml

# remove static libraries
find $RPM_BUILD_ROOT -name "*.a" -execdir rm -fv '{}' \;
find $RPM_BUILD_ROOT -name "*.la" -execdir rm -fv '{}' \;

%ldconfig_scriptlets

%files
# leave out ChangeLog : zero length
%doc README REMARKS AUTHORS
%license COPYING COPYING.LIB
%config(noreplace) %{_sysconfdir}/xmedcon.css
%{_bindir}/medcon
%{_bindir}/%{name}
%{_libdir}/*so.*
%{_mandir}/man1/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%files devel
%doc README
%license COPYING COPYING.LIB
%{_mandir}/man3/*
%{_mandir}/man4/*
%{_libdir}/*.so
%{_datadir}/aclocal/*
%{_includedir}/%{name}/
%{_bindir}/%{name}-config

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 28 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.22.0-1
- Update to 0.22.0 fix rhbz#1902428

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.16.2-1
- Update to 0.16.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.16.1-1
- Update to latest upstream release 0.16.1 fixes rhbz #1566287

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.1-3
- Remove obsolete scriptlets

* Wed Jan 03 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.14.1-2
- Remove stray requires

* Sat Dec 30 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.14.1-1
- Update to latest upstream release
- remove png patch that isn't needed any more
- re-do configure patch
- use upstream appdata, remove our bit

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.10.7-15
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.10.7-11
- Fix for #904264

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 28 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.10.7-9
- Use Tom's patch to fix FTBFS because of libpng 1.5
- Details here: rhbz#843662

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.10.7-6
- Rebuild for new libpng

* Sun Nov 13 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.7-5
- Correct placements of includes and configure command
- RHBZ #753246

* Tue Aug 09 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.7-4
- Move xmedcon-config to -devel
- Correct requires for -devel
- Add icon, scriptlets
- Add desktop file, scriptlets
- Add a xmedconrc.linux file in docs
- Remove defattr

* Tue Aug 09 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.7-3
- Fix license tag
- remove rpath
- https://bugzilla.redhat.com/show_bug.cgi?id=714328#c3
- Fix sed

* Sun Jul 03 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.7-2
- Make it use fPIC

* Fri Jun 17 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.7-1
- Initial rpm build
- Based on the spec built by Erik Nolf for the srpm available at
- http://xmedcon.sourceforge.net/Main/Download

