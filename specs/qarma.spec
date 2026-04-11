Name:           qarma
Version:        1.1.1
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

%conf
%qmake_qt6

%build
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Fri Apr 10 2026 Shawn W Dunn <sfalken@opensuse.org> - 1.1.1-1
- Update to 1.1.1

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 11 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 1.0.0-1
- Initial Packaging
