%define         xulrunner_still_beta   1
#%%define         betaver                svn3690_trunk

#
# When changing release number, please make it sure that
# the new EVR won't be higher than the one of higher branch!!
#
# Currently this spec file does not support libgda module.
# libgda-2 is needed, API change for libgda-3 needs investigation
# - Mamoru Tasaka

%define ruby_base_req ruby(release)

%undefine __brp_mangle_shebangs

Name:           ruby-gnome2
Version:        0.90.4
#
# When changing release number, please make it sure that
# the new EVR won't be higher than the one of higher branch!!
#
Release:        23%{?dist}
Summary:        Ruby binding of libgnome/libgnomeui-2.x

# SPDX confirmed
License:        LGPL-2.1-only AND LGPL-2.1-or-later
URL:            http://ruby-gnome2.sourceforge.jp/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-all-%{version}.tar.gz
#Source0:        %{name}-all-%{version}-%{betaver}.tar.gz
Patch1:         ruby-gnome2-0.90.4-newpng.patch
# Fix for build error with gcc8 -O2 + ruby 2.5, rb_funcall argument number fix
Patch4:         ruby-libart-arglength-fix.patch
Patch6:         ruby-gnome2-rb_secure.patch
Patch14:        ruby-gnome2-implicit-int-7.patch
Patch15:        ruby-gnome2-c99.patch


BuildRequires:  make
BuildRequires:  ruby ruby-devel gtk2-devel libgnome-devel libgnomeui-devel
# pkg-config.rb moved to rubygem-pkg-config, and now this is needed for BR
BuildRequires:  rubygem(pkg-config)
# The following line must actually be fixed in rubygem-pkg-config side.
# Will surely fix.
BuildRequires:  gcc
BuildRequires:  rubygems
BuildRequires:  %ruby_base_req

# Add system wide library (not ruby-gnome2 internal) to BR
BuildRequires:  rubygem-glib2-devel

Requires:       %ruby_base_req
Requires:       ruby(gnomecanvas2) = %{version}-%{release}

Provides:       ruby(gnome2) =  %{version}-%{release}

%description
Ruby/GNOME2 is a Ruby binding of libgnome/libgnomeui-2.x.

%package devel
Summary:        Development libraries and header files for ruby-gnome2
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gnome2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnome2-devel) = %{version}-%{release}

%description devel
Ruby/GNOME2 is a Ruby binding of libgnome/libgnomeui-2.x.
This package provides libraries and header files for ruby-gnome2

%package -n ruby-bonobo2
Summary:        Ruby binding of libbonobo-2.x
License:        LGPL-2.1-only

BuildRequires:  ruby ruby-devel
BuildRequires:  libbonoboui-devel

Requires:       %ruby_base_req ruby(gtk2) >= %{version}

Provides:       ruby(bonobo2) = %{version}-%{release}

%description -n ruby-bonobo2
Ruby/Bonobo2 is a Ruby binding of libbonobo-2.x.

%package -n ruby-bonobo2-devel
Summary:        Development libraries and header files for ruby-bonobo2
License:        LGPL-2.1-only

Requires:       ruby(bonobo2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(bonobo2-devel) = %{version}-%{release}

%description -n ruby-bonobo2-devel
Ruby/Bonobo2 is a Ruby binding of libbonobo-2.x.
This package provides libraries and header files for ruby-bonobo2

%package -n ruby-bonoboui2
Summary:        Ruby binding of libbonoboui-2.x
License:        LGPL-2.1-only

BuildRequires:  ruby ruby-devel
BuildRequires:  libbonoboui-devel libgnomeui-devel
BuildRequires:  rubygem-gtk2-devel

Requires:       %ruby_base_req ruby(gnome2) = %{version}-%{release}

Provides:       ruby(bonoboui2) = %{version}-%{release}

%description -n ruby-bonoboui2
Ruby/BonoboUI2 is a Ruby binding of libbonoboui-2.x.

%package -n ruby-bonoboui2-devel
Summary:        Development libraries and header files for ruby-bonoboui2
License:        LGPL-2.1-only

Requires:       ruby(bonoboui2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(bonoboui2-devel) = %{version}-%{release}

%description -n ruby-bonoboui2-devel
Ruby/BonoboUI2 is a Ruby binding of libbonoboui-2.x.
This package provides libraries and header files for ruby-bonoboui2

%package -n ruby-gconf2
Summary:        Ruby binding of GConf-2.x
License:        LGPL-2.1-only AND LGPL-2.1-or-later

BuildRequires:  ruby ruby-devel GConf2-devel

Requires:       %ruby_base_req ruby(glib2) >= %{version}

Provides:       ruby(gconf2) =  %{version}-%{release}

%description -n ruby-gconf2
Ruby/GConf2 is a Ruby binding of GConf-2.x.

%package -n ruby-gconf2-devel
Summary:        Development libraries and header files for ruby-gconf2
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gconf2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gconf2-devel) = %{version}-%{release}

%description -n ruby-gconf2-devel
Ruby/GConf2 is a Ruby binding of GConf-2.x.
This package provides libraries and header files for ruby-gconf2

%package -n ruby-gnomecanvas2
Summary:        Ruby binding of GnomeCanvas-2.x
License:        LGPL-2.1-only AND LGPL-2.1-or-later

BuildRequires:  ruby ruby-devel gtk2-devel libgnomecanvas-devel

Requires:       %ruby_base_req
Requires:       ruby(gtk2) >= %{version} 
Requires:       ruby(libart2) = %{version}-%{release}

Provides:       ruby(gnomecanvas2) =  %{version}-%{release}

%description -n ruby-gnomecanvas2
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.

%package -n ruby-gnomecanvas2-devel
Summary:        Development libraries and header files for ruby-gnomecanvas2
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gnomecanvas2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnomecanvas2-devel) = %{version}-%{release}

%description -n ruby-gnomecanvas2-devel
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.
This package provides libraries and header files for ruby-gnomecanvas2

%package -n ruby-gnomevfs
Summary:        Ruby binding of GnomeVFS-2.0.x
License:        LGPL-2.1-only AND LGPL-2.1-or-later

BuildRequires:  ruby ruby-devel gnome-vfs2-devel

Requires:       %ruby_base_req
Requires:       ruby(glib2) >= %{version}

Provides:       ruby(gnomevfs) =  %{version}-%{release}

%description -n ruby-gnomevfs
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.

%package -n ruby-gnomevfs-devel
Summary:        Development libraries and header files for ruby-gnomevfs
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gnomevfs) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnomevfs-devel) = %{version}-%{release}

%description -n ruby-gnomevfs-devel
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.
This package provides libraries and header files for ruby-gnomevfs

%package -n ruby-gtkglext
Summary:        Ruby binding of GtkGLExt
License:        LGPL-2.1-only AND LGPL-2.1-or-later

BuildRequires:  ruby ruby-devel gtk2-devel gtkglext-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gtk2-devel) = %{version}

Requires:       %ruby_base_req
Requires:       rubygem(ruby-opengl)
Requires:       ruby(gtk2) >= %{version}

Provides:       ruby(gtkglext) = %{version}-%{release}

%description -n ruby-gtkglext
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.

%package -n ruby-gtkglext-devel
Summary:        Development libraries and header files for ruby-gtkglext
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gtkglext) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gtkglext-devel) = %{version}-%{release}

%description -n ruby-gtkglext-devel
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.
This package provides libraries and header files for ruby-gtkglext

%package -n ruby-libart2
Summary:        Ruby binding of Libart_lgpl
License:        LGPL-2.1-only

BuildRequires:  ruby ruby-devel libart_lgpl-devel libpng-devel libjpeg-devel
#BuildRequires:  ruby(glib2-devel) = %{version}

Requires:       %ruby_base_req

Provides:       ruby(libart2) = %{version}-%{release}

%description -n ruby-libart2
Ruby/Libart2 is a Ruby binding of Libart_lgpl. 

%package -n ruby-libart2-devel
Summary:        Development libraries and header files for ruby-libart2
License:        LGPL-2.1-only

Requires:       ruby(libart2) = %{version}-%{release}
Requires:       libart_lgpl-devel ruby-devel
Requires:       pkgconfig

Provides:       ruby(libart2-devel) = %{version}-%{release}

%description -n ruby-libart2-devel
Ruby/Libart2 is a Ruby binding of Libart_lgpl. 
This package provides libraries and header files for ruby-libart2


%package -n ruby-libglade2
Summary:        Ruby bindings of Libglade2
License:        LGPL-2.1-only

BuildRequires:  ruby ruby-devel gtk2-devel libgnome-devel libglade2-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gnome2) = %{version}

Requires:       %ruby_base_req
Requires:       ruby(gtk2) >= %{version}
Requires:       ruby(gnome2) = %{version}-%{release}

Provides:       ruby(libglade2) = %{version}-%{release}

%description -n ruby-libglade2
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This provides a very simple interface to the libglade library,
to load interfaces dynamically from a glade file.

%package -n ruby-libglade2-devel
Summary:        Development libraries and header files for ruby-libglade2
License:        LGPL-2.1-only

Requires:       ruby(libglade2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(libglade2-devel) = %{version}-%{release}

%description -n ruby-libglade2-devel
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This package provides libraries and header files for ruby-libglade2

%prep
%setup -q -n %{name}-all-%{version}
#%%setup -q -n %{name}-all-%{version}-%{betaver}

# Remove diretories no longer going to build
rm -rf \
	atk \
	gdk_pixbuf2 \
	gio2 \
	glib2 \
	gtk2 \
	gtkhtml2 \
	panel-applet \
	pango \
	poppler \
	rsvg2 \
	vte \
	goocanvas \
	gstreamer \
	gnomeprint \
	gnomeprintui \
	gtkmozembed \
	gtksourceview \
	gtksourceview2 \
	%{nil}
sed -i extconf.rb \
	-e 's|^priorlibs.*$|priorlibs\t= []|'

%patch -P1 -p1 -b .newpng
%patch -P4 -p1 -b .rb25
%patch -P6 -p1
%patch -P14 -p1
%patch -P15 -p1

# Fix /usr/local
grep -rl /usr/local/bin . | grep -v ChangeLog | \
	xargs -r sed -i -e 's|/usr/local/bin|/usr/bin|g'

# Keep timestamps as much as possible
find . -type f -name depend | xargs sed -i -e 's|-m 0644 -v|-m 0644 -p -v|'

# Fix the attributes of some files
# suppress lots of messages..
set +x
find . -name \*.rb -or -name \*.c | while read f ; do
        chmod 0644 $f
done
set -x

sed -i.config \
	-e 's|\([( \+]\)Config:|\1RbConfig:|g' \
	extconf.rb run-test.rb

# ruby 3 build fix
sed -i.ruby3 \
	gtkglext/src/rbgtkglext.c \
	-e 's|EXTERN|RUBY_EXTERN|'

# ruby 3.2 build fix
grep -rl rb_cData . | xargs sed -i.ruby32 -e 's|rb_cData|rb_cObject|'

# cleanup
# find . -type d -path '*/sample/*.svn' | sort -r | xargs rm -rf

# Kill tainted feature, fix -Werror=implicit-funciton-declaration
sed -i gnomevfs/src/gnomevfs-file.c \
	-e 's|rb_tainted_str_new|rb_str_new|'

%build
export CFLAGS="$RPM_OPT_FLAGS -Werror=implicit-function-declaration"
ruby extconf.rb --vendor

make %{?_smp_mflags} -k

%install
mkdir -p $RPM_BUILD_ROOT%{ruby_vendorarchdir}
mkdir -p $RPM_BUILD_ROOT%{ruby_vendorlibdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}

export pkgconfigdir=$RPM_BUILD_ROOT%{_libdir}/pkgconfig
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p" \
    ruby=ruby \
    %{nil}

# Handle manually
# ????
install -cpm 0755 */src/*.so \
    $RPM_BUILD_ROOT%{ruby_vendorarchdir}
install -cpm 0755 libglade/bin/ruby-glade-create-template \
    $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT/bin

%files
%doc gnome/README gnome/ChangeLog gnome/COPYING.LIB gnome/sample
%doc AUTHORS NEWS
%{ruby_vendorlibdir}/gnome2.rb
%{ruby_vendorarchdir}/gnome2.so

%files devel
%{_libdir}/pkgconfig/ruby-gnome2.pc

%files -n ruby-bonobo2
%doc bonobo/ChangeLog bonobo/COPYING.LIB bonobo/README
%{ruby_vendorlibdir}/bonobo2.rb
%{ruby_vendorarchdir}/bonobo2.so

%files -n ruby-bonobo2-devel
%{_libdir}/pkgconfig/ruby-bonobo2.pc

%files -n ruby-bonoboui2
%doc bonoboui/ChangeLog bonoboui/COPYING.LIB bonoboui/README
%{ruby_vendorlibdir}/bonoboui2.rb
%{ruby_vendorarchdir}/bonoboui2.so

%files -n ruby-bonoboui2-devel
%{_libdir}/pkgconfig/ruby-bonoboui2.pc

%files -n ruby-gconf2
%doc gconf/ChangeLog gconf/COPYING.LIB gconf/README gconf/sample
%{ruby_vendorlibdir}/gconf2.rb
%{ruby_vendorarchdir}/gconf2.so

%files -n ruby-gconf2-devel
%{_libdir}/pkgconfig/ruby-gconf2.pc

%files -n ruby-gnomecanvas2
%doc gnomecanvas/ChangeLog gnomecanvas/COPYING.LIB gnomecanvas/README gnomecanvas/sample
%{ruby_vendorlibdir}/gnomecanvas2.rb
%{ruby_vendorarchdir}/gnomecanvas2.so

%files -n ruby-gnomecanvas2-devel
%{_libdir}/pkgconfig/ruby-gnomecanvas2.pc

%files -n ruby-gnomevfs
%doc gnomevfs/ChangeLog gnomevfs/COPYING.LIB gnomevfs/README
%{ruby_vendorlibdir}/gnomevfs.rb
%{ruby_vendorarchdir}/gnomevfs.so

%files -n ruby-gnomevfs-devel
%{_libdir}/pkgconfig/ruby-gnomevfs.pc

%files -n ruby-gtkglext
%doc gtkglext/ChangeLog COPYING.LIB gtkglext/README gtkglext/README.rbogl gtkglext/sample
%{ruby_vendorlibdir}/gtkglext.rb
%{ruby_vendorarchdir}/gtkglext.so

%files -n ruby-gtkglext-devel
%{_libdir}/pkgconfig/ruby-gtkglext.pc

%files -n ruby-libart2
%doc libart/ChangeLog libart/COPYING.LIB libart/README libart/sample
%{ruby_vendorlibdir}/libart2.rb
%{ruby_vendorarchdir}/libart2.so

%files -n ruby-libart2-devel
%{ruby_vendorarchdir}/rbart.h
%{_libdir}/pkgconfig/ruby-libart2.pc

%files -n ruby-libglade2
%doc libglade/ChangeLog libglade/COPYING.LIB libglade/README libglade/sample
%{_bindir}/ruby-glade-create-template
#%%{ruby_vendorlibdir}/libglade2.rb
%attr(755, root, root) %{ruby_vendorlibdir}/libglade2.rb
%{ruby_vendorarchdir}/libglade2.so

%files -n ruby-libglade2-devel
%{_libdir}/pkgconfig/ruby-libglade2.pc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-22
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-20
- SPDX migration

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 0.90.4-17
- Fix C compatibility issues (#2256908)

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-16
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sun Oct 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-15
- Remove patches applied for the components which are no longer built

* Wed Oct  4 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-14
- Clean up subdirectories in advance no longer being built
- No longer use tainted function and fix build with -Werror=implicit-function-declaration

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 28 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-12
- Change BR: ruby-cairo-devel to rubygem-cairo-devel

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-11.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-11.1
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Fri Dec  2 2022 Florian Weimer <fweimer@redhat.com> - 0.90.4-11
- Port to C99

* Wed Oct  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-10
- Fix build with ruby3.2 wrt rb_cData removal

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-9.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-9.9
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-9.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-9.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-9.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-9.5
- F-34: rebuild against ruby 3.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-9.4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-9.1
- F-32: rebuild against ruby27

* Mon Aug 26 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-9
- Kill no-longer-working Obsoletes
- Remove gtksourceview2 BuildRequires, actually no longer needed

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-8.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-8.2
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-8
- Kill gtksourceview2 subpackage, already suplied by other package

* Wed Feb 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-7.9
- Fix build error on libart with gcc8 -O2 + ruby 2.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-7.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.90.4-7.7
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-7.6
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-7.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-7.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-7.2
- F-26: rebuild for ruby24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-7
- F-24: rebuild against ruby23

* Wed Jul  8 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.90.4-6
- Retire obsolete components

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-5
- Backport G_DEF_ERROR2 definition fix (bug 1213627)

* Thu Jan 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-4
- F-22: rebuild for ruby 2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Vít Ondruch <vondruch@redhat.com> - 0.90.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.90.4-2
- F-19: rebuild for ruby 2.0, with various strange workaround
- Kill no longer needed files more

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-1.9.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.90.4-1.9.3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.90.4-1.9.2
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-1.9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.4-1.9
- Fix dependency on ruby-gtkglext

* Wed Mar 07 2012 Vít Ondruch <vondruch@redhat.com> - 0.90.4-1.8
- Fix ruby(opengl) missing dependency.

* Mon Feb 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.90.4-1.7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-1.6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.rog> - 0.90.4-1.6
- Patch for new libpng

* Tue Aug  2 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.4-1.5
- Kill support for gtkhtml2 on F-16+

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.4-1.4
- No longer build vte, already switched to gem
- Kill BR: gnome-panel-devel on F-15+
- F-16: kill gtkmozembed for now

* Sat Mar  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.4-1.3
- Kill panelapplet2, it won't build with GNOME3
- Delete modules which are already converted into gem form

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-1.2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.90.4-1.2.1
- rebuild (poppler)

* Sat Dec 18 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-15: rebuild against new poppler

* Sun Nov  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.4-1.1
- Patch for GLib 2.27.1 API
- F-15: rebuild against new poppler

* Mon Oct 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.4-1
- 0.90.4

* Sun Oct 24 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.3-1
- 0.90.3

* Tue Oct 05 2010 jkeating - 0.90.2-1.1
- Rebuilt for gcc bug 634757

* Mon Oct  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-1.2
- Use upstream patch for poppler 0.15.0 issue

* Sat Oct  2 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-1.1
- F-15: patch for poppler 0.15.0

* Mon Sep 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-1
- 0.90.2

* Sun Sep 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.1-2
- Change ruby-gtk2 part inter-dependencies from "equality" to "not less than"
  for preparation for introducing ruby-gtk2 part gems

* Fri Sep 24 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.1-1
- 0.90.1

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.19.4-3.1
- rebuild (poppler)

* Tue Jun 22 2010 Matthias Clasen <mclasen@redhat.com> - 0.19.4-2
- Rebuild against new poppler

* Fri May  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-13+: rebuild

* Thu Apr 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.4-1
- Update to 0.19.4, drop all upstreamed patches

* Fri Nov 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.3-5
- Patch to compile with xulrunner 1.9.2

* Sat Nov  7 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- release++

* Sun Nov  1 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- release++

* Sun Sep 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.3-2
- Fix crash when moving cursor on fantasdic 1.0 beta 7
  (ruby-gnome2-Bugs-2865895)

* Fri Sep 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.3-1
- Update to 0.19.3
- Released source does not support gio yet

* Sat Sep 19 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Try rev 3690
- Massive pkgconfig files renaming
- Enable gio support

* Thu Sep 10 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- release++

* Mon Aug  3 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.1-1
- Update to 0.19.1, drop all upstreamed patches
- Introduce many -devel subpackages containing pkgconfig file

* Sun Jul 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.0-4
- F-12: Mass rebuild

* Thu Jul 09 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.0-3
- Make ruby-gtkglext require ruby(opengl)

* Wed Jul 01 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.0-2
- Install more needed header files in ruby-gtk2-devel (bug 509035)
- Keep timestamps on installed header files

* Tue Jun 30 2009 Christopher Aillon <caillon@redhat.com>
- Rebuild against newer gecko

* Thu Jun 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.0-1
- Update to 0.19.0

* Mon Apr 27 2009 Christopher Aillon <caillon@redhat.com> - 0.18.1-7
- Rebuild against newer gecko

* Sat Mar 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.18.1-6
- Bump release again

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 26 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.18.1-3
- Bump release
- Patch to compile panel-applet
- Take care of directory owership (bug 474608)

* Thu Nov 13 2008 Allisson Azevedo <allisson@gmail.com> 0.18.1-1
- Update to 0.18.1

* Mon Oct  6 2008 Allisson Azevedo <allisson@gmail.com> 0.18.0-1
- Update to 0.18.0
- Removed ruby-gnome2-0.17.0-bz456816.patch

* Thu Sep 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.17.0-3
- Patch from svn to fix Ruby/Glib bug (bug 456816)

* Fri Sep 12 2008 Allisson Azevedo <allisson@gmail.com> 0.17.0-2
- Rebuild against new gstreamer-devel

* Tue Sep  9 2008 Allisson Azevedo <allisson@gmail.com> 0.17.0-1
- Update to 0.17.0
- Removed ruby-gnome2-0.17.0-rc1-newgtk-021303.patch

* Sat Jul 19 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.17.0-0.4.rc1
- F-9+: relax gecko libs dependency
- F-9+: bump version to fix EVR problem between F-8 branch

* Sun Jun 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.17.0-0.2.rc1
- F-10: gtk/gtkfilesystem.h is removed from GTK 2.13.3+, some symbols no
  longer available (bug 451402, thanks to Matthias Clasen)

* Sun Jun  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.17.0-0.1.rc1
- 0.17.0 rc1
- Remove upstreamed patches - 2 patches remain
  - ruby-gnome2-0.17.0-rc1-script.patch
  - ruby-gnome2-all-0.16.0-xulrunner.patch
- Restrict ruby abi dependency to exact 1.8 version
- Fix the license (to strict LGPLv2)

* Thu Mar 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.16.0-28
- Workarround for poppler 0.7.2

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.16.0-27
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-26
- Add BR: poppler-glib-devel

* Sat Jan 26 2008 Allisson Azevedo <allisson@gmail.com> 0.16.0-25
- Fix libglade2 Undefined method error (bugzilla #428781)

* Fri Jan 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-24
- Remove workaround for ruby static archive (#428384 solved)
- Add BR: gecko-devel-unstable

* Sun Dec 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-23
- Revert the wrong patch against src/lib/gtkmozembed.rb

* Sun Dec 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-22
- Update xulrunner patch (#402591)
- Some misc fix for maybe glib2 >= 2.15.0
- Workarround for #226381 c11

* Fri Dec 28 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-21
- Add xulrunner patch from bugzilla #402591
- Rebuild against gecko-lib 1.9 (xulrunner)

* Tue Dec  4 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-20
- Fix CVE-2007-6183, format string vulnerability (bugzilla #402871)

* Tue Dec  4 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-19
- Back to building against gecko 1.8.1.10 (firefox) until #402591 is 
  fixed.

* Sun Dec  2 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-18
- Rebuild against gecko-lib 1.9 (xulrunner)

* Tue Nov 27 2007 Christopher Aillon <caillon@redhat.com> 0.16.0-17
- Rebuild against newer gecko

* Tue Nov 13 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-16
- Fix my typo in BuildRequires

* Tue Nov 13 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-15
- Rebuild against gecko-libs and gecko-devel (firefox 2.0.0.9).

* Thu Oct 25 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-14
- Rebuild against gecko-libs and gecko-devel

* Wed Oct 24 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-13
- Rebuild against new firefox

* Thu Sep 13 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-12
- Newpoppler.patch updated for poppler 0.6

* Sat Sep  8 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-11
- Rebuild against new poppler
- Changed license to LGPLv2+

* Thu Aug  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-10
- Adjust to GLib 2.14 API + typo fix in glib module

* Thu Aug  9 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-9
- Rebuild against new firefox

* Fri Aug  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-8
- Apply patch extracted from CVS to build glib gtk poppler

* Fri Jul 20 2007 Jesse Keating <jkeating@redhat.com> 0.16.0-7
- Rebuild against new firefox

* Thu May 31 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-6
- New gecko engine

* Mon Apr 9 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-5
- Changed buildrequires and requires

* Mon Apr 9 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-4
- Changed buildrequires and requires

* Mon Apr 9 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-3
- Changed buildrequires and requires
- Changed license for LGPL

* Mon Apr 2 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-2
- Changed buildrequires and requires
- Changed make install for keep timestamps
- Changed package summary

* Sun Mar 24 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-1
- Initial RPM release
- Thanks Stephanos Manos for base spec
