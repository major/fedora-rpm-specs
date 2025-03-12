# Where lock files are stored
%global _lockdir /run/lock/lockdev

%global checkout 20111007git
%global co_date  2011-10-07

#http://lists.fedoraproject.org/pipermail/devel/2011-August/155358.html
%global _hardened_build 1

Summary: A library for locking devices
Name: lockdev
Version: 1.0.4
Release: %autorelease -p -e %{checkout}
License: LGPL-2.1-or-later
URL: https://alioth.debian.org/projects/lockdev/

# This is a nightly snapshot downloaded via
# https://alioth.debian.org/snapshots.php?group_id=100443
Source0: lockdev-%{version}.%{checkout}.tar.gz

Patch1: lockdev-euidaccess.patch
Patch2: 0001-major-and-minor-functions-moved-to-sysmacros.h.patch

Requires(post): glibc
Requires(postun): glibc
Requires: systemd

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: systemd
BuildRequires: make

%description
Lockdev provides a reliable way to put an exclusive lock to devices
using both FSSTND and SVr4 methods.

%package devel
Summary: The header files for the lockdev library
Requires: lockdev = %{version}-%{release}

%description devel
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods. The lockdev-devel
package contains the development headers.


%prep
%setup -q -n lockdev-scm-%{co_date}

# Replace access() calls with euidaccess() (600636#c33)
%patch -P1 -p1 -b .access
%patch -P2 -p1

# Create a sysusers.d config file
cat >lockdev.sysusers.conf <<EOF
g lock 54
EOF

%build
# Generate version information from git release tag
./scripts/git-version > VERSION

# To satisfy automake
touch ChangeLog

# Bootstrap autotools
autoreconf --verbose --force --install

CFLAGS="%{optflags} -D_PATH_LOCK=\\\"%{_lockdir}\\\"" \
%configure --disable-static --enable-helper --disable-silent-rules

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

# %%ghosted, but needs to be in buildroot
# on reboot re-created by %%{_prefix}/lib/tmpfiles.d/legacy.conf
mkdir -p %{buildroot}%{_lockdir}

# install /usr/lib/tmpfiles.d/lockdev.conf (#1324184)
mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
cat > ${RPM_BUILD_ROOT}%{_tmpfilesdir}/lockdev.conf <<EOF
# See tmpfiles.d(5) for details

d %{_lockdir} 0775 root lock -
EOF

install -m0644 -D lockdev.sysusers.conf %{buildroot}%{_sysusersdir}/lockdev.conf


%post
if [ $1 -eq 1 ] ; then
# for the time until first reboot
%tmpfiles_create lockdev.conf
fi

%files
%{license} COPYING
%doc AUTHORS
%ghost %dir %attr(0775,root,lock) %{_lockdir}
%attr(2711,root,lock)  %{_sbindir}/lockdev
%{_tmpfilesdir}/lockdev.conf
%{_libdir}/*.so.*
%{_mandir}/man8/*
%{_sysusersdir}/lockdev.conf

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/lockdev.pc
%{_mandir}/man3/*
%{_includedir}/*

%changelog
%autochangelog
