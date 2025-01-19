Name:           imhex
Version:        1.36.2
Release:        2%{?dist}
Summary:        A hex editor for reverse engineers and programmers

License:        GPL-2.0-only AND Zlib AND MIT AND Apache-2.0
# imhex is gplv2.  capstone is custom.
# see license dir for full breakdown
URL:            https://imhex.werwolv.net/
# We need the archive with deps bundled
Source0:        https://github.com/WerWolv/%{name}/releases/download/v%{version}/Full.Sources.tar.gz#/%{name}-%{version}.tar.gz
# default to including the same-version patterns as a suggested package
Source1:        https://github.com/WerWolv/ImHex-Patterns/archive/refs/tags/ImHex-v%{version}.tar.gz#/%{name}-patterns-%{version}.tar.gz

Patch:          lunasvg-cmake.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dbus-devel
BuildRequires:  file-devel
BuildRequires:  freetype-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libglvnd-devel
BuildRequires:  glfw-devel
BuildRequires:  json-devel
BuildRequires:  libcurl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libzstd-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  llvm-devel
BuildRequires:  mbedtls-devel
BuildRequires:  yara-devel
BuildRequires:  nativefiledialog-extended-devel
%if 0%{?rhel}
BuildRequires:  gcc-toolset-13
%endif
%if 0%{?fedora} >= 40
BuildRequires:  capstone-devel
BuildRequires:  lunasvg-devel
%endif

Recommends:     imhex-patterns = %{version}-%{release}

Provides:       bundled(gnulib)
%if 0%{?fedora} < 40
Provides:       bundled(capstone) = 5.0.1
%endif
Provides:       bundled(imgui) = 1.90.8
Provides:       bundled(libromfs)
Provides:       bundled(microtar)
Provides:       bundled(libpl) = %{version}
Provides:       bundled(xdgpp)
# working on packaging this, bundling for now as to now delay updates
Provides:       bundled(miniaudio) = 0.11.11

# [7:02 PM] WerWolv: We're not supporting 32 bit anyways soooo
# [11:38 AM] WerWolv: Officially supported are x86_64 and aarch64
ExclusiveArch:  x86_64 %{arm64}

%description
ImHex is a Hex Editor, a tool to display, decode and analyze binary data to
reverse engineer their format, extract informations or patch values in them.

What makes ImHex special is that it has many advanced features that can often
only be found in paid applications. Such features are a completely custom binary
template and pattern language to decode and highlight structures in the data, a
graphical node-based data processor to pre-process values before they're
displayed, a disassembler, diffing support, bookmarks and much much more. At the
same time ImHex is completely free and open source under the GPLv2 language.


%package patterns
Summary:        Hex patterns, include patterns and magic files for the use with the ImHex Hex Editor
License:        GPL-2.0-only
Requires:       imhex >= %{version}-%{release}
%description patterns
Hex patterns, include patterns and magic files for the use with
the ImHex Hex Editor


%package devel
Summary:        Development files for %{name}
License:        GPL-2.0-only
%description devel
%{summary}


%prep
%autosetup -n ImHex -p1
# remove bundled libs we aren't using
rm -rf lib/third_party/{curl,fmt,llvm,nlohmann_json,yara}
%if 0%{?fedora}
rm -rf lib/third_party/capstone
%endif

# the cmake scripts look for patterns to be in ImHex-Patterns
mkdir -p ImHex-Patterns && tar -xf %{SOURCE1} -C ImHex-Patterns --strip-components=1

%build
%if 0%{?rhel}
. /opt/rh/gcc-toolset-13/enable
%set_build_flags
CXXFLAGS+=" -std=gnu++2b"
%endif
%cmake \
 -D CMAKE_BUILD_TYPE=Release             \
 -D IMHEX_STRIP_RELEASE=OFF              \
 -D IMHEX_OFFLINE_BUILD=ON               \
 -D USE_SYSTEM_NLOHMANN_JSON=ON          \
 -D USE_SYSTEM_FMT=ON                    \
 -D USE_SYSTEM_CURL=ON                   \
%if 0%{?fedora}
 -D USE_SYSTEM_LLVM=ON                   \
 -D USE_SYSTEM_CAPSTONE=ON               \
 -D USE_SYSTEM_LUNASVG=ON                \
%endif
 -D USE_SYSTEM_YARA=ON                   \
 -D USE_SYSTEM_NFD=ON                    \
 -D IMHEX_ENABLE_UNIT_TESTS=ON

%cmake_build


%check
# build binaries required for tests
%cmake_build --target unit_tests
%ctest --exclude-regex '(Helpers/StoreAPI|Helpers/TipsAPI|Helpers/ContentAPI)'
# Helpers/*API exclude tests that require network access


%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# this is a symlink for the old appdata name that we don't need
rm -f %{buildroot}%{_metainfodir}/net.werwolv.%{name}.appdata.xml

# AppData
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/net.werwolv.%{name}.metainfo.xml

# install licenses
%if ! 0%{?fedora} >= 40
cp -a lib/third_party/capstone/LICENSE.TXT                           %{buildroot}%{_datadir}/licenses/%{name}/capstone-LICENSE
cp -a lib/third_party/capstone/suite/regress/LICENSE                 %{buildroot}%{_datadir}/licenses/%{name}/capstone-regress-LICENSE
%endif
cp -a lib/third_party/microtar/LICENSE                               %{buildroot}%{_datadir}/licenses/%{name}/microtar-LICENSE
cp -a lib/third_party/xdgpp/LICENSE                                  %{buildroot}%{_datadir}/licenses/%{name}/xdgpp-LICENSE

# remove when all paths are added to the cmake file
# https://github.com/WerWolv/ImHex/blob/master/cmake/build_helpers.cmake#L477
for i in nodes plugins scripts themes yara;
do
    cp -ra ImHex-Patterns/$i %{buildroot}%{_datadir}/imhex/$i
done


%files
%license %{_datadir}/licenses/%{name}/
%doc README.md
%{_bindir}/imhex
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_libdir}/libimhex.so.*
%{_libdir}/%{name}/
%{_metainfodir}/net.werwolv.%{name}.metainfo.xml
%exclude %{_bindir}/imhex-updater
%{_datadir}/mime/packages/%{name}.xml


%files patterns
%license ImHex-Patterns/LICENSE
%{_datadir}/%{name}/{constants,encodings,includes,magic,nodes,patterns,plugins,scripts,themes,yara}/


%files devel
%{_libdir}/libimhex.so
%{_datadir}/%{name}/sdk/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 30 2024 Jonathan Wright <jonathan@almalinux.org> - 1.36.2-1
- update to 1.36.2 rhbz#2333991

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> 1.35.4-3
- Rebuilt for mbedTLS 3.6.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Jonathan Wright <jonathan@almalinux.org> - 1.35.4-1
- update to 1.35.4 rhbz#2296493

* Tue Jul 02 2024 Jonathan Wright <jonathan@almalinux.org> - 1.35.3-1
- update to 1.35.3 rhbz#2295185

* Sat Jun 29 2024 Jonathan Wright <jonathan@almalinux.org> - 1.35.1-1
- update to 1.35.1

* Tue Jun 04 2024 Jonathan Wright <jonathan@almalinux.org> - 1.34.0-1
- update to 1.34.0 rhbz#2271246

* Sun Mar 24 2024 Jonathan Wright <jonathan@almalinux.org> - 1.33.2-1
- Update to 1.33.2 rhbz#2256886

* Sat Mar 02 2024 Jonathan Wright <jonathan@almalinux.org> - 1.33.1-1
- update to 1.33.1 rhbz#2267471

* Sun Feb 25 2024 Jonathan Wright <jonathan@almalinux.org> - 1.33.0-1
- update to 1.33.0

* Tue Feb 13 2024 Jonathan Wright <jonathan@almalinux.org> - 1.32.2-1
- update to 1.32.2 rhbz#2256886

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jonathan Wright <jonathan@almalinux.org> - 1.32.1-1
- Update to 1.32.1 rhbz#2256174

* Thu Nov 30 2023 Jonathan Wright <jonathan@almalinux.org> - 1.31.0-1
- Build fedora 40+ against system capstone
- Build fedora 39+ with llvm16-devel (compat package) rhbz#2246094
- Build EPEL9 with GCC 13
- update to 1.31.0 rhbz#2217232

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Jonathan Wright <jonathan@almalinux.org> - 1.30.1-4
- Use tar to uncompress source1 - rhel9 does not have rpmuncompress

* Mon Jul 03 2023 Jonathan Wright <jonathan@almalinux.org> - 1.30.1-3
- Create imhex-patterns subpackage rhbz#2219447

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.30.1-2
- Rebuilt due to fmt 10 update.

* Mon Jun 26 2023 Jonathan Wright <jonathan@almalinux.org> - 1.30.1-1
- update to 1.30.1 rhbz#2217232

* Mon May 22 2023 Jonathan Wright <jonathan@almalinux.org> - 1.29.0-1
- update to 1.29.0 rhbz#2208884

* Thu Apr 13 2023 Jonathan Wright <jonathan@almalinux.org> - 1.28.0-2
- rebuild to fix FTI on f37 related to libyara

* Tue Apr 04 2023 Jonathan Wright <jonathan@almalinux.org> - 1.28.0-1
- update to 1.28.0 rhbz#2184379

* Fri Mar 31 2023 Jonathan Wright <jonathan@almalinux.org> - 1.27.1-3
- rebuild against yara 4.3

* Thu Feb 16 2023 Jonathan Wright <jonathan@almalinux.org> - 1.27.1-2
- stop building on ppc64le

* Thu Feb 16 2023 Jonathan Wright <jonathan@almalinux.org> - 1.27.1-1
- update to 1.27.1 rhbz#2170425

* Sun Feb 12 2023 Jonathan Wright <jonathan@almalinux.org> - 1.27.0-1
- update to 1.27.0 rhbz#2169215

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Jonathan Wright <jonathan@almalinux.org> - 1.26.2-2
- remove unndeeded BR on python3-devel

* Thu Jan 05 2023 Jonathan Wright <jonathan@almalinux.org> - 1.26.2-1
- update to 1.26.2 rhbz#2158673

* Wed Jan 04 2023 Jonathan Wright <jonathan@almalinux.org> - 1.26.0-1
- update to 1.26.0 rhbz#2158207

* Tue Nov 15 2022 Jonathan Wright <jonathan@almalinux.org> - 1.25.0-1
- update to 1.25.0 rhbz#2142599

* Wed Oct 12 2022 Jonathan Wright <jonathan@almalinux.org> - 1.24.3-1
- update to 1.24.3

* Mon Oct 10 2022 Jonathan Wright <jonathan@almalinux.org> - 1.24.2-1
- update to 1.24.2

* Mon Oct 10 2022 Jonathan Wright <jonathan@almalinux.org> - 1.24.1-1
- update to 1.24.1

* Mon Oct 10 2022 Jonathan Wright <jonathan@almalinux.org> - 1.24.0-1
- Update to 1.24.0 rhbz#2133163

* Sat Sep 17 2022 Jonathan Wright <jonathan@almalinux.org> - 1.23.2-1
- Update to 1.23.2 rhbz#2127614

* Thu Sep 15 2022 Jonathan Wright <jonathan@almalinux.org> - 1.23.0-1
- Update to 1.23.0 rhbz#2127174

* Sun Sep 04 2022 Jonathan Wright <jonathan@almalinux.org> - 1.22.0-1
- Update to 1.22.0 rhbz#2124107

* Wed Aug 17 2022 Jonathan Wright <jonathan@almalinux.org> - 1.21.2-2
- Document packaged intervaltree lib

* Wed Aug 17 2022 Jonathan Wright <jonathan@almalinux.org> - 1.21.2-1
- Update to 1.21.2 (fixes rhbz#2119220)
- Use system libnfd (nativefiledialog-extended)
- More EPEL spec prep

* Mon Aug 15 2022 Jonathan Wright <jonathan@almalinux.org> - 1.21.1-1
- Update to 1.21.1

* Sun Aug 14 2022 Jonathan Wright <jonathan@almalinux.org> - 1.21.0-2
- Updates requires to ensure package needed for file dialogs is present

* Sun Aug 14 2022 Jonathan Wright <jonathan@almalinux.org> - 1.21.0-1
- Update to 1.21.0

* Fri Aug 12 2022 Jonathan Wright <jonathan@almalinux.org> - 1.20.0-2
- EPEL9 prep
- Build on ppc64le

* Fri Aug 05 2022 Jonathan Wright <jonathan@almalinux.org> - 1.20.0-1
- Initial package build
