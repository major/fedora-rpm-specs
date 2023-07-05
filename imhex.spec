Name:           imhex
Version:        1.30.1
Release:        4%{?dist}
Summary:        A hex editor for reverse engineers and programmers

License:        GPL-2.0-only AND Zlib AND MIT AND Apache-2.0
# imhex is gplv2.  capstone is custom.  nativefiledialog is Zlib.
# see license dir for full breakdown
URL:            https://imhex.werwolv.net/
# We need the archive with deps bundled
Source0:        https://github.com/WerWolv/%{name}/releases/download/v%{version}/Full.Sources.tar.gz#/%{name}-%{version}.tar.gz
# default to including the same-version patterns as a suggested package
Source1:        https://github.com/WerWolv/ImHex-Patterns/archive/refs/tags/ImHex-v%{version}.tar.gz#/%{name}-patterns-%{version}.tar.gz

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
BuildRequires:  llvm-devel
BuildRequires:  mbedtls-devel
BuildRequires:  yara-devel
BuildRequires:  nativefiledialog-extended-devel
%if 0%{?rhel}
BuildRequires:  gcc-toolset-12
%endif

Recommends:     imhex-patterns = %{version}-%{release}

Provides:       bundled(gnulib)
Provides:       bundled(capstone) = 5.0-rc2
Provides:       bundled(imgui)
Provides:       bundled(libromfs)
Provides:       bundled(microtar)
Provides:       bundled(libpl)
Provides:       bundled(xdgpp)
# working on packaging this, bundling for now as to now delay updates
Provides:       bundled(miniaudio) = 0.11.11

# ftbfs on these arches.  armv7hl might compile when capstone 5.x
# is released upstream and we can build against it
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


%prep
%autosetup -n ImHex
# remove bundled libs we aren't using
rm -rf lib/external/{curl,fmt,llvm,nlohmann_json,yara}

%build
%if 0%{?rhel}
. /opt/rh/gcc-toolset-12/enable
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
 -D USE_SYSTEM_LLVM=ON                   \
 -D USE_SYSTEM_YARA=ON                   \
 -D USE_SYSTEM_NFD=ON                    \
# when capstone >= 5.x is released we should be able to build against \
# system libs of it \
# -D USE_SYSTEM_CAPSTONE=ON

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
cp -a lib/external/nativefiledialog/LICENSE                       %{buildroot}%{_datadir}/licenses/%{name}/nativefiledialog-LICENSE
cp -a lib/external/capstone/LICENSE.TXT                           %{buildroot}%{_datadir}/licenses/%{name}/capstone-LICENSE
cp -a lib/external/capstone/suite/regress/LICENSE                 %{buildroot}%{_datadir}/licenses/%{name}/capstone-regress-LICENSE
cp -a lib/external/microtar/LICENSE                               %{buildroot}%{_datadir}/licenses/%{name}/microtar-LICENSE
cp -a lib/external/xdgpp/LICENSE                                  %{buildroot}%{_datadir}/licenses/%{name}/xdgpp-LICENSE

# install patterns
/usr/bin/tar -xf %{SOURCE1}
mkdir %{buildroot}%{_datadir}/imhex
for i in constants encodings includes magic nodes patterns plugins scripts tests themes tips yara;
do
    cp -ra ImHex-Patterns-ImHex-v%{version}/$i %{buildroot}%{_datadir}/imhex/$i
done

%files
%license %{_datadir}/licenses/%{name}/
%doc README.md
%{_bindir}/imhex
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_libdir}/libimhex.so*
%{_libdir}/%{name}/
%{_metainfodir}/net.werwolv.%{name}.metainfo.xml


%files patterns
%license ImHex-Patterns-ImHex-v%{version}/LICENSE
%{_datadir}/imhex/*


%changelog
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
