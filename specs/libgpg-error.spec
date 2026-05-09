Name: libgpg-error
Version: 1.61
Release: %autorelease
Summary: Library for error values used by GnuPG components
URL: https://www.gnupg.org/related_software/libgpg-error/
License: LGPL-2.1-or-later AND (BSD-3-Clause OR LGPL-2.1-or-later) AND FSFULLR AND GPL-2.0-or-later

Source0: https://www.gnupg.org/ftp/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
Source1: https://www.gnupg.org/ftp/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc
Patch1: libgpg-error-1.29-multilib.patch

BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: gawk, gettext, autoconf, automake, gettext-devel, libtool
BuildRequires: texinfo
BuildRequires: gettext-autopoint
BuildRequires: make

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package devel
Summary: Development files for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future. This package
contains files necessary to develop applications using libgpg-error.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

autoreconf -f

# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g;s|@GPG_ERROR_CONFIG_HOST@|none|g' src/gpg-error-config.in
sed -i -e '/--variable=host/d' src/gpg-error-config-test.sh.in

# Modify configure to drop rpath for /usr/lib64
sed -i -e 's|sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/lib /usr/lib %{_libdir}|g' configure

%build
%configure --disable-static \
	--disable-rpath \
	--disable-languages \
	--enable-install-gpg-error-config
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%check
make check

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING COPYING.LIB
%doc AUTHORS README NEWS
%{_bindir}/gpg-error
%{_libdir}/libgpg-error.so.0*
%{_datadir}/libgpg-error

%files devel
%{_bindir}/gpg-error-config
%{_bindir}/gpgrt-config
%{_bindir}/yat2m
%{_libdir}/libgpg-error.so
%{_libdir}/pkgconfig/gpg-error.pc
%{_includedir}/gpg-error.h
%{_includedir}/gpgrt.h
%{_datadir}/aclocal/gpg-error.m4
%{_datadir}/aclocal/gpgrt.m4
%{_infodir}/gpgrt.info*
%{_mandir}/man1/gpg-error-config.*
%{_mandir}/man1/gpgrt-config.*

%changelog
%autochangelog
