Name:           libfakekey
Version:        0.3
%global so_version 0
Release:        %autorelease
Summary:        Library for converting characters to X key-presses

License:        LGPL-2.0-or-later
URL:            https://git.yoctoproject.org/cgit/cgit.cgi/libfakekey
Source:         %{url}/snapshot/libfakekey-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

# We stopped building PDF documentation in Fedora 42; we can remove this after
# Fedora 44 reaches end-of-life.
Obsoletes:      libfakekey-doc < 0.3-22

%description
libfakekey is a simple library for converting UTF-8 characters into 'fake' X
key-presses.

%package        devel
Summary:        Development files for libfakekey

Requires:       libfakekey%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xtst)

%description    devel
The libfakekey-devel package contains libraries and header files for developing
applications that use libfakekey.


%prep
%autosetup


%conf
# The tarball generated from the git tag has no configure script, so this is
# mandatory. See autogen.sh (which, however, we do not use because we need to
# use the %%configure macro).
autoreconf -f -i -v
%configure --disable-static


%build
%make_build


%install
%make_install


# The only test is more like a demo; running it is not valuable


%files
%license COPYING
%{_libdir}/libfakekey.so.%{so_version}{,.*}


%files devel
%{_includedir}/fakekey/
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc


%changelog
%autochangelog
