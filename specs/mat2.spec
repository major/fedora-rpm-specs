%global modname lib%{name}

Name:           mat2
Version:        0.14.0
Release:        %autorelease
Summary:        Metadata removal tool, supporting a wide range of commonly used file formats

# License file provided by Python module, see:
# rpm -q --licensefiles {python3_sitelib}/{name}-{version}.dist-info/LICENSE
License:        LGPL-3.0-or-later
URL:            https://github.com/jvoisin/mat2
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{version}.tar.gz.asc
Source2:        gpgkey-9FCDEE9E1A381F311EA62A7404D041E8171901CC.gpg
# Skip two tests that fail on Fedora.  At least one is, and possibly both are,
# related to the glycin changes in Fedora 43+.  One JPEG test fails because
# glycin fails when reading a DAC format inside a JPEG.  One TIFF test fails for
# unknown reasons; it simply fails to clean the metadata.  This implies that
# this package fails, in part, to fulfill its purpose on F43+.
Patch0:          %{name}-skip-broken-tests.patch
# Fix test failures with Python 3.15
Patch1:          %{name}-py315-fix.patch

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -l %{modname}

BuildRequires:  gdk-pixbuf2
BuildRequires:  gnupg2
BuildRequires:  gobject-introspection
BuildRequires:  librsvg2
BuildRequires:  mailcap
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  poppler-glib

# Test dependencies
BuildRequires:  ffmpeg-free
BuildRequires:  perl-Image-ExifTool

Requires:       python3-%{modname} = %{version}-%{release}

Suggests:       %{name}-dolphin = %{version}-%{release}

%py_provides python3-%{name}

%global _description %{expand:
Metadata consist of information that characterizes data. Metadata are used to
provide documentation for data products. In essence, metadata answer who,
what, when, where, why, and how about every facet of the data that are being
documented.

Metadata within a file can tell a lot about you. Cameras record data about
when a picture was taken and what camera was used. Office documents like PDF
or Office automatically adds author and company information to documents and
spreadsheets. Maybe you don't want to disclose those information.

This is precisely the job of mat2: getting rid, as much as possible, of
metadata.

mat2 provides:

  - a library called 'libmat2';
  - a command line tool called 'mat2',
  - a service menu for Dolphin, KDE's default file manager

If you prefer a regular graphical user interface, you might be interested in
'Metadata Cleaner', which uses mat2 under the hood.}

%description %_description

# Library package
%package     -n python3-%{modname}
Summary:        Library for %{name}

Requires:       gdk-pixbuf2
Requires:       librsvg2
Requires:       mailcap
Requires:       poppler-glib

# To avoid conflicts with 'ffmpeg-free' vs 'ffmpeg' from RPM Fusion
Recommends:     %{_bindir}/ffmpeg
Recommends:     perl-Image-ExifTool

Recommends:     %{name} = %{version}-%{release}

%description -n python3-%{modname} %_description

Library for %{name}.

# Dolphin package
%package        dolphin
Summary:        Dolphin integration for %{name}

Requires:       dolphin
# For Dolphin integration icon: mat2.svg
Requires:       hicolor-icon-theme
Requires:       kdialog
Requires:       kf5-filesystem
Requires:       python3-%{modname} = %{version}-%{release}

%description dolphin %_description

Dolphin integration for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%install -a
# E: non-executable-script
chmod 0755 %{buildroot}%{python3_sitelib}/%{modname}/__init__.py
# Install Dolphin integration
install -D -p dolphin/%{name}.desktop -t \
    %{buildroot}%{_datadir}/kservices5/
# Install Dolphin integration icon
install -D -p -m 644 data/%{name}.svg -t \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%check
%{py3_test_envvars} %{python3} -m unittest discover

%files
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.md CHANGELOG.md doc/*.md

%files dolphin
%doc dolphin/README.md
%{_datadir}/icons/hicolor/scalable/*/*.svg
# No need to validate .desktop file for KDE services.
# https://develop.kde.org/docs/apps/dolphin/service-menus/
%{_datadir}/kservices5/%{name}.desktop

%changelog
%autochangelog
