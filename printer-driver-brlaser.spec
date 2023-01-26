# Use QORTEC's fork for now since upstream appears unmaintained.
# See https://github.com/pdewacht/brlaser/issues/145
%global forgeurl https://github.com/QORTEC/brlaser

Name:           printer-driver-brlaser
Version:        6.2
%forgemeta
Release:        %autorelease
Summary:        Brother laser printer driver

License:        GPLv2+
URL:            %{forgeurl}
Source0:        %{forgesource}

Patch0:         0001-fix-build-under-Fedora-38.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cups-devel
Requires:       cups-filesystem
Requires:       ghostscript

%description
brlaser is a CUPS driver for Brother laser printers.

Although most Brother printers support a standard printer language
such as PCL or PostScript, not all do. If you have a monochrome
Brother laser printer (or multi-function device) and the other open
source drivers don't work, this one might help.

For a detailed list of supported printers, please refer to
%{forgeurl}

%prep
%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_cups_serverbin}/filter/rastertobrlaser
%{_datadir}/cups/drv/brlaser.drv
%doc README.md
%license COPYING

%changelog
%autochangelog
