Name:           python-setuptools-gettext
Version:        0.1.3
Release:        4%{?dist}
Summary:        Setuptools gettext extension plugin

License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/setuptools-gettext
Source0:        %{pypi_source setuptools-gettext}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Setuptools helpers for gettext. Compile .po files into .mo files.

%package -n     python3-setuptools-gettext
Summary:        %{summary}

%description -n python3-setuptools-gettext
Setuptools helpers for gettext. Compile .po files into .mo files.

%prep
%autosetup -n setuptools-gettext-%{version}
rm -rf ./setuptools_gettext.egg-info
sed -e 's/setuptools>=46.1/setuptools/' -i setup.cfg

# Clarify license, until this change has made it into an upstream release:
# https://github.com/breezy-team/setuptools-gettext/pull/11
sed -e 's/\(License :: OSI Approved ::\) Apache Software License/\1 GNU General Public License v2 or later (GPLv2+)/' \
    -i PKG-INFO setup.cfg

%build
%py3_build

%install
%py3_install

%check
%py3_check_import setuptools_gettext

%files -n python3-setuptools-gettext
%doc README.md
%license COPYING
%{python3_sitelib}/setuptools_gettext/
%{python3_sitelib}/setuptools_gettext-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.3-3
- Rebuilt for Python 3.12

* Thu May 4 2023 Björn Lindström <bkhl@elektrubadur.se> - 0.1.3-2
- Add missing dist tag in release number.

* Sat Apr 29 2023 Björn Lindström <bkhl@elektrubadur.se> - 0.1.3-1
- Initial package.
