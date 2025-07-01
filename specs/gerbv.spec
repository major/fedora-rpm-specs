Name:             gerbv
Version:          2.10.0
Release:          %autorelease
Summary:          Gerber file viewer from the gEDA toolkit
License:          GPL-2.0-only
URL:              https://github.com/gerbv/gerbv
Source:           https://github.com/gerbv/gerbv/archive/refs/tags/%{name}-%{version}.tar.gz

# https://github.com/gerbv/gerbv/issues/255
Patch0:           gerbv-2.10.0-Fix-Fails-GCC15.patch

# fix for https://bugzilla.redhat.com/show_bug.cgi?id=2331596
Requires:         gdk-pixbuf2-modules-extra

BuildRequires:    gcc-c++
BuildRequires:    make
BuildRequires:    automake
BuildRequires:    gettext-devel
BuildRequires:    libtool
BuildRequires:    desktop-file-utils
BuildRequires:    ImageMagick-devel
BuildRequires:    libpng-devel
BuildRequires:    pkgconfig(gtk+-2.0)

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
%autosetup -p1
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


%changelog
%autochangelog
