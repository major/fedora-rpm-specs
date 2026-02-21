# Specfile for DAR, the disk archiver
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=210790

# Static build is disabled by default by fedora policy, but also because the
# latest versions of glibc don't seem to compile proper static binaries.  Use
# "--with static" to enable the static subpackage
%define with_static %{?_with_static: 1} %{?!_with_static: 0}

Name:           dar
Version:        2.8.3
Release:        %autorelease
Summary:        Software for making/restoring incremental CD/DVD backups
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://dar.linux.free.fr
Source0:        ftp://ftp.dm3c.org/dar.linux.free.fr/Releases/Source_code/%{name}-%{version}.tar.gz
Source1:        README.Fedora

BuildRequires:  bzip2-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  gpgme-devel
BuildRequires:  libargon2-devel
BuildRequires:  libattr-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  librsync-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  rhash-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
Requires:       par2cmdline

%description
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extented attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.

%package -n libdar
Summary:    Library providing support for the DAR API

%description -n libdar
Common library code for DAR.

%package -n libdar-devel
Summary:    Development files for libdar
Requires:   libdar%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libdar-devel
This package contains the header files and libraries for developing
programs that use the DAR API (libdar).

# The following two subpackages are only built when enabled via "--with static"
%if %{with_static}

%package -n dar-static
Summary:    Statically linked version of dar

%description -n dar-static
Statically linked version of dar that can be installed onto backup disks for
easier file retrieval.

%package -n libdar-static-devel
Summary:    Statically linked dar library files

%description -n libdar-static-devel
Statically linked version of dar libraries that can be installed onto backup
disks for easier file retrieval.

%endif

%prep
%autosetup -n %{name}-%{version}

%build
# Options
%if %{with_static}
    STATIC=""
%else
    STATIC="--disable-dar-static --disable-static"
%endif

%configure --disable-build-html $STATIC --enable-mode=64

# Remove Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
%find_lang %{name}

# Remove the libtool archive files
rm -f  %{buildroot}/%{_libdir}/*.la

# Delete the sample files that we can't seem to disable
rm -rf %{buildroot}/%{_datadir}/dar/

# Remove the doc makefiles so they don't get installed along with the other files.
rm -f doc/Makefile*
rm -f doc/*/Makefile*

# Rename the documentation directory so it makes more sense after installation.
mv doc html

# Sample scripts should not be executable
chmod 0644 html/samples/*

# Install the fedora readme
cp -a %{SOURCE1} .

%ldconfig_scriptlets   -n libdar


%files -f %{name}.lang
%doc html/ AUTHORS ChangeLog COPYING NEWS README THANKS TODO README.Fedora

%{_bindir}/dar
%{_bindir}/dar_cp
%{_bindir}/dar_manager
%{_bindir}/dar_slave
%{_bindir}/dar_split
%{_bindir}/dar_xform
%config(noreplace) %{_sysconfdir}/darrc
%{_mandir}/man1/*

%files -n libdar
%{_libdir}/*.so.*

%files -n libdar-devel
%{_includedir}/dar/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%if %{with_static}

%files -n dar-static
%{_bindir}/dar_static

%files -n libdar-static-devel
%{_libdir}/*.a
%endif

%changelog
%autochangelog
