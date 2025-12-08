Version:       6.2.0
%global tag %{version}
%global forgeurl https://github.com/OpenTTD/grfcodec
%forgemeta

Name:           grfcodec
Release:        %autorelease
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-ng-compat-devel

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.


%prep
%forgeautosetup


%build
%cmake
%cmake_build


%install
%cmake_install

%files
%doc changelog.txt COPYING
%doc docs/*.txt docs/readme.md
%{_bindir}/grfcodec
%{_bindir}/grfid
%{_bindir}/grfstrip
%{_bindir}/nforenum
%{_mandir}/man1/grfcodec.1.gz
%{_mandir}/man1/grfid.1.gz
%{_mandir}/man1/grfstrip.1.gz
%{_mandir}/man1/nforenum.1.gz


%changelog
%autochangelog
