%bcond check 1
%bcond qt 1

%global gnupg2_min_ver 2.2.24
%global libgpg_error_min_ver 1.36

Name:           gpgme
Summary:        GnuPG Made Easy - high level crypto API
Version:        1.17.1
Release:        %autorelease

# MIT: src/cJSON.{c,h} (used by gpgme-json)
License:        LGPL-2.1-or-later AND MIT
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source2:        gpgme-multilib.h

## downstream patches
# Don't add extra libs/cflags in gpgme-config/cmake equivalent
Patch1001:      0001-don-t-add-extra-libraries-for-linking.patch
# add -D_FILE_OFFSET_BITS... to gpgme-config, upstreamable
Patch1002:      gpgme-1.3.2-largefile.patch
# Let's fix stupid AX_PYTHON_DEVEL
Patch1003:      0001-fix-stupid-ax_python_devel.patch
# Allow extra options to be passed to setup.py during installation
Patch1004:      0002-setup_py_extra_opts.patch

## upstream patches dealing with date and time overflow on 32-bit machines
# Before gpgme 1.18.0
Patch2001:      0001-qt-Prevent-u32-overflow-when-calculating-expiration.patch
Patch2002:      0002-qt-tests-Allow-1-day-offset-for-expiration-date.patch
# After gpgme 1.18.0
Patch2003:      0003-qt-Make-sure-expiration-time-is-interpreted-as-unsigned.patch
Patch2004:      0004-qt-tests-Log-the-actual-error-code-if-the-assertion-fails.patch
Patch2005:      0005-qt-tests-Make-sure-expiration-time-is-interpreted-as-unsigned.patch
Patch2006:      0006-qt-tests-Make-test-pass-on-32-bit-systems.patch
Patch2007:      0007-cpp-Fix-handling-of-no-key-or-invalid-time-situation.patch

## temporary downstream fixes
# Skip lang/qt/tests/t-remarks on gnupg 2.4+
Patch3001:      1001-qt-skip-test-remarks-for-gnupg2-2.4.patch

#BuildRequires:  autoconf
#BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gawk
BuildRequires:  gnupg2 >= %{gnupg2_min_ver}
BuildRequires:  gnupg2-smime
BuildRequires:  libgpg-error-devel >= %{libgpg_error_min_ver}
BuildRequires:  libassuan-devel >= 2.4.2

# For python bindings
BuildRequires:  swig

# to remove RPATH
BuildRequires:  chrpath

# For AutoReq cmake-filesystem
BuildRequires:  cmake

Requires:       gnupg2 >= %{gnupg2_min_ver}

# On the following architectures workaround multiarch conflict of -devel packages:
%define multilib_arches %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libgpg-error-devel%{?_isa} >= %{libgpg_error_min_ver}

%description devel
%{summary}.

%package -n %{name}pp
Summary:        C++ bindings/wrapper for GPGME
Obsoletes:      gpgme-pp < 1.8.0-7
Provides:       gpgme-pp = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{name}pp
%{summary}.

%package -n %{name}pp-devel
Summary:        Development libraries and header files for %{name}-pp
Obsoletes:      gpgme-pp-devel < 1.8.0-7
Provides:       gpgme-pp-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-devel%{?_isa}
# For automatic provides
BuildRequires:  cmake

%description -n %{name}pp-devel
%{summary}

%if %{with qt}
%package -n q%{name}
Summary:        Qt API bindings/wrapper for GPGME
Requires:       %{name}pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)

%description -n q%{name}
%{summary}.

%package -n q%{name}-devel
Summary:        Development libraries and header files for %{name}
# before libqgpgme.so symlink was moved to avoid conflict
Conflicts:      kdepimlibs-devel < 4.14.10-17
Requires:       q%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}pp-devel%{?_isa}
# For automatic provides
BuildRequires:  cmake

%description -n q%{name}-devel
%{summary}.
%endif

%package -n python3-gpg
Summary:        %{name} bindings for Python 3
BuildRequires:  python3-devel
# Needed since Python 3.12+ drops distutils
BuildRequires:  python3-setuptools
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      platform-python-gpg < %{version}-%{release}

%description -n python3-gpg
%{summary}.

%prep
%autosetup -p1

## HACK ALERT
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpgme-config.in

# The build machinery does not support Python 3.9+ yet
# https://github.com/gpg/gpgme/pull/4
sed -i 's/3.8/%{python3_version}/g' configure

%build
# People neeed to learn that you can't run autogen.sh anymore
#./autogen.sh

# Since 1.16.0, we need to explicitly pass -D_LARGEFILE_SOURCE and
# -D_FILE_OFFSET_BITS=64 for the QT binding to build successfully on 32-bit
# platforms.
export CFLAGS='%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
export CXXFLAGS='%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
# Explicit new lines in C(XX)FLAGS can break naive build scripts
export CFLAGS="$(echo ${CFLAGS} | tr '\n\\' '  ')"
export CXXFLAGS="$(echo ${CXXFLAGS} | tr '\n\\' '  ')"
export SETUPTOOLS_USE_DISTUTILS=local

%configure --disable-static --disable-silent-rules --enable-languages=cpp,%{?with_qt:qt,}python
%make_build

%install
# When using distutils from setuptools 60+, ./setup.py install use
# the .egg format. This forces setuptools to use .egg-info format.
# SETUP_PY_EXTRA_OPTS is introduced by the Patch1004 above.
export SETUPTOOLS_USE_DISTUTILS=local
export SETUP_PY_EXTRA_OPTS="--single-version-externally-managed --root=/"
%make_install

# unpackaged files
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la

# Hack to resolve multiarch conflict (#341351)
%ifarch %{multilib_arches}
mv %{buildroot}%{_bindir}/gpgme-config{,.%{_target_cpu}}
cat > gpgme-config-multilib.sh <<__END__
#!/bin/sh
exec %{_bindir}/gpgme-config.\$(arch) \$@
__END__
install -D -p gpgme-config-multilib.sh %{buildroot}%{_bindir}/gpgme-config
mv %{buildroot}%{_includedir}/gpgme.h \
   %{buildroot}%{_includedir}/gpgme-%{__isa_bits}.h
install -m644 -p -D %{SOURCE2} %{buildroot}%{_includedir}/gpgme.h
%endif
chrpath -d %{buildroot}%{_bindir}/%{name}-tool
chrpath -d %{buildroot}%{_bindir}/%{name}-json
chrpath -d %{buildroot}%{_libdir}/lib%{name}pp.so*
%if %{with qt}
chrpath -d %{buildroot}%{_libdir}/libq%{name}.so*
%endif

# autofoo installs useless stuff for uninstall
rm -vf %{buildroot}%{python2_sitelib}/gpg/install_files.txt
rm -vf %{buildroot}%{python3_sitelib}/gpg/install_files.txt

%if %{with check}
%check
make check
%endif

%files
%license COPYING* LICENSES
%doc AUTHORS NEWS README*
%{_bindir}/%{name}-json
%{_libdir}/lib%{name}.so.11*

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-tool
%ifarch %{multilib_arches}
%{_bindir}/%{name}-config.%{_target_cpu}
%{_includedir}/%{name}-%{__isa_bits}.h
%endif
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_datadir}/aclocal/%{name}.m4
%{_infodir}/%{name}.info*
%{_libdir}/pkgconfig/%{name}*.pc

%files -n %{name}pp
%doc lang/cpp/README
%{_libdir}/lib%{name}pp.so.6*

%files -n %{name}pp-devel
%{_includedir}/%{name}++/
%{_libdir}/lib%{name}pp.so
%{_libdir}/cmake/Gpgmepp/

%if %{with qt}
%files -n q%{name}
%doc lang/qt/README
%{_libdir}/libq%{name}.so.15*

%files -n q%{name}-devel
%{_includedir}/q%{name}/
%{_includedir}/QGpgME/
%{_libdir}/libq%{name}.so
%{_libdir}/cmake/QGpgme/
%endif

%files -n python3-gpg
%doc lang/python/README
%{python3_sitearch}/gpg-*.egg-info/
%{python3_sitearch}/gpg/

%changelog
%autochangelog
