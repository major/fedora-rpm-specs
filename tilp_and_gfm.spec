%global forgeurl https://github.com/debrouxl/tilp_and_gfm
%global commit 752aef4dc2b2fdd21a06cda03130375d8d4ad9b6
%if 0%{?el7}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global forgesource %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
%global date 20220201
%else
%forgemeta
%endif

Name:           tilp_and_gfm
Version:        1.19
%if 0%{?el7}
Release:        %autorelease -s %{date}git%{shortcommit}
%else
Release:        %autorelease
%endif
Summary:        Desktop applications to manage Texas Instruments calculators

License:        GPLv2+
URL:            http://lpg.ticalc.org/prj_tilp
Source0:        %{forgesource}

BuildRequires:  desktop-file-utils
%if 0%{?el7}
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libappstream-glib

BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  tilibs-devel

%description
TiLP and GFM are desktop applications to handle communications and file exchange
with Texas Instruments calculators.

%package -n     tilp
Summary:        Texas Instruments handheld(s) <-> PC communication program
# Replace retired packages in F35, remove once F37 is branched
Obsoletes:      tilp2 < 1.18-14
Provides:       tilp2 = %{version}-%{release}

%description -n tilp
TiLP is a Texas Instruments handhelds <-> PC communication program for Linux.
It is able to use any type of link cable (Gray/Black/Silver/Direct Link) with
any calculator.

With TiLP, you can transfer files from your PC to your Texas Instruments
calculator, and vice-versa. You can also make a screen dump, send/receive data,
backup/restore contents, install FLASH applications, or upgrade the  OS.

%package -n     gfm
Summary:        Texas Instruments handheld(s) file manipulation program

%description -n gfm
The GFM is an application allowing for the manipulation of single/group/tigroup
files from Texas Instruments handhelds. It can create a new file, open an
existing file, save file, rename variables, remove variables, create folders,
group files into a group/tigroup file, and ungroup a group/tigroup file into
single files.

%prep
%if 0%{?el7}
%autosetup -n %{name}-%{commit} -p1

# Drop unsupported flags
sed -i -e 's/-Werror=date-time//' -e 's/-Werror=return-type//' CMakeLists.txt
%else
%forgeautosetup -p1
%endif

# Fix line endings
sed -i 's/\r$//' tilp/trunk/RELEASE
# Relocate icons license
mv tilp/trunk/icons/COPYRIGHT tilp/trunk/COPYRIGHT.icons
mv gfm/trunk/icons/COPYRIGHT gfm/trunk/COPYRIGHT.icons

%build
# Generate missing POT files
pushd tilp/trunk/po && intltool-update --pot && popd
pushd gfm/trunk/po && intltool-update --pot && popd

# Build TiLP and GFM
%if 0%{?el7}
%cmake3
%cmake3_build
%else
%cmake
%cmake_build
%endif

%install
%if 0%{?el7}
%cmake3_install
%else
%cmake_install
%endif
%find_lang tilp2
%find_lang GFM

# Remove useless files
rm -r %{buildroot}%{_datadir}/tilp2/desktop
find %{buildroot} -name \*.bat -exec rm '{}' \;
find %{buildroot} -name Makefile.am -exec rm '{}' \;

# Fix binary name and add compatibility symlink
mv %{buildroot}%{_bindir}/tilp2 %{buildroot}%{_bindir}/tilp
ln -s tilp %{buildroot}%{_bindir}/tilp2

# Install MIME types
%if 0%{?el7}
mkdir -p %{buildroot}%{_datadir}/mime/packages
%endif
install -Dpm0644 -t %{buildroot}%{_datadir}/mime/packages \
  tilp/trunk/desktop/tilp.xml

# Install desktop files
mkdir -p %{buildroot}/%{_datadir}/applications
sed -e 's:@bindir@:%{_bindir}:' \
    -e 's:@pixmapsdir@:%{_datadir}/tilp2/pixmaps:' \
    < tilp/trunk/desktop/tilp.desktop.in \
    > %{buildroot}%{_datadir}/applications/tilp.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/tilp.desktop
sed -e 's:@bindir@:%{_bindir}:' \
    -e 's:@pixmapsdir@:%{_datadir}/gfm/pixmaps:' \
    < gfm/trunk/desktop/gfm.desktop.in \
    > %{buildroot}%{_datadir}/applications/gfm.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/gfm.desktop

# Install appdata files
%if 0%{?el7}
mkdir -p %{buildroot}%{_metainfodir}
%endif
install -Dpm0644 -t %{buildroot}%{_metainfodir} \
  tilp/trunk/desktop/tilp.appdata.xml
install -Dpm0644 -t %{buildroot}%{_metainfodir} \
  gfm/trunk/desktop/gfm.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -n tilp -f tilp2.lang
%license tilp/trunk/COPYING tilp/trunk/COPYRIGHT.icons
%doc tilp/trunk/AUTHORS tilp/trunk/ChangeLog tilp/trunk/README tilp/trunk/RELEASE
%{_bindir}/tilp
%{_bindir}/tilp2
%{_mandir}/man1/tilp.1*
%{_datadir}/tilp2
%{_datadir}/mime/packages/tilp.xml
%{_datadir}/applications/tilp.desktop
%{_metainfodir}/tilp.appdata.xml

%files -n gfm -f GFM.lang
%license gfm/trunk/COPYING gfm/trunk/COPYRIGHT.icons
%doc gfm/trunk/AUTHORS gfm/trunk/ChangeLog gfm/trunk/README
%{_bindir}/gfm
%{_mandir}/man1/gfm.1*
%{_datadir}/gfm
%{_datadir}/applications/gfm.desktop
%{_metainfodir}/gfm.appdata.xml

%changelog
%autochangelog
