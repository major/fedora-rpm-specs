#%%global gittag 4.1.0
%global commit b7bfc6eb31464287b5d65cb3f1e36d7dbf3dd381
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20221006

Name:           xephem
%if "%{?gittag}"
Version:        4.1.0
%else
Version:        4.1.0^%{date}%{shortcommit}
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
# Desktop file is not provided by upstream
Source1:        io.github.xephem.desktop

# Patch to use system libraries and not override CFLAGS
Patch:          xephem_makefile.patch

ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  groff-base
BuildRequires:  make
BuildRequires:  motif-devel
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


%build
%if 0%{?epel}
%set_build_flags
%endif

pushd GUI/xephem
%make_build
popd


%install
# There's no automated install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_datadir}/%{name}

pushd GUI/xephem
install -p -m0755 %{name} %{buildroot}/%{_bindir}
install -p -m0644 %{name}.1 %{buildroot}/%{_mandir}/man1/
cp -pR auxil %{buildroot}%{_datadir}/%{name}
cp -pR catalogs %{buildroot}%{_datadir}/%{name}
cp -pR fifos %{buildroot}%{_datadir}/%{name}
cp -pR fits %{buildroot}%{_datadir}/%{name}
cp -pR gallery %{buildroot}%{_datadir}/%{name}
cp -pR help %{buildroot}%{_datadir}/%{name}
cp -pR lo %{buildroot}%{_datadir}/%{name}

# Create file to tell xephem where to find resources
cat >%{buildroot}%{_sysconfdir}/XEphem <<EOF
XEphem.ShareDir: %{_datadir}/%{name}
EOF

popd

# Provide a desktop entry
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m0644 GUI/xephem/XEphem.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/


%check
# Tests currently fail, need to check with upstream
#pushd tests
#make run-test
#popd


%files
%license LICENSE LICENSE.liblilxml
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/io.github.%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/XEphem.png

%files      data
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/XEphem


%changelog
%autochangelog
