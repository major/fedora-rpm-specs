%global pypi_name aeidon

Name:           python-%{pypi_name}
Version:        1.15
Release:        23%{?dist}
Summary:        Subtitle file manipulation library

License:        GPL-3.0-or-later
URL:            https://pypi.org/project/%{pypi_name}/
Source0:        https://files.pythonhosted.org/packages/bd/72/cfd1471d97c31dd34a4f5222a6d5a0950fe07f2c8b961bc4a233b8e7dff7/%{pypi_name}-%{version}.tar.gz 

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  gettext

%generate_buildrequires
%pyproject_buildrequires -R

%description
Aeidon is a library for reading, writing and manipulating
text-based subtitle files.

%package -n python3-%{pypi_name}
Summary:        %{summary}
Obsoletes:      python3-aeidon < %{version}-%{release}

%description -n python3-%{pypi_name}
Aeidon is a library for reading, writing and manipulating
text-based subtitle files.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf .egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# As this package is split from Gaupol, we do not ship Gaupol-related files
rm -f %{buildroot}%{_bindir}/gaupol
rm -rf %{buildroot}%{python3_sitelib}/gaupol
rm -rf %{buildroot}%{_datadir}/gaupol/
rm -f %{buildroot}%{_datadir}/applications/io.otsaloma.gaupol.desktop
rm -rf %{buildroot}%{_datadir}/icons/hicolor/
rm -rf %{buildroot}%{_datadir}/locale/
rm -f %{buildroot}%{_mandir}/man1/gaupol.1
rm -f %{buildroot}%{_datadir}/metainfo/io.otsaloma.gaupol.appdata.xml
rm -rf %{buildroot}%{python3_sitelib}/tests/

%check
%py3_check_import %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING
%doc README.md

%changelog
* Tue Aug 26 2025 Sudip Shil <sshil@redhat.com> - 1.15-23
- Initial packaging from official PyPI source
