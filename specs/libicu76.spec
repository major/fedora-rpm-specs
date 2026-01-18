#%%global debugtrace 1

# Set to 0 when upgrading to a new ICU release that contains up-to-date timezone data.
# (or update the timezone data update..).
%global use_tzdata_update 0

%define version_dash %{gsub %{version} %. -}
%define version_underscore %{gsub %{version} %. _}

Name:      libicu76
Version:   76.1
Release:   2%{?dist}
Summary:   Compat package with icu 76.1 libraries

License:   Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND NAIST-2003 AND LicenseRef-Fedora-Public-Domain
URL:       http://site.icu-project.org/
Source0:   https://github.com/unicode-org/icu/releases/download/release-%{version_dash}/icu4c-%{version_underscore}-src.tgz
%if 0%{?use_tzdata_update}
Source1:   https://github.com/unicode-org/icu/releases/download/release-%{version_dash}/icu4c-%{version_underscore}-data.zip
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

# To be removed next release, rhbz#2335638
Patch101: 0001-ICU-22954-USet-C-iterator-return-std-u16string.patch
Patch102: 0002-ICU-22954-U_ICU_NAMESPACE_OR_INTERNAL-header-only-lo.patch
Patch103: 0003-ICU-22954-intltest.h-IcuTestErrorCode-usable-without.patch
Patch104: 0004-ICU-22954-header-only-test-USet-C-iterators.patch
Patch105: 0005-ICU-22954-Partially-revert-PR-3295-U_ICU_NAMESPACE_O.patch
Patch106: 0006-ICU-22954-USetHeaderOnlyTest-use-unique_ptr.patch
Patch107: 0007-ICU-22954-Delete-copy-assign-from-IcuTestErrorCode.patch
Patch108: 0008-ICU-22954-Workaround-Replace-std-u16string-member-wi.patch
Patch109: 0009-ICU-22954-Revert-to-using-std-u16string-instead-of-U.patch


# Explicitly conflict with older icu packages that ship libraries
# with the same soname as this compat package
Conflicts: libicu < 77

%description
Compatibility package with icu libraries ABI version 76.


%{!?endian: %global endian %(%{__python3} -c "import sys;print (0 if sys.byteorder=='big' else 1)")}
# " this line just fixes syntax highlighting for vim that is confused by the above and continues literal


%prep
%autosetup -p1 -n icu
%if 0%{?use_tzdata_update}
pushd source
unzip -o %{SOURCE1}
rm -f data/in/icudt*l.dat
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

%install
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
%doc readme.html
%{_libdir}/*.so.*


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 76.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 30 2025 Frantisek Zatloukal <fzatlouk@redhat.com> - 76.1-1
- Initial compat package
