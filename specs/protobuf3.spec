# Build -python subpackage
%bcond_without python
# Build -python subpackage with C++. This significantly improves performance
# compared to the pure-Python implementation.
%bcond_without python_cpp

#global rcver rc2

Summary:        Protocol Buffers - Google's data interchange format
Name:           protobuf3
# NOTE: perl-Alien-ProtoBuf has an exact-version dependency on the version of
# protobuf with which it was built; it therefore needs to be rebuilt even for
# “patch” updates of protobuf.
Version:        3.19.6
%global so_version 30
Release:        %autorelease

# The entire source is BSD-3-Clause, except the following files, which belong
# to the build system; are unpackaged maintainer utility scripts; or are used
# only for building tests that are not packaged—and so they do not affect the
# licenses of the binary RPMs:
#
# FSFAP:
#   m4/ax_cxx_compile_stdcxx.m4
#   m4/ax_prog_cc_for_build.m4
#   m4/ax_prog_cxx_for_build.m4
# Apache-2.0:
#   python/mox.py
#   python/stubout.py
#   third_party/googletest/
#     except the following, which are BSD-3-Clause:
#       third_party/googletest/googletest/test/gtest_pred_impl_unittest.cc
#       third_party/googletest/googletest/include/gtest/gtest-param-test.h
#       third_party/googletest/googletest/include/gtest/gtest-param-test.h.pump
#       third_party/googletest/googletest/include/gtest/internal/gtest-param-util-generated.h
#       third_party/googletest/googletest/include/gtest/internal/gtest-param-util-generated.h.pump
#       third_party/googletest/googletest/include/gtest/internal/gtest-type-util.h
#       third_party/googletest/googletest/include/gtest/internal/gtest-type-util.h.pump
# MIT:
#   conformance/third_party/jsoncpp/json.h
#   conformance/third_party/jsoncpp/jsoncpp.cpp
License:        BSD-3-Clause
URL:            https://github.com/protocolbuffers/protobuf
Source0:        %{url}/archive/v%{version}%{?rcver}/protobuf-%{version}%{?rcver}-all.tar.gz

Source1:        ftdetect-proto.vim
Source2:        protobuf-init.el

# We bundle a copy of the exact version of gtest that is used by upstream in
# the source RPM rather than using the system copy. This is to be discouraged,
# but necessary in this case.  It is not treated as a bundled library because
# it is used only at build time, and contributes nothing to the installed
# files.  We take measures to verify this in %%check. See
# https://github.com/protocolbuffers/protobuf/tree/v%%{version}/third_party to
# check the correct commit hash.
%global gtest_url https://github.com/google/googletest
%global gtest_commit 5ec7f0c4a113e2f18ac2c6cc7df51ad6afc24081
%global gtest_dir googletest-%{gtest_commit}
# For tests (using exactly the same version as the release)
Source3:        %{gtest_url}/archive/%{gtest_commit}/%{gtest_dir}.tar.gz

# Man page hand-written for Fedora in groff_man(7) format based on “protoc
# --help” output.
Source4:        protoc.1

# https://github.com/protocolbuffers/protobuf/issues/8082
Patch1:         protobuf-3.14-disable-IoTest.LargeOutput.patch
# Disable tests that are failing on 32bit systems
Patch2:         disable-tests-on-32-bit-systems.patch
# Backport upstream commit da973aff2adab60a9e516d3202c111dbdde1a50f:
#   Fix build with Python 3.11
#
#   The PyFrameObject structure members have been removed from the public C API.
Patch4:         protobuf-3.19.4-python3.11.patch

# A bundled copy of jsoncpp is included in the conformance tests, but the
# result is not packaged, so we do not treat it as a formal bundled
# dependency—thus the virtual Provides below is commented out. The bundling is
# removed in a later release:
#   Make jsoncpp a formal dependency
#   https://github.com/protocolbuffers/protobuf/pull/10739
# The bundled version number is obtained from JSONCPP_VERSION_STRING in
# conformance/third_party/jsoncpp/json.h.
# Provides:       bundled(jsoncpp) = 1.6.5

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  emacs
BuildRequires:  zlib-devel

%description
Protocol Buffers are a way of encoding structured data in an efficient
yet extensible format. Google uses Protocol Buffers for almost all of
its internal RPC protocols and file formats.

Protocol buffers are a flexible, efficient, automated mechanism for
serializing structured data – think XML, but smaller, faster, and
simpler. You define how you want your data to be structured once, then
you can use special generated source code to easily write and read
your structured data to and from a variety of data streams and using a
variety of languages. You can even update your data structure without
breaking deployed programs that are compiled against the "old" format.

%package compiler
Summary:        Protocol Buffers compiler
Requires:       %{name} = %{version}-%{release}

%description compiler
This package contains Protocol Buffers compiler for all programming
languages

%package devel
Summary:        Protocol Buffers C++ headers and libraries
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-compiler = %{version}-%{release}
Requires:       zlib-devel

Obsoletes:      protobuf-static < 3.19.6-4

%description devel
This package contains Protocol Buffers compiler for all languages and
C++ headers and libraries

%package lite
Summary:        Protocol Buffers LITE_RUNTIME libraries

%description lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%package lite-devel
Summary:        Protocol Buffers LITE_RUNTIME development libraries
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-lite = %{version}-%{release}

Obsoletes:      protobuf-lite-static < 3.19.6-4

%description lite-devel
This package contains development libraries built with
optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%if %{with python}
%package -n python3-protobuf3
Summary:        Python bindings for Google Protocol Buffers
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
%if %{with python_cpp}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%else
BuildArch:      noarch
%endif
Conflicts:      %{name}-compiler > %{version}
Conflicts:      %{name}-compiler < %{version}

%description -n python3-protobuf3
This package contains Python libraries for Google Protocol Buffers
%endif

%package vim
Summary:        Vim syntax highlighting for Google Protocol Buffers descriptions
BuildArch:      noarch
# We don’t really need vim or vim-enhanced to be already installed in order to
# install a plugin for it. We do need to depend on vim-filesystem, which
# provides the necessary directory structure.
Requires:       vim-filesystem

%description vim
This package contains syntax highlighting for Google Protocol Buffers
descriptions in Vim editor

%package emacs
Summary:        Emacs mode for Google Protocol Buffers descriptions
BuildArch:      noarch
Requires:       emacs-filesystem >= %{_emacs_version}
Obsoletes:      protobuf-emacs-el < 3.6.1-4

%description emacs
This package contains syntax highlighting for Google Protocol Buffers
descriptions in the Emacs editor.

%prep
%setup -q -n protobuf-%{version}%{?rcver} -a 3
%ifarch %{ix86}
# IoTest.LargeOutput fails on 32bit arches
# https://github.com/protocolbuffers/protobuf/issues/8082
%patch 1 -p1
# Need to disable more tests that fail on 32bit arches only
%patch 2 -p0
%endif
%patch 4 -p1 -b .python311

# Copy in the needed gtest/gmock implementations.
%setup -q -T -D -b 3 -n protobuf-%{version}%{?rcver}
rm -rvf 'third_party/googletest'
mv '../%{gtest_dir}' 'third_party/googletest'

find -name \*.cc -o -name \*.h | xargs chmod -x
chmod 644 examples/*

rm -f src/solaris/libstdc++.la

%build
iconv -f iso8859-1 -t utf-8 CONTRIBUTORS.txt > CONTRIBUTORS.txt.utf8
mv CONTRIBUTORS.txt.utf8 CONTRIBUTORS.txt
export PTHREAD_LIBS="-lpthread"
./autogen.sh
%configure --disable-static

# -Wno-error=type-limits:
#     https://bugzilla.redhat.com/show_bug.cgi?id=1838470
#     https://github.com/protocolbuffers/protobuf/issues/7514
#     https://gcc.gnu.org/bugzilla/show_bug.cgi?id=95148
#  (also set in %%check)
%make_build CXXFLAGS="%{build_cxxflags} -Wno-error=type-limits"

%if %{with python}
pushd python
%py3_build %{?with_python_cpp:-- --cpp_implementation}
popd
%endif

%{_emacs_bytecompile} editors/protobuf-mode.el


%check
%make_build check CXXFLAGS="%{build_cxxflags} -Wno-error=type-limits"


%install
%make_install %{?_smp_mflags} STRIPBINARIES=no INSTALL="%{__install} -p" CPPROG="cp -p"
find %{buildroot} -type f -name "*.la" -exec rm -f {} +

# protoc.1 man page
install -p -m 0644 -D -t '%{buildroot}%{_mandir}/man1' '%{SOURCE4}'

%if %{with python}
pushd python
%py3_install %{?with_python_cpp:-- --cpp_implementation}
%if %{without python_cpp}
find %{buildroot}%{python3_sitelib} -name \*.py -exec sed -i -e '1{\@^#!@d}' {} +
%endif
popd
%endif
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/proto.vim
install -p -m 644 -D editors/proto.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/proto.vim

mkdir -p %{buildroot}%{_emacs_sitelispdir}/protobuf
install -p -m 0644 editors/protobuf-mode.el %{buildroot}%{_emacs_sitelispdir}/protobuf
install -p -m 0644 editors/protobuf-mode.elc %{buildroot}%{_emacs_sitelispdir}/protobuf
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_emacs_sitestartdir}

%files
%doc CHANGES.txt CONTRIBUTORS.txt README.md
%license LICENSE
%{_libdir}/libprotobuf.so.%{so_version}{,.*}

%files compiler
%doc README.md
%license LICENSE
%{_bindir}/protoc
%{_mandir}/man1/protoc.1*
%{_libdir}/libprotoc.so.%{so_version}{,.*}

%files devel
%dir %{_includedir}/google
%{_includedir}/google/protobuf/
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.so
%{_libdir}/pkgconfig/protobuf.pc
%doc examples/add_person.cc examples/addressbook.proto examples/list_people.cc examples/Makefile examples/README.md

%files emacs
%license LICENSE
%{_emacs_sitelispdir}/protobuf/
%{_emacs_sitestartdir}/protobuf-init.el

%files lite
%license LICENSE
%{_libdir}/libprotobuf-lite.so.%{so_version}{,.*}

%files lite-devel
%{_libdir}/libprotobuf-lite.so
%{_libdir}/pkgconfig/protobuf-lite.pc

%if %{with python}
%files -n python3-protobuf3
%if %{with python_cpp}
%dir %{python3_sitearch}/google
%{python3_sitearch}/google/protobuf/
%{python3_sitearch}/protobuf-%{version}%{?rcver}-py3.*.egg-info/
%{python3_sitearch}/protobuf-%{version}%{?rcver}-py3.*-nspkg.pth
%else
%license LICENSE
%dir %{python3_sitelib}/google
%{python3_sitelib}/google/protobuf/
%{python3_sitelib}/protobuf-%{version}%{?rcver}-py3.*.egg-info/
%{python3_sitelib}/protobuf-%{version}%{?rcver}-py3.*-nspkg.pth
%endif
%doc python/README.md
%doc examples/add_person.py examples/list_people.py examples/addressbook.proto
%endif

%files vim
%license LICENSE
%{_datadir}/vim/vimfiles/ftdetect/proto.vim
%{_datadir}/vim/vimfiles/syntax/proto.vim

%changelog
%autochangelog
