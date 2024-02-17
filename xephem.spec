%global gittag 4.2.0
#%%global commit a2da14bfc6727b1255df6f31ac4ce89d4bd881c8
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global date 20240205

Name:           xephem
%if "%{?gittag}"
Version:        %{gittag}
%else
Version:        4.1.0^%{date}.git%{shortcommit}
%endif
Release:        %autorelease
Summary:        Scientific-grade interactive astronomical ephemeris software
License:        MIT-advertising and LGPL-2.1-or-later

URL:            https://%{name}.github.io
%if "%{?gittag}"
Source0:        https://github.com/XEphem/XEphem/archive/%{gittag}/XEphem-%{version}.tar.gz
%else
Source0:        https://github.com/XEphem/XEphem/archive/%{commit}/XEphem-%{commit}.tar.gz
%endif
# Desktop and appstream metadata files are not provided in upstream sources
Source1:        io.github.xephem.desktop
Source2:        io.github.xephem.metainfo.xml

# Patch to use system libraries and not override CFLAGS
# Proposed upstream: https://github.com/XEphem/XEphem/pull/58
Patch:          xephem_makefile.patch

# Patch to use cmake to build and install
# Proposed upstream: https://github.com/XEphem/XEphem/pull/60
Patch:          xephem_with_cmake.patch

# Define _GNU_SOURCE, so that <time.h> declares strptime, an X/Open
# extension that is not available by default in the glibc headers.
# Submitted upstream: <https://github.com/XEphem/XEphem/pull/73>
Patch:          xephem-c99.patch

ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  groff-base
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  motif-devel
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)

Requires:       %{name}-data = %{version}-%{release}
Requires:       curl
Requires:       gzip

%description
XEphem is a scientific-grade interactive astronomical ephemeris software.
It can calculate ephemeris for astronomical objects and display the results
in tabular or graphical output.

XEphem can also be used to control telescopes, generate sky maps, perform
image analysis and much more.


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    data
The %{name}-data package contains data files for %{name} functionality.


%prep
%if "%{?gittag}"
%autosetup -p1 -n XEphem-%{version}
%else
%autosetup -p1 -n XEphem-%{commit}
%endif

# Remove libraries sources for which we want to use system libraries
rm -rf libpng/
rm -rf libjpegd/
rm -rf libz/
rm -rf libXm/

# Rename liblilxml license files
cp liblilxml/LICENSE LICENSE.liblilxml

# Change hardcoded resources directory for flatpak
%if 0%{?flatpak}
sed -i -e 's|/etc/XEphem|/app/etc/XEphem|g' GUI/xephem/{splash.c,xephem.c}
%endif


%build
%if 0%{?epel}
%set_build_flags
%endif

%cmake
%cmake_build

# Create standard size icons
for d in 32 48 64 128 ; do
    convert GUI/xephem/XEphem.png -geometry ${d}x${d} -depth 8 -background none xephem-${d}.png
done

# Old manual build method
#pushd GUI/xephem
#%%make_build
#popd


%install
%cmake_install

# Old manual install method
# There's no automated install
#mkdir -p %%{buildroot}%%{_bindir}
#mkdir -p %%{buildroot}%%{_mandir}/man1/
#mkdir -p %%{buildroot}%%{_datadir}/%%{name}
#pushd GUI/xephem
#install -p -m0755 %%{name} %%{buildroot}/%%{_bindir}
#install -p -m0644 %%{name}.1 %%{buildroot}/%%{_mandir}/man1/
#cp -pR auxil %%{buildroot}%%{_datadir}/%%{name}
#cp -pR catalogs %%{buildroot}%%{_datadir}/%%{name}
#cp -pR fifos %%{buildroot}%%{_datadir}/%%{name}
#cp -pR fits %%{buildroot}%%{_datadir}/%%{name}
#cp -pR gallery %%{buildroot}%%{_datadir}/%%{name}
#cp -pR help %%{buildroot}%%{_datadir}/%%{name}
#cp -pR lo %%{buildroot}%%{_datadir}/%%{name}
#popd

# Create file to tell xephem where to find resources
mkdir -p %{buildroot}%{_sysconfdir}
cat >%{buildroot}%{_sysconfdir}/XEphem <<EOF
XEphem.ShareDir: %{_datadir}/%{name}
EOF

# Provide a desktop entry
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install icons
for d in 32 48 64 128 ; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${d}x${d}/apps/
    install -p -m0644 xephem-${d}.png %{buildroot}%{_datadir}/icons/hicolor/${d}x${d}/apps/xephem.png
done

# Install appstream metadata
mkdir -p %{buildroot}%{_metainfodir}
install -p -m0644 %{SOURCE2} %{buildroot}%{_metainfodir}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

pushd tests
make run-test
popd


%files
%license LICENSE LICENSE.liblilxml
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/io.github.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/xephem.png
%{_metainfodir}/io.github.%{name}.metainfo.xml

%files      data
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/XEphem


%changelog
%autochangelog
