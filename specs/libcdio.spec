Name: libcdio
Version: 2.3.0
Release: %autorelease
Summary: CD-ROM input and control library
# include/cdio/ecma_167.h and lib/driver/netbsd.c and lib/udf/udf_fs.c are BSD-2-Clause
# src/getopt* are LGPL-2.1-or-later
License: GPL-3.0-or-later AND BSD-2-Clause AND LGPL-2.1-or-later
URL: http://www.gnu.org/software/libcdio/
Source0: https://github.com/libcdio/libcdio/releases/download/%{version}/libcdio-%{version}.tar.bz2
Source2: libcdio-no_date_footer.hml
Source3: cdio_config.h

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig doxygen
BuildRequires: ncurses-devel
BuildRequires: help2man
BuildRequires: gettext-devel
BuildRequires: chrpath
BuildRequires: make

%description
This library provides an interface for CD-ROM access. It can be used
by applications that need OS- and device-independent access to CD-ROM
devices.

%package devel
Summary: Header files and libraries for %{name}
# doc/* is GFDL-1.2-or-later
License: GPL-3.0-or-later AND BSD-2-Clause AND LGPL-2.1-or-later AND GFDL-1.2-or-later
Requires: %{name} = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.


%prep
%autosetup

iconv -f ISO88591 -t utf-8 -o THANKS.utf8 THANKS && mv THANKS.utf8 THANKS

%build
%ifarch %{ix86}
# avoid implicit declaration of fseeko64, lseek64
export CPPFLAGS="$CPPFLAGS -D_LARGEFILE64_SOURCE"
%endif
%configure \
	--disable-vcd-info \
	--disable-dependency-tracking \
	--disable-cddb \
	--disable-static \
	--disable-rpath
%make_build

# another multilib fix; remove the architecture information from version.h
sed -i -e "s,%{version} .*$,%{version}\\\",g" include/cdio/version.h

cd doc/doxygen
sed -i -e "s,HTML_FOOTER.*$,HTML_FOOTER = libcdio-no_date_footer.hml,g; \
		s,EXCLUDE .*$,EXCLUDE = ../../include/cdio/cdio_config.h,g;" Doxyfile
cp %{SOURCE2} .
./run_doxygen

%install
%make_install

# multilib header hack; taken from postgresql.spec
case `uname -i` in
	i386 | x86_64 | ppc | ppc64 | s390 | s390x | sparc | sparc64 )
		mv $RPM_BUILD_ROOT%{_includedir}/cdio/cdio_config.h $RPM_BUILD_ROOT%{_includedir}/cdio/cdio_config_`uname -i`.h
		install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_includedir}/cdio
		;;
	*)
		;;
esac

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

rm -rf examples
mkdir -p examples/C++
cp -a example/{*.c,README} examples
cp -a example/C++/{*.cpp,README} examples/C++

# fix timestamps of generated man-pages
for i in cd-info iso-read iso-info cd-read cd-drive; do
	# remove build architecture information from man pages
	sed -i -e 's, version.*linux-gnu,,g' $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
	# remove libtool leftover from man pages
	sed -i -e 's,lt-,,g;s,LT-,,g' $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
	# fix timestamps to be the same in all packages
	touch -r src/$i.help2man $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
done

# remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/*.so.*

%check
# disable test using local CDROM
%{__sed} -i -e "s,testiso9660\$(EXEEXT),,g" \
	    -e "s,testisocd\$(EXEEXT),,g" \
	    -e "s,check_paranoia.sh check_opts.sh, check_opts.sh,g" \
	    test/Makefile
make check


%files
%license COPYING
%doc AUTHORS NEWS.md README.md README-libcdio.md THANKS TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_infodir}/*
%{_mandir}/man1/*


%files devel
%doc doc/doxygen/html examples
%{_includedir}/cdio
%{_includedir}/cdio++
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
%autochangelog
