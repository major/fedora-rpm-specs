# Use ondrejbudai's fork for now since upstream appears unmaintained.
# See https://github.com/pdewacht/brlaser/issues/145
%global forgeurl https://github.com/ondrejbudai/brlaser
%global commit   7716c7d44230f5955061d1e8896425c6e8e57b59
%global date     20220509

Name:           printer-driver-brlaser
Version:        6
%forgemeta
Release:        3%{?dist}
Summary:        Brother laser printer driver

License:        GPLv2+
URL:            %{forgeurl}
Source0:        %{forgesource}

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
%forgesetup

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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 09 2022 Ondrej Budai <ondrej@budai.cz> - 6-2
- Add support for many devices by pulling merging unmerged upstream PRs

* Sun Mar 27 2022 Ondrej Budai <ondrej@budai.cz> - 6-1
- Initial package version
