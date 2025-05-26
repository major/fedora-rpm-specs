%global         testcommit  591b5a053f9aa15245ccbd1d334cf3f8031b1035
%global         testshortcommit  %(c=%{testcommit}; echo ${c:0:7})
%global         srcname muon
Name:           muon-meson
Version:        0.4.0
Release:        %{autorelease}
Summary:        C implementation of meson

# Main code is GPL-3.0-only
# MIT src/external/tinyjson.c
# MIT src/memmem.c
# unlicense src/sha_256
# MIT src/external/samurai/graph.c
# MIT src/external/samurai/parse.c
# MIT src/external/samurai/build.c
# MIT src/external/samurai/scan.c
# MIT src/external/samurai/env.c
# MIT src/external/samurai/tree.c
# MIT src/external/samurai/log.c
# MIT src/external/samurai/util.c
# MIT src/external/samurai/deps.c
# MIT src/external/samurai/tool.c
# MIT src/external/samurai/htab.c
# MIT src/external/samurai/samu.c

License:        Apache-2.0 AND GPL-3.0-only AND MIT AND Unlicense
URL:            https://muon.build
Source0:        https://git.sr.ht/~lattis/%{srcname}/archive/%{version}.tar.gz#/muon-%{version}.tar.gz
Source1:        https://github.com/muon-build/meson-tests/archive/%{testcommit}/meson-tests-%{testshortcommit}.tar.gz
# Skip tests which fail
Patch:          skip-tests.patch

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpkgconf-devel
BuildRequires:  pkgconf
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyyaml)
BuildRequires:  scdoc

# These are built in to provide needed
# functionality.
Provides:       bundled(memmem)
Provides:       bundled(samurai)
Provides:       bundled(sha_256)
Provides:       bundled(tiny_json)

%description
An implementation of the meson build system in c99 with minimal dependencies.

%prep
%autosetup -n %{srcname}-%{version} -p 1
tar xf %{SOURCE1}
mv meson-tests-%{testcommit} subprojects/meson-tests

%build
CFLAGS="-fPIE -DBOOTSTRAP_NO_TRACY %{optflags}" ./bootstrap.sh %{_vpath_builddir}
%{_vpath_builddir}/muon-bootstrap setup \
 -Dprefix=%{_prefix} \
 -Dwebsite=false \
 -Dstatic=false \
 -Ddocs=enabled \
 -Dsamurai=enabled \
 -Dlibarchive=enabled \
 -Dlibcurl=enabled \
 -Dlibpkgconf=enabled \
 %{_vpath_builddir}
%{_vpath_builddir}/muon-bootstrap -C %{_vpath_builddir} samu

%check
%{_vpath_builddir}/muon -C %{_vpath_builddir} test

%install
DESTDIR=%{buildroot} %{_vpath_builddir}/muon \
       -C %{_vpath_builddir} install

%files
%license LICENSES/Apache-2.0.txt
%license LICENSES/GPL-3.0-only.txt
%license LICENSES/MIT.txt
%license LICENSES/Unlicense.txt
%{_bindir}/muon
%{_mandir}/man1/muon.*
# Conflicts with meson documentation
%exclude %{_mandir}/man5/meson.*


%changelog
%autochangelog
