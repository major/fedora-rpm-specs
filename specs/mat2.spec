# File "/builddir/build/BUILD/mat2-0.13.4/tests/test_libmat2.py", line 559, in test_all_parametred
#   self.assertIn(k, case['expected_meta'], '"%s" is not in "%s" (%s)' % (k, case['expected_meta'], case['name']))
# AssertionError: 'VideoFullRangeFlag' not found in
%bcond_with tests
# Non-automatically generated dependencies.
# Reusable for BuildRequires and Requires.
%global non_auto_gen_deps gdk-pixbuf2-modules librsvg2 mailcap perl-Image-ExifTool poppler-glib python3-mutagen

%global modname lib%{name}

Name:       mat2
Version:    0.13.5
Release:    %autorelease
Summary:    Metadata removal tool, supporting a wide range of commonly used file formats

# License file provided by Python module, see:
# rpm -q --licensefiles {python3_sitelib}/{name}-{version}.dist-info/LICENSE
License:    LGPL-3.0-or-later
URL:        https://0xacab.org/jvoisin/mat2
Source0:    %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    https://0xacab.org/-/project/1139/uploads/060efa77668fa7f6d9baeb8a327857af/%{name}-%{version}.tar.gz.asc
Source2:    gpgkey-9FCDEE9E1A381F311EA62A7404D041E8171901CC.gpg

BuildArch:  noarch

BuildRequires:  gnupg2
BuildRequires:  python3-devel >= 3.9
BuildRequires:  python3-setuptools
%if %{with tests}
# 'bubblewrap' doesn't work in mock
BuildRequires:  %{non_auto_gen_deps}
BuildRequires:  ffmpeg-free
BuildRequires:  python3-gobject
%endif

Requires:   %{non_auto_gen_deps}
Requires:   python3-%{modname} = %{version}-%{release}

# To avoid conflicts with 'ffmpeg-free' vs 'ffmpeg' from RPM Fusion
Recommends: /usr/bin/ffmpeg

Recommends: bubblewrap

Suggests:   %{name}-dolphin = %{version}-%{release}

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
'Metadata Cleaner', which is using mat2 under the hood.}

%description %_description


# Library package
%package -n python3-%{modname}
Summary:    Library for %{name}

Recommends: %{name} = %{version}-%{release}

BuildArch:  noarch

%description -n python3-%{modname} %_description

Library for %{name}.


# Dolphin package
%package    dolphin
Summary:    Dolphin integration for %{name}

BuildArch:  noarch

Requires:   dolphin
# For Dolphin integration icon: mat2.svg
Requires:   hicolor-icon-theme
Requires:   kdialog
Requires:   kf5-filesystem
Requires:   python3-%{modname} = %{version}-%{release}

%description dolphin %_description

Dolphin integration for %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}
# E: non-executable-script
chmod +x %{buildroot}%{python3_sitelib}/%{modname}/__init__.py
# Install Dolphin integration
install -D -p dolphin/%{name}.desktop -t \
    %{buildroot}%{_datadir}/kservices5/
# Install Dolphin integration icon
install -D -p -m 644 data/%{name}.svg -t \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/


%check
%if %{with tests}
%{py3_test_envvars} %{python3} -m unittest discover
%endif


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
