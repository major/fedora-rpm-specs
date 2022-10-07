Name:           pageedit
Version:        1.9.20
Release:        1%{?dist}
Summary:        ePub visual XHTML editor

License:        GPL-3.0-or-later AND Apache-2.0
URL:            https://sigil-ebook.com/
Source0:        https://github.com/Sigil-Ebook/PageEdit/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  desktop-file-utils

Provides:       bundled(gumbo) = 0.9.2

ExclusiveArch: %{qt5_qtwebengine_arches}


%description
An ePub visual XHTML editor based on Sigil's Deprecated BookView.


%prep
%autosetup -n PageEdit-%{version}


%build
%cmake -DINSTALL_BUNDLED_DICTS=0 -DSHARE_INSTALL_PREFIX:PATH=%{_prefix}
%cmake_build


%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING.txt
%doc ChangeLog.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg


%changelog
* Tue Oct 04 2022 Dan Horák <dan@danny.cz> - 1.9.20-1
- initial Fedora version
