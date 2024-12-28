Name:           python-debian
Version:        0.1.51
Release:        %autorelease
Summary:        Modules for Debian-related data formats
# debfile.py, arfile.py, debtags.py are release under GPL v3 or above
# everything else is GPLv2+
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Source0:        http://ftp.debian.org/debian/pool/main/p/python-debian/python-debian_%{version}.tar.xz
URL:            https://salsa.debian.org/python-debian-team/python-debian
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#tests
BuildRequires:  dpkg
BuildRequires:  python3-chardet
BuildRequires:  python3-pytest
%if ! 0%{?rhel}
BuildRequires:  python3-apt
%endif

%global _description\
This package provides Python modules that abstract many formats of Debian\
related files. Currently handled are:\
* Debtags information (debian.debtags module)\
* debian/changelog (debian.changelog module)\
* Packages files, pdiffs (debian.debian_support module)\
* Control files of single or multiple RFC822-style paragraphs, e.g.\
  debian/control, .changes, .dsc, Packages, Sources, Release, etc.\
  (debian.deb822 module)\
* Raw .deb and .ar files, with (read-only) access to contained\
  files and meta-information

%description %_description

%package -n python3-debian
Summary:        Modules for Debian-related data formats
BuildRequires:  python3-devel
Requires:       python3-chardet
Requires:       xz
Requires:       python3-six
Suggests:       gnupg
%if ! 0%{?rhel}
Recommends:     python3-apt
%endif

%description -n python3-debian
This package provides Python modules that abstract many formats of Debian
related files. Currently handled are:
* Debtags information (debian.debtags module)
* debian/changelog (debian.changelog module)
* Packages files, pdiffs (debian.debian_support module)
* Control files of single or multiple RFC822-style paragraphs, e.g.
  debian/control, .changes, .dsc, Packages, Sources, Release, etc.
  (debian.deb822 module)
* Raw .deb and .ar files, with (read-only) access to contained
  files and meta-information


%prep
%autosetup -p1 -n python-debian-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files debian

%check
%pyproject_check_import

%files -n python3-debian -f %{pyproject_files}
%doc README.rst HISTORY.deb822

%changelog
%autochangelog
