Name:           libdsk
Version:        1.5.22
Release:        %autorelease
Summary:        Library for accessing disk images
License:        LGPL-2.0-or-later
URL:            http://www.seasip.info/Unix/LibDsk
Source0:        http://www.seasip.info/Unix/LibDsk/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  make

%description
A library for accessing disk images, particularly for use with emulators.


%package devel
Summary:    Development files for libdsk
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for libdsk.


%package tools
Summary:    Tools for use with libdsk
Requires:   %{name} = %{version}

%description tools
Tools for use with libdsk.


%prep
%setup -q

# Fix dodgy permissions on files that end up in debuginfo package
find . -name '*.[ch]' | xargs chmod 0644

# EOL fixes for files that end up in the debuginfo package
sed -i 's/\r//' lib/*.h

# Character encoding fixes
iconv -f iso8859-1 doc/libdsk.txt -t utf8 > doc/libdsk.conv \
    && /bin/mv -f doc/libdsk.conv doc/libdsk.txt


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%ldconfig_scriptlets


%files
%{_libdir}/libdsk.so.*
%doc doc/COPYING ChangeLog TODO doc/libdsk.{pdf,txt}


%files tools
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*


%files devel
%{_libdir}/libdsk.so
%{_includedir}/libdsk.h
%doc doc/cfi.html doc/apridisk.html doc/protocol.txt


%changelog
%autochangelog
