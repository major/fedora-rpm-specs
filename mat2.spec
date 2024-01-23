%bcond_without tests
# Non-automatically generated dependencies.
# Reusable for BuildRequires and Requires.
%global non_auto_gen_deps gdk-pixbuf2-modules librsvg2 mailcap perl-Image-ExifTool poppler-glib

%global modname lib%{name}

Name:       mat2
Version:    0.13.4
Release:    4%{?dist}
Summary:    Metadata removal tool, supporting a wide range of commonly used file formats

# License file provided by Python module, see:
# rpm -q --licensefiles {python3_sitelib}/{name}-{version}.dist-info/LICENSE
License:    LGPL-3.0-or-later
URL:        https://0xacab.org/jvoisin/mat2
Source0:    %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/uploads/95d1f3782dfc731545fd9b467c594cb2/%{name}-%{version}.tar.gz.asc
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
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}
# Fix man installation dir
mkdir -p %{buildroot}%{_mandir}/man1/
mv %{buildroot}/%{_prefix}/man/man1/%{name}.1 \
    %{buildroot}%{_mandir}/man1/
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
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.4-3
- build: Conform Fedora packaging guidelines for official repo
- build: Add 'dolphin' sub-package and split into app and library sub-package
- build: Use automatically generated dependencies for Python deps
- build: Use new Python macros https://docs.fedoraproject.org/en-US/packaging-guidelines/Python
- license: Convert to SPDX
- test: Use {py3_test_envvars} for tests
- style: Convert identations to spaces

* Thu Aug 03 2023 Antoine Tenart <antoine.tenart@ack.tf> - 0.13.4-2
- Add librsvg2 as a dependency.

* Thu Aug 03 2023 Antoine Tenart <antoine.tenart@ack.tf> - 0.13.4-1
- Bump to 0.13.4.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.13.4

* Mon Jan 30 2023 Antoine Tenart <antoine.tenart@ack.tf> - 0.13.2-1
- Bump to 0.13.2.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.13.2

* Mon Jan 09 2023 Antoine Tenart <antoine.tenart@ack.tf> - 0.13.1-1
- Bump to 0.13.1.
- Due to upstream removal, removed the mat2-nautilus package.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.13.1

* Mon Jul 11 2022 Antoine Tenart <antoine.tenart@ack.tf> - 0.13.0-1
- Bump to 0.13.0.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.13.0

* Wed May 11 2022 Antoine Tenart <antoine.tenart@ack.tf> - 0.12.4-1
- Bump to 0.12.4.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.12.4

* Sat Feb 05 2022 Antoine Tenart <antoine.tenart@ack.tf> - 0.12.3-1
- Bump to 0.12.3.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.12.3

* Tue Aug 31 2021 Antoine Tenart <antoine.tenart@ack.tf> - 0.12.2-1
- Bump to 0.12.2.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.12.2

* Mon Mar 22 2021 Antoine Tenart <antoine.tenart@ack.tf> - 0.12.1-1
- Bump to 0.12.1.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.12.1

* Sat Dec 19 2020 Antoine Tenart <antoine.tenart@ack.tf> - 0.12.0-1
- Bump to 0.12.0.
- See https://0xacab.org/jvoisin/mat2/-/blob/master/CHANGELOG.md#0120-2020-12-18

* Sun Mar 29 2020 Antoine Tenart <antoine.tenart@ack.tf> - 0.11.0-1
- Bump to 0.11.0.
- See https://0xacab.org/jvoisin/mat2/-/blob/master/CHANGELOG.md#0110-2020-03-29

* Mon Feb 10 2020 Antoine Tenart <antoine.tenart@ack.tf> - 0.10.1-1
- Bump to 0.10.1.
- See https://0xacab.org/jvoisin/mat2/tags/0.10.1

* Mon Dec 02 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.10.0-1
- Bump to 0.10.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.10.0

* Sat May 11 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.9.0-1
- Bump to 0.9.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.9.0

* Wed Apr 24 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.8.0-3
- Enable tarball verification.
- Add build time checks.

* Wed Mar 27 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.8.0-2
- Install mat2's man page and docs.
- Stop listing ffmpeg as a mandatory dependency.

* Fri Mar 22 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.8.0-1
- Bump to 0.8.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.8.0
- See https://0xacab.org/jvoisin/mat2/tags/0.7.0

* Sat Nov 10 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.6.0-1
- Bump to 0.6.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.6.0

* Wed Oct 24 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.5.0-1
- Bump to 0.5.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.5.0

* Thu Oct 11 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.4.0-1
- Bump to 0.4.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.4.0

* Sat Sep 01 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.3.1-1
- Bump to 0.3.1.
- See https://0xacab.org/jvoisin/mat2/tags/0.3.1

* Thu Aug 23 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.3.0-1
- Bump to 0.3.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.3.0

* Wed Jul 11 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.2.0-1
- Bump to 0.2.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.2.0

* Fri Jul 06 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.1.3-1
- Bump to 0.1.3.
- See https://0xacab.org/jvoisin/mat2/tags/0.1.3
- See https://0xacab.org/jvoisin/mat2/tags/0.1.2

* Tue Jun 12 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.1.1-1
- First mat2 package.
