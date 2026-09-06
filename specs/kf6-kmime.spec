%global  framework kmime

Name:    kf6-%{framework}
Version: 6.30.0
Release: 2%{?dist}
Summary: The KMime Library

License: BSD-2-Clause AND BSD-3-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)

BuildRequires:  cmake(KF6Codecs)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Codecs)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.
 
%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1

%conf
%cmake_kf6

%build
%cmake_build_kf6

%install
%cmake_install_kf6
%find_lang libkmime6 --with-qt

%files -f libkmime6.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Mime.so.*

%files devel
%{_kf6_includedir}/KMime/
%{_kf6_libdir}/libKF6Mime.so
%{_kf6_libdir}/cmake/KF6Mime/

%files doc
%{_qt6_docdir}/*.qch
 
%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Sat Sep 05 2026 Steve Cossette <farchord@gmail.com> - 6.30.0-2
- Added qdocs to kmime

* Fri Sep 04 2026 Steve Cossette <farchord@gmail.com> - 6.30.0-1
- 6.30.0

* Fri Aug 07 2026 Steve Cossette <farchord@gmail.com> - 6.29.0-1
- 6.29.0

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jul 04 2026 Steve Cossette <farchord@gmail.com> - 6.28.0-1
- 6.28.0

* Sat Jun 6 2026 Steve Cossette <farchord@gmail.com> - 6.27.0-1
- Initial release (Rename/version scheme change from kmime)
- Removed doc subpackage (It's been empty for a while)
- Cleaned up dependancies
