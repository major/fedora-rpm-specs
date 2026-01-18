%bcond check 1
# No Qt5 on RHEL 10 and higher
%bcond qt5 %[ 0%{?rhel} < 10 ]
%bcond qt6 1
%bcond devel 0

%global gnupg2_min_ver 2.2.24
%global libgpg_error_min_ver 1.36

# we are doing out of source build
%global _configure ../configure

%global sname gpgme

Name:           compat-gpgme124
Summary:        GnuPG Made Easy - high level crypto API
Version:        1.24.3
Release:        12%{?dist}

# MIT: src/cJSON.{c,h} (used by gpgme-json)
License:        LGPL-2.1-or-later AND MIT
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig
Source3:        https://gnupg.org/signature_key.asc
Source2:        gpgme-multilib.h

## downstream patches
# Don't add extra libs/cflags in gpgme-config/cmake equivalent
Patch1001:      0001-don-t-add-extra-libraries-for-linking.patch
# add -D_FILE_OFFSET_BITS... to gpgme-config, upstreamable
Patch1002:      gpgme-1.3.2-largefile.patch
# Allow extra options to be passed to setup.py during installation
Patch1004:      0002-setup_py_extra_opts.patch

## temporary downstream fixes
# Skip lang/qt/tests/t-remarks on gnupg 2.4+
Patch3001:      1001-qt-skip-test-remarks-for-gnupg2-2.4.patch


BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gawk
BuildRequires:  texinfo
BuildRequires:  gnupg2 >= %{gnupg2_min_ver}
BuildRequires:  gnupg2-smime
BuildRequires:  gpgverify
BuildRequires:  libgpg-error-devel >= %{libgpg_error_min_ver}
BuildRequires:  libassuan-devel >= 2.4.2

# to remove RPATH
BuildRequires:  chrpath

# For AutoReq cmake-filesystem
BuildRequires:  cmake

Requires:       gnupg2 >= %{gnupg2_min_ver}

# On the following architectures workaround multiarch conflict of -devel packages:
%global multilib_arches %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package -n compat-gpgmepp124
Summary:        C++ bindings/wrapper for GPGME
Provides:       gpgme-pp = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n compat-gpgmepp124
%{summary}.

%if %{with devel}
%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libgpg-error-devel%{?_isa} >= %{libgpg_error_min_ver}

%description devel
%{summary}.

%package -n compat-%{sname}pp124-devel
Summary:        Development libraries and header files for %{name}-pp
Provides:       gpgme-pp-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-devel%{?_isa}

%description -n compat-%{sname}pp-devel
%{summary}
%endif

%if %{with qt5}
%package -n compat-q%{sname}124-qt5
Summary:        Qt5 API bindings/wrapper for GPGME
Requires:       compat-%{sname}pp124%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
Obsoletes:      q%{name} < 1.20.0
Provides:       q%{name}

%description -n compat-q%{sname}124-qt5
%{summary}.
%endif

%if %{with qt6}
%package -n compat-q%{sname}124-qt6
Summary:        Qt6 API bindings/wrapper for GPGME
Requires:       compat-%{sname}pp124%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Test)

%description -n compat-q%{sname}124-qt6
%{summary}.
%endif


%if %{with devel}
%if %{with qt5} || %{with qt6}
%package -n compat-q%{sname}124-common-devel
Summary:        Common development header files for %{name}-qt5 and %{name}-qt6
Requires:       compat-%{sname}pp124-devel%{?_isa}

%description -n compat-q%{sname}-common-devel
%{summary}.
%endif

%if %{with qt5}
%package -n q%{name}-qt5-devel
Summary:        Development libraries and header files for %{name}-qt5
# before libqgpgme.so symlink was moved to avoid conflict
Conflicts:      kdepimlibs-devel < 4.14.10-17
Requires:       q%{sname}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       q%{sname}-common-devel%{?_isa}
Obsoletes:      q%{sname}-devel < 1.20.0
Provides:       q%{sname}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       q%{sname}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n compat-q%{sname}124-qt5-devel
%{summary}.
%endif

%if %{with qt6}
%package -n compt-q%{sname}124-qt6-devel
Summary:        Development libraries and header files for %{name}-qt6
Requires:       q%{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       q%{name}-common-devel%{?_isa}

%description -n compat-q%{sname}124-qt6-devel
%{summary}.
%endif
%endif

%prep
%{gpgverify} --keyring=%{SOURCE3} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -n gpgme-%{version} -p1 -S gendiff

## HACK ALERT
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpgme-config.in

%build
# Since 1.16.0, we need to explicitly pass -D_LARGEFILE_SOURCE and
# -D_FILE_OFFSET_BITS=64 for the QT binding to build successfully on 32-bit
# platforms.
export CFLAGS='%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
export CXXFLAGS='%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
# Explicit new lines in C(XX)FLAGS can break naive build scripts
export CFLAGS="$(echo ${CFLAGS} | tr '\n\\' '  ')"
export CXXFLAGS="$(echo ${CXXFLAGS} | tr '\n\\' '  ')"
export SETUPTOOLS_USE_DISTUTILS=local
# bypass configure check which fails with GCC 16
export ac_cv_prog_cxx_cxx11=''

# Also build either qt5 or qt6
mkdir build
pushd build
%configure --disable-static --disable-silent-rules --enable-languages=%{?with_qt5:qt,}%{!?with_qt5:%{?with_qt6:qt6,}}cpp
%make_build
popd

# Build qt6 in extra step if qt5 has been build
%if %{with qt5} && %{with qt6}
mkdir bqt6
pushd bqt6
%configure --disable-static --disable-silent-rules --enable-languages=cpp,qt6
%make_build
popd
%endif

%install
# When using distutils from setuptools 60+, ./setup.py install use
# the .egg format. This forces setuptools to use .egg-info format.
# SETUP_PY_EXTRA_OPTS is introduced by the Patch1004 above.
export SETUPTOOLS_USE_DISTUTILS=local
export SETUP_PY_EXTRA_OPTS="--single-version-externally-managed --root=/"
# Aliso install either qt5 or qt6
pushd build
%make_install
popd
# Install qt6 in extra step if qt5 has been installed
%if %{with qt5} && %{with qt6}
pushd bqt6
%make_install
popd
%endif

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
chrpath -d %{buildroot}%{_bindir}/%{sname}-tool
chrpath -d %{buildroot}%{_bindir}/%{sname}-json
chrpath -d %{buildroot}%{_libdir}/lib%{sname}pp.so*
# qt5
%if %{with qt5}
chrpath -d %{buildroot}%{_libdir}/libq%{sname}.so*
%endif
# qt6
%if %{with qt6}
chrpath -d %{buildroot}%{_libdir}/libq%{sname}qt6.so*
%endif

%if %{without devel}
rm -rf %{buildroot}%{_includedir}
rm -f %{buildroot}%{_libdir}/*.so
rm -rf %{buildroot}%{_libdir}/cmake
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -f %{buildroot}%{_bindir}/gpgme-config*
rm -f %{buildroot}%{_bindir}/gpgme-tool
rm -rf %{buildroot}%{_datadir}/aclocal
rm -rf %{buildroot}%{_datadir}/info/gpgme.*
%endif

# delete unwanted tools
rm -f %{buildroot}%{_bindir}/%{sname}-json
rm -f %{buildroot}%{_mandir}/man1/%{sname}-json.*

%if %{with check}
%check
pushd build
make check
popd
%endif

%files
%license COPYING* LICENSES
%doc AUTHORS NEWS README*
%{_libdir}/lib%{sname}.so.11*

%files -n compat-%{sname}pp124
%doc lang/cpp/README
%{_libdir}/lib%{sname}pp.so.6*

%if %{with devel}
%files devel
%{_bindir}/%{sname}-config
%{_bindir}/%{sname}-tool
%ifarch %{multilib_arches}
%{_bindir}/%{sname}-config.%{_target_cpu}
%{_includedir}/%{sname}-%{__isa_bits}.h
%endif
%{_includedir}/%{sname}.h
%{_libdir}/lib%{sname}.so
%{_datadir}/aclocal/%{sname}.m4
%{_infodir}/%{sname}.info*
%{_libdir}/pkgconfig/%{sname}*.pc

%files -n compat-%{sname}pp124-devel
%{_includedir}/%{sname}++/
%{_libdir}/lib%{sname}pp.so
%{_libdir}/cmake/Gpgmepp/
%endif

%if %{with qt5}
%files -n compat-q%{sname}124-qt5
%doc lang/qt/README
%{_libdir}/libq%{sname}.so.15*
%endif

%if %{with qt6}
%files -n compat-q%{sname}124-qt6
%{_libdir}/libq%{sname}qt6.so.15*
%endif

%if %{with devel}
%if %{with qt5} || %{with qt6}
%files -n compat-q%{sname}124-common-devel
%endif

%if %{with qt5}
%files -n compat-q%{sname}124-qt5-devel
%{_includedir}/q%{sname}-qt5/
%{_libdir}/libq%{sname}.so
%{_libdir}/cmake/QGpgme/
%endif

%if %{with qt6}
%files -n compat-q%{sname}124-qt6-devel
%{_includedir}/q%{sname}-qt6/
%{_libdir}/libq%{sname}qt6.so
%{_libdir}/cmake/QGpgmeQt6/
%endif
%endif

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Nov 12 2025 Michal Hlavinka <mhlavink@redhat.com> - 1.24.3-10
- bump release number to be higher than old non-compat package

* Fri Oct 17 2025 Michal Hlavinka <mhlavink@redhat.com> - 1.24.3-1
- intial build


