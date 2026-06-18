Name:           krop
Version:        0.7.0
Release:        %autorelease
Summary:        Tool to crop PDF files with an eye towards e-readers
License:        GPL-3.0-or-later
URL:            https://arminstraub.com/software/krop
Source0:        https://arminstraub.com/downloads/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-pypdf
BuildRequires:  python3-pyqt6
BuildRequires:  python3-PyMuPDF

Requires:       python3-%{name} = %{version}-%{release}

%description
Krop is a simple graphical tool to crop the pages of PDF files. A unique feature
of krop is its ability to automatically split pages into sub-pages to fit the
limited screen size of devices such as e-readers. This is particularly useful if
your e-reader does not support convenient scrolling.

%package -n python3-%{name}
Summary:        Python 3 module for %{name}
Requires:       python3-pypdf
Requires:       python3-pyqt6
Requires:       python3-PyMuPDF

%description -n python3-%{name}
%{summary}.

%prep
%autosetup
# Replace references to Ubuntu/apt-get in user-facing error messages
find . -type f -name '*.py' -exec sed -i -e 's/of ubuntu/of Fedora/Ig' \
 -e 's|apt-get|dnf|g' '{}' +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%check
%pyproject_check_import -e krop.mainwindowui_qt5
desktop-file-validate %{buildroot}%{_datadir}/applications/com.arminstraub.krop.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.arminstraub.krop.metainfo.xml

%files
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_metainfodir}/com.arminstraub.krop.metainfo.xml
%{_datadir}/applications/com.arminstraub.krop.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.arminstraub.krop.svg
%{_mandir}/man1/%{name}.1*

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
