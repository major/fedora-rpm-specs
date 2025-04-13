# Disable LTO
#ld: sha2.o (symbol from plugin): undefined reference to symbol 'SHA384_Final@@OPENSSL_1_1_0'
%global _lto_cflags %nil


Name:           sleuthkit
Version:        4.13.0
Release:        %autorelease
Summary:        The Sleuth Kit (TSK)

# Automatically converted from old format: CPL and IBM and GPLv2+ - review is highly recommended.
License:        CPL-1.0 AND IPL-1.0 AND GPL-2.0-or-later
URL:            https://www.sleuthkit.org
Source0:        https://github.com/sleuthkit/sleuthkit/archive/sleuthkit-%{version}/sleuthkit-%{version}.tar.gz
Patch0:         0001-Avoid-defining-bool-datatype.patch

BuildRequires: make
BuildRequires:  libtool

# afflib - BSD with advertising, GPL incompatible
BuildRequires:  gcc-c++
BuildRequires:  afflib-devel >= 3.3.4
# libewf - Newer versions are plain BSD (older are BSD with advertising)
BuildRequires:  libewf-devel
BuildRequires:  perl-generators
BuildRequires:  sqlite-devel

%{?_with_java:
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils

Requires:       java >= 1:1.6.0
Requires:       jpackage-utils
}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: file
Requires: mac-robber

%description
The Sleuth Kit (TSK) is a collection of UNIX-based command line tools that
allow you to investigate a computer. The current focus of the tools is the
file and volume systems and TSK supports FAT, Ext2/3, NTFS, UFS,
and ISO 9660 file systems


%package        libs
Summary:        Library for %{name}

%description    libs
The %{name}-libs package contains library for %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       sqlite-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
autoreconf -vif


%build
#export LIBS='-lpthread -ldl'
%configure --disable-static \
 %{!?_with_java:--disable-java}

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc ChangeLog.txt NEWS.txt
%license licenses/*
# License is CPL 1.0 exept for some files.
%{_bindir}/blkcalc
%{_bindir}/blkcat
%{_bindir}/blkls
%{_bindir}/blkstat
#{_bindir}/disk_sreset
#{_bindir}/disk_stat
#fcat conflicts with freeze fcat
%exclude %{_bindir}/fcat
%{_bindir}/ffind
%{_bindir}/fiwalk
%{_bindir}/fls
%{_bindir}/fsstat
%{_bindir}/hfind
%{_bindir}/icat
%{_bindir}/ifind
%{_bindir}/ils
%{_bindir}/img_cat
%{_bindir}/img_stat
%{_bindir}/istat
%{_bindir}/jcat
%{_bindir}/jpeg_extract
%{_bindir}/jls
# This file is described as GPL in the doc
# But the license remains CPL in the source.
%{_bindir}/mactime
##
%{_bindir}/mmcat
%{_bindir}/mmls
%{_bindir}/mmstat
%{_bindir}/pstat
%{_bindir}/sigfind
%{_bindir}/sorter
## This file is GPLv2+
%{_bindir}/srch_strings
%{_bindir}/tsk_comparedir
%{_bindir}/tsk_gettimes
%{_bindir}/tsk_imageinfo
%{_bindir}/tsk_loaddb
%{_bindir}/tsk_recover
%{_bindir}/usnjls
#
%{_mandir}/man1/blkcalc.1*
%{_mandir}/man1/blkcat.1*
%{_mandir}/man1/blkls.1*
%{_mandir}/man1/blkstat.1*
#{_mandir}/man1/disk_sreset.1*
#{_mandir}/man1/disk_stat.1*
%exclude %{_mandir}/man1/fcat.1*
%{_mandir}/man1/ffind.1*
%{_mandir}/man1/fls.1*
%{_mandir}/man1/fsstat.1*
%{_mandir}/man1/hfind.1*
%{_mandir}/man1/icat.1*
%{_mandir}/man1/ifind.1*
%{_mandir}/man1/ils.1*
%{_mandir}/man1/img_cat.1*
%{_mandir}/man1/img_stat.1*
%{_mandir}/man1/istat.1*
%{_mandir}/man1/jcat.1*
%{_mandir}/man1/jls.1*
%{_mandir}/man1/mactime.1*
%{_mandir}/man1/mmcat.1*
%{_mandir}/man1/mmls.1*
%{_mandir}/man1/mmstat.1*
%{_mandir}/man1/sigfind.1*
%{_mandir}/man1/sorter.1*
%{_mandir}/man1/tsk_comparedir.1*
%{_mandir}/man1/tsk_gettimes.1*
%{_mandir}/man1/tsk_loaddb.1*
%{_mandir}/man1/tsk_recover.1*
%{_mandir}/man1/usnjls.1.*
%dir %{_datadir}/tsk
%{_datadir}/tsk/sorter/

%files libs
# CPL and IBM
%{_libdir}/*.so.*

%files devel
# CPL and IBM
%{_includedir}/tsk/
%{_libdir}/*.so
%{_libdir}/pkgconfig/tsk.pc


%changelog
%autochangelog
