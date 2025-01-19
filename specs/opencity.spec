Name:           opencity
Version:        0.0.6.5
Release:        26%{?dist}
Summary:        Full 3D city simulator game project

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.opencity.info
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}stable.tar.bz2
Source1:        %{name}.appdata.xml
# Remove bundled libraries tinyxml, tinyxpath and binreloc from Makefiles.am
Patch0:        %{name}.remove_bundled_libraries.patch
# Remove binreloc references from code.
Patch1:        %{name}.remove_binreloc_references.patch

BuildRequires: make
BuildRequires:  SDL-devel SDL_image-devel SDL_net-devel SDL_mixer-devel 
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libtool autoconf
BuildRequires:  tinyxml-devel tinyxpath-devel
BuildRequires:  gcc-c++

Requires: %{name}-data


%description
This is just another city simulation.
The idea is simple: you have to build a city with 3 types of "zones":
Residential, Commercial and Industrial.
They depend on each other during their development.
Try to give them what they need and watch your city growing up.

%package data
Summary: Data files for opencity
BuildArch: noarch
%description data
Data files for opencity.

%prep
%setup -q -n %{name}-%{version}stable
%patch -P0

%patch -P1
rm -rf src/tinyxml/
rm -rf src/tinyxpath/
rm -rf src/binreloc/

# Replace obsolete macro
sed -i 's+AC_PROG_LIBTOOL+LT_INIT+g' configure.ac

#Fix bad include
sed -i 's+#include "tinyxml/tinyxml.h"+#include "tinyxml.h"+g' src/zen.cpp 

#Fix some paths (only sDataDir and sConfigDir, because sSaveDir is detected without binreloc)
sed -i 's+static string sDataDir\t\t= "";+static string sDataDir\t\t= "%{_datadir}/%{name}/";+g' src/main.cpp
sed -i 's+static string sConfigDir\t= "";+static string sConfigDir\t= "%{_sysconfdir}/%{name}/";+g' src/main.cpp
sed -i 's+static string sDataDir\t\t= "";+static string sDataDir\t\t= "%{_datadir}/%{name}/";+g' src/zen.cpp
sed -i 's+static string sConfigDir\t= "";+static string sConfigDir\t= "%{_sysconfdir}/%{name}/";+g' src/zen.cpp

for f in COPYRIGHT AUTHORS docs/FAQ_it.txt docs/README_es.txt docs/README_it.txt
do
iconv -f iso8859-1 -t utf-8 $f > $f.conv && mv -f $f.conv $f
done

#Fix some bad ending lines
sed -i 's/\r$//' docs/*_it.txt


%build
# https://sourceforge.net/p/opencity/code/HEAD/tree/trunk/opencity/autogen.sh
aclocal
libtoolize -c
autoconf
autoheader
automake -a -c

%configure CXXFLAGS="-I%{_includedir}/tinyxpath \
-DWITHOUT_BINRELOC %{optflags}" LDFLAGS="-ltinyxml -ltinyxpath"

make %{?_smp_mflags}


%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Install the appdata file
mkdir %{buildroot}%{_datadir}/appdata/
install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# Documentation handled by %%doc
rm -rfv %{buildroot}%{_defaultdocdir}/%{name}


%files
%doc AUTHORS README docs/FAQ* docs/README*
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%config(noreplace) %{_sysconfdir}/%{name}

%files data
%{_datadir}/%{name} 
%license COPYING COPYRIGHT


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.6.5-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Alexandre Moine <nobrakal@fedoraproject.org> - 0.0.6.5-10
- Add gcc-c++ as a build dependency.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 01 2015 Alexandre Moine <nobrakal@gmail.com> 0.0.6.5-3
- Remove double installation of doc files
- Remove --include %%{_includedir}/tinyxml.h of CXX flags
- Move license into -data subpackage

* Fri Jul 31 2015 Alexandre Moine <nobrakal@gmail.com> 0.0.6.5-2
- Add %%{optflags} to CXXFLAGS.
- Set BuildArch: noarch to -data.
- Remove explicit dependency tinyxml and tinyxpath.
- Remove double installed license file.
- Use %%doc to take care of doc files.
- Remove useless %%{name}.remove_install_files.patch

* Tue Jul 14 2015 Alexandre Moine <nobrakal@gmail.com> 0.0.6.5-1
- Change "%%{_sysconfdir}/%%{name}" to "%%config(noreplace) %%{_sysconfdir}/%%{name}".
- Add COPYING and COPYRIGHT to %%license section.
- Add a data subpackage.
- Remove bundled tinyxml, tinyxpath and binreloc.
- Add an appdata file.

* Wed Feb 18 2015 Alexandre Moine <nobrakal@gmail.com> 0.0.6.4-1
- Initial spec.
