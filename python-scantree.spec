%global srcname scantree

Name:           python-%{srcname}
Version:        0.0.1
Release:        3%{?dist}
Summary:        Flexible recursive directory iterator

License:        MIT
URL:            https://github.com/andhus/%{srcname}
Source0:        https://github.com/andhus/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Recursive directory iterator supporting:
- flexible filtering including wildcard path matching
- in memory representation of file-tree (for repeated access)
- efficient access to directory entry properties (posix.DirEntry interface)
  extended with real path and path relative to the recursion root directory
- detection and handling of cyclic symlinks


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
Recursive directory iterator supporting:
- flexible filtering including wildcard path matching
- in memory representation of file-tree (for repeated access)
- efficient access to directory entry properties (posix.DirEntry interface)
  extended with real path and path relative to the recursion root directory
- detection and handling of cyclic symlinks


%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pytest


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Scott K Logan <logans@cottsay.net> - 0.0.1-2
- Convert to use pyproject-rpm-macros

* Wed Jul 27 2022 Scott K Logan <logans@cottsay.net> - 0.0.1-1
- Initial package (rhbz#2111672)
