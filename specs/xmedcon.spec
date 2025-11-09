Name:           xmedcon
Version:        0.25.3
Release:        %autorelease
Summary:        A medical image conversion utility and library

# Please refer to http://xmedcon.sourceforge.net/pub/readme/README for details
# None of the libraries are bundled, they are appear to be modified versions of code taken
# from the respective sources
# License needs more looking into to confirm correctness. All licenses are FOSS compatible though
# Automatically converted from old format: LGPLv2+ and Copyright only and MIT and BSD and libtiff - review is highly recommended.
License:        LGPL-2.1-or-later AND LicenseRef-Callaway-Copyright-only AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD and libtiff
URL:            http://xmedcon.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         xmedcon-configure.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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

appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_datadir}/metainfo/xmedcon.appdata.xml

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
%{_datadir}/metainfo/xmedcon.appdata.xml
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
%autochangelog

