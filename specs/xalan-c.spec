%bcond icu 1

Name:           xalan-c
Version:        1.12.0
# The soversion is made from the major and minor version numbers, e.g. 112 for
# version 1.12.x. We could do this automatically…
#   %%global so_version %%(echo %%{version} | cut -d . -f -2 | tr -d .)
# …but we do not do so because we want to make sure we detect any soversion
# update.
%global so_version 112
Release:        %autorelease
Summary:        Xalan XSLT processor for C/C++

# The entire source is Apache-2.0, except cmake/RunTest.cmake, which is
# libtiff, but is a build-system file that does not contribute to the licenses
# of the binary RPMs.
License:        Apache-2.0
SourceLicense:  %{license} AND libtiff
URL:            https://apache.github.io/xalan-c/
%global tag Xalan-C_%{gsub %{version} . _}
%global tar_name xalan_c-%(echo %{version} | cut -d . -f -2)
%global forgeurl https://github.com/apache/xalan-c/
%global releaseurl %{forgeurl}/releases/download/%{tag}
Source0:        %{releaseurl}/%{tar_name}.tar.gz
Source1:        %{releaseurl}/%{tar_name}.tar.gz.asc
Source2:        %{releaseurl}/KEYS
# Man page hand-written for Fedora in groff_man(7) format based on Xalan -?
Source3:        Xalan.1

# ICU 75 needs C++17
# https://bugs.gentoo.org/934471
#
# Fixes:
#
# [FTBFS] with icu-76.1
# https://bugzilla.redhat.com/show_bug.cgi?id=2332317
#
# Note that this patch is too trivial for there to be any need to associate a
# license with it; the patch merely adjusts the value of CMAKE_CXX_STANDARD
# from 14 to 17.
Patch:          https://gitweb.gentoo.org/repo/gentoo.git/plain/dev-libs/xalan-c/files/xalan-c-1.12-icu-75.patch

Patch: gcc_15_fixes.patch

BuildRequires:  gnupg2
BuildRequires:  cmake
# Either make or ninja is supported.
BuildRequires:  ninja-build
BuildRequires:  gcc-c++

BuildRequires:  dos2unix
BuildRequires:  hardlink

BuildRequires:  xerces-c-devel
%if %{with icu}
BuildRequires:  libicu-devel
%endif

Requires:       xalan-c-libs%{?_isa} = %{version}-%{release}

%global common_description %{expand:
The Apache Xalan-C++ Project provides a library and a command line program to
transform XML documents using a stylesheet that conforms to XSLT 1.0 standards.

Xalan is a project of the Apache Software Foundation.}

%description %{common_description}

This package contains the command-line tool.


%package        libs
Summary:        Shared libraries for xalan-c

%description libs
The xalan-c-libs package contains libraries needed by the command-line tool and
by applications that use xalan-c.


%package        devel
Summary:        Development files for xalan-c
Requires:       xalan-c-libs%{?_isa} = %{version}-%{release}

%description devel
The xalan-c-devel package contains libraries and header files for developing
applications that use xalan-c.


%package doc
Summary:        Documentation for xalan-c

# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# Normally, we would enable the Doxygen PDF documentation as a lesser
# substitute, but building it fails with:
#   ! TeX capacity exceeded, sorry [pool size=5905151].
BuildArch:      noarch

%description doc
Documentation for xalan-c. See https://apache.github.io/xalan-c/ for full HTML
documentation.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n %{tar_name} -p 1

# https://github.com/apache/xalan-c/pull/35
chmod -v a-x NOTICE

# Remove the Autotools build system cruft from the samples; otherwise, it would
# be installed as documentation. We leave the CmakeLists.txt even though it
# cannot be used standalone; it is used in the build (even though the built
# samples are only tested and not installed), and is annoying to exclude.
rm -vf samples/configure samples/configure.in

# Convert line endings as needed:
find docs samples src -type f -exec file '{}' '+' |
  grep -F 'CRLF' |
  awk -F ':' '{ print $1 }' |
  xargs dos2unix --keepdate


%conf
%cmake %{?with_icu:-Dtranscoder=icu} -GNinja


%build
%cmake_build


%install
%cmake_install
# Remove CMake-installed docs in favor of using the doc macro. We refer to
# _prefix/share instead of _datadir to mirror how the install path is defined
# in the relevant CMakeLists.txt. Note also that we do *not* want to install
# the HTML version of the API documentation.
rm -rf %{buildroot}%{_prefix}/share/doc/xalan-c/api

install -t '%{buildroot}%{_docdir}/%{name}-doc' -D -p -m 0644 \
    README.md docs/*.md
cp -rvp docs/images/ samples/ '%{buildroot}%{_docdir}/%{name}-doc'
hardlink -c -v '%{buildroot}%{_docdir}/%{name}-doc'

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE3}'


%check
%ctest


%files
%{_bindir}/Xalan
%{_mandir}/man1/Xalan.1*


%files libs
%license CREDITS LICENSE NOTICE

%{_libdir}/libxalanMsg.so.%{so_version}{,.*}
%{_libdir}/libxalan-c.so.%{so_version}{,.*}


%files devel
%{_libdir}/libxalanMsg.so
%{_libdir}/libxalan-c.so

%{_includedir}/xalanc/

%dir %{_libdir}/cmake/XalanC
%{_libdir}/cmake/XalanC/*.cmake

%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/xalan-c.pc


%files doc
%license CREDITS LICENSE NOTICE

%{_docdir}/%{name}-doc/


%changelog
%autochangelog
