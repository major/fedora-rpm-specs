%global date 20230219
%global revision 625

Name:           xtideuniversalbios
Version:        2.0.0^%{date}svn%{revision}
Release:        %autorelease
Summary:        XTIDE Universal BIOS

License:        GPL-2.0-or-later
URL:            https://www.xtideuniversalbios.org
# Generated with ./update_snapshot.sh
Source:         %{name}-r%{revision}.tar.gz
Source:         update_snapshot.sh

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  mingw32-gcc-c++
BuildRequires:  nasm
BuildRequires:  perl
BuildRequires:  sed
BuildRequires:  upx

BuildArch:      noarch

%description
XTIDE Universal BIOS makes it possible to use modern large ATA hard disks or
Compact Flash cards on old PC's. You can then enjoy quiet or noiseless drives
with more capacity than you'll ever need for old computers.

XTIDE Universal BIOS (also known as simply "XUB") can be used on any IBM PC,
XT, AT or 100% compatible system.

%prep
%autosetup -n %{name}-r%{revision}

# Convert makefiles from Windows to Linux
find . -type f -name makefile -exec sed -i '{}' -e 's:\\:/:g' -e 's:\*\.\*:*:g' \;
sed -i Serial_Server/makefile \
  -e 's:/c :-c :g' \
  -e 's:/Febuild:-o build:g' \
  -e 's:/Fobuild:-o build:g'

# Fix end of line encoding
sed -i 's/\r$//' XTIDE_Universal_BIOS/Doc/*.txt

%build
for target in \
  BIOS_Drive_Information_Tool \
  XTIDE_Universal_BIOS
do
  %make_build -C "$target" \
    AS="nasm" \
    MAKE="make" \
    RM="rm -rf"
done

# BIOS_Drive_Information_Tool is too small to be compressed with upx so it's
# built above without using the release target
for target in \
  Configurator \
  Serial_Server \
  XTIDE_Universal_BIOS_Configurator_v2
do
  %make_build -C "$target" release \
    AS="nasm" \
    CXX="%{mingw32_target}-g++" \
    CXXFLAGS="-Os -DWIN32 -fpermissive" \
    MAKE="make" \
    RM="rm -rf"
done

%install
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name} \
  BIOS_Drive_Information_Tool/Build/biosdrvs.com \
  Configurator/Build/idecfg.com \
  Serial_Server/build/serdrive.exe \
  XTIDE_Universal_BIOS/Build/*.bin \
  XTIDE_Universal_BIOS_Configurator_v2/Build/xtidecfg.com

%files
%license license.txt
%doc XTIDE_Universal_BIOS/Doc/*
%{_datadir}/%{name}/

%changelog
%autochangelog
