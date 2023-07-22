#%%global debugtrace 1

# Set to 0 when upgrading to a new ICU release that contains up-to-date timezone data.
# (or update the timezone data update..).
%global use_tzdata_update 0
# Adjust to version major; used in tzdata update.
%global icu_major 72

Name:      libicu72
Version:   72.1
Release:   2%{?dist}
Summary:   International Components for Unicode

License:   Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:       http://site.icu-project.org/
Source0:   https://github.com/unicode-org/icu/releases/download/release-72-1/icu4c-72_1-src.tgz
%if 0%{?use_tzdata_update}
Source1:   https://github.com/unicode-org/icu/releases/download/release-72-1/icu4c-72_1-data.zip
Source2:   https://raw.githubusercontent.com/unicode-org/icu-data/main/tzdata/icunew/2022b/44/metaZones.txt
Source3:   https://raw.githubusercontent.com/unicode-org/icu-data/main/tzdata/icunew/2022b/44/timezoneTypes.txt
Source4:   https://raw.githubusercontent.com/unicode-org/icu-data/main/tzdata/icunew/2022b/44/windowsZones.txt
Source5:   https://raw.githubusercontent.com/unicode-org/icu-data/main/tzdata/icunew/2022b/44/zoneinfo64.txt
%endif
Source10:   icu-config.sh

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: doxygen, autoconf, python3
BuildRequires: make

Patch4: gennorm2-man.patch
Patch5: icuinfo-man.patch

# Explicitly conflict with older icu packages that ship libraries
# with the same soname as this compat package
Conflicts: libicu < 73

%description
Tools and utilities for developing with icu.

%prep
%autosetup -p1 -n icu
%if 0%{?use_tzdata_update}
pushd source
unzip -o %{SOURCE1}
rm -f data/in/icudt%{icu_major}l.dat
cp -v -f %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} data/misc
popd
%endif

%build
pushd source
autoconf
CFLAGS='%optflags -fno-strict-aliasing'
CXXFLAGS='%optflags -fno-strict-aliasing'
# Endian: BE=0 LE=1
%if ! 0%{?endian}
CPPFLAGS='-DU_IS_BIG_ENDIAN=1'
%endif

#rhbz856594 do not use --disable-renaming or cope with the mess
OPTIONS='--with-data-packaging=library --disable-samples'
%if 0%{?debugtrace}
OPTIONS=$OPTIONS' --enable-debug --enable-tracing'
%endif
%configure $OPTIONS

#rhbz#225896
sed -i 's|-nodefaultlibs -nostdlib||' config/mh-linux
#rhbz#813484
sed -i 's| \$(docfilesdir)/installdox||' Makefile
# There is no source/doc/html/search/ directory
sed -i '/^\s\+\$(INSTALL_DATA) \$(docsrchfiles) \$(DESTDIR)\$(docdir)\/\$(docsubsrchdir)\s*$/d' Makefile
# rhbz#856594 The configure --disable-renaming and possibly other options
# result in icu/source/uconfig.h.prepend being created, include that content in
# icu/source/common/unicode/uconfig.h to propagate to consumer packages.
test -f uconfig.h.prepend && sed -e '/^#define __UCONFIG_H__/ r uconfig.h.prepend' -i common/unicode/uconfig.h

# more verbosity for build.log
sed -i -r 's|(PKGDATA_OPTS = )|\1-v |' data/Makefile

%make_build
%make_build doc


%install
rm -rf $RPM_BUILD_ROOT source/__docs
%make_install %{?_smp_mflags} -C source
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so.*

# Remove files that aren't needed for the compat package
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/icu/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_sbindir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/icu/
rm -rf $RPM_BUILD_ROOT%{_mandir}

%check
# test to ensure that -j(X>1) didn't "break" man pages. b.f.u #2357
if grep -q @VERSION@ source/tools/*/*.8 source/tools/*/*.1 source/config/*.1; then
    exit 1
fi
%make_build -C source check

# log available codes
pushd source
LD_LIBRARY_PATH=lib:stubdata:tools/ctestfw:$LD_LIBRARY_PATH bin/uconv -l


%files
%license LICENSE
%{_libdir}/*.so.*


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 72.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 72.1-1
- Initial packaging based on libicu69
