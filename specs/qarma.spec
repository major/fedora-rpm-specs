Name:           qarma
Version:        1.0.0
Release:        1%{?dist}
Summary:        Tool for creating Qt dialog boxes

License:        GPL-2.0-only
URL:            https://github.com/luebking/qarma
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)

%description
Qarma is a tool to create dialog boxes, based on Qt. It's a clone of
Zenity which was written for GTK+.

%prep
%autosetup -p1


%build
%qmake_qt6
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Sat Jan 11 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 1.0.0-1
- Initial Packaging
