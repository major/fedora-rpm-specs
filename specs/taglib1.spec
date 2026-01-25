%bcond devel 0
%bcond tests 1

%global common_description %{expand:
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags.
This is a compatibility version for packages not yet rebuilt for taglib 2.}

Name:       taglib1
Summary:    Audio Meta-Data Library (compat version)
Version:    1.13.1
Release:    %autorelease -b 9

License:    (LGPL-2.1-only OR MPL-1.1) AND BSD-2-Clause AND LGPL-2.1-only
URL:        https://taglib.github.io/
Source0:    https://taglib.github.io/releases/taglib-%{version}%{?beta}.tar.gz

# http://bugzilla.redhat.com/343241
# fix multilib, and drop -lz flag to consumers (probably only needed for static linking)
Patch0:     taglib-1.13.1-multilib.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: zlib-devel
%if %{with tests}
BuildRequires: cppunit-devel
%endif

Conflicts:     taglib < 2.0
Provides:      bundled(utf8cpp)

%description
%{common_description}

%if %{with devel}
%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: taglib-devel >= 2.0

%description devel
Files needed when building software with %{name}.
%endif

%prep
%autosetup -n taglib-%{version}%{?beta} -p1

%build
%{cmake} \
%if %{with tests}
  -DBUILD_TESTS:BOOL=ON \
%endif
  -DCMAKE_BUILD_TYPE:STRING="Release"

%cmake_build

%install
%cmake_install

%if %{without devel}
rm -f  %{buildroot}%{_bindir}/taglib-config
rm -fr %{buildroot}%{_includedir}/taglib/
rm -f  %{buildroot}%{_libdir}/libtag*.so
rm -f  %{buildroot}%{_libdir}/pkgconfig/*.pc
%endif

%check
%if %{with tests}
%ctest
%endif

%files
%doc AUTHORS NEWS
%license COPYING.LGPL COPYING.MPL
%{_libdir}/libtag.so.1*
%{_libdir}/libtag_c.so.0*

%if %{with devel}
%files devel
%{_bindir}/taglib-config
%{_includedir}/taglib/
%{_libdir}/libtag.so
%{_libdir}/libtag_c.so
%{_libdir}/pkgconfig/taglib.pc
%{_libdir}/pkgconfig/taglib_c.pc
%endif

%changelog
%autochangelog
